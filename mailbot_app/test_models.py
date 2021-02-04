#!./env/bin/python3
import unittest
import datetime
import models as md
# from models import *
import time


class TestModels(unittest.TestCase):

    def test_addNewClient(self):

        # Add a Client with already exists
        client = md.Client()
        client.cpf = '092.329.507-07'
        client.name = 'Sergio Ribeiro'
        client.email = 'ssribeiro@gmail.com'
        client.mobile = 21998052210
        client.address = 'Rua Stanley Gomes, 131, Casa - Rio de Janeiro - RJ'
        return self.assertTrue(client.add(md.Session()))

    def test_addExistingClient(self):

        # Add a Client with already exists
        client = md.Client()
        client.cpf = '102.821.607-60'
        client.name = 'Priscilla Varges'
        client.email = 'pri_varges@yahoo.com.br'
        client.mobile = 21996266824
        client.address = 'Rua Stanley Gomes, 131, Casa - Rio de Janeiro - RJ'
        return self.assertFalse(client.add(md.Session()))
    
    def test_getExistingClientByCPF(self,cpf):

        # Add a Client with already exists
        try:
            client = md.Session().query(md.Client).filter(md.Client.cpf == cpf).first()
            return self.assertIsInstance(client,md.Client)
        except:
            return False
        
    # def test_addOrder(self):
    #     # Add a Client
    #     order = md.Order()
    #     order.id = 1098
    #     order.datetime = datetime.datetime.utcnow
    #     order.email = 'pri_varges@yahoo.com.br'
    #     order.shipment_method = 'Motoboy'
    #     order.shipment_price = 9.00

    #     clientCPF = Client()

    #     order.client = 

# MAnual Test
def main():
    testModels = TestModels()
    testModels.test_addClient()
    
# Attribute main call to mailbot_app
if __name__ == '__main__':
    # # Automatic Testing
    unittest.main()
    # MAnual Testing
    # main()