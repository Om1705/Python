#!/usr/bin/python3

import requests

url = "https://www.youtube.com"
data = requests.get(url,timeout=10)



print (data.status_code)    #Gives Status Code
print ("     ")
print (data.headers)        #Gives data in dictionary data type 
print ("     ")
print (data.headers['server'])  #Gives value of a specific key
print ("     ")
print (data.headers.items())     #Changes the dict data type to List 
print ("    ")


for a,b in data.headers.items():
    print ("{} : {}".format (a,b))


#print (data.text)        #print body in ASCII Block

