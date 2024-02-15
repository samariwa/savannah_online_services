from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail, Message
# from sqlalchemy import func
from datetime import timedelta
from flask_wtf.csrf import CSRFProtect
from flask_mobility import Mobility
import os

secret = ''
recaptcha_pub_key = ''
recaptcha_priv_key = ''

secret = os.environ.get('LOCAL_APP_SCRT')
recaptcha_pub_key = os.environ.get('L_RECAPTCHA_PUBLIC_KEY')
recaptcha_priv_key = os.environ.get('L_RECAPTCHA_PRIVATE_KEY')

# Get important values from env
conn_string = os.environ.get('CONN_STR')
mail_usr = os.environ.get('MAIL_USERNAME')
mail_pwd = os.environ.get('MAIL_PASSWORD')
organization = {
    "mobile": os.environ.get('MOBILE'),
    "email": os.environ.get('EMAIL'),
    "location": os.environ.get('LOCATION'),
}


# config app and connect DB to app
app = Flask(__name__)

# Debug value is set to true for development purposes
app.config['DEBUG'] = True
app.config['TESTING'] = False
# app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = secret

app.config['RECAPTCHA3_PUBLIC_KEY'] = recaptcha_pub_key
app.config['RECAPTCHA3_PRIVATE_KEY'] = recaptcha_priv_key

#Mailtrap

app.config['MAIL_SERVER'] = 'sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# Live mail
"""
app.config['MAIL_SERVER'] = 'mail.symphafresh.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
"""
# app.config['MAIL_DEBUG'] =  True #Set to true for development purposes
app.config['MAIL_USERNAME'] = mail_usr
app.config['MAIL_PASSWORD'] = mail_pwd
app.config['MAIL_DEFAULT_SENDER'] = ('CIFOR-ICRAF', mail_usr)
app.config['MAIL_MAX_EMAILS'] = None  # Prevents many emails are sent out
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False
# define session timeout configuraton
#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)
#app.session_interface = CustomSessionInterface()
# define password reset / account verification token lifetime
app.config['TOKEN_LIFETIME'] = 5
# define product delivery time limit
app.config['DELIVERY_TIME_LIMIT'] = 25
# define remember me cookie lifetime
global REMEMBER_ME_COOKIE_TIMEOUT
REMEMBER_ME_COOKIE_TIMEOUT = 60 * 60 * 24 * 7  # 1 week

# disable json key sorting by the jsonify function
app.config['JSON_SORT_KEYS'] = False
# setup mail
mail = Mail(app)

# db
db = SQLAlchemy(app)

# setup password encryption
bcrypt = Bcrypt(app)

# csrf protection initializaton
csrf = CSRFProtect(app)

# Login management setup
login_manager = LoginManager(app)

# flask mobility (checks if device is a mobile phone)
mobility = Mobility(app)

# Login settings
login_manager.login_view = "admin_login"
login_manager.login_message_category = "warning"
login_manager.session_protection = "strong"
# at this point we can import views, or do so in our run.py
# I'll use run.py for the sake my vscode linter


