"""
Author:Ananthakrishnan KV
Date:30/11/2024
Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    Every number should contain exactly 10 digits.
    The first digit should be 7 or 8 or 9
"""
number=input("Enter your pone number: ")
def phone_number():
    if (len(number)==10 and (number[0]=='7' or number[0]=='8' or number[0]=='9')):
        print(f"The number is Valid :{number}")
    else:
        print(f"The number is invalid:{number}")
phone_number()


