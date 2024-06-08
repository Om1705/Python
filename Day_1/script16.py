#!/usr/bin/python3

# TASK :
#    python3 script.py -s admin -d google.com
#                                   {domain}



import argparse,subprocess as ss

parser = argparse.ArgumentParser(description="This is Domain Resolver")

parser.add_argument("-s",type=str,help=" Provide Sub domain Name ",required=True)
parser.add_argument("-d",type=str,help=" Provide Domain Name ",required=True)

a=parser.parse_args()

print(ss.getoutput("host -t a {}.{}".format(a.s,a.d)))
