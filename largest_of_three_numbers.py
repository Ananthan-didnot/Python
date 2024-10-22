'''
Auther :Ananthakrishnan K V
Date   :22-10-2024
Python program to find the largest of three numbers
'''


num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is larger")
elif num2>num1 and num2>num3:
    print(f"{num2} is larger")
else:
    print(f"{num3} is larger")