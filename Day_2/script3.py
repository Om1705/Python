#!/usr/bin/python3


try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()

except IOError as a:
    print("IOError:", a)

except Exception as b:
    print("CommonError:", b)

finally:
    print("Finally its over")
