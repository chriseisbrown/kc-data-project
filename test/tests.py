'''
Created on 8 Dec 2014

@author: chriseisbrown
'''
import unittest
from datetime import date
from datetime import datetime
import data_loader


class Test(unittest.TestCase):


    def testCalculateDayOfWeekOffset(self):
        date1 = datetime.strptime('10/12/2014', "%d/%m/%Y").date()
        date2 = datetime.strptime('12/12/2014', "%d/%m/%Y").date()
        self.assertEqual(data_loader.calculate_day_of_week_offset(date1, date2), 2, 'Incorrect date difference returned')
        
    
    def test_generate_next_weekly_occurences(self):
        today = datetime.strptime('10/12/2014', "%d/%m/%Y").date()
        # occurs weekly on Mondays
        started_on = datetime.strptime('8/12/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('29/12/2014', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('15/12/2014', "%d/%m/%Y").date(), datetime.strptime('22/12/2014', "%d/%m/%Y").date()]
        next_occurs_list = data_loader.generate_next_weekly_occurence_list(today, started_on, ends_on)
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring dates not calculated correctly')
        
    def test_generate_next_monthly_day_occurence_on_last_Wednesday_of_month(self):
        today = datetime.strptime('10/12/2014', "%d/%m/%Y").date()
        # this event started on Wed 29 Oct and occurs on last Wed of each month
        started_on = datetime.strptime('29/10/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('04/02/2015', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('31/12/2014', "%d/%m/%Y").date(), datetime.strptime('28/01/2015', "%d/%m/%Y").date()]
        
        next_occurs_list = data_loader.resize_next_dates(data_loader.generate_next_day_of_month_occurence_list(today, started_on, ends_on), 2)
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring date not calculated correctly')
    
    
    def test_generate_next_monthly_day_occurence_on_first_Wednesday_of_month(self):
        today = datetime.strptime('15/12/2014', "%d/%m/%Y").date()
        # this event started on a Wed and occurs on first Wed of each month
        started_on = datetime.strptime('05/11/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('04/02/2015', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('07/01/2015', "%d/%m/%Y").date(), datetime.strptime('04/02/2015', "%d/%m/%Y").date()]
        
        next_occurs_list = data_loader.resize_next_dates(data_loader.generate_next_day_of_month_occurence_list(today, started_on, ends_on), 2)    
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring date not calculated correctly')
        
        
    def test_generate_next_monthly_date_occurence_on_16th_of_month(self):
        today = datetime.strptime('17/12/2014', "%d/%m/%Y").date()
        # this event started on a Wed and occurs on first Wed of each month
        started_on = datetime.strptime('16/11/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('16/02/2015', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('16/01/2015', "%d/%m/%Y").date(), datetime.strptime('16/02/2015', "%d/%m/%Y").date()]
        next_occurs_list = data_loader.resize_next_dates(data_loader.generate_next_date_of_month_occurence_list(today, started_on, ends_on), 2)     
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring date not calculated correctly')
        
    def test_generate_next_monthly_date_occurence_on_16th_of_month_takes_account_of_end_date(self):
        today = datetime.strptime('17/12/2014', "%d/%m/%Y").date()
        # this event started on a Wed and occurs on first Wed of each month
        started_on = datetime.strptime('16/11/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('15/02/2015', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('16/01/2015', "%d/%m/%Y").date()]
        next_occurs_list = data_loader.resize_next_dates(data_loader.generate_next_date_of_month_occurence_list(today, started_on, ends_on), 2)     
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring date not calculated correctly')        
    
    def test_generate_next_fortnightly_occurence_on_every_other_Saturday_of_month(self): 
        today = datetime.strptime('02/10/2014', "%d/%m/%Y").date()
        # occurs every other Sat
        started_on = datetime.strptime('27/09/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('04/02/2015', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('11/10/2014', "%d/%m/%Y").date(), datetime.strptime('25/10/2014', "%d/%m/%Y").date()]
        next_occurs_list = data_loader.resize_next_dates(data_loader.generate_next_fortnightly_occurence_list(today, started_on, ends_on), 2)
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring dates not calculated correctly')    
    
    def test_generate_one_off_occurence(self):
        today = datetime.strptime('17/12/2014', "%d/%m/%Y").date()
        # occurs once on this date only
        started_on = datetime.strptime('27/12/2014', "%d/%m/%Y").date()
        ends_on = datetime.strptime('27/12/2015', "%d/%m/%Y").date()
        expected_next_occurs_list = [datetime.strptime('27/12/2014', "%d/%m/%Y").date()]
        next_occurs_list = data_loader.generate_one_off_occurence_list(today, started_on, ends_on)
        self.assertEqual(expected_next_occurs_list, next_occurs_list, 'Next occurring date not calculated correctly')   
    
    def testFindDayOfWeek(self):
        test_date =  datetime.strptime('10/12/2014', "%d/%m/%Y").date()
        self.assertEqual(data_loader.find_day_of_week(test_date), 'Wed', 'Incorrect day name returned')
        
    def test_resize_next_dates_smaller_output_list(self):
        num = 1
        input_list = [datetime.strptime('07/01/2015', "%d/%m/%Y").date(), datetime.strptime('04/02/2015', "%d/%m/%Y").date()]
        expected_list = [datetime.strptime('07/01/2015', "%d/%m/%Y").date()]
        data_loader.resize_next_dates(input_list, num)
        self.assertEqual(expected_list, data_loader.resize_next_dates(input_list, num), 'Next occurring dates not calculated correctly')
        
    def test_resize_next_dates_smaller_input_list_than_specified(self):
        num = 2
        input_list = [datetime.strptime('07/01/2015', "%d/%m/%Y").date()]
        expected_list = [datetime.strptime('07/01/2015', "%d/%m/%Y").date()]
        data_loader.resize_next_dates(input_list, num)
        self.assertEqual(expected_list, data_loader.resize_next_dates(input_list, num), 'Next occurring dates not calculated correctly')
        
    def test_resize_next_dates_empty_input_list(self):
        num = 2
        input_list = []
        expected_list = []
        data_loader.resize_next_dates(input_list, num)
        self.assertEqual(expected_list, data_loader.resize_next_dates(input_list, num), 'Next occurring dates not calculated correctly')
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    


