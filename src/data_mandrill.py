'''
Created on 19 Dec 2014
This is a test rig for the Mandrill API
@author: chriseisbrown
'''
import mandrill

try:
    to_email = 'chris.brown@adaptivelab.com'
    to_name = 'Chris B'
    html_string = '<p>Example HTML content in a string</p>'
    
    mandrill_client = mandrill.Mandrill('cF8W6ieOlJoYSdewzmaE7A')
    message = {
     'attachments': None,
     'auto_html': None,
     'auto_text': None,
     'bcc_address': None,
     'from_email': 'chriseisbrown@btconnect.com',
     'from_name': 'Kids Connect',
     'headers': {'Reply-To': 'message.reply@example.com'},
     'html': html_string,
     'important': False,
     'inline_css': None,
     'merge': True,
     'subject': 'Please check your data',
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
    
    print result

except mandrill.Error, e:
    # Mandrill errors are thrown as exceptions
    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
    # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
    raise