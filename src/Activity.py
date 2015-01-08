'''
Created on 8 Jan 2015
An activity class to describe a ServiceProvider's activities
@author: chriseisbrown
'''
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
