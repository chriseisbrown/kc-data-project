'''
@author: chriseisbrown
Created 3 Dec 2014
'''
import argparse
import os

from datetime import date
from datetime import datetime
from datetime import timedelta

from dateutil.relativedelta import *
from dateutil.rrule import *

from xlrd import open_workbook
from xlwt import Workbook


class ServiceProvider(object):
    def __init__(self):
        self.id = ""
        self.name = ""
        self.primary_email = ""
        self.activities = []

    def display(self):
        print 'Service provider:', self.id, ' ', self.name, ' ', self.primary_email
        for a in self.activities:
            a.display()
        
    def addActivity(self, activity):
        self.activities.append(activity)


class Activity(object):
    def __init__(self):
        self.id = ""
        self.name = ""
        self.introduction = ""
        self.day = None
        self.time = ""
        self.next_dates = []

    def display(self):
        # will show encoding problems as ??? in output report
        print 'Activity:', self.id, ' ', self.name, ' ', self.day, ' ', self.time
        print 'Next occurs:'
        if self.next_dates:
            for i in range(len(self.next_dates)):
                print self.next_dates[i].strftime('%d/%m/%Y'), ' at ', self.time
        
        print self.introduction.encode('utf-8')
        #print 'Activity:', self.id, ' ', self.name, ' ', self.introduction.encode('utf-8', 'ignore')

# globals
day_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

def find_day_of_week(in_date):
    'Given a date, return the name of its day of the week'
    return day_names[in_date.weekday()]

def calculate_day_of_week_offset(date1, date2):
        return date2.weekday() - date1.weekday() 

def generate_next_weekly_occurence_list(today_date, start_on_date, ends_on_date):
    next_occurs = []
    date_offset = calculate_day_of_week_offset(today_date, start_on_date)
    if date_offset <= 0:
        date_offset += 7
    offset_delta = timedelta(days=date_offset)
    next_date = today_date + offset_delta
    if next_date <= ends_on_date:
        next_occurs.append(next_date)
        next_date += timedelta(days=7)
        if next_date <= ends_on_date:
            next_occurs.append(next_date)         
    return next_occurs   

def generate_next_fortnightly_occurence_list(today_date, start_on_date, ends_on_date):
    next_occur_list = generate_next_fortnightly_occurences(today_date, start_on_date, ends_on_date)
    return next_occur_list

def generate_next_fortnightly_occurences(today_date, start_on_date, ends_on_date):
    'generates the next occurrences of the day of the month that an event falls on, e.g.; first Sat in every month'  
    # get day number that event occurs on
    day_num = start_on_date.weekday()
   
    next_occur_list = list(rrule(WEEKLY, interval=2, byweekday=day_num, dtstart=start_on_date, until=ends_on_date))
    result_list = []
    for i in range(len(next_occur_list)):
        if next_occur_list[i].date() > today_date and next_occur_list[i].date() <= ends_on_date:
            result_list.append(next_occur_list[i].date())  
    return result_list  

def generate_next_day_of_month_occurence(today_date, start_on_date):
    'returns just one generated future event date'
    next_occur_list = generate_next_day_of_month_occurences(today_date, start_on_date, 12)
    next_occurs = next_occur_list[0]
    return next_occurs.date()

def generate_next_day_of_month_occurence_list(today_date, start_on_date, ends_on_date):
    next_occur_list = generate_next_day_of_month_occurences(today_date, start_on_date, ends_on_date, 12)
    return next_occur_list
    
def generate_next_day_of_month_occurences(today_date, start_on_date, ends_on_date, num_to_generate):
    'generates the next occurrences of the day of the month that an event falls on, e.g.; first Sat in every month'  
    # generate next occurrences    
    next_occur_list = list(rrule(MONTHLY, count=num_to_generate, dtstart=start_on_date))
    result_list = []
    for event_date in next_occur_list:
        adjusted_date = event_date + timedelta(days=calculate_day_of_week_offset(event_date.date(), start_on_date)) 
        if adjusted_date.date() > today_date and adjusted_date.date() <= ends_on_date:
            result_list.append(adjusted_date.date())
    return result_list


def generate_next_date_of_month_occurence_list(today_date, start_on_date, ends_on_date):
    next_occur_list = generate_next_date_of_month_occurences(today_date, start_on_date, ends_on_date, 12)
    return next_occur_list

def generate_next_date_of_month_occurences(today_date, start_on_date, ends_on_date, num_to_generate):
    'generates the next monthly occurrences of the date'    
    next_occur_list = list(rrule(MONTHLY, count=num_to_generate, dtstart=start_on_date))
    result_list = []
    for i in range(len(next_occur_list)):
        if next_occur_list[i].date() > today_date and next_occur_list[i].date() <= ends_on_date:
            result_list.append(next_occur_list[i].date())
    return result_list

def generate_one_off_occurence_list(today_date, start_on_date, ends_on_date):
    'returns just the one-off event date generated future event date'
    next_occur_list = []
    if today_date < start_on_date and today_date <= ends_on_date:
        next_occur_list.append(start_on_date)
    return next_occur_list

def generate_default_occurence(today_date, in_date):
    print 'WARNING: No date recurrence method exists for this recurrence frequency'
    next_occur_list = []
    return next_occur_list


def resize_next_dates(next_dates, num):
    'given a list, return a list of num elements'
    return_list = []
    for event_date in next_dates:
        if len(return_list) < num:
            return_list.append(event_date)
        else:
            break
    return return_list


