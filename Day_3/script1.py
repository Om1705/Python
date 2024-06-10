#!/usr/bin/python3

#   Day 2       Date : 10/06/24

import requests as rr

url = "https://api.khatabook.com/v1/auth/request-otp"

header ={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}


payload = '{"country_code":"+91","phone":"1234567890","app_signature":"Jc/Zu7qNqQ2"}'

data = rr.post(url , data = payload , headers=header , timeout=20)

print (data.status_code)

print (data.text)

