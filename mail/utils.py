import os
import smtplib, imaplib, email
from bs4 import BeautifulSoup
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv 
from datetime import datetime
# from imap_tools import Q, AND, OR, NOT


# def buildFilterQuery(fieldsDict):
    
#     filterQuery = 
    
#     return filterQuery

# Email Server Class
class EmailServer():

    def __init__(self,dotEnv_path=None):
        load_dotenv()
        # load_dotenv(dotEnv_path)
        self.SMTP_SERVER = os.environ.get('SMTP_SERVER')
        self.IMAP_SERVER = os.environ.get('IMAP_SERVER')
        self.SMTP_PORT = os.environ.get('SMTP_PORT')
        self.EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
        self.EMAIL_PASSWORD = os.environ.get('APP_PASS')
        self.TIME_FORMAT = os.environ.get('TIME_FORMAT')
        print(self.SMTP_PORT)
        print(self.IMAP_SERVER)

    # Method: Check for mails in certain mailbox and filter query
    def checkForMails(self,mailbox='INBOX',filterQuery='UNSEEN'):
        # Context
        with imaplib.IMAP4_SSL(self.IMAP_SERVER) as imap:
            # Login
            typ, _ =imap.login(self.EMAIL_ADDRESS,self.EMAIL_PASSWORD)
            print(typ)
            # Select Mailbox
            imap.select(mailbox)

            #Search on specific folder/marker
            _,search_data, = imap.search(None,filterQuery)
            
            mailIDs = search_data[0].split()
            print(len(mailIDs))
            return imap, mailIDs, len(mailIDs)

    def readMessages(self,mailbox='INBOX',filterQuery='UNSEEN',htmlFile = None):

        # #Check for Mails
        # imap,mailIDs,numOfMails = self.checkForMails(mailbox,filterQuery)

        # Context
        with  imaplib.IMAP4_SSL(self.IMAP_SERVER) as imap:
            # Login
            typ, _ =imap.login(self.EMAIL_ADDRESS,self.EMAIL_PASSWORD)   
            messagesList = []
            # Select Mailbox
            imap.select(mailbox)

            #Search on specific folder/marker
            _,search_data, = imap.search(None,filterQuery)
            # Split Mail IDs
            mailIDs = search_data[0].split()
            
            # Loop over search results
            for mailID in mailIDs:
                messageDict = {}
                # Get mail data
                _,mailData = imap.fetch(mailID,'(RFC822)')
                # Collect message from mail data
                _,mail_bytes = mailData[0]
                # Scrape mail with BeatifulSoup Library
                soup = BeautifulSoup(mail_bytes, 'lxml')
                # print(soup.prettify())
                
                # If desired write html file with mail content
                if (htmlFile != None):
                        # File Context
                    with open(htmlFile, "w") as file:
                        # write message into html File
                        file.write(str(soup))
                

                emailMessage = email.message_from_bytes(mail_bytes)
                
                # Read Mail Header
                email_header = {}
                for headerTag in ['subject','to','from','date']:
                    
                    if headerTag == 'date':
                        dateTimeData = datetime.strptime(emailMessage[headerTag],self.TIME_FORMAT)
                        email_header[headerTag] = dateTimeData.timestamp()
                        # email_header['Timezone'] = dateTimeData.timetz().tzname()
                    else:
                        email_header[headerTag] = emailMessage[headerTag]

                    print("{}:{}".format(headerTag,email_header[headerTag])) 
                                    
                # Sets Dict Header
                messageDict['header'] = email_header
                
                # Read Mail Body
                for part in emailMessage.walk():
                    if part.get_content_type()=="text/plain":
                        email_body = part.get_payload(decode=True).decode()

                    elif part.get_content_type()=="text/html":
                        email_body = part.get_payload(decode=True).decode()

                # Sets Dict Body 
                messageDict['body'] = email_body
                print(messageDict)
                #Append to messages list
                messagesList.append(messageDict)

        return messagesList    


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
            msg['Cc'] = recipients['Cc']
            msg.attach(MIMEText(body, 'plain'))
            
            # Send Mail
            try:
                # TODO: Set SSL Connection
                # # Create a secure SSL context
                # context = ssl.create_default_context()
                
                # Send Email
                smtp.sendmail(from_addr=msg['From'],to_addrs=msg['To'],msg=msg.as_string())
                print('Mail sent successfully!')
                
                return True,None
            except Exception as e:
                # Print any error messages to stdout
                print(e)
                return False,e