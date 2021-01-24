#!./env/bin/python3
import unittest
import utils as ut
import time


class TestUtils(unittest.TestCase):
    def test_checkForPurchases(self):
        # Che
        mailIDs, lenMailIDs = ut.checkForPurchases()
        
        return self.assertIsNotNone(mailIDs),self.assertGreater(lenMailIDs,0)

# MAnual Test
def main():
    testUtils = TestUtils()
    testUtils.test_checkForPurchases()

# Attribute main call to mailbot_app
if __name__ == '__main__':
    # # Automatic Testing
    unittest.main()
    # MAnual Testing
    # main()