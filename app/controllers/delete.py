"""delete.py
A module to perform all DELETE operations in CRUD

order:
-Customer Crud: Customer, Cart, Wishlist
-User Crud : User, Account_Verification, Logged_Devices, Newsletter_Subscribers
-Staff Crud: Staff, Staff_Role
-Product cruds: Product_Category, Product_Unit, Product, Supplier,
 Product_Batch, Product_Movement, Product_Reclass_Detail
-Sales & Orders cruds: Order, Order_Detail, Delivery, Transaction_Detail
"""
from app.models import User, Account_Verification, Logged_Devices
from app.models import Customer
from app.models import Order
from sqlalchemy.orm.exc import NoResultFound
from app.response import respond
from app import app, db
import os

"""Update:
- Due to interlinkage of models using CASCADE option, we're going to
  be adding a status to each model and then using this status to tell if an
  instance is allowed to perform a given operation or be performed on
  a given operation.

  for uniformity, the first approach will be adding a field to each Model
  named `db_status` whose value will either be 'active' or 'deleted'

- this is going to avoid changing status fields for fields which already
  have a status e.g customer has customer_status. A customer can have
  their own status which has nothing to do with them being deleted or
  does. However, when we invoke the delete function, we're going to
  implement a soft delete changing their status to deleted.

- This enables us to still have a customer account with all their details
  even after we delete thus we can't loose important information if a customer
  accidentally deletes their account or if staff accidentally or fraudulently
  deletes an order or transaction

- for models like transaction, having a db_status field will avoid us
  changing transaction_status field which can have important info
  especially for data analytics, etc.

- there will be two functions to change delete status back and forth
  i.e `toggle_delete()`
"""

def toggle_delete(model_instance):
    """
    toggle_delete(model_instance)

    A function to change the db_status of a given instance to deleted

    input expected is a fetched instance of a model in our db
    which has db_status as a field
    """
    if model_instance.db_status != "deleted":
        model_instance.db_status = "deleted"
        db.session.commit()

def toggle_active(model_instance):
    """
    toggle_active(model_instance)

    A function to change the db_status of a given instance to active

    input expected is a fetched instance of a model in our db
    which has db_status as a field
    """
    if model_instance.db_status != "active":
        model_instance.db_status = "active"
        db.session.commit()

########################################################################
#                  USER-RELATED DELETE FUNCTIONS                      #
########################################################################
def delete_user(id):
    """"
    delete_user(id)

    A method to soft delete a user given a specific staff id

    If successful, the function returns the 200(OK) HTTP status code otherwise
    name of exception raised
    """
    try:
        user_to_delete = db.session.execute(
            db.select(User).filter_by(id=id)).one()[0]
        toggle_delete(user_to_delete)
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return type(err).__name__
    
def delete_account_verification_entry(id):
    """"
    delete_account_verification_entry(id)

    A method to soft delete an account verification entry given a specific staff id

    If successful, the function returns the 200(OK) HTTP status code otherwise
    name of exception raised
    """
    try:
        verificaton_entry_to_delete = db.session.execute(
            db.select(Account_Verification).filter_by(id=id)).one()[0]
        toggle_delete(verificaton_entry_to_delete)
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return type(err).__name__
    
def delete_device_log(id):
    """"
    delete_device_log(id)

    A method to soft delete a device log given a specific log id

    If successful, the function returns the 200(OK) HTTP status code otherwise
    name of exception raised
    """
    try:
        log_to_delete = db.session.execute(
            db.select(Logged_Devices).filter_by(id=id)).one()[0]
        toggle_delete(log_to_delete)
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return type(err).__name__
    
########################################################################
#                CUSTOMER-RELATED DELETE FUNCTIONS                     #
########################################################################


def delete_customer(id):
    """"
    delete_customer(id)

    A method to soft delete a customer given a specific customer id

    If successful, the funciton returns the 200(OK) HTTP status code otherwise
    name of exception raised
    """
    try:
        customer_to_delete = db.session.execute(
            db.select(Customer).filter_by(id=id)).one()[0]
        toggle_delete(customer_to_delete)
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return type(err).__name__

######################################################################
#                        ORDER DELETE FUNCTIONS                      #
######################################################################
def delete_order(id):
    """
    delete_order(id)

    A method to soft delete a customer's order initiated either by the customer or
    admin. This method should also initiate soft deletes for other instances
    related to the order.

    i.e the delivery, order_details, transaction_details
    """
    try:
        order_to_delete = db.session.execute(
            db.select(Order).filter_by(id=id)).one()[0]

        toggle_delete(order_to_delete)
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return type(err).__name__