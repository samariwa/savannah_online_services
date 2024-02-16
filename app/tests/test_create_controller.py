import unittest
from app import app
app.app_context().push()
from app.controllers.create import *
from app.general_functions import get_uuid, generate_random_string

class TestCreateController(unittest.TestCase):
    def test_create_user(self):
        """
        Tests the create_user controller function
        """
        # create user object kwargs
        user1_data = {
                 'first_name':'XXXX', 
                 'last_name':'XXXX',
                 'user_status':'active',
                 'email_address':'XXXX@domain.com',
                 'password':'*******'
        }
        # The test below checks for the case where the user is successfully created
        self.assertEqual(create_user(**user1_data), 'Created')
        # The test below checks for the case where the email address is already registered
        self.assertEqual(create_user(**user1_data), 'IntegrityError')
        # create user object kwargs
        user2_data = {'first_name':'YYYY', 
                 'last_name':'YYYY',
                 'user_status':'value_not_in_enum',
                 'email_address':'YYYY@domain.com',
                 'password':'*******'
        }
        # The test below checks for the case where a wrong user_status enum value is passed
        self.assertEqual(create_user(**user2_data), 'DataError')

    def test_create_customer(self):
        """
        Tests the create_customer controller function
        """
        # create customer object kwargs
        customer1_data = {
                 'customer_code': get_uuid(),
                 'first_name':'XXXX', 
                 'last_name':'XXXX',
                 'phone_no':'+254713924502'
        }
        # The test below checks for the case where the customer is successfully created
        self.assertEqual(create_customer(**customer1_data), 'Created')
        # The test below checks for the case where the phone_no is already in registered
        self.assertEqual(create_customer(**customer1_data), 'IntegrityError')

    def test_create_order(self):
        """
        Tests the create_order controller function
        """
        # create order object kwargs
        order1_data = {
                 'customer_id': 1,
                 'order_ref': generate_random_string(10),
                 'amount':'2300', 
                 'time':'13:00'
        }
        # The test below checks for the case where the order is successfully created
        self.assertEqual(create_order(**order1_data), 'Created')
        # The test below checks for the case where the order_ref # is existing
        self.assertEqual(create_order(**order1_data), 'IntegrityError')
    
        
