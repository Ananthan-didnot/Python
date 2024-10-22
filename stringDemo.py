'''
Auther:Ananthakrishnan K V
Date:15/10/2024
Python program to check whether the given number
is positive or negative
'''

number = int(input("Enter a a number:"))
if number>0:
    print(f"The number {number} is Positive")
elif number<0:
    print(f"The number {number} is Negative")
else:
    print(f"The given number {number} is zero")