import os
import imaplib, email

# Load Environtment Variables at .env
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('APP_PASS')
IMAP_SERVER = os.environ.get('IMAP_SERVER')


# Context
with imaplib.IMAP4_SSL(IMAP_SERVER)as imap:
    # Login
    imap.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    imap.select("INBOX")

    _,search_data, = imap.search(None,'UNSEEN')
    
    for num in search_data[0].split():
        # print(num)
        _,data = imap.fetch(num,'(RFC822)')
        _,msg_bytes = data[0]
        email_msg = email.message_from_bytes(msg_bytes)
        # Read Mail Header
        email_header = {}
        for header in ['subject','to','from','date']:
          email_header[header] = email_msg[header]
        #   print("{}:{}".format(header,email_msg[header])) 
        print(email_header)
        # Read Mail Body
        for part in email_msg.walk():
            if part.get_content_type()=="text/plain":
                email_body = part.get_payload(decode=True)
                print(email_body.decode())
            elif part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
                email_body = part.get_payload(decode=True)
                print(email_body.decode())