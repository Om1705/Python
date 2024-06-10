#!/usr/bin/python3


import sys,re,requests


url = "https://api.healthifyme.com/in/"

h = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

data = requests.get(url, headers=h, timeout=10)

#print(data.text)
#collect = re.findall(".*@")
a = data.text.split()
for i in a:
    collect = re.finditer("\w+@\w+\.\w{2,3}",i)
    for x in collect:
        print(x.group())

