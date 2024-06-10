#!/usr/bin/python3


#
#               Thi st
#
#
#
#
#


import argparse, requests

parser = argparse.ArgumentParser(description="This Is TOOL to Check the sub-domain is ALIVE or DEAD")

parser.add_argument("-f", help="Provide Sub Domain file", required=True)

a=parser.parse_args()

f = open(a.f,"r")

r = f.readlines()


for i in r:
    try:
        
        url = "http://{}".format(i.strip())
        
        h = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}

        data = requests.get(url ,headers=h, timeout=10)

        c = data.status_code

        if c == 200:
            print(url + "  [{}]".format(c))'
        elif c== 301 or c==302:
            print("https://" + str(i.strip()) + " [{}]".format(c))
        elif c == 403:
            print(url + " [{}]".format(c))

    except:
        pass
