import requests
from time import sleep

while True:
    resp=requests.get("http://127.0.0.1:5000/")
    print(resp.status_code)
    print(resp.json())
    sleep(1)