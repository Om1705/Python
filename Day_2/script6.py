#!/usr/bin/python3

import requests
while True:
    url = "https://webhook.site/a7d47df1-0153-4449-b8c3-570f300e665e"

    h= {'User-Agent':'Khada hun aaj bhi wahi Ki dil fir bekaraar hai Khada hun aaj bhi wahin Ki tera intezaar hai'}
    data = requests.get(url,headers=h,timeout=10)


    print(data.status_code)















