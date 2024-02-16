"""This module contains general functions that can be applicable throughout the project"""
import string, random, uuid
from app import app
# time modules
from datetime import datetime,  timedelta, date

def create_timestamp():
    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")

def date_today():
    return datetime_to_standard_date(datetime.today())

def get_expected_delivery_time(order_time):
    """
    get_expected_delivery_time(order_time)
    This function is used to calculate the expected delivery time given the
    set time limit and the time of order passed in as an argument.
    """
    delivery_limit = timedelta(minutes=app.config['DELIVERY_TIME_LIMIT'])
    expected_delivery_time = order_time + delivery_limit

    return expected_delivery_time

# Function to convert string to datetime
def str_to_datetime(str):
    format = '%Y-%m-%d %H:%M:%S'  # The format
    date_time = datetime.strptime(str, format)

    return date_time

def datetime_to_standard_date(date_time):
    return date_time.strftime("%Y-%m-%d")

# Function to convert datetime to time
def datetime_to_time(date_time):
    return date_time.strftime('%H:%M')

# Function to convert datetime to time
def stringify_datetime_object(date_time):
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def timestamp_to_standard_format(timestamp_str):
    return timestamp_str.strftime('%d/%m %H:%M')

def is_datetime_object(value):
    return isinstance(value, datetime)

def is_date_object(value):
    return isinstance(value, date)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    """ This function generates a random string of combined characters and digits\
    based on the size specified as an argument and returns it """
    return ''.join(random.choice(chars) for _ in range(size))

def empty_input_fields(fields):
    return [key for key, value in fields.items() if value == '']

def get_uuid():
    # Generate a version 4 UUID
    uuid4 = uuid.uuid4()

    # Convert UUID to string
    uuid_str = str(uuid4)

    return uuid_str

def generate_random_string(length):
    """
    This function generates a random string of specified length
    """
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))