import unittest
from app.general_functions import get_uuid, generate_random_string
from app.models import *

class TestUser(unittest.TestCase):
    def test_user_object_creation(self):
        """
        Tests the User object creation
        """
        #create a user object
        user1 = User(first_name='XXXX', 
                     last_name='XXXX',
                     user_status='active',
                     email_address='XXXX@domain.com',
                     password='*******'
                     )
        # Checking for the attributes of the created object
        self.assertEqual(user1.first_name, 'XXXX')
        self.assertEqual(user1.last_name, 'XXXX')
        self.assertEqual(user1.user_status, 'active')
        self.assertEqual(user1.email_address, 'XXXX@domain.com')

class TestCustomer(unittest.TestCase):
    def test_customer_object_creation(self):
        """
        Tests the Customer object creation
        """
        # create a customer object
        customer1 = Customer(
                     customer_code=get_uuid(),
                     first_name='YYYY', 
                     last_name='YYYY',
                     phone_no='+254712932815'
                     )
        # Checking for the attributes of the created object
        self.assertEqual(len(customer1.customer_code), 36)
        self.assertEqual(customer1.first_name, 'YYYY')
        self.assertEqual(customer1.last_name, 'YYYY')     
        self.assertEqual(customer1.phone_no, '+254712932815')

class TestOrder(unittest.TestCase):
    def test_order_object_creation(self):
        """
        Tests the Order object creation
        """
        # create an order object
        order1 = Order(
                     order_ref=generate_random_string(8),
                     customer_id=45, 
                     amount=3000,
                     time='12:34:45'
                     )
        # Checking for the attributes of the created object
        self.assertEqual(len(order1.order_ref), 8)
        self.assertEqual(order1.customer_id, 45)
        self.assertEqual(order1.amount, 3000)     
        self.assertEqual(order1.time, '12:34:45')