from app import app
import json
from app.general_functions import stringify_datetime_object, datetime_to_standard_date,\
date_today
from app.controllers.read import fetch_all_departments, fetch_all_users,\
fetch_all_roles, fetch_all_staff, fetch_all_customers, fetch_all_customer_accounts,\
fetch_all_customer_refunds, fetch_all_product_categories, fetch_all_product_units,\
fetch_all_products, fetch_all_product_batches, fetch_all_account_verifications,\
fetch_all_logged_devices, fetch_all_newsletter_subscribers, fetch_all_cart_data,\
fetch_all_wishlist_data, fetch_all_product_reclass_categories, fetch_all_suppliers,\
fetch_all_product_reclass_items, fetch_all_product_reclass_details

backup_data = {}
date = date_today()
backup_location = 'app/backup_restore/backup_files/backup_data_'+date+'.json'

def prepare_backup_file():
    app.logger.info('preparing for system data backup...')
    open(backup_location, "w").close()
    app.logger.info('backup preparation complete...')

def run_backup():
    app.logger.info('starting backup...')
    backup_departments()
    backup_staff_roles()
    backup_staff()
    backup_customers()
    backup_users()
    backup_account_verification_data()
    backup_logged_devices_data()
    backup_cart_data()
    backup_wishlist_data()
    backup_newsletter_subscribers_data()
    backup_customer_account_data()
    backup_customer_refund_data()
    backup_product_category_data()
    backup_product_unit_data()
    backup_product_data()
    backup_supplier_data()
    backup_product_batch_data()
    backup_product_reclass_category_data()
    backup_product_reclass_item_data()
    backup_product_reclass_detail_data()
    app.logger.info('finishing up backup job...')
    with open(backup_location, 'a') as fp:
        json.dump(backup_data, fp, indent=4)
        fp.close()
    app.logger.info("data backup completed successfully")

