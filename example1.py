import os
import smtplib
import imghdr
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('APP_PASS')

print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

# with smtplib.SMTP_SSL('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
    
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    
#     subject = 'Grav dinner this weekend'
#     body = 'How about dinner at 6pm this saturday?'
    
#     msg = f'Subject:{subject} \n\n {body}
#     print(msg)
#     smtp.sendmail(EMAIL_ADDRESS, 'sergio@lmmp.mec.puc-rio.br')