import unittest
from app import app
app.app_context().push()
from app.controllers.delete import *
from app.controllers.read import *

class TestDeleteController(unittest.TestCase):
    def test_delete_customer(self):
        """
        Tests the delete_customer controller function
        """
        # fetch the old customer details [before deletion]
        old_customer_details = fetch_customer(4)
        old_db_status = old_customer_details.db_status
        # The test below checks for the case where the customer is successfully deleted
        self.assertEqual(delete_customer(4), 'OK')
        # fetch the new customer details [after deletion]
        new_customer_details = fetch_customer(4)
        new_db_status = new_customer_details.db_status
        # check that the old and new db_status are different
        self.assertNotEqual(old_db_status, new_db_status)
        # check that the old db status was active
        self.assertEqual(old_db_status, 'active')
        # check that the new db status is deleted
        self.assertEqual(new_db_status, 'deleted')

    def test_delete_order(self):
        """
        Tests the delete_order controller function
        """
        # fetch the old order details [before deletion]
        old_order_details = fetch_order(2)
        old_db_status = old_order_details.db_status
        # The test below checks for the case where the order is successfully deleted
        self.assertEqual(delete_order(2), 'OK')
        # fetch the new order details [after deletion]
        new_order_details = fetch_order(2)
        new_db_status = new_order_details.db_status
        # check that the old and new db_status are different
        self.assertNotEqual(old_db_status, new_db_status)
        # check that the old db status was active
        self.assertEqual(old_db_status, 'active')
        # check that the new db status is deleted
        self.assertEqual(new_db_status, 'deleted')