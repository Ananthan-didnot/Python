'''
Auther: Ananthakrishnan K V
Date: 06-10-2024
Python program that uses functions from the math module to perform the following operations on a number provided by the user:

Find the square root.
Calculate the factorial.
Raise the number to the power of 2.
'''

import math

number1=int(input("Enter a number: "))

square_root = math.sqrt(number1)
factorial = math.factorial(number1)
exponential = math.pow(number1,2)
print(square_root)
print(factorial)
print(exponential)