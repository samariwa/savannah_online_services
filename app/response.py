from app import app
from flask import flash

"""
This module contains all responses in the application with their
corresponding codes in a dictionary format
"""
response_dictionary = {
    # For each response category outlined below, leave extra blank codes that can be used in future
    # Authentication success
    # Code points to array containing message and flash message category (for flash color output)
    'SF001': ['Success! You are logged in', 'success'],
    'SF002': ['Dear user: You just logged out. We hope to see you soon', 'info'],
    'SF003': ['Dear user: Password successfully reset', 'info'],
    'SF004': ['Dear user: Your account has successfully been activated. Log in to proceed', 'success'],
    'SF005': ['Dear user: Account successfully created!', 'success'],
    'SF006': ['Dear user: We have just sent you a verification email to your mailbox. To proceed, please verify your account', 'info'],
    'SF007': ['Dear user: Please check your mailbox for a password reset link. The link expires in ' + str(app.config['TOKEN_LIFETIME']) + ' minutes', 'success'],
    'SF008': ['Dear user: Your account has successfully been activated. Please reset your password to proceed', 'info'],
    'SJ001': ['',''],
    # Authentication errors
    # Code points to array containing message and flash message category (for flash color output)
    'SF009': ['Dear user: Invalid login, Try again', 'danger'],
    'SF010': ['Dear user: An error was encountered when creating your account, please contact support', 'warning'],
    'SF011': ['Dear user: You might have an account, recover if you forgot password or contact support', 'warning'],
    'SF012': ['Dear user: Kindly enter email address used in registration', 'warning'],
    'SF013': ['Dear user: Please reset with a password that has not been previously used', 'warning'],
    'SF014': 'Please verify that you are not a robot',
    'SF015': ['Dear user: An unexpected error was encountered. Please Try again', 'warning'],
    'SF016': 'Please Enter Your First Name',
    'SJ009': 'Please Enter Your Last Name',
    'SJ010': 'Please Enter Your Physical Address',
    'SJ011': 'Please Enter Your Email Address',
    'SJ012': 'Please Enter Your Mobile Number',
    'SJ013': 'Please Enter Your Password',
    'SJ014': 'Please Confirm Your Password',
    'SJ015': 'Password Must Have a Minimum of 8 Characters',
    'SJ016': 'Please Enter a Memorable Password',
    'SK009': 'Your Passwords Do Not Match',
    'SK010': 'Email Deliverability Check Failed',
    'SK011': 'Please Enter a Valid Phone Number',
    'SK012': 'Please Agree To the Terms & Conditions To Proceed',
    'SK013': 'Physical Address Too Long',
    'SK014': 'First Name Too Long',
    'SK015': 'Last Name Too Long',
    'SK016': ['Dear user: Your account is on hold. Please contact support', 'warning'],
    'SL009': ['Dear user: No Internet Connection', 'warning'],
    # POST errors
    # Code points to array containing error description and a user friendly message
    'SF017': ['Image Missing', 'Error: Image Missing'],
    'SF018': ['Invalid Image', 'Error: Invalid Image. Allowed formats (.png, .jpg, .jpeg, .gif)'],
    'SF019': ['Value Error', 'Error: The refund value cannot be greater than the account balance'],
    'SJ017': ['Value Error', 'Error: The reclass quantity cannot be greater than the quantity of the source product'],
    'SJ018': ['Value Error', 'Error: The damaged quantity cannot be greater than the current quantity'],
    'SJ019': ['Download Error', 'Error: File not Found'],
    # Database errors
    # Code points to array containing error description and a user friendly message
    'SF020': ['IntegrityError', 'Resource Exists'],
    'SF021': ['TypeError', 'Invalid Argument'],
    'SF022': ['DataError', 'Invalid Data Type'],
    # Access Rights errors
    'SF023': ['Dear User, You do not have sufficient rights to view this page!', 'danger'],
    # Successful HTTP responses
    # Code points to error description
    '200': 'OK',
    '201': 'Created',
    # Client HTTP errors
    # Code points to error description
    '400': 'Bad Request',
    '403': 'Forbidden',
    '404': 'Not Found',
    '405': 'Method Not Allowed',
    '408': 'Request Timeout',
    '413': 'Request Entity Too Large',
    '415': 'Unsupported Media Type',
    '422': 'Unprocessable Entity',
    '429': 'Too Many Requests',
    # Server HTTP errors
    # Code points to error description
    '500': 'Internal Server Error',
    '503': 'Service Unavailable',
    'X01': 'Delivery Assigned to another person'
}


def respond(code):
    """
    This function takes in the code (a key of the response_dictionary) and
    returns the value that could either be an array or string
    """
    return response_dictionary[code]


def flash_response(response):
    """
    This function takes in response array from the respond function and outputs
    a flash message based on the index values.
    """
    return flash(respond(response)[0],
                 category=respond(response)[1])
