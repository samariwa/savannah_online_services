import requests
from app.mpesa_tests.get_token import get_token, get_access_token

def simulate():
    requestUrl = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate'
    access_token = get_access_token()

    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {access_token}'}
    request_body = {
        "ShortCode": "600999",
        "CommandID": "CustomerPayBillOnline",
        "BillRefNumber": "PaymentSimulation",
        "Msisdn": "254708374149",
        "Amount": 1
    }

    response = requests.post(requestUrl, headers=headers, json=request_body)
    return response.json()