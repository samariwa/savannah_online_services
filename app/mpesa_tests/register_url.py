import requests
from app.mpesa_tests.get_token import get_token, get_access_token
from app import app

def register_url(ShortCode):
    """
    # Sandbox
    requestUrl = 'https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl'
    myUrl = "https://9dc7-41-90-179-155.ngrok-free.app/admin/validate/"
    """
    # Production
    requestUrl = 'https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl'
    myUrl = "https://sympha-app.herokuapp.com/crud/validate"
   
    token = get_access_token()
    header = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    app.logger.info(header)
    payload = {
        "ShortCode": ShortCode,
        "ResponseType": "Completed",
        "ConfirmationURL": myUrl,
        "ValidationURL": myUrl,
    }

    response = requests.request(
        "POST",
        requestUrl,
        headers=header,
        json=payload
    )
    app.logger.info(response.text)
