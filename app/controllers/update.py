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
from app.models import Staff, Staff_Role, Department, Participant
from app.models import Event, Event_Venues, Session, Session_Registration
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
    
def update_department(**kwargs):
    """"
    update_department(**kwargs)

    A method to update details of a department given a specific department id

    expected use:
        update_department(id=d_id, department="Finance", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['department']
        department_to_update = db.session.execute(
            db.select(Department).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"department_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__
    
def update_admin(**kwargs):
    """"
    update_admin(**kwargs)

    A method to update details of an admin given a specific admin id

    expected use:
        update_admin(id=a_id, first_Name="John Doe", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['first_name', 'last_name']
        admin_to_update = db.session.execute(
            db.select(Staff).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"admin_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__ 

def update_participant(**kwargs):
    """"
    update_participant(**kwargs)

    A method to update details of a participant given a specific participant id

    expected use:
        update_participant(id=p_id, first_Name="John Doe", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['first_name', 'last_name']
        participant_to_update = db.session.execute(
            db.select(Participant).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"participant_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__ 

def update_event(**kwargs):
    """"
    update_event(**kwargs)

    A method to update details of an event given a specific event id

    expected use:
        update_event(id=e_id, event="Science Week", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['event']
        event_to_update = db.session.execute(
            db.select(Event).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"event_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__

def update_event_venue(**kwargs):
    """"
    update_event_venue(**kwargs)

    A method to update details of an event venue given a specific event venue id

    expected use:
        update_event_venue(id=e_id, event_venue="Main Conference Hall", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['venue']
        event_venue_to_update = db.session.execute(
            db.select(Event_Venues).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"event_venue_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__

def update_session(**kwargs):
    """"
    update_session(**kwargs)

    A method to update details of a session venue given a specific session id

    expected use:
        update_session(id=s_id, session="Restoration of Forests in South East Asia", ...)

    If successful , the function returns the 200(OK) HTTP status code,
    otherwise returns Name of the type of exception

    kwargs must have an id
    """
    try:
        fields = ['session', 'session_description']
        session_to_update = db.session.execute(
            db.select(Session).filter_by(id=kwargs['id'])
        ).one()[0]
        for field in fields:
            if kwargs.get(field):
                order = f"session_to_update.{field} = kwargs.get('{field}')"
                exec(order)
                db.session.commit()
        return respond('200')
    except Exception as err:
        app.logger.error(f"Unexpected {err=}"
            "Ensure that each call has an id as one of the kwargs.\n"
            "If you called this from the shell, do a db.session.rollback()"
            " before continuing")
        return type(err).__name__         
     
