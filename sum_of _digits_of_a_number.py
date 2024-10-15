'''
Auther:Ananthakrishnan K V
Date:15/10/2024
Python program to find the sum
of digits of a number
'''

num = int(input("Enter a number:"))

sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+r
print(sum)