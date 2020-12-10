import os
import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load Environtment Variables at .env
load_dotenv()
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('APP_PASS')
# Test Environment Variables
# print(EMAIL_ADDRESS)
# print(EMAIL_PASSWORD)

# Context 
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    # smtp.ehlo()
    # smtp.starttls()
    # smtp.ehlo()
    
    # Login
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
    # Setup subject and body
    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6pm this saturday?'

    # MiltiPart Mail - 
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'sergio@lmmp.mec.puc-rio.br'
    msg.attach(MIMEText(body, 'plain'))

    # Simple Text Message
    # msg = f'Subject:{subject} \n\n {body}'
    print(msg.as_string())

    # Send Mail
    try:
        # TODO: Set SSL Connection
        # # Create a secure SSL context
        # context = ssl.create_default_context()
        
        # Send Email
        smtp.sendmail(from_addr=msg['From'],to_addrs=msg['To'],msg=msg.as_string())
        print('Mail sent successfully!')
    except Exception as e:
        # Print any error messages to stdout
        print(e)