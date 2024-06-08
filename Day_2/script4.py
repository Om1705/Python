#!/usr/bin/python3


#Statement :  
#               -read a file which contains targets
#               -run os command
#                   host -t domain.txt
#               -use readlines()
#               Hint : Use i.strip()
#
#       
#       Task 2: 
#                   host -t domain.txt -o file.txt
#                   store the result in a txt file 
#                   Take the file name from user
#                   
#                   And If user didnt gave the file name then only give the result DONT STORE RESULT IN FILE 


def fun1():

    import argparse
    import subprocess as ss


    parser = argparse.ArgumentParser(description="This is Domain resolver")

    parser.add_argument("-f",help="Provide domains list file", required=True)
    parser.add_argument("-o",help="Provide a new text file name",required=False)
    a = parser.parse_args()

    f = open(a.f,"r")
    b = f.readlines()
    for i in b:
        if a.o:
            h = open(a.o,"a")
            d = h.writelines(ss.getoutput("host -t a {}".format(i)))
            h.close()
        else:
            print(ss.getoutput("host -t a {}".format(i)))
       
    f.close()
try:
    fun1()

except IOError as a:
    print(a)




















    