INPUT_DIR = "../input-data/"
OUTPUT_DIR = "../output-data/"
INPUT_FILE_NAME = "Data collection.xlsx"
OUTPUT_FILE_NAME = "Data report.xls"

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--send", help="dispatches e-mails to service providers",
                    action="store_true")
    
    parser.add_argument("--folder", type=str, help="folder to load from, defaults to {}".format(INPUT_DIR))
    parser.add_argument("--filename", type=str, help="file to load data, defaults to {}".format(INPUT_FILE_NAME))

    args = parser.parse_args()
    if args.send:
        print "SENDING E-MAILS TO SERVICE PROVIDERS"
    
    folder_name = ""
    if args.folder:
        folder_name = args.folder
    else:
        folder_name = INPUT_DIR
        
    file_name = ""
    if args.filename:
        file_name = args.filename
    else:
        file_name = INPUT_FILE_NAME  
        
    infile = os.path.join(folder_name, file_name)    
    print "using input data from file {}".format(infile)
    
    wb = open_workbook(infile)
    for s in wb.sheets():
        print 'Found sheet:', s.name
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
    print

    '''print wb.sheet_names()
    for sheet_name in wb.sheet_names():
        print wb.sheet_by_name(sheet_name)
    ''' 
    
    # make service provider map       
    provider_sheet = wb.sheet_by_name('Service providers')
    sp_ids = provider_sheet.col_values(0,1)
    sp_names = provider_sheet.col_values(1,1)
    sp_primary_emails = provider_sheet.col_values(4,1)
    
    providers = {}
    i=0        
    for sp_id in sp_ids:
        #print 'Service provider:', sp_id  
        sp = ServiceProvider()
        sp.id = sp_id
        sp.name = sp_names[i]
        sp.primary_email = sp_primary_emails[i]
        
        i=i+1
        
        providers[sp_id] = sp
    
    # for each activity in activities sheet, attach activity to appropriate provider     
    activity_sheet = wb.sheet_by_name('Activities')
    act_ids = activity_sheet.col_values(0,1)
    act_provider_ids = activity_sheet.col_values(1,1)
    act_names = activity_sheet.col_values(3,1)
    act_intros = activity_sheet.col_values(5,1)
    act_start_dates = activity_sheet.col_values(7,1)
    act_last_dates = activity_sheet.col_values(8,1)
    act_start_times = activity_sheet.col_values(9,1)
    act_recurrences = activity_sheet.col_values(11,1)
    
    j=0
    for activity_provider_id in act_provider_ids:
        provider = providers.get(activity_provider_id)
        if provider != None:
            ac = Activity()
            ac.id = act_ids[j]
            ac.name = act_names[j]
            ac.introduction = act_intros[j]
            ac.time = act_start_times[j]
            
            # work out what day the activity runs on from its start date
            start_date = datetime.strptime(act_start_dates[j], "%d/%m/%Y").date()
            ac.day = find_day_of_week(start_date)
            
            ends_on_date = datetime.strptime(act_last_dates[j], "%d/%m/%Y").date()
            
            branch = {0 : generate_one_off_occurence_list,
                      1 : generate_next_weekly_occurence_list,
                      2 : generate_next_fortnightly_occurence_list,
                      3 : generate_next_day_of_month_occurence_list,
                      4 : generate_next_date_of_month_occurence_list}             
            next_dates = branch.get(act_recurrences[j], generate_default_occurence)(date.today(), start_date, ends_on_date)
            
            HOW_MANY = 2
            ac.next_dates = resize_next_dates(next_dates, HOW_MANY)
            
            provider.addActivity(ac)
        else:
            print 'Activity id:', act_ids[j], ' has a provider_id of ', activity_provider_id, ' which does not match a service provider id' 
                
        j += 1
        
    
    # output for report
    
    wb = Workbook()
    ws = wb.add_sheet('Kids Connect output', cell_overwrite_ok=True)
    ws.row(0).write(0,'provider id')
    ws.row(0).write(1,'provider name')
    ws.row(0).write(2,'e-mail')
    ws.row(0).write(3,'activity id')
    ws.row(0).write(4,'activity name')
    ws.row(0).write(5,'introduction')
    ws.row(0).write(6,'day')
    ws.row(0).write(7,'time')
    ws.row(0).write(8,'next event 1')
    ws.row(0).write(9,'next event 2')
    
    row_num = 1
    
    for k in providers.keys():
        provider = providers.get(k)
        print "Processing provider {}".format(provider.id)
        
        for activity in provider.activities:
            ws.row(row_num).write(0,provider.id)
            ws.row(row_num).write(1,provider.name)
            ws.row(row_num).write(2,provider.primary_email)
            
            ws.row(row_num).write(3,activity.id)
            ws.row(row_num).write(4,activity.name)
            ws.row(row_num).write(5,activity.introduction)
            
            ws.row(row_num).write(6,activity.day)
            ws.row(row_num).write(7,activity.time)
            
            if len(activity.next_dates) > 0:
                event_col = 8
                for next_event_date in activity.next_dates:
                    ws.row(row_num).write(event_col, next_event_date.strftime('%d-%m-%Y'))
                    event_col += 1

            row_num += 1
        
    
    
    out_folder_name = OUTPUT_DIR
    out_file_name = OUTPUT_FILE_NAME      
    output_file = os.path.join(out_folder_name, out_file_name)
    wb.save(output_file)
    print "writing output data to file {}".format(output_file)


    

