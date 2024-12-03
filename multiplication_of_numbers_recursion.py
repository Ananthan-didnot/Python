"""
Author:Ananthakrishnan KV
Date:2/1/2024
Recursive function to multiply two positive numbers
"""



def mult_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+mult_numbers(n1,n2-1)
print(mult_numbers(10,4))