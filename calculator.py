'''
AUther: Ananthakrishnan K V
Date: 08-10-2024
A simple calculator
'''

num1 = float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

sum = (num1+num2)
print(f"The sum of {num1} and {num2} is: {sum}")

difference = (num2-num1)
print(f"The difference when {num1} is subtracted from {num2} is: {difference}")

product = (num1*num2)
print(f"The product of {num1} and {num2} is: {product}")

division = round((num1/num2),2)
print(f"The quotient when {num1} is divided by {num2} is: {division}")

mod = (num1%num2)
print(f"The remainder when {num1} is divided by {num2} is: {mod}")

result = (num1 + num2) * num3 / 2
print(f"The result of ({num1} + {num2}) * {num3} / 2 is: {result}")