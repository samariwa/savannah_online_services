from app import app, organization, db, mail, csrf, Message, timedelta,\
     REMEMBER_ME_COOKIE_TIMEOUT, oauth
from oauthlib.oauth2 import WebApplicationClient
from app.response import respond, flash_response
from flask import render_template, redirect, url_for, flash, request, Markup,\
    abort, session
from functools import wraps
from flask_wtf.csrf import generate_csrf
from app.models import User, Account_Verification, Logged_Devices
from app.general_functions import id_generator, datetime, create_timestamp
from app.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from app.controllers.create import create_user, create_device_log,\
     create_account_verification_entry
from app.controllers.update import update_user
from app.controllers.read import read_user, fetch_local_account_user, fetch_google_account_user
from flask_login import login_user, logout_user, login_required, current_user, login_manager
from sqlalchemy.orm import sessionmaker
import urllib.request
import logging

# login redirect
def login_required_redirect(login_url, login_message):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if not current_user.is_authenticated:
                flash_response('SF023')
                logging.info(login_message)
                return redirect(url_for(login_url))
            return f(*args, **kwargs)
        return decorated
    return decorator

def connect(host='http://google.com'):
    """
    This method tries internet connectivity and returns true if
    there is else false
    """
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

##########################################################################################################
## Admin Auth ###########################################################################################
@app.route('/auth/admin/registration', methods=['GET', 'POST'])
@app.route('/auth/admin/registration/', methods=['GET', 'POST'])
@app.route('/auth/admin/register', methods=['GET', 'POST'])
@app.route('/auth/admin/register/', methods=['GET', 'POST'])
def registration():
    """
    This route is for the admin registration page. 
    Thats is when someone is creating a local account
    """
    if not connect():
        # check if there is no internet connection and let user know
        flash_response('SL009')
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = create_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email_address=form.email_address.data,
            login_status=0,
            password=form.password1.data
        )
        if user_to_create == respond('201'):
            # send a verification email to activate the account
            return redirect(url_for('send_admin_verification_email',
                                    page='login',
                                    user_firstname=form.first_name.data,
                                    email=form.email_address.data))

    if form.errors != {}:
        # in this case, the form was submitted and there were errors
        for err_msg in form.errors.values():
            # Show error messages that have not been raised. E.g. recaptcha challenge fail
            flash(
                f"Dear user: {', '.join(err_msg)}",
                category="warning"
            )
    return render_template('auth/admin/registration.html', form=form)

@app.route('/auth/admin/login', methods=['GET', 'POST'])
@app.route('/auth/admin/login/', methods=['GET', 'POST'])
@app.route('/auth/admin/signin', methods=['GET', 'POST'])
@app.route('/auth/admin/signin/', methods=['GET', 'POST'])
def admin_login():
    """
    This route is for the admin login page. Thats is when someone uses a local account
    """
    if not connect():
        # check if there is no internet connection and let user know
        flash_response('SL009')
    form = LoginForm()
    # check of the remember me cookie is available
    if 'email' in request.cookies:
        # if cookie named email is available then the pair (with password) are set
        # retrieve the cookie values and set them as values for the login fields
        form.email_address.data = request.cookies.get('email')
        form.remember_me.data = True
    """ form validation on submit as in the line below takes care of recaptcha\
    verification and proceeds if the challenge has beeen passed """
    if form.validate_on_submit():
        attempted_user = fetch_local_account_user(email_address=form.email_address.data)
        # Here, check for login attempts and lock the account

        # check if the user exists and the hashed passsword match and that the user is active
        if (attempted_user is not None and
            attempted_user.check_password_correction(attempted_password=form.password.data) and
            attempted_user.user_status == 'active'):
            login_user(attempted_user)
            login_update =  update_user(
                id=attempted_user.id,
                login_status=1,
                login_attempts=0,
                last_activity=create_timestamp())
            # if auth log is created, proceed
            if login_update == respond('200'):
                if request.MOBILE:
                    device = 'mobile'
                else:
                    device = 'desktop/laptop'
                # store the user device details in the database
                device_log = create_device_log(
                    user_id=attempted_user.id,
                    device_type=device,
                    browser=request.headers.get('User-Agent'),
                    ip_address=request.environ['REMOTE_ADDR']
                )
                # if device log is created successfully
                if device_log == respond('201'):
                    #######staff= read_staff(id=attempted_user.staff_id)
                    flash_response('SF001')
                    response = redirect(url_for('admin_dashboard'))
                    """
                    if remember me checkbox has been checked, set the cookie values afresh
                    (regardless of whether they already existed or not) with the age limits
                    for the remember me cookies which are set in the app init configs
                    """
                    # implement the True or False version of the chackbox below
                    if form.remember_me.raw_data != []:
                        response.set_cookie(
                            'email', form.email_address.data, max_age=REMEMBER_ME_COOKIE_TIMEOUT)
                    else:
                        """
                        If the checkbox is not checked / has been unchecked, check if the
                        remember me cookie exists and if so delete it
                        """
                        if 'email' in request.cookies:
                            response.delete_cookie('email')
                            form.remember_me.data = False
                    return response
                # if device log creation fails
                else:
                    flash_response('SF015')
            # if auth log creation fails
            else:
                flash_response('SF015')
        # if user exists but account has not yet been verified
        elif attempted_user and attempted_user.user_status == 'inactive':
            # fetch the customer associated with that user for purposes of retrieving name
            ####staff = read_staff(id=attempted_user.staff_id)
            """
            Give the user the ability to resend the verification email incase the cannot trace
            the verification email or the token expired. Using a flash message to do so.
            """
            flash(Markup("Dear user: Your account has not been verified. \
            Please check your mailbox for a verification email.\
            If you did not receive, you can \
            <a href='/auth/admin/verification-mail/login/"+attempted_user.first_name+"/"+form.email_address.data+"' \
            style='color: inherit;'>\
            <u>resend the email</u></a>"), category="warning")
        elif attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data) and\
             attempted_user.user_status == 'suspended':
            flash_response('SK016')
        elif attempted_user:
            # the login attempt was not successful and user exists
            login_update =  update_user(
                id=attempted_user.id,
                login_attempts=attempted_user.login_attempts + 1)
            flash_response('SF009')
        else:
            # the user doesn't exist
            flash_response('SF009')
    if form.errors != {}:
        # in this case, the form was submitted and there were errors
        for err_msg in form.errors.values():
            # Show error messages that have not been raised. E.g. recaptcha challenge fail
            flash(
                f"Dear user: {', '.join(err_msg)}",
                category="warning"
            )
    # what happens when the form has not yet been submitted
    return render_template('auth/admin/login.html', form=form)

@app.route('/auth/admin/google-login')
@app.route('/auth/admin/google_login')
@app.route('/auth/admin/google-login/')
@app.route('/auth/admin/google_login/')
def admin_google_login():
    return oauth.SavannahOnlineServices.authorize_redirect(redirect_uri='https://redirectmeto.com/http://savannahservices.servehttp.com:8000/auth/admin/google-login/callback')

@app.route('/auth/admin/google-login/callback')
def admin_google_callback():
    token = oauth.SavannahOnlineServices.authorize_access_token()
    user = read_user(email_address=token['userinfo']['email'])
    email_verified = token['userinfo']['email_verified']
    if user and email_verified:
        login_user(user)
        user.login_status = 1
        user.last_activity = create_timestamp()
        db.session.commit()
        flash_response('SF001')
    elif email_verified:
        user_to_create = create_user(
            first_name=token['userinfo']['given_name'],
            last_name=token['userinfo']['family_name'],
            email_address=token['userinfo']['email'],
            profile_picture=token['userinfo']['picture'],
            account_source='google',
            user_status='active',
            login_status=1
        )
        user = read_user(email_address=token['userinfo']['email'])
        if user_to_create == respond('201'):
            login_user(user)
            flash_response('SF001')
    else:
        flash_response('SJ001')
        return redirect(url_for('admin_login'))
    return redirect(url_for('admin_dashboard'))

@app.route('/auth/admin/logout')
@app.route('/auth/admin/signout')
@app.route('/auth/admin/logout/')
@app.route('/auth/admin/signout/')
def admin_logout_page():
    """
    # set login status to false
    user = User.query.get(id)
    user.login_status = 0
    db.session.commit()
    """
    if current_user.is_authenticated:
        logout_user()
        logging.info('---------------------- Admin Logout ----------------------')
        logging.info(f"{current_user} logged out")
        session.pop('_flashes', None)
    flash_response('SF002')
    return redirect(url_for('admin_login'))

@app.route('/auth/admin/forgot-password', methods=['GET', 'POST'])
@app.route('/auth/admin/forgot_password', methods=['GET', 'POST'])
@app.route('/auth/admin/forgot-password/', methods=['GET', 'POST'])
@app.route('/auth/admin/forgot_password/', methods=['GET', 'POST'])
def admin_forgot_password():
    if not connect():
        # check if there is no internet connection and let user know
        flash_response('SL009')
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        # check if email address exists in the database
        user_exists = read_user(email_address=form.email_address.data)
        if user_exists:
            # generate a token that will be used to verify if the user owns that email address
            verification_id = id_generator(10)
            # get the expiry datetime for the token
            expiry_in_minutes = app.config['TOKEN_LIFETIME']
            # Add 5 minutes to now
            expiry_time = datetime.now() + timedelta(minutes=expiry_in_minutes)
            # store the token in the database with expiry time
            reset_token = create_account_verification_entry(
                user_id=user_exists.id,
                token=verification_id,
                token_expiry=expiry_time
            )
            # if the reset token is successfully created
            if reset_token == respond('201'):
                # send email functionality
                msg = Message('Savannah Online Services Password Reset Request', recipients=[
                user_exists.email_address],
                    html=render_template(
                        'mail/admin-password-reset.html',
                        sender = ('Admin Savannah','admin@savannah.com'),
                        firstname=user_exists.first_name,
                        verification_code=verification_id,
                        organization=organization
                    )
                )
                mail.send(msg)
                flash_response('SF007')
        else:
            flash_response('SF012')
    if form.errors != {}:
        # in this case, the form was submitted and there were errors
        for err_msg in form.errors.values():
            # Show error messages that have not been raised. E.g. recaptcha challenge fail
            flash(
                f"Dear user: {', '.join(err_msg)}",
                category="warning"
            )
    return render_template('auth/admin/forgot-password.html', form=form)

@app.route('/auth/admin/reset-password', methods=['GET', 'POST'])
@app.route('/auth/admin/reset_password', methods=['GET', 'POST'])
@app.route('/auth/admin/reset-password/', methods=['GET', 'POST'])
@app.route('/auth/admin/reset_password/', methods=['GET', 'POST'])
def admin_reset_password():
    """ this function verifies that the verifcation code exists in the database
    and that it has not expired before returning the page """
    if not connect():
        # check if there is no internet connection and let user know
        flash_response('SL009')
    # verify that the token in the get request exists in the database
    token = request.args.get('verification_code')
    attempted_token = Account_Verification.token_object(token)
    token_result = Account_Verification.token_validate(attempted_token)
    if token_result == "valid":
        form = ResetPasswordForm()
        if form.validate_on_submit():
            local_account_user = fetch_local_account_user(id=attempted_token.user_id)
            if local_account_user and local_account_user.check_password_correction(attempted_password=form.password1.data):
                flash_response('SF013')
            else:
                change_password = update_user(
                    id=attempted_token.user_id,
                    account_source='local',
                    password=form.password1.data
                )
                if change_password == respond('200'):
                    flash_response('SF003')
                else:
                    flash_response('SF015')
                return redirect(url_for('admin_login'))
        if form.errors != {}:
            # in this case, the form was submitted and there were errors
            for err_msg in form.errors.values():
                # Show error messages that have not been raised. E.g. recaptcha challenge fail
                flash(
                    f"Dear user: {', '.join(err_msg)}",
                    category="warning"
                )
        return render_template('auth/admin/reset-password.html', form=form)
    elif token_result == "invalid":
        return render_template('auth/admin-auth-error.html', error="Invalid Token", return_page="login")
    elif token_result == "expired":
        return render_template('auth/admin-auth-error.html', error="Token Expired", return_page="login")

@app.route('/auth/admin/activation')
def activate_staff_account():
    """
    This function activates the user account is the token attached to the link
    in the email is similar to the one generated and stored in the database.
    This verification should be done in the specified time to confirm that indeed it
    is the legitimate user who has created that account.
    """
    if not connect():
        # check if there is no internet connection and let user know
        flash_response('SL009')
    # get the verification code in the url
    token = request.args.get('verification_code')
    """
    Get the token object associated with that token from the database
    None will be returned is associated object doesnt exist and will be
    handled in the next step
    """
    attempted_token = Account_Verification.token_object(token)
    """
    Validate the token in terms of existence and exiry
    'valid' is returned if token is valid
    'invalid' is returned if token does not exist
    'expired' is returned if token has expired
    """
    token_result = Account_Verification.token_validate(attempted_token)
    # If the token is valid, activate the account and redirect to login for user log in
    if token_result == "valid":
        # Fetch user id associated with the valid token & activate their account
        change_status =  update_user(
            id=attempted_token.user_id,
            user_status='active')
        if change_status == respond('200'):
            flash_response('SF004')
        return redirect(url_for('admin_login'))
    # If token is invalid or expired, redirect to the error page
    elif token_result == "invalid":
        """
        Here we wont give the resending option because the token does not exist.
        This is to prevent token forgery.
        **kwargs:
        error: The error message to be passed in the error page
        return_page: The page for the anchor link in the error page that the user can return to
        """
        return render_template('auth/admin-auth-error.html', error="Invalid Token", return_page="login")
    elif token_result == "expired":
        """
        We will give the user an option to resend a different token to the mailbox linked
        to the expired token using a flash message
        **kwargs:
        error: The error message to be passed in the error page
        return_page: The page for the anchor link in the error page that the user can return to
        """
        # fetch user associated with the expired token and the staff by extension
        user = read_user(id=attempted_token.user_id)
        #staff = read_staff(id=user.staff_id)
        # The user and staff objects are used to retrieve their name and email used in the verification url
        flash(Markup("Dear user: You can \
            <a href='/auth/admin/verification-mail/login/"+user.email_address+"' \
            style='color: inherit;'>\
            <u>resend the email</u></a> for account verification"), category="warning")
        return render_template('auth/admin-auth-error.html', error="Token Expired", return_page="login")

@app.route('/auth/admin/verification-mail/<page>/<user_firstname>/<email>')
def send_admin_verification_email(page, user_firstname, email):
    """
    This function resends the account verification email to the admin when
    trying to activate their account with an expired verification token
    URL params include:
    page: the page to redirect to when the email has been sent
    user_firstname: The fisrtname of the staff
    email: the email address of the staff to which the email will be sent to
    """
    if not connect():
        # check if there is no internet connection and let user know
        flash_response('SL009')
    fetch_user = read_user(email_address=email)
    # generate a token that will be used to verify if the user owns that email address
    verification_id = id_generator(10)
    # get the expiry datetime for the token
    expiry_in_minutes = app.config['TOKEN_LIFETIME']
    # Add 5 minutes to now
    expiry_time = datetime.now() + timedelta(minutes=expiry_in_minutes)
    # store the token in the database with expiry time
    verification_token = create_account_verification_entry(
        user_id=fetch_user.id,
        token=verification_id,
        token_expiry=expiry_time
    )
    # send email functionality if token is successfully stored
    if verification_token == respond('201'):
        msg = Message('Savannah Online Services Admin Account Verification', recipients=[
            fetch_user.email_address],
            html=render_template('mail/admin-account-activation.html',
            firstname=user_firstname,
            verification_code=verification_id,
            organization=organization))
    # recepients can accomodate a list of many recepients
    mail.send(msg)
    # if page was 'login'
    if page == 'login':
        flash_response('SF006')
        return redirect(url_for('admin_login'))
    # if the redirect page is not 'login' it is invalid so redirect to error page
    else:
        return render_template('auth/auth-error.html', error="Oops! An error occurred", return_page="admin_login")
