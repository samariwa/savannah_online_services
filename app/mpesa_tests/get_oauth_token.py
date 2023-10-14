import base64
import requests
import json
from app import app

consumer_key = "7BVG6YE8GE0fPMpFKj2dsAtnCv58p08Z"
consumer_secret = "28lTH9an2ZyAQidh"
sample_string = f"{consumer_key}:{consumer_secret}"
sample_string_bytes = sample_string.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

app.logger.info(base64_string)

app.logger.info(f"Bearer {base64_string}")
app.logger.info(base64_bytes)
response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': f"Basic {base64_string}" })
app.logger.info(response.text.encode('utf8'))
"""
# 'UDA1RGZIeGlZWFJEN3F6ZTVYdTlDeWlURk9ST296dWc6czdHZUwzREFKeWxmUDc1Rw=='
response = requests.request("GET", 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials', headers = { 'Authorization': f'Basic {base64_string}' })
app.logger.info(response.text.encode('utf8'))
# b'{\n            "access_token": "di9CkCgBEIJphMHmNx82XafCZuZ8",\n            "expires_in": "3599"\n        }\n        '
json.loads(response.text.encode('utf8'))
# {'access_token': 'gZ9A4MCgA9FisdHhNQSkZDzz1JJC', 'expires_in': '3599'}
token = json.loads(response.text.encode('utf8'))['access_token'] 

app.logger.info(token)

Headers
Key: Authorization
Value: Basic SW9iYnhQQTJTUjQ3U1o3TDNnc3I4Y1BaY2R4cEdFeWI6NXFFYkJVY0pzVUxpZmZQdQ==
"""

