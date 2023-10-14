import requests
import base64
from flask import jsonify

sample_string = "P05DfHxiYXRD7qze5Xu9CyiTFOROozug:s7GeL3DAJylfP75G"


def get_auth(Username, Pass):
    sample_string = f"{Username}:{Pass}"
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def get_token():
    """get_token
    A function to return a token given organization short_code
    This is only temporary till we can hardcode the shortcode
    """
    # For production
    """
    auth_token = get_auth(
        "7BVG6YE8GE0fPMpFKj2dsAtnCv58p08Z",
        "28lTH9an2ZyAQidh"
    )
    """
    # For sandbox

    auth_token = get_auth(
        'ifDqd6upeBzjX3LN6nJEzh6dSLt9l9UE',
        'lAdOGUl5l8JWAv8d'
    )
    
    headers = {
        'Authorization': f"Basic {auth_token}"
    }
    # For production
    """
    url = 'https://api.safaricom.co.ke/oauth/v1/'\
        'generate?grant_type=client_credentials'
    """
    # For sandbox

    url = 'https://sandbox.safaricom.co.ke/oauth/v1/'\
          'generate?grant_type=client_credentials'
    
    response = requests.request(
        "GET",
        url,
        headers=headers
    )

    return response.json()['access_token']

def get_access_token():
    """
    # Sandbox
    consumer_key = 'ifDqd6upeBzjX3LN6nJEzh6dSLt9l9UE'
    consumer_secret = 'lAdOGUl5l8JWAv8d'
    access_token_url = 'https://sandbox.safaricom.co.ke/oauth/v1/'\
                       'generate?grant_type=client_credentials'
    """
    # Production
    consumer_key = '7BVG6YE8GE0fPMpFKj2dsAtnCv58p08Z'
    consumer_secret = '28lTH9an2ZyAQidh'
    access_token_url = 'https://api.safaricom.co.ke/oauth/v1/'\
                       'generate?grant_type=client_credentials'
    
    # Production
    headers = {'Content-Type': 'application/json'}
    auth = (consumer_key, consumer_secret)
    try:
        response = requests.get(access_token_url, headers=headers, auth=auth)
        response.raise_for_status()
        result = response.json()
        access_token = result['access_token']
        return access_token
    except requests.exceptions.RequestException as e:
        return e
