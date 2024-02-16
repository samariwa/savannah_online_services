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
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
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
#                              CUSTOMER                                #
########################################################################
class Customer(db.Model):
    """Customer:
    A class for the customer objects that are to be represented in the
    database.
    """
    __tablename__ = 'customers'
    id = db.Column(db.Integer(), primary_key=True)
    customer_code = db.Column(db.String(length=100),  nullable=False, unique=True)
    first_name = db.Column(db.String(length=30), nullable=False)
    last_name = db.Column(db.String(length=30), nullable=False)
    phone_no = db.Column(
        db.String(length=30),
        nullable=False,
        unique=True,
        # format
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
        server_default=func.now(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )

    def __repr__(self):
        return f"#{self.id} {self.first_name}: {self.last_name}"

########################################################################
#                                ORDER                                 #
########################################################################
 
class Order(db.Model):
    """Order:
    A class for the order objects that are to be represented in the
    database.
    """

    __tablename__ = "orders"
    id = db.Column(db.Integer(), primary_key=True)
    order_ref = db.Column(db.String(length=100),  nullable=False, unique=True)
    customer_id = db.Column(
        db.Integer(),
        db.ForeignKey("customers.id", ondelete="CASCADE"),
        nullable=False,
    )
    amount = db.Column(db.Float(), nullable=False)
    time = db.Column(
        db.Time(),
        nullable=False,
        default=str(datetime.now().strftime("%H:%M:%S")),
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
        server_default=func.now(),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        onupdate=func.now(),
    )

    def __repr__(self):
        return f"#{self.id} Amt:{self.amount}"
    
########################################################################
#                              SMS LOGS                                #
########################################################################
 
class SMS_LOG(db.Model):
    """SMS_LOG:
    A class for the sms log objects that are to be represented in the
    database.
    """

    __tablename__ = "sms_logs"
    id = db.Column(db.Integer(), primary_key=True)
    order_ref_id = db.Column(
        db.String(length=100),
        db.ForeignKey("orders.order_ref", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )
    sms_info = db.Column(
        db.Enum(
            "order_creation",
            "order_update",
            name="sms_information",
        ),
        nullable=False,
        default="order_creation",
    )
    log_message_id = db.Column(db.String(length=100),  nullable=False, unique=True)
    log_message = db.Column(db.String(length=100),  nullable=False)
    customer_code = db.Column(db.String(length=100), nullable=False)
    status = db.Column(db.String(length=30), nullable=False)
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

    def __repr__(self):
        return f"#{self.id} Amt:{self.status}"