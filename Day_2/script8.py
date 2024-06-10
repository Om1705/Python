#!/usr/bin/python3

import requests,random

url="https://pastebin.com/raw/01yJu4gY"

h={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

data = requests.get(url,headers=h,timeout=10)

#print(data.text)
d = data.text.split("\r\n")


for i in d:

    url1=i.strip()
     
    data2 = requests.get(url1, headers=h,  timeout=10)
    num = str (random.randint(1,100))
    g = open("image"+num+".jpg","wb")

    g.write(data.content)

    g.close()

