import requests
from time import sleep

while True:
    resp=requests.get("http://192.168.0.20:5000/aud")
    print(resp.status_code)
    print(resp.json())
    sleep(1)