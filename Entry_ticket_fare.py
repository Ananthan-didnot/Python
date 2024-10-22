'''Auther:Ananthakrishnan K V
Date:15/10/2024
Python program to determine the emtry ticket fare
in a zoo based on age
'''



age = int(input("Enter your age:"))
if age<10:
    print("Entry ticket fare=7")
elif    age>=10 and age<60:
    print("Entry ticket fare=10")
else:
    print("Entry ticket fare=5")
