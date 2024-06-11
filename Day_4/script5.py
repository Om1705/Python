#!/usr/bin/python3

# CTF POSt ME


import requests as rr

url = "http://192.168.43.101:89/"

header ={'User-Agent':'Mozilla/5.0'}


payload = '{"username":"X","password":"71urlkufp","Agent X says" :"Hack-A-Day with me_dheeraj"}'

data = rr.post(url,data=payload,headers=header,timeout=20)

print (data.status_code)

print (data.text)

