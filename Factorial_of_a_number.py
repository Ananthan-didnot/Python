'''
Auther:Ananthakrishnan K V
Date:29-10-2024
Python program to find the factorial of a number
'''

number = int(input("Entert a number: "))

factorial=1
while number>0:
    factorial=factorial*number
    number-=1
print(factorial)