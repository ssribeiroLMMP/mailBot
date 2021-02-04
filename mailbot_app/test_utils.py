#!./env/bin/python3
import unittest
import utils as ut
# from models import *
import time


class TestUtils(unittest.TestCase):
    def test_checkForPurchases(self):
        # Check for purchase mails
        mailIDs, lenMailIDs = ut.checkForPurchases()
        
        return self.assertIsNotNone(mailIDs),self.assertGreater(lenMailIDs,0)

    def test_checkForPayments(self):
        # Check for paymento confirmation mails
        mailIDs, lenMailIDs = ut.checkForPayments()
        
        return self.assertIsNotNone(mailIDs),self.assertGreater(lenMailIDs,0)

    def test_logRecentPurchasesHTML(self):
        # Check for paymento confirmation mails
        recentPurchasesList = ut.logRecentPurchasesHTML()
        
        return self.assertTrue(len(ut.os.listdir('./temp')) == len(recentPurchasesList))
    
    # def test_models(self):
    #     # Check for paymento confirmation mails
        
        
    #     return self.assertTrue(len(ut.os.listdir('./temp')) == len(recentPurchasesList))



# MAnual Test
def main():
    testUtils = TestUtils()
    # testUtils.test_checkForPurchases()
    # testUtils.test_checkForPayments()
    testUtils.test_logRecentPurchasesHTML()
    testUtils.test_models()

# Attribute main call to mailbot_app
if __name__ == '__main__':
    # # Automatic Testing
    unittest.main()
    # MAnual Testing
    # main()