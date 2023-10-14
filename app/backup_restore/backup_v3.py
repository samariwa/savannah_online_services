from app import app
import json
from app.general_functions import stringify_datetime_object, datetime_to_standard_date,\
    is_datetime_object, is_date_object, date_today
from app.models import *
from app.controllers.read import fetch_all_departments, fetch_all_users,\
    fetch_all_roles, fetch_all_staff, fetch_all_customers, fetch_all_customer_accounts,\
    fetch_all_customer_refunds, fetch_all_product_categories, fetch_all_product_units,\
    fetch_all_products, fetch_all_product_batches, fetch_all_account_verifications,\
    fetch_all_logged_devices, fetch_all_newsletter_subscribers, fetch_all_cart_data,\
    fetch_all_wishlist_data, fetch_all_product_reclass_categories, fetch_all_suppliers,\
    fetch_all_product_reclass_items, fetch_all_product_reclass_details, fetch_all_expenses,\
    fetch_all_product_movement_records, fetch_all_expense_categories, fetch_all_orders,\
    fetch_all_expense_payment_details,fetch_all_mpesa_payments, fetch_all_order_details,\
    fetch_all_transaction_details, fetch_all_deliveries, fetch_all_stk_push_results,\
    fetch_all_stk_customer_responses, fetch_all_customer_account_transactions
from app.aws.s3.backup_upload import upload_backup_file

backup_data = {}
date = date_today()
backup_location = 'app/backup_restore/backup_files/backup_data_'+date+'.json'

def get_model_attributes(class_name):
    """
    This function fetches the attributes of the slqalchemy model
    passed in as a parameter
    """
    return [
        column.name for column in class_name.__table__.columns
    ]


system_data = {
    'department_data': {
        'fxn': fetch_all_departments,
        'attributes': get_model_attributes(Department)
    },

    'staf_role_data': {
        'fxn': fetch_all_roles,
        'attributes': get_model_attributes(Staff_Role)
    },

    'staff_data': {
        'fxn': fetch_all_staff,
        'attributes': get_model_attributes(Staff)
    },

    'customer_data': {
        'fxn': fetch_all_customers,
        'attributes': get_model_attributes(Customer)
    },

    'user_data': {
        'fxn': fetch_all_users,
        'attributes': get_model_attributes(User)
    },

    'account_verification_data': {
        'fxn': fetch_all_account_verifications,
        'attributes': get_model_attributes(Account_Verification)
    },

    'logged_device_data': {
        'fxn': fetch_all_logged_devices,
        'attributes': get_model_attributes(Logged_Devices)
    },

    'cart_data': {
        'fxn': fetch_all_cart_data,
        'attributes': get_model_attributes(Cart)
    },

    'wishlist_data': {
        'fxn': fetch_all_wishlist_data,
        'attributes': get_model_attributes(Wishlist)
    },

    'newsletter_subscriber_data': {
        'fxn': fetch_all_newsletter_subscribers,
        'attributes': get_model_attributes(Newsletter_Subscribers)
    },

    'customer_account_data': {
        'fxn': fetch_all_customer_accounts,
        'attributes': get_model_attributes(Customer_Account)
    },

    'customer_refund_data': {
        'fxn': fetch_all_customer_refunds,
        'attributes': get_model_attributes(Customer_Refunds)
    },

    'customer_account_transaction_data': {
        'fxn': fetch_all_customer_account_transactions,
        'attributes': get_model_attributes(Customer_Account_Transaction)
    },

    'product_category_data': {
        'fxn': fetch_all_product_categories,
        'attributes': get_model_attributes(Product_Category)
    },

    'product_unit_data': {
        'fxn': fetch_all_product_units,
        'attributes': get_model_attributes(Product_Unit)
    },

    'product_data': {
        'fxn': fetch_all_products,
        'attributes': get_model_attributes(Product)
    },

    'supplier_data': {
        'fxn': fetch_all_suppliers,
        'attributes': get_model_attributes(Supplier)
    },

    'product_batch_data': {
        'fxn': fetch_all_product_batches,
        'attributes': get_model_attributes(Product_Batch)
    },

    'product_reclass_category_data': {
        'fxn': fetch_all_product_reclass_categories,
        'attributes': get_model_attributes(Product_Reclass_Category)
    },

    'product_reclass_item_data': {
        'fxn': fetch_all_product_reclass_items,
        'attributes': get_model_attributes(Product_Reclass_Item)
    },

    'product_reclass_detail_data': {
        'fxn': fetch_all_product_reclass_details,
        'attributes': get_model_attributes(Product_Reclass_Detail)
    },

    'product_movement_data': {
        'fxn': fetch_all_product_movement_records,
        'attributes': get_model_attributes(Product_Movement)
    },

    'expense_category_data': {
        'fxn': fetch_all_expense_categories,
        'attributes': get_model_attributes(Expense_Category)
    },

    'expense_data': {
        'fxn': fetch_all_expenses,
        'attributes': get_model_attributes(Expense)
    },

    'expense_payment_detail_data': {
        'fxn': fetch_all_expense_payment_details,
        'attributes': get_model_attributes(Expense_Payment_Detail)
    },

    'mpesa_payment_data': {
        'fxn': fetch_all_mpesa_payments,
        'attributes': get_model_attributes(Mpesa_Payment)
    },

    'order_data': {
        'fxn': fetch_all_orders,
        'attributes': get_model_attributes(Order)
    },

    'order_detail_data': {
        'fxn': fetch_all_order_details,
        'attributes': get_model_attributes(Order_Detail)
    },

    'transaction_detail_data': {
        'fxn': fetch_all_transaction_details,
        'attributes': get_model_attributes(Transaction_Detail)
    },

    'delivery_data': {
        'fxn': fetch_all_deliveries,
        'attributes': get_model_attributes(Delivery)
    },

    'stk_push_result_data': {
        'fxn': fetch_all_stk_push_results,
        'attributes': get_model_attributes(Stk_Push_Result)
    },

    'stk_customer_response_data': {
        'fxn': fetch_all_stk_customer_responses,
        'attributes': get_model_attributes(Stk_Push_Customer_Response)
    },
}

