import requests
import base64
from datetime import datetime
from app.mpesa_tests.get_token import get_token, get_access_token
from app import app

def get_timestamp():
    """20230321193306"""
    now = datetime.now() # current date and time

    timestamp_daraja = now.strftime("%Y%m%d%H%M%S")
    return timestamp_daraja


def generate_password(ShortCode, passkey, timestamp):
    """generate_password
    base64.encode(Shortcode+Passkey+Timestamp)
    """
    sample_string = f"{ShortCode}{passkey}{timestamp}"
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def push_request(ShortCode):
    """9354275
    174379
    6125693"""
    PartyA = 254702110627
    Amount = 1
    myUrl = "https://sympha-app.herokuapp.com/crud/stk-push-result"
    requestUrl = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    timestamp = get_timestamp()
    access_token = get_token()
    passkey = "1c4cf5e92ee09b6baa4f17da60fdedb89a1d37e237f9ff829d20b393bce0f17a"

    #testkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    password = generate_password(ShortCode, passkey, timestamp)

    header = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    app.logger.info(header)

    payload = {
        "BusinessShortCode": ShortCode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": Amount,
        "PartyA": PartyA,
        "PartyB": 9354275,
        "PhoneNumber": PartyA,
        "CallBackURL": myUrl,
        "AccountReference": "null",
        "TransactionDesc": "MeatGroceries"
    }

    response = requests.request(
        "POST",
        requestUrl,
        headers=header,
        json=payload
    )
    app.logger.info(response.json())

def initiate_stk_push(msisdn, amount):
    access_token = get_access_token()

    # Production
    endpoint = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    myUrl = 'https://sympha-app.herokuapp.com/crud/stk-push-result'
    """
    # Sandbox
    endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    myUrl = 'https://9dc7-41-90-179-155.ngrok-free.app/crud/stk-push-result'
    """
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {access_token}'}
    now = datetime.now() # current date and time
    timestamp = now.strftime("%Y%m%d%H%M%S")
    shortcode = "6125693"
    passkey = "1c4cf5e92ee09b6baa4f17da60fdedb89a1d37e237f9ff829d20b393bce0f17a"
    password = generate_password(shortcode, passkey, timestamp)
    payload = {
        "BusinessShortCode": shortcode,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": amount,
        "PartyA": msisdn,
        "PartyB": 9354275,
        "PhoneNumber": msisdn,
        "CallBackURL": myUrl,
        "AccountReference": "null",
        "TransactionDesc": "MeatGroceries"
    }
    result = requests.post(endpoint, headers=headers, json=payload)
    return result.json()