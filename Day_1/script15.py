#!/usr/bin/python3


#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error meaasage.
#If the score is between 0.0 and 1.0
#Print a grade using the following table:
#
#Score Grade:
#
#   >=0.9              A
#   >=0.8              B
#   >=0.7              C
#   >=0.6              D
#   <=0.6              F
#   Anything Else      BAD SCORE


while True:

    i=(input("Enter score : "))

    if "1.0" >= i >="0.9":
        print("A")
    elif "0.9" > i >= "0.8":
        print("B")
    elif "0.8" > i >="0.7":
        print("C")
    elif "0.7" > i >= "0.6":
        print("D")
    elif i < "0.6":
        print("F")
    else:
        print("BAD SCORE")

