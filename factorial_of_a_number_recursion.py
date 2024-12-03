"""
Author:Ananthakrishnan KV
Date:2/1/2024
Program to find the factorial of a number using Recursion
"""



def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))