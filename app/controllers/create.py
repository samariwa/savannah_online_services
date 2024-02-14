"""
###############################################
#           B L U E P R I N T                 #
###############################################
Each create Function takes in **kwargs as input and passes it into
the model

If need be, it checks for existence of the record before doing
db.session.add()
It can also call other functions, in case creation of one model
instance might affect other model instances
if the commit is successful, it returns the created instance.
Otherwise, the create functions return A str depicting the type of error that
caused the create not to be successful
and logs onto the terminal the suspect error
with a better way to call the create function

This implies that API calls that note that Create functions returned a
type str should respond with 400 or 424
        **It is important to do session rollbacks and perhaps a flush when
        a create function fails in order to avoid other errors in the system.
        (Just a hunch)

However, if the create function called returns an object, then respond with 201
"""
import os
from app.models import User, Account_Verification, Logged_Devices
from app.models import Customer
from app.models import Order
from app.response import respond
from app import app, db, mail, organization, Message
from flask import render_template, send_file
from app.general_functions import id_generator, datetime, get_uuid, timedelta
########################################################################
#                    USER-RELATED CREATE FUNCTIONS                     #
########################################################################

def create_user(**kwargs):
    """
    create_user(**kwargs):

    A function to create a user of our system
    E.g: create staff user

    create_user(staff_id=staff_id, email_address='test@sympha.com', password='abc123')
    If it's successful, 
    it returns the 201 successfully created status code
    Once the user is created, a unique password is set and an email
    sent to them for account verification and a password reset
    If the creation fails, the function prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        user_to_create = User(**kwargs)
        db.session.add(user_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'staff_id': 'integer, nullable, unique',
            'user_status': 'enum, not null, default=inactivate',
            'email_address': 'string, not null, unique, length=50',
            'login_status': 'integer, default=0',
            'last_activity': 'datetime, default=current datetime',
            'login_attempts': 'integer, default=0',
            'password_hash': 'string, not null, length=60',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_user({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__


def create_account_verification_entry(**kwargs):
    """
    create_account_verification_entry(**kwargs)

    A method to create an account verification entry. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        account_verification_entry = Account_Verification(**kwargs)
        db.session.add(account_verification_entry)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'user_id': 'integer, not null',
            'token': 'string, not null, length=10',
            'token_expiry': 'datetime, not null, default=current datetime',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_account_verification_entry({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__


def create_device_log(**kwargs):
    """
    create_device_log(**kwargs)

    A method to create a device log once a device logs in to the system. 
    If it's successful, it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        device_log = Logged_Devices(**kwargs)
        db.session.add(device_log)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'user_id': 'integer, not null',
            'device_type': 'string, not null, length=30',
            'browser': 'string, not null, length=200',
            'ip_address': 'not null, length=30',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_device_log({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__

########################################################################
#                        CUSTOMER CREATE FUNCTIONS                     #
########################################################################
def create_customer(**kwargs):
    """
    create_customer(**kwargs)

    A method to create a customer. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        customer_to_create = Customer(**kwargs)
        db.session.add(customer_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'customer_code': 'string, not null, length=100, unique',
            'first_name': 'string, not null, length=30',
            'last_name': 'string, not null, length=30',
            'phone_no': 'string, not null, length=30, unique',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_customer({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__

###############################################################################
#                            ORDERS CREATE FUNCTIONS                          #
###############################################################################
def create_order(**kwargs):
    """
    create_order(**kwargs)

    A method to create a customer order
    if it's successful, it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        order_to_create = Order(**kwargs)
        # include a  check for quantity requested vs available
        db.session.add(order_to_create)
        db.session.commit()
        return order_to_create.id
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'customer_id': 'integer, not null',
            'amount': 'float, not null',
            'time': 'time, not null',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_order({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__