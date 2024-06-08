#!/usr/bin/python3

import sys,subprocess

a=sys.argv[1]

if a == "-c":
    if sys.argv[2]:
        subprocess.call(sys.argv[2],shell=True)
    else:
        print("Provide a valid command")

elif a == "-h":
    print("-c : command")
    print("usage :","-c cmd")
else:
    print("Enter a valid option, see -h for help")



