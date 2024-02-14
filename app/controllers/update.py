"""update.py
A module to perform all UPDATE operations in CRUD

order:
-Customer Crud: Customer, Cart, Wishlist
-User Crud : User, Account_Verification, Logged_Devices, Newsletter_Subscribers
-Staff Crud: Staff, Staff_Role
-Product cruds: Product_Category, Product_Unit, Product, Supplier,
 Product_Batch, Product_Movement, Product_Reclass_Detail
-Sales & Order Cruds: Order, Order_Detail, Delivery, Transaction_Detail
"""
from app import app
from app.models import User, Account_Verification, Logged_Devices
from app.models import Customer
from app.models import Order
from app.response import respond

from app.general_functions import create_timestamp, datetime
from app import db
from sqlalchemy import or_
########################################################################
#                USER-RELATED UPDATE FUNCTIONS                         #
########################################################################
def update_user(**kwargs):
    """"
    update_user(**kwargs)

    A method to update details of the user given a specific user id

    expected use:
        update_user(id=u_id, password_hash="fdsd%$3(@w762Ty2897^@876@80", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['password', 'user_status', 'login_status', 'login_attempts',]
        user_to_update = db.session.execute(
            db.select(User).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"user_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__

########################################################################
#                CUSTOMER-RELATED UPDATE FUNCTIONS                     #
########################################################################
def update_customer(**kwargs):
    """"
    update_customer(**kwargs)

    A method to update details of the customer given a specific customer id

    expected use:
        update_customer(id=c_id, note="Awesome Customer", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = [
            'first_name',
            'last_name',
            'phone_no',
        ]
        customer_to_update = db.session.execute(
            db.select(Customer).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"customer_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__

########################################################################
#                      ORDER-RELATED UPDATE FUNCTIONS                  #
########################################################################

def update_order(**kwargs):
    """
    update_order(**kwargs)

    A method to update details of a specific order.

    In general, the function takes in kwargs containing the new values
    to be updated in the respective fields.

    expected use:
        update_order(id=order_id, amount=2500, ...)
    * some of these new kwargs might be calculated from order_details, etc

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    ** Discuss whethere there are fields that should not be updateable

    kwargs must have an id
    """
    try:
        fields = [
            'amount',
            'time',
        ]
        print("xxxxxxxxx")
        print(kwargs['id'])
        order_to_update = db.session.execute(
            db.select(Order).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                if field == 'amount':
                    order = f"order_to_update.{field} = str(kwargs.get('{field}'))"
                else:
                    order = f"order_to_update.{field} = kwargs.get('{field}')"
                
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__