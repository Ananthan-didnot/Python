'''
Auther :Ananthakrishnan K V
Date   :22-10-2024
Python program to convert temperature values back and forth between Celsius and Fahrenheit.
 The user should be able to input a temperature in Celsius or Fahrenheit,
 and the program should convert it to the other unit using the formula
'''


temp = float(input("Enter temperature: "))
unit = input("Is this in (C)elcius or (F)ahrenheit: ")

if unit == 'C' or unit== 'c':
    f=(9/5*temp)+32
    print(f"{temp} celcius is {f} fahrenheit")
elif unit =='F' or unit == "f":
    c=5/9*(temp-32)
    print(f"{temp} fahrenheit is {c} celcius")
else:
    print(f"{unit} is invalid input")
