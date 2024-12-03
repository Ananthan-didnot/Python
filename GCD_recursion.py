"""
Author:Ananthakrishnan KV
Date:2/1/2024
Recursive function to find the greatest common divisor of two positive numbers.
"""

def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
print(gcd(1220,516))