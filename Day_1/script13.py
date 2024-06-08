#!/usr/bin/python3

#System calls       
#Trying os.system  and  subprocess.call

import os,subprocess

a = subprocess.call("pwd", shell=True)
print(a)
print("")
b = os.system("ls")
print("")
c = subprocess.getoutput("pwd")
print(" ")
print(c)