def prepare_backup_file():
    app.logger.info('preparing for system data backup...')
    open(backup_location, "w").close()
    app.logger.info('backup preparation complete...')


def run_backup():
    """
    This function loopes through the tables defined in the system data
    dictionary and fetches their corresponding 'fetch_all_...' functions and
    attributes for the purpose of creating the JSON data with all the data objects
    The JSON file is written in a .json file as its backup destination
    """
    try:
        # loop through all the models in the system data dict
        for model_key, data in system_data.items():
            # log beginning of model data
            app.logger.info(f"backing up {model_key.replace('_', ' ')}...")
            """
            create a list that will store all JSON data for a model. Each json
            string contains a row of data
            """
            model_data = []
            """
            call the data fetch function associated with the model and 
            store the results in a variable
            """
            table = data['fxn']()
            """
            Loop through each object of the data fetched. This data is in form of
            a list of objects
            """
            for row in table:
                # create an empty dictionary that will carry row attribute and values
                values = {}
                for attribute in data['attributes']:
                    # get the attribute values from the object
                    value = eval(f"row.{attribute}")
                    """
                    If the value is a data or datatime object and is not None, 
                    stringify it. Timestamps from the objects are returned as 
                    datetime objects but we need them at strings
                    """
                    if is_datetime_object(value) and value is not None:
                        value = stringify_datetime_object(value)
                    elif is_date_object(value) and value is not None:
                        value = datetime_to_standard_date(value)
                    # add the key(attr) and value to the empty dictionary we created
                    values[attribute] = value
                # add the dictionary (row) to the list that carries the entire model data
                model_data.append(values)
                """
                add the model data list to the global data dictionary that will be 
                written in the backup file
                """
            backup_data[model_key] = model_data
            # log completion of the model backup
            app.logger.info(f"{model_key.replace('_', ' ')} backup complete")
        # After alll loops (models) log backup completion
        app.logger.info('finishing up backup job...')
        # dump the global json with all data into the backup destination file
        with open(backup_location, 'a') as fp:
            json.dump(backup_data, fp, indent=4)
            fp.close()
        # log completion of backup process
        app.logger.info("data backup completed successfully")
        # upload file to AWS
        return upload_backup_file(backup_location, f"{date}.json")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))
