'''
Created on 19 Dec 2014
This script reads in a validated input xls and e-mails the service providers
with details of their upcoming activities
@author: chriseisbrown
'''
import mandrill
import argparse
import os
from xlrd import open_workbook


def generate_email_to_provider(provider):
    print "generating e-mail to provider {} {}".format(provider.id, provider.name)

    try:
        # assemble data from service provider to set up the e-mail
        to_email = "chris.brown@adaptivelab.com"
        #to_email = "tracey_gilbert@yahoo.com"
        
        to_name = provider.name    
        subject = provider.name + " - time to check your KidsConnect activities"
        
        html_heading = "<h>KidsConnect data check</h>"
        html_blurb1 = "<p>Hi {}, it's time to check your entries for KidsConnect. On file we have the following activities that you are running:</p>".format(provider.name)      
        
        table_section = ""
        activity_row_header = "<th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th>".format("Activity", "Runs on", "at", "Next on", "and then")
        activity_table_row = "<tr>{}</tr>".format(activity_row_header)

        for activity in provider.activities:     
            activity_row_cells = "<td>{}</td><td>{}</td><td>{}</td>".format(activity.name, activity.day, activity.time)
            activity_next_dates = "<td></td><td></td>"
            
            if len(activity.next_dates) > 0:
                activity_dates = ""
                for next_event_date in activity.next_dates:
                    activity_dates += "<td>{}</td>".format(next_event_date.strftime('%d-%m-%Y'))
                activity_next_dates = activity_dates
            else:
                activity_next_dates = "<td>{}</td><td>{}</td>".format("*", "*")
            
            activity_row_cells += activity_next_dates
            activity_table_row += "<tr>{}</tr>".format(activity_row_cells)     
                                
        activity_table = "<table>{}</table>".format(activity_table_row)
        table_section = activity_table
        
        html_blurb2 = "<p>Please can you check the details we've provided and let us know if they are correct by replying to this e-mail."
        html_blurb3 = "<p>If there are any errors then please e-mail or call us on XXX-XXX-XXXX at your earliest convenience."
        html_blurb4 = "<p>If there is a * marked in any of your entries then we are lacking some data so please advise us."
        
        html_signature = "<p> Thanks! from the team at KidsConnect </P>"
        
        html_string = html_heading + html_blurb1 + table_section + html_blurb2 + html_blurb3 + html_blurb4 + html_signature
        
        mandrill_client = mandrill.Mandrill('cF8W6ieOlJoYSdewzmaE7A')
        message = {
         'attachments': None,
         'auto_html': None,
         'auto_text': None,
         'bcc_address': None,
         'from_email': 'chriseisbrown@btconnect.com',
         'from_name': 'Kids Connect',
         'headers': {'Reply-To': 'Rachel@kidsconnect.org.uk'},
         'html': html_string,
         'important': False,
         'inline_css': None,
         'merge': True,
         'subject': subject,
         'tags': ['password-resets'],
         'text': 'Example text content',
         'to': [{'email': to_email,
                 'name': to_name,
                 'type': 'to'}],
         'track_clicks': None,
         'track_opens': None,
         'tracking_domain': None,
         'url_strip_qs': None,
         'view_content_link': None}
        
        result = mandrill_client.messages.send(message=message, async=False, ip_pool='Main Pool')
        '''
        [{'_id': 'abc123abc123abc123abc123abc123',
          'email': 'recipient.email@example.com',
          'reject_reason': 'hard-bounce',
          'status': 'sent'}]
        '''
        
        result_dict = result[0]
        send_status = result_dict["status"]
        if send_status not in "sent":
            print "ERROR: did not send e-mail to {}".format(to_email)
            print result
        else:
            print "sent e-mail to provider {} {} [{}]".format(provider.id, to_name, to_email)
            
        reject_reason = result_dict["reject_reason"]
        if reject_reason is not None:
            print "ERROR: e-mail rejected by {}".format(to_email)
        
    
    except mandrill.Error, e:
        # Mandrill errors are thrown as exceptions
        print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
        # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
        raise