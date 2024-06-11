#!/usr/bin/python3

# CTF POSt ME


import requests as rr

url = "http://192.168.43.101:89/"

header ={'User-Agent':'Hack-A-Day with me_dheeraj'}

payload = {"username":"admin","password":"71urlkufpsdnlkadsf"}

data = rr.post(url,params=payload,headers=header,timeout=20)

print (data.status_code)

print (data.text)


