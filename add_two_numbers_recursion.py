"""
Author:Ananthakrishnan KV
Date:2/1/2024
Recursive function to add two positive numbers.
"""


def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1 + 1, n2 - 1)

print(add_numbers(5,8))