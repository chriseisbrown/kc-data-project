'''
@author: chriseisbrown
A ServiceProvider class to hold data about providers
Created 3 Dec 2014
'''

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

