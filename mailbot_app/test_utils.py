#!./env/bin/python3
import unittest
import utils as ut
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


# MAnual Test
def main():
    testUtils = TestUtils()
    testUtils.test_checkForPurchases()
    testUtils.test_checkForPayments()

# Attribute main call to mailbot_app
if __name__ == '__main__':
    # # Automatic Testing
    unittest.main()
    # MAnual Testing
    # main()