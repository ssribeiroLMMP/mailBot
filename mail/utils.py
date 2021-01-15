import os
import smtplib
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailServer():
    def __init__(self,dotEnv_path=None):
        # load_dotenv(dotEnv_path)
        self.SMTP_SERVER = os.environ.get('SMTP_SERVER')
        self.SMTP_PORT = os.environ.get('SMTP_PORT')
        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('APP_PASS')

    def sendMessage(self,recipients,subject,body):
        
        # Context 
        with smtplib.SMTP_SSL(self.SMTP_SERVER, self.SMTP_PORT) as smtp:
            # smtp.ehlo()
            # smtp.starttls()
            # smtp.ehlo()
            
            # Login
            smtp.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
            
            # MultiPart Mail - 
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = self.EMAIL_ADDRESS
            msg['To'] = recipients['To']
            msg.attach(MIMEText(body, 'plain'))
            
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