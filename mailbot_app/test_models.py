#!./env/bin/python3
import unittest
import datetime
import models as md
# from models import *
import time


class TestModels(unittest.TestCase):

    def test_addNewClient(self):

        # Add a Client which does not exist in Database
        client = md.Client()
        client.cpf = '092.329.507-07'
        client.name = 'Sergio Ribeiro'
        client.email = 'ssribeiro@gmail.com'
        client.mobile = 21998052210
        client.address = 'Rua Stanley Gomes, 131, Casa - Rio de Janeiro - RJ'
        return self.assertTrue(client.add(md.Session()))

    def test_addNewClient_2(self):

        # Add a Client which does not exist in Database
        client = md.Client()
        client.cpf = '102.821.607-61'
        client.name = 'Priscilla Varges Dopelganger'
        client.email = 'pri_varges@yahoo.com.br'
        client.mobile = 2132154656
        client.address = 'Rua Stanley Gomes, 131, Casa - Rio de Janeiro - RJ'
        return self.assertTrue(client.add(md.Session()))

    def test_addExistingClient(self):

        # Add a Client which already exists
        client = md.Client()
        client.cpf = '102.821.607-60'
        client.name = 'Priscilla Varges'
        client.email = 'pri_varges@yahoo.com.br'
        client.mobile = 21996266824
        client.address = 'Rua Stanley Gomes, 131, Casa - Rio de Janeiro - RJ'
        return self.assertFalse(client.add(md.Session()))
    
    # def test_getExistingClientByCPF(self,cpf):

    #     # Add a Client with already exists
    #     try:
    #         client = md.Session().query(md.Client).filter(md.Client.cpf == cpf).first()
    #         return self.assertIsInstance(client,md.Client)
    #     except:
    #         return False
        
    def test_addOrder(self):
        
        # Add a Client
        order = md.Order()
        order.number = 1096
        order.datetime = datetime.datetime.utcnow()
        order.client = '102.821.607-60'
        order.shipment_method = 'Motoboy'
        order.shipment_price = 9.00
        order.subtotal = 20.0
        return self.assertTrue(order.add(md.Session()))

    def test_addOrderItem(self):
        # Add a Client
        orderItem = md.OrderItem()
        orderItem.order_number = 1095
        orderItem.item_id = 1
        orderItem.description = 'Item de teste'
        orderItem.quantity = 10
        orderItem.unit_price = 9.00
        return self.assertTrue(orderItem.add(md.Session()))   

# MAnual Test
def main():
    testModels = TestModels()
    # testModels.test_addClient()
    # testModels.test_addNewClient()
    # testModels.test_addNewClient_2()
    # testModels.test_addExistingClient()
    # testModels.test_addOrder()
    # testModels.test_addOrderItem()
    
# Attribute main call to mailbot_app
if __name__ == '__main__':
    # # Automatic Testing
    # unittest.main()
    # Manual Testing
    main()