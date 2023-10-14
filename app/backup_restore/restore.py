from app.controllers.create import *
from app.controllers.update import update_customer_account_attributes
from app.general_functions import date_today
import json

date = date_today()
backup_location = 'app/backup_restore/backup_files/backup_data_'+date+'.json'

key_function_mapper = {
    'department_data': 'create_department',
    'staff_role_data': 'create_staff_role',
    'staff_data': 'create_staff',
    'customer_data': 'create_customer',
    'user_data': 'create_user',
    'account_verification_data': 'create_account_verification_entry',
    'logged_device_data': 'create_device_log',
    'cart_data': 'create_cart_entry',
    'wishlist_data': 'create_wishlist_entry',
    'newsletter_subscriber_data': 'create_newsletter_subscriber',
    'customer_account_data': 'update_customer_account_attributes',
    'customer_refund_data': 'create_customer_refund',
    'customer_account_transaction_data': 'create_customer_account_transaction',
    'product_category_data': 'create_product_category',
    'product_unit_data': 'create_product_unit',
    'product_data': 'create_product',
    'supplier_data': 'create_supplier',
    'product_batch_data': 'create_product_batch',
    'product_reclass_category_data': 'create_reclass_category',
    'product_reclass_item_data': 'create_reclass_item',
    'product_reclass_detail_data': 'create_reclass_detail',
    'product_movement_data': 'create_prod_mvt',
    'expense_category_data': 'create_expense_category',
    'expense_data': 'create_expense',
    'mpesa_payment_data': 'create_mpesa_payment',
    'order_data': 'create_order',
    'order_detail_data': 'create_order_detail',
    'transaction_detail_data': 'create_transaction_detail',
    'delivery_data': 'create_delivery',
    'stk_push_result_data': 'create_stk_push_result',
    'stk_customer_response_data': 'create_stk_push_customer_response',
}
# Global variable to store the JSON data
restoration_data = {}

def prepare_data_restoration():
    # Drop all the tables at once
    db.drop_all()
    # Create all the tables at once
    db.create_all()
    global restoration_data
    app.logger.info('preparing for system data restoration...')
    with open(backup_location, 'r') as fp:
        restoration_data = json.load(fp)
        fp.close()
    app.logger.info('restoration preparation complete...')

def restore_data():
    """
    restore_data()

    This function executes a restore operation by fetching the data
    that is store in the json file.
    It loops through the json file and gets each dictionary of data
    and passes them to the sqlalchemy bulk create function that coincides
    the data
    """

    # Sample JSON data representing multiple users
    for key in restoration_data.keys():
        object_storage = []
        for object in restoration_data[key]:
            # Access the function using globals() or locals()
            create_function = globals().get(key_function_mapper[key])
            # Check if the function exists and is callable
            if create_function is not None and callable(create_function):
                # Execute function
                create_function(**object)
    app.logger.info('restoration job complete ...')
    app.logger.info('cleaning up...')
    app.logger.info('restoration successfully completed')