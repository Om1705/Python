#!/usr/bin/python3

f=open("file.txt","w+")
f.write("THIS IS SECONFD LINE ")


f.close()

f=open("file.txt","r")
print(f.read())
f.close()
