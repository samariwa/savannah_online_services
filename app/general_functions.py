"""This module contains general functions that can be applicable throughout the project"""
import string
import random
import uuid
# for creating customers
from app import app, db, mail, Message, organization
from flask import render_template
# time modules
from datetime import datetime,  timedelta, date
from app.response import respond
import os
from werkzeug.utils import secure_filename
import pandas as pd

def create_timestamp():
    now = datetime.now()

    return now.strftime("%Y-%m-%d %H:%M:%S")

def date_today():
    return datetime_to_standard_date(datetime.today())

def date_tomorrow():
    return datetime_to_standard_date(datetime.today() + timedelta(1))

def date_1_day_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(1))

def date_2_days_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(2))

def date_3_days_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(3))

def date_4_days_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(4))

def date_5_days_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(5))

def date_6_days_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(6))

def date_next_week():
    return datetime_to_standard_date(datetime.today() + timedelta(7))

def date_week_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(7))

def date_2_weeks_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(14))

def date_3_weeks_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(21))

def date_4_weeks_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(28))

def date_month_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(30))

def date_2_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(60))

def date_quater_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(90))

def date_trimester_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(120))

def date_5_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(150))

def date_half_year_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(180))

def date_7_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(210))

def date_8_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(240))

def date_9_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(270))

def date_10_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(300))

def date_11_months_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(330))

def date_year_ago():
    return datetime_to_standard_date(datetime.today() - timedelta(360))

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


def allowed_image(filename):
    allowed_extensions = set(['png', 'jpg', 'jpeg', 'gif'])
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def upload_image(file, storage_path):
    result = {}
    if file.filename == '':
        result['status'] = respond('SF017')[0]
    elif file and allowed_image(file.filename):
        filename = secure_filename(create_timestamp()+'.jpeg')
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), storage_path, filename))
        result['status'] = respond('200')
        result['filename'] = filename
    else:
        result['status'] = respond('SF018')[0]
    return result

def empty_input_fields(fields):
    return [key for key, value in fields.items() if value == '']

def get_uuid():
    # Generate a version 4 UUID
    uuid4 = uuid.uuid4()

    # Convert UUID to string
    uuid_str = str(uuid4)

    return uuid_str


def update_model_using_defaults(csv_filename: str, new_cols_with_defaults: dict, create_controller):
    """update_model_using_defaults:
    A function used to update a database table with downloaded csv in a format that
    closely resembles our table/model. Typically, we will use this to populate default
    values once we add a new column to a database table.

    If using this with a csv whose column names do not resemble our column names for
    the table, we have to change this. 

    Args:
        csv_filename: (string) The name of the csv file that has the values to add to
                                the database
        new_cols_with_defaults: (dict) A dictionary in the following format
                        {'new_column_name': "default value"}
        create_controller: (function) A function used to populate values into the database
                                for member of the Model in question

    Note:
    - At this point, you have exported the current database into a csv file and added the
      required extra columns using sql or the psql dashboard
    - If you don't have a controller, just create one and import it into the place from which
      you are calling this function: i.e flask shell, etc
    
    This function might be biased to removing the id columns. This is to prevent duplicate
    pks and such errors. it is advisable to remove the PK column from the csv using any means
    if it does not have the name 'id'

    Example:
    >>> from app.controllers.create import create_mpesa_payment_record
    >>> from app.general_functions import update_model_using_defaults
    >>> update_model_using_defaults(
            "mpesa_txns.csv",
            {
                "source": "safaricom",
                "org_ac_bal": 0
            },
            create_mpesa_payment_record
        )
    """
    try:
        df = pd.read_csv(csv_filename)
        headers = list(df.columns)
        headers.remove('id')
        headers.remove('updated_at') # for NaN errors (Temporary)
        for i, row in df.iterrows():
            values = {header: row[header] for header in headers}
            for header in headers:
                values[header] = row[header]
            for col in new_cols_with_defaults:
                # add defaults    
                values[col] = new_cols_with_defaults[col]
            create_controller(**values)
        app.logger.info(f"Successfully Updated from {csv_filename}")
    except Exception as e:
        app.logger.error(e)

def comma_number_format(number):
    return f"{number:,}"