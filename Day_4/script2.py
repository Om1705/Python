#!/usr/bin/python3



#        Port SCANNER using argparse

#       python3 script2.py  -h x.x.x.x -p 80




import socket,time,argparse

parser = argparse.ArgumentParser(description="This is PORT SCANNER")
parser.add_argument("-host",type=str, help="Provide command",required=True)
parser.add_argument("-p",type=str, help="Enter port no", required=True)

a=parser.parse_args()


host1 = a.host

'''if "-" in a.p:
    port1 = a.p.split('-')
    fun2()

if "," in a.p:
    port1 = a.p.split(',')
    fun1()'''

def run(port):
    #sock.close()
    try:
        #socket.timeout(5)
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host1, port))
       # sock.settimeout(5)
        sock.close()
        return True
    except:
        return False

def fun1():
    for i in port1:
        if run(int(i)):
            print("Open",":   ",i)
    
        else:
            print("Closed",":   ",i)


def fun2():
    for i in range(int(port1[0]),int(port1[1])+1):
        if run(int(i)):
            print("Open",":  ",i)
        else:
            print("Closed", ":  ",i)


if "-" in a.p:
    port1 = a.p.split('-')
    fun2()
elif "," in a.p:
    port1 = a.p.split(',')
    fun1()
else:
    port1 = a.p.split(',')
    fun1()