def backup_departments():
    try:
        app.logger.info("backing up department data...")  
        departments = fetch_all_departments()
        department_data = []
        for data in departments:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                        'department': data.department,
                        'db_status': data.db_status, 
                        'created_at': stringify_datetime_object(data.created_at),
                        'updated_at': updated_at}
            department_data.append(values)
        backup_data['department_data'] = department_data         
        app.logger.info("department data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_staff_roles():
    try:
        app.logger.info("backing up staff roles data...")
        staff_roles = fetch_all_roles()
        staff_role_data = []
        for data in staff_roles:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                        'department_id': data.department_id,
                        'role': data.role,
                        'db_status': data.db_status, 
                        'created_at': stringify_datetime_object(data.created_at),
                        'updated_at': updated_at}
            staff_role_data.append(values)
        backup_data['staff_role_data'] = staff_role_data
        app.logger.info("staff roles data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_staff():
    try:
        app.logger.info("backing up staff data...")
        staff = fetch_all_staff()
        staff_data = []
        for data in staff:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'role_id': data.role_id,
                      'first_name': data.first_name,
                      'last_name': data.last_name,
                      'id_number': data.id_number,
                      'yob': data.yob,
                      'gender': data.gender,
                      'nssf_number': data.nssf_number,
                      'nhif_number': data.nhif_number,
                      'db_status': data.db_status, 
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            staff_data.append(values)
        backup_data['staff_data'] = staff_data
        app.logger.info("staff data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_customers():
    try:
        app.logger.info("backing up customer data...")
        customers = fetch_all_customers()
        customer_data = []
        for data in customers:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'first_name': data.first_name,
                      'last_name': data.last_name,
                      'location': data.location,
                      'phone_no': data.phone_no,
                      'customer_type': data.customer_type,
                      'note': data.note,
                      'customer_status': data.customer_status,
                      'credit_customer': data.credit_customer,
                      'db_status': data.db_status, 
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            customer_data.append(values)
        backup_data['customer_data'] = customer_data
        app.logger.info("customer data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_users():
    try:
        app.logger.info("backing up user data...")
        users = fetch_all_users()
        user_data = []
        for data in users:
            last_activity = data.last_activity
            updated_at = data.updated_at
            if data.last_activity is not None:
                last_activity = stringify_datetime_object(data.last_activity)
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'customer_id': data.customer_id,
                      'staff_id': data.staff_id, 
                      'user_status': data.user_status,
                      'email_address': data.email_address, 
                      'login_status': data.login_status,
                      'last_activity': last_activity, 
                      'login_attempts': data.login_attempts,
                      'password_hash': data.password_hash,
                      'db_status': data.db_status, 
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            user_data.append(values)
        backup_data['user_data'] = user_data
        app.logger.info("user data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_account_verification_data():
    try:
        app.logger.info("backing up account verification data...")
        account_verification = fetch_all_account_verifications()
        account_verification_data = []
        for data in account_verification:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id,
                      'user_id': data.user_id, 
                      'token': data.token,
                      'token_expiry': stringify_datetime_object(data.token_expiry),
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            account_verification_data.append(values)
        backup_data['account_verification_data'] = account_verification_data
        app.logger.info("account verification data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_logged_devices_data():
    try:
        app.logger.info("backing up logged devices data...")
        logged_devices = fetch_all_logged_devices()
        logged_device_data = []
        for data in logged_devices:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'user_id': data.user_id,
                      'device_type': data.device_type,
                      'browser': data.browser,
                      'ip_address': data.ip_address,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            logged_device_data.append(values)
        backup_data['logged_device_data'] = logged_device_data
        app.logger.info("logged devices data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_cart_data():
    try:
        app.logger.info("backing up cart data...")
        cart = fetch_all_cart_data()
        cart_data = []
        for data in cart:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'customer_id': data.customer_id,
                      'product_id': data.product_id,
                      'quantity': data.quantity,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            cart_data.append(values)
        backup_data['cart_data'] = cart_data
        app.logger.info("cart data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_wishlist_data():
    try:
        app.logger.info("backing up wishlist data...")
        wishlist = fetch_all_wishlist_data()
        wishlist_data = []
        for data in wishlist:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'customer_id': data.customer_id,
                      'product_id': data.product_id,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            wishlist_data.append(values)
        backup_data['wishlist_data'] = wishlist_data
        app.logger.info("wislist data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_newsletter_subscribers_data():
    try:
        app.logger.info("backing up newsletter subscribers data...")
        newsletter_subscribers = fetch_all_newsletter_subscribers()
        newsletter_subscriber_data = []
        for data in newsletter_subscribers:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'registered_user': data.registered_user,
                      'email_address': data.email_address,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            newsletter_subscriber_data.append(values)
        backup_data['newsletter_subscriber_data'] = newsletter_subscriber_data
        app.logger.info("newsletter subscribers data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_customer_account_data():
    try:
        app.logger.info("backing up customer account data...")
        customer_accounts = fetch_all_customer_accounts()
        customer_account_data = []
        for data in customer_accounts:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'customer_id': data.customer_id,
                      'account_balance': data.account_balance,
                      'total_debt': data.total_debt,
                      'db_status': data.db_status, 
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            customer_account_data.append(values)
        backup_data['customer_account_data'] = customer_account_data
        app.logger.info("customer account data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_customer_refund_data():
    try:
        app.logger.info("backing up customer refund data...")
        customer_refunds = fetch_all_customer_refunds()
        customer_refund_data = []
        for data in customer_refunds:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'customer_account_id': data.customer_account_id,
                      'old_account_balance': data.old_account_balance,
                      'new_account_balance': data.new_account_balance,
                      'amount_refunded': data.amount_refunded,
                      'db_status': data.db_status,
                      'refund_date': datetime_to_standard_date(data.refund_date),
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            customer_refund_data.append(values)
        backup_data['customer_refund_data'] = customer_refund_data
        app.logger.info("customer refund data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_category_data():
    try:
        app.logger.info("backing up product category data...")
        product_categories = fetch_all_product_categories()
        product_category_data = []
        for data in product_categories:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'category_name': data.category_name,
                      'category_image': data.category_image,
                      'category_status': data.category_status,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_category_data.append(values)
        backup_data['product_category_data'] = product_category_data
        app.logger.info("product category data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_unit_data():
    try:
        app.logger.info("backing up product unit data...")
        product_units = fetch_all_product_units()
        product_unit_data = []
        for data in product_units:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'unit_name': data.unit_name,
                      'measurement_mode': data.measurement_mode,
                      'product_unit_status': data.product_unit_status,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_unit_data.append(values)
        backup_data['product_unit_data'] = product_unit_data
        app.logger.info("product unit data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_data():
    try:
        app.logger.info("backing up product data...")
        products = fetch_all_products()
        product_data = []
        for data in products:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'category_id': data.category_id,
                      'unit_id': data.unit_id,
                      'sub_unit_id': data.sub_unit_id,
                      'product_name': data.product_name,
                      'product_description': data.product_description,
                      'subunit_replenish_qty': data.subunit_replenish_qty,
                      'total_qty': data.total_qty,
                      'restock_level': data.restock_level,
                      'image': data.image,
                      'product_status': data.product_status,
                      'contains': data.contains,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_data.append(values)
        backup_data['product_data'] = product_data
        app.logger.info("product data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_supplier_data():
    try:
        app.logger.info("backing up supplier data...")
        suppliers = fetch_all_suppliers()
        supplier_data = []
        for data in suppliers:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'supplier_name': data.supplier_name,
                      'supplier_contact': data.supplier_contact,
                      'supplier_status': data.supplier_status,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            supplier_data.append(values)
        backup_data['supplier_data'] = supplier_data
        app.logger.info("supplier data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_batch_data():
    try:
        app.logger.info("backing up product batch data...")
        product_batches = fetch_all_product_batches()
        product_batch_data = []
        for data in product_batches:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'batch_id': data.batch_id, 
                      'product_id': data.product_id,
                      'supplier_id': data.supplier_id,
                      'qty_purchased': data.qty_purchased,
                      'current_qty': data.current_qty,
                      'damaged': data.damaged,
                      'date_received': datetime_to_standard_date(data.date_received),
                      'buying_price': data.buying_price,
                      'selling_discount': data.selling_discount,
                      'selling_price': data.selling_price,
                      'expiry_date': datetime_to_standard_date(data.expiry_date),
                      'batch_status': data.batch_status,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_batch_data.append(values)
        backup_data['product_batch_data'] = product_batch_data
        app.logger.info("product batch data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_reclass_category_data():
    try:
        app.logger.info("backing up product reclass category data...")
        product_reclass_categories = fetch_all_product_reclass_categories()
        product_reclass_category_data = []
        for data in product_reclass_categories:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'reclass_parent_product_id': data.reclass_parent_product_id,
                      'reclass_category_name': data.reclass_category_name,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_reclass_category_data.append(values)
        backup_data['product_reclass_category_data'] = product_reclass_category_data
        app.logger.info("product reclass category data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_reclass_item_data():
    try:
        app.logger.info("backing up product reclass item data...")
        product_reclass_items = fetch_all_product_reclass_items()
        product_reclass_item_data = []
        for data in product_reclass_items:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'reclass_category_id': data.reclass_category_id,
                      'reclass_child_product_id': data.reclass_child_product_id,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_reclass_item_data.append(values)
        backup_data['product_reclass_item_data'] = product_reclass_item_data
        app.logger.info("product reclass item data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))

def backup_product_reclass_detail_data():
    try:
        app.logger.info("backing up product reclass detail data...")
        product_reclass_details = fetch_all_product_reclass_details()
        product_reclass_detail_data = []
        for data in product_reclass_details:
            updated_at = data.updated_at
            if data.updated_at is not None:
                updated_at = stringify_datetime_object(data.updated_at)
            values = {'id': data.id, 
                      'parent_batch_id': data.parent_batch_id,
                      'reclass_source_item_id': data.reclass_source_item_id,
                      'reclass_destination_item_id': data.reclass_destination_item_id,
                      'reclass_qty': data.reclass_qty,
                      'db_status': data.db_status,
                      'created_at': stringify_datetime_object(data.created_at),
                      'updated_at': updated_at}
            product_reclass_detail_data.append(values)
        backup_data['product_reclass_detail_data'] = product_reclass_detail_data
        app.logger.info("product reclass detail data backup complete...")
    except Exception as err:
        app.logger.error(type(err).__name__+':'+str(err))