"""read.py
A module to perform all READ operations in CRUD

order:
-User Crud : User, Account_Verification, Logged_Devices, Newsletter_Subscribers
-Staff Crud: Staff, Staff_Role
"""
from app.models import User , Account_Verification , Logged_Devices 
from app.models import Customer
from app.models import Order

from sqlalchemy import or_, func
from app import app, db

"""
========================================================
Things to impelement in read controller:
Have a way of:
i) All objects details
ii) Count objects
iii) Reading LIKE filter
========================================================
"""
########################################################################
#                    USER-RELATED READ FUNCTIONS                      #
########################################################################
def read_user(**kwargs):
    """"
    read_user(**kwargs)

    Gets details of one user given any unique attribute

    If found, the function returns the user as an object, otherwise None
    """
    try:
        user_to_get = User.query.filter_by(**kwargs).first()
        if user_to_get is None:
            return None
        else:
            return user_to_get
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return None
    
def fetch_all_users():
    """
    fetch_all_users()

    function that fetches all users in the database regardless of the db status
    """
    return db.session.execute(
        db.select(User.id, User.staff_id, User.user_status,
                  User.email_address, User.login_status, User.last_activity,
                  User.login_attempts, User.db_status, User.password_hash,
                  User.created_at, User.updated_at)
                  .order_by(User.id.asc())
                ).all()

def fetch_all_account_verifications():
    """
    fetch_all_account_verifications()

    function that fetches all user account verification data in the database 
    regardless of the db status
    """
    return db.session.execute(
        db.select(Account_Verification.id, Account_Verification.user_id, 
                  Account_Verification.token, Account_Verification.token_expiry,
                  Account_Verification.db_status, Account_Verification.created_at, 
                  Account_Verification.updated_at)
                  .order_by(Account_Verification.id.asc())
                ).all()

def fetch_all_logged_devices():
    """
    fetch_all_logged_devices()

    function that fetches all logged devices data in the database 
    regardless of the db status
    """
    return db.session.execute(
        db.select(Logged_Devices.id, Logged_Devices.user_id, 
                  Logged_Devices.device_type, Logged_Devices.browser,
                  Logged_Devices.ip_address, Logged_Devices.db_status, 
                  Logged_Devices.created_at, Logged_Devices.updated_at)
                  .order_by(Logged_Devices.id.asc())
                ).all()

########################################################################
#                 CUSTOMER-RELATED READ FUNCTIONS                      #
########################################################################

def fetch_active_customers():
    """
    fetch_active_customers()

    Fetches all customers who have neither been blacklisted nor soft deleted
    It gets joined with the customer accounts models in order to fetch their
    account balances and debts if there are
    """
    customers = db.session.execute(
        db.select(Customer.id, Customer.customer_code, Customer.first_name, 
                  Customer.last_name, Customer.phone_no)
        .filter(
            Customer.db_status != 'deleted'
        )
        .order_by(Customer.id.asc())
    ).all()

    return customers

def fetch_customer(customer_id):
    """"
    fetch_customer(customer_id)

    A method to get details of one customer given a specific customer id
    If found, the funciton returns the customer as an object, otherwise None

    * note the .one() and [0]
    """
    try:
        customer_to_get = db.session.execute(
            db.select(Customer).filter_by(id=customer_id)).one()
        if customer_to_get is None:
            return None
        else:
            return customer_to_get[0]
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return None

########################################################################
#                    ORDER-RELATED READ FUNCTIONS                      #
########################################################################

def fetch_active_orders():
    """fetch_order_by_date:
    Fetch all active orders that have been made
    """
    all_Orders = db.session.execute(
        db.select(Order.id, Customer.first_name, Customer.last_name, Order.amount, Order.time)
        .filter(
            Order.db_status != 'deleted'
        )
        .join(Customer, Customer.id == Order.customer_id)
        .order_by(Order.id.asc())
    ).all()
    return all_Orders

def fetch_order(order_id):
    """"
    fetch_order(order_id)

    A method to get details of an order given a specific order id
    If found, the funciton returns the order as an object, otherwise None

    * note the .one() and [0]
    """
    try:
        order_to_get = db.session.execute(
            db.select(Order).filter_by(id=order_id)).one()
        if order_to_get is None:
            return None
        else:
            return order_to_get[0]
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return None
    

    