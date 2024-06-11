#!/usr/bin/python3

import socket,time

#sock = socket.socket()

host1 = input("Enter ip: ")

#port1 = int(input("Enter a port number: "))

def run(port):
    #sock.close()
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((host1, port))
        sock.close()
        #sock.timeout(5)
        return True

    except:
        return False
        #sock.close()

for i in range(20,30):
    #sock.close()
    if run(i):
        print("Open",":",i)
        sock.close()
    else:
        print("Close",":",i)
        #time.sleep(5)

