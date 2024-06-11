#!/usr/bin/python3



#        Port SCANNER using argparse

#       python3 script2.py  -h x.x.x.x -p 80




import socket,time,argparse

parser = argparse.ArgumentParser(description="This is PORT SCANNER")
parser.add_argument("-host",type=str, help="Provide host",required=True)
parser.add_argument("-p",type=str, help="Enter port no", required=False)
parser.add_argument("-iL",type=str, help="Provide a proper file name", required=False)
parser.add_argumrnt("-exclude",type=int, help="Provide a port to Exclude",required=False)

a=parser.parse_args()

if a.p and a.iL:
    print("Please enter a valid input : Either Enter -p or -iL ")
    exit()
host1 = a.host

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
    f = open(a.iL, "r")
    for i in f.readlines():
        if i==a.exclude:
            exit()
        else:
        if run(int(i)):
            print("Open",)
            print("Closed",":   ",i)


def fun2():
    for i in range(int(port1[0]),int(port1[1])+1):
        if run(int(i)):
            print("Open",":  ",i)
        else:
            print("Closed", ":  ",i)

if a.p:
    if "-" in a.p:
        port1 = a.p.split('-')
        fun2()
    elif "," in a.p:
        port1 = a.p.split(',')
        fun1()
    else:
        port1 = a.p.split(',')
        fun1()

if a.iL:
    f = open(a.iL, "r")
    for i in f.readlines():
        if run(int(i.strip())):
            print("Open",":  ",i)
        else:
            print("Closed",":  ",i)
