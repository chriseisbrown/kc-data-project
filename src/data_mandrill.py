'''
Created on 19 Dec 2014

@author: chriseisbrown
'''
import mandrill

try:
    mandrill_client = mandrill.Mandrill('cF8W6ieOlJoYSdewzmaE7A')
    message = {
     'attachments': None,
     'auto_html': None,
     'auto_text': None,
     'bcc_address': 'chris.brown@adaptivelab.com',
     'from_email': 'chriseisbrown@btconnect.com',
     'from_name': 'Kids Connect',
     'headers': {'Reply-To': 'message.reply@example.com'},
     'html': '<p>Example HTML content</p>',
     'important': False,
     'inline_css': None,
     'merge': True,
     'subject': 'Check your data',
     'tags': ['password-resets'],
     'text': 'Example text content',
     'to': [{'email': 'chris.brown@adaptivelab.com',
             'name': 'Chris B',
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

except mandrill.Error, e:
    # Mandrill errors are thrown as exceptions
    print 'A mandrill error occurred: %s - %s' % (e.__class__, e)
    # A mandrill error occurred: <class 'mandrill.UnknownSubaccountError'> - No subaccount exists with the id 'customer-123'    
    raise