from app import db, bcrypt, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


"""
=========================================================
GROUND RULES
- An update to Models might require an update to controllers
- Sometimes, order of models on this file matters
==========================================================
"""
#####################################################################
#                      USER                                         #
#####################################################################


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    staff_id = db.Column(
        db.Integer(), db.ForeignKey('staff.id'), nullable=True, unique=True)
    user_status = db.Column(
        db.Enum(
            "active",
            "inactive",
            "suspended",
            # case where it was active but has temporarily been put on hold
            name="user_status",
        ),
        nullable=False,
        default="inactive",
    )
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    login_status = db.Column(db.Integer(), default=0)
    last_activity = db.Column(db.DateTime(
        timezone=True), default=func.now())
    login_attempts = db.Column(db.Integer(), default=0)

    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), onupdate=func.now())
    password_hash = db.Column(db.String(length=60), nullable=False)
    account_verification = db.relationship(
        'Account_Verification', backref='reset_token')
    logged_devices = db.relationship(
        'Logged_Devices', backref='user_device')

    def __repr__(self):
        return f"{self.email_address}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(
            self.password_hash, attempted_password)

    def is_superuser(self):
        """is_admin
        A method to check if given staff has superuser role rights
        Return:
            True or False
        """
        if self.staff_id != None:
            return self.staff.role.role == "SuperUser"
        return False


    def is_admin(self):
        """is_admin
        A method to check if given staff has admin role rights
        Return:
            True or False
        """
        if self.staff_id != None:
            return self.staff.role.role == "Admin"
        return False

    def has_role(self, *roles):
        """
        Current Roles:
            Admin
            Superuser

        A method to determine whether given user has the respective role
        for all roles, only one has to be confirmed for us to allow access
        Args:
            "Role_Name" As stated above


        Return:
            True or False
        """
        for role in roles:
            if self.is_superuser() and role == 'SuperUser':
                return True
            elif self.is_admin() and role == 'Admin':
                return True

        # if none of the roles were confirmed
        return False

class Account_Verification(db.Model):
    __tablename__ = 'account_verification'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(
        db.Integer(), db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(length=10), nullable=False)
    token_expiry = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        server_default=func.now()
    )
    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now()
    )

    def token_validate(attempted_token):
        if attempted_token is not None:
            if attempted_token.token_expiry > datetime.now(attempted_token.token_expiry.tzinfo):
                return "valid"
            elif attempted_token.token_expiry < datetime.now(attempted_token.token_expiry.tzinfo):
                return "expired"
        else:
            return "invalid"

    def token_object(token):
        return Account_Verification.query.filter_by(
            token=token).first()

class Logged_Devices(db.Model):
    __tablename__ = 'logged_devices'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(
        db.Integer(), db.ForeignKey('users.id'))
    device_type = db.Column(db.String(length=30), nullable=False)
    browser = db.Column(db.String(length=200), nullable=False)
    ip_address = db.Column(db.String(length=30), nullable=False)

    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now()
    )

########################################################################
#                STAFF                                                 #
########################################################################
class Staff(db.Model):
    __tablename__ = 'staff'
    id = db.Column(db.Integer(), primary_key=True)
    role_id = db.Column(
        db.Integer(),
        db.ForeignKey('staff_roles.id'),
        nullable=False,
    )
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    # uselist=False ensures one to one relationship
    staff = db.relationship('User', backref='staff', uselist=False)

    def __repr__(self):
        return f"#{self.id} {self.first_name}: {self.last_name}"

class Staff_Role(db.Model):
    """
    Here we define the role of a given staff and use this to determine
    access rights for different users in different pages

    Current Staff Roles Department IDs:
        Admin: id 1

    checking roles:

    User.staff.department_id == 1 and User.staff.role == "Admin"

    """
    __tablename__ = 'staff_roles'
    id = db.Column(db.Integer(), primary_key=True)
    department_id = db.Column(
        db.Integer(),
        db.ForeignKey('departments.id'),
        nullable=False,
    )
    role = db.Column(db.String(length=20),  nullable=False)
    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",  # consider default deleted for OTP
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    staff = db.relationship('Staff', backref='role')

    def __repr__(self):
        return f"Role #{self.id} {self.role}"

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer(), primary_key=True)
    department = db.Column(db.String(length=20),  nullable=False)

    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",  # consider default deleted for OTP
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    role = db.relationship('Staff_Role', backref='department')
    participant = db.relationship('Participant', backref='department')

    def __repr__(self):
        return f"{self.department} Department_ID#: {self.id} {self.role}"
    
class Participant(db.Model):
    __tablename__ = 'participants'
    id = db.Column(db.Integer(), primary_key=True)
    department_id = db.Column(
        db.Integer(),
        db.ForeignKey('departments.id'),
        nullable=False,
    )
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    email_address = db.Column(db.String(length=50),
                              nullable=False, unique=True)
    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    # uselist=False ensures one to one relationship
    session_registration = db.relationship('Session_Registration', backref='participant')

    def __repr__(self):
        return f"#{self.id} {self.first_name}: {self.last_name}"

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer(), primary_key=True)
    event = db.Column(db.String(length=20),  nullable=False)
    start_date = db.Column(db.Date(), default=str(datetime.now().date()), nullable=False)
    end_date = db.Column(db.Date(), default=str(datetime.now().date()), nullable=False)
    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    session = db.relationship('Session', backref='event')

    def __repr__(self):
        return f"{self.event} Event_ID#: {self.id}"
    
class Event_Venues(db.Model):
    __tablename__ = 'event_venues'
    id = db.Column(db.Integer(), primary_key=True)
    venue = db.Column(db.String(length=20),  nullable=False)

    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",  # consider default deleted for OTP
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    session = db.relationship('Session', backref='event_venue')

    def __repr__(self):
        return f"{self.department} Event_Venue_ID#: {self.id} {self.role}"
    
class Session(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer(), primary_key=True)
    event_id = db.Column(
        db.Integer(),
        db.ForeignKey('events.id'),
        nullable=False,
    )
    event_venue_id = db.Column(
        db.Integer(),
        db.ForeignKey('event_venues.id'),
        nullable=False,
    )
    session = db.Column(db.String(length=20),  nullable=False)
    session_description = db.Column(db.String(length=500),  nullable=False)
    start_timestamp = db.Column(db.DateTime(timezone=True), default=str(datetime.now()), nullable=False)
    end_timestamp = db.Column(db.DateTime(timezone=True), default=str(datetime.now()), nullable=False)
    db_status = db.Column(
        db.Enum(
            "inactive",
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="inactive",
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )
    session_registration = db.relationship('Session_Registration', backref='session')

    def __repr__(self):
        return f"{self.session} Session_ID#: {self.id}"
    
class Session_Registration(db.Model):
    __tablename__ = 'session_registration'
    id = db.Column(db.Integer(), primary_key=True)
    session_id = db.Column(
        db.Integer(),
        db.ForeignKey('sessions.id'),
        nullable=False,
    )
    participant_id = db.Column(
        db.Integer(),
        db.ForeignKey('participants.id'),
        nullable=False,
    )
    db_status = db.Column(
        db.Enum(
            "active",
            "deleted",
            name="delete_status",
        ),
        nullable=False,
        default="active",
    )
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )


    def __repr__(self):
        return f"{self.session} Session_Registration_ID#: {self.id}"