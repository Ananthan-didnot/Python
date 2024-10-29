'''
Auther:Ananthakrishnan K V
Date:29-10-2024
Python program to print multiplication table of entered number
'''
number = int(input("Enter a number:"))

for i in range(1,13):
    print(f"{number} * {i}\t= {number*i}")
