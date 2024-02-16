import unittest
from app.models import *

class TestUser(unittest.TestCase):
    def test_user_object_creation(self):
        user1 = User(first_name='XXXX', 
                     last_name='XXXX',
                     user_status='active',
                     email_address='XXXX@domain.com',
                     password='*******'
                     )
        
        self.assertEqual(user1.first_name, 'XXXX')
        self.assertEqual(user1.last_name, 'XXXX')
        self.assertEqual(user1.user_status, 'active')
        self.assertEqual(user1.email_address, 'XXXX@domain.com')

class TestCustomer(unittest.TestCase):
    def test_customer_object_creation(self):
        pass

class TestOrder(unittest.TestCase):
    def test_order_object_creation(self):
        pass