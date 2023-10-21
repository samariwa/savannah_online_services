"""read.py
A module to perform all READ operations in CRUD

order:
-Customer Crud: Customer, Cart, Wishlist
-User Crud : User, Account_Verification, Logged_Devices, Newsletter_Subscribers
-Staff Crud: Staff, Staff_Role
-Product cruds: Product_Category, Product_Unit, Product, Supplier,
 Product_Batch, Product_Movement, Product_Reclass_Detail
"""
from app.models import User , Account_Verification , Logged_Devices 
from app.models import Staff, Staff_Role, Department


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
#                     STAFF RELATED READ FUNCTIONS                     #
########################################################################
def fetch_all_roles():
    """
    fetch_all_roles()

    function that fetches all staff roles in the database regardless of the db status
    """
    return db.session.execute(
        db.select(Staff_Role.id, Staff_Role.department_id, Staff_Role.role, 
                  Staff_Role.db_status, Staff_Role.created_at, Staff_Role.updated_at)
                  .order_by(Staff_Role.id.asc())
                ).all()

def fetch_active_roles():
    """
    fetch_active_roles()

    Fetches all staff roles that have not been soft deleted
    """
    return Staff_Role.query.filter(Staff_Role.role != 'SuperUser', Staff_Role.db_status != 'deleted').order_by(Staff_Role.id.asc())

def fetch_all_departments():
    """
    fetch_all_departments()

    function that fetches all departments in the database regardless of the db status
    """
    return db.session.execute(
        db.select(Department.id, Department.department, Department.db_status,
                  Department.created_at, Department.updated_at)
                  .order_by(Department.id.asc())
                ).all()

def fetch_active_admins():
    """
    fetch_active_admins()

    Fetches all admins that have not been soft deleted
    """
    admins = db.session.execute(
        db.select(User.id, User.email_address, User.user_status, Staff.first_name, Staff.last_name,
                   Staff_Role.role, Department.department
        ).join(Staff, Staff.id == User.staff_id)
        .join(Staff_Role, Staff.role_id == Staff_Role.id)
        .join(Department, Staff_Role.department_id == Department.id)
        .filter(Staff_Role.role != 'SuperUser', User.db_status != 'deleted')
        .order_by(User.id.asc())
    )
    return admins

def fetch_all_staff():
    """
    fetch_all_staff()

    function that fetches all staff in the database regardless of the db status
    """
    return db.session.execute(
        db.select(Staff.id, Staff.role_id, Staff.first_name, Staff.last_name,
                  Staff.db_status, Staff.created_at, Staff.updated_at)
                  .order_by(Staff.id.asc())
                ).all()

def read_staff(id):
    """"
    read_staff(id)

    A method to get details of one staff given a specific staff id
    If found, the function returns the customer as an object, otherwise None

    * note the .one() and [0]
    """
    try:
        staff_to_get = db.session.execute(
            db.select(Staff).filter_by(id=id)).one()
        if staff_to_get is None:
            return None
        else:
            return staff_to_get[0]
    except Exception as err:
        app.logger.error(f"Unexpected {err=}")
        return None