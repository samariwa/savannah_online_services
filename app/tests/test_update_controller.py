import unittest
from app import app, db
app.app_context().push()
from app.controllers.update import *
from app.controllers.read import *

class TestUpdateController(unittest.TestCase):
    def test_update_customer(self):
        """
        Tests the update_customer controller function
        """
        # fetch the old customer details [before update]
        old_customer_details = fetch_customer(3)
        old_name = old_customer_details.first_name
        # create customer object kwargs with values to update
        customer1_data = {
                 'id': 3,
                 'first_name':'AAAA', 
                 'last_name':'ZZZZ',
                 'phone_no':'+254712934542'
        }
        # The test below checks for the case where the customer is successfully updated
        self.assertEqual(update_customer(**customer1_data), 'OK')
        # create customer object kwargs with values to update
        customer2_data = {
                 'id': 4,
                 'first_name':'YYYY', 
                 'last_name':'ZZZZ',
                 'phone_no':'+254798989898'
        }
        # The test below checks for the case where the phone_no is already in registered
        self.assertEqual(update_customer(**customer2_data), 'IntegrityError')
        db.session.rollback()
        # fetch the new customer details [after update]
        new_customer_details = fetch_customer(3)
        new_name = new_customer_details.first_name
        # The test below check that the old and new customer details are not the same e.g. first_name
        self.assertNotEqual(old_name, new_name)
        

    def test_update_order(self):
        """
        Tests the update_order controller function
        """
        # fetch the old order details [before update]
        old_order_details = fetch_order(2)
        old_amt = old_order_details.amount
        # create order object kwargs with values to update
        order1_data = {
                 'id': 2,
                 'amount':'2500'
        }
        # The test below checks for the case where the order is successfully updated
        self.assertEqual(update_order(**order1_data), 'OK')
         # fetch the new order details [new update]
        new_order_details = fetch_order(2)
        new_amt = new_order_details.amount
        # The test below check that the old and new order details are not the same e.g. amount
        self.assertNotEqual(old_amt, new_amt)