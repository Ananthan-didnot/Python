'''
Auther:Ananthakrishnan K V
Date:29-10-2024
Python program to check whether the entered number is Prime or not
'''
number = int(input("Enter a number: "))

isprime=True
for i in range(2,number//2+1):
    if number % i ==0:
        isprime=False
        break
if isprime:
    print(f"The number {number} is a prime number")
else:
    print(f"The number {number} is not a prime number")