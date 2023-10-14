import requests
from app import app

app.logger.info("---------------------CRON JOB-----------------------")
req = {"start": True}
url = "https://sympha-app.herokuapp.com/admin/scheduler/"
# url = "http://127.0.0.1:5000/admin/scheduler/"
res = requests.post(url, json=req)

print(res.text)
