'''
Auther :Ananthakrishnan K V
Date   :22-10-2024
Python program to convert temperature values back and forth between Celsius and Fahrenheit.
 The user should be able to input a temperature in Celsius or Fahrenheit,
 and the program should convert it to the other unit using the formula
'''


temperature = float(input("Enter temperature: "))
scale = input("Is this in (C)elcius or (F)ahrenheit: ")

if scale == 'C' or scale== 'c':
    f=(9/5*temperature)+32
    print(f"{temperature} celcius is {f} fahrenheit")
elif scale =='F' or scale == "f":
    c=5/9*(temperature-32)
    print(f"{temperature} fahrenheit is {c} celcius")
else:
    print(f"{scale} is invalid input")
