"""create.py
A module to perform all create operations in CRUD

order:
-Staff Crud: Staff, Staff_Role
-User Crud : User, Account_Verification, Logged_Devices
*Point to note: not all create operations are named create_... because it
doesn't make sense. E.g for product, we have reclass_product to
work on Product_Reclass_Detail model


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
from app.models import Staff, Staff_Role, Department, Participant
from app.models import Event, Event_Venues, Session, Session_Registration
from app.response import respond
from app import app, db, mail, organization, Message
from flask import render_template, send_file
from app.general_functions import id_generator, datetime, get_uuid, timedelta


########################################################################
#                   STAFF-RELATED CREATE FUNCTIONS                     #
########################################################################
def create_staff(**kwargs):
    """
    create_staff(**kwargs)

    A method to create a staff. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        staff_to_create = Staff(**kwargs)
        db.session.add(staff_to_create)
        db.session.commit()
        # create_user(staff_id=staff_to_create.id, password='abc123')
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'role_id': 'integer, not null',
            'first_name': 'string, not null, length=30',
            'last_name': 'string, not null, length=30',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_staff({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__


def create_staff_role(**kwargs):
    """
    create_staff_role(**kwargs)

    A method to create a staff role. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        staff_role_to_create = Staff_Role(**kwargs)
        db.session.add(staff_role_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'department_id': 'integer, not null',
            'role': 'string, not null, length=20',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_staff_role({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__
    
def create_department(**kwargs):
    """
    create_department(**kwargs)

    A method to create a department. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        department_to_create = Department(**kwargs)
        db.session.add(department_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'department': 'string, not null, length=20',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_department({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__

def create_admin(**kwargs):
    """
    create_admin(**kwargs)

    A method to create an admin. If it's successful, 
    it returns the 201 successfully created status code
    Once the user is created, a unique password is set and an email
    sent to them for account verification and a password reset
    If the creation fails, the function prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        staff_to_create = Staff(role_id=kwargs['role'], first_name=kwargs['firstname'], last_name=kwargs['lastname'])
        db.session.add(staff_to_create)
        db.session.commit()
        user_to_create = User(staff_id=staff_to_create.id, email_address=kwargs['email_address'], password=get_uuid())
        db.session.add(user_to_create)
        db.session.commit()
        # generate a token that will be used to verify if the user owns that email address
        verification_id = id_generator(10)
        # get the expiry datetime for the token
        expiry_in_minutes = app.config['TOKEN_LIFETIME']
        # Add 5 minutes to now
        expiry_time = datetime.now() + timedelta(minutes=expiry_in_minutes)
        # store the token in the database with expiry time
        verification_token = create_account_verification_entry(
            user_id=user_to_create.id,
            token=verification_id,
            token_expiry=expiry_time
        )
        msg = Message('Sympha Fresh Admin Account Verification', recipients=[
            kwargs['email_address']], 
            html=render_template('mail/admin-account-activation.html', 
            firstname=kwargs['firstname'], 
            verification_code=verification_id, 
            organization=organization))
        # recepients can accomodate a list of many recepients
        mail.send(msg)
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'first_name': 'string, not null, length=30',
            'last_name': 'string, not null, length=30',
            'email_address': 'string, not null, length=50',
            'role_id': 'integer, not null',
            'password': 'string, not null',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_admin({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__
    
    
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
    
def create_participant(**kwargs):
    """
    create_participant(**kwargs)

    A method to create a participant. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        participant_to_create = Participant(**kwargs)
        db.session.add(participant_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'department_id': 'integer, not null',
            'first_name': 'string, not null, length=30',
            'last_name': 'string, not null, length=30',
            'email_address': 'string, not null, length=50, unique',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_participant({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__
    
def create_event(**kwargs):
    """
    create_event(**kwargs)

    A method to create an event. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        event_to_create = Event(**kwargs)
        db.session.add(event_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'event': 'string, not null, length=20',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_event({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__
    
def create_event_venue(**kwargs):
    """
    create_event_venue(**kwargs)

    A method to create an event venue. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        event_venue_to_create = Event_Venues(**kwargs)
        db.session.add(event_venue_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'venue': 'string, not null, length=20',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_event_venue({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__
    
def create_session(**kwargs):
    """
    create_session(**kwargs)

    A method to create an event session. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        session_to_create = Session(**kwargs)
        db.session.add(session_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'event_id': 'integer, not null',
            'event_venue_id': 'integer, not null',
            'session_name': 'string, not null, length=20',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_session({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__
    
def create_session_registration(**kwargs):
    """
    create_session_registration(**kwargs)

    A method to create an event session registration. If it's successful, 
    it returns the 201 successfully created status code
    otherwise it prints exception with a message
    The error msg helps the user create a better query the next time
    """
    try:
        session_registration_to_create = Session_Registration(**kwargs)
        db.session.add(session_registration_to_create)
        db.session.commit()
        return respond('201')
    except Exception as err:
        db.session.rollback()
        expected_args = {
            'session_id': 'integer, not null',
            'participant_id': 'integer, not null',
        }
        app.logger.error(f"Unexpected {err=}\n"
            "To avoid incorrect format, use the following:\n"
            f"create_session_registration({expected_args})\n"
            "If you called this from the shell, "
            "do a db.session.rollback() before continuing")
        return type(err).__name__