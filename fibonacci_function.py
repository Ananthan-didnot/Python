"""
Author:Ananthakrishnan KV
Date:3/1/2024
Program to define a module to find Fibonacci Numbers and import the module to another program.
"""



def fibonacci():
    n=int(input("Enter the limit: "))
    first_num=1
    second_num=0
    third_num=0
    for i in range(n):
        print(third_num)
        third_num=first_num+second_num
        first_num=second_num
        second_num=third_num


