#!./env/bin/python3
import unittest
import utils as ut
import time
from dotenv import load_dotenv 

class TestUtils(unittest.TestCase):

    # Test class population
    def test_loadDotEnv(self):
        load_dotenv()
        emailServer = ut.EmailServer()
        self.assertIsNotNone(emailServer.SMTP_PORT,msg='Is None!')

    def test_sendMail(self):
        emailServer = ut.EmailServer()
        recipients = {'To':'sergio@lmmp.mec.puc-rio.br',
            'Cc':'ssribeiro@gmail.com'}

        subject = 'New Test Message'
        body = 'How about dinner at 6pm this saturday?'
        
        # Test
        result,exception = emailServer.sendMessage(recipients,subject,body)
        self.assertTrue(result)
        print(exception)

# Attribute main call to mailbot_app
if __name__ == '__main__':
    unittest.main()