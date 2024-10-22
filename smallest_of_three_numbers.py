'''Auther:Ananthakrishnan K V
Date:15/10/2024
Python program to determine the smallest number from given numbers'''



num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter Third number:"))
if num1<num2 and num1<num3:
    print(f"{num1} is smaller")
elif num2<num3 and num2<num1:
    print(f"{num2} is smaller")
else:
    print(f"{num3} is smaller")

