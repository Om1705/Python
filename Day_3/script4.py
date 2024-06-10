#!/usr/bin/python3


import sys,re,requests


url = "https://www.bincodes.com/random-creditcard-generator/"

h = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

data = requests.get(url, headers=h, timeout=10)

#print(type(data.text))
for i in re.findall("[0-9]{14,16}",data.text):
    print("Card no  :" ,i)

