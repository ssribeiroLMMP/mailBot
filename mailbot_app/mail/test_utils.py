#!./env/bin/python3
import unittest
import utils as ut
import time

class TestUtils(unittest.TestCase):

    # Test class population
    def test_loadDotEnv(self):
        emailServer = ut.EmailServer()
        return self.assertIsNotNone(emailServer.SMTP_PORT,msg='Is None!')

    # Test send message method
    def test_sendMessage(self):
        emailServer = ut.EmailServer()
        recipients = {'To':'sergio@lmmp.mec.puc-rio.br', # 'lojavirtual@stelio.com.br',# 
            'Cc':'ssribeiro@gmail.com'}

        subject = 'New Test Message'
        body = 'How about dinner at 6pm this saturday?'
        
        # Check if Result is True
        result,exception = emailServer.sendMessage(recipients,subject,body)
        return self.assertTrue(result)

    # Test Check for Mails method
    def test_checkForMails(self):
        mailbox='INBOX'
        filterQuery='UNSEEN'
        #Check for Mails
        emailServer = ut.EmailServer()
        imap,mailIDs,numOfMails = emailServer.checkForMails(mailbox,filterQuery)
        
        # Chech if it returns a number greater than zero
        return self.assertGreater(numOfMails,0)

    # Test Check for Mails method
    def test_readMessages(self,mailbox='INBOX',filterQuery='UNSEEN'):
        
        #Check for Mails
        emailServer = ut.EmailServer()
        messagesList = emailServer.readMessages(mailbox=mailbox,filterQuery=filterQuery,htmlFile = None)
        
        # Check if it returns a list
        return self.assertIsInstance(messagesList,type([1,2]))
    
def main():
    testUtils = TestUtils()
    testUtils.test_readMessages(mailbox='INBOX',filterQuery='(FROM "nao-responder@mercadolivre.com") (SUBJECT "A sua encomenda") (UNSEEN)')

# Attribute main call to mailbot_app
if __name__ == '__main__':
    # Automatic Testing
    # unittest.main()
    # # Manual Testing(Debug)
    main()