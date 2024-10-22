'''
Auther:Ananthakrishnan K V
Date:15/10/2024
Python program that calculate the final amount
 after applying the discount
'''
from termios import INPCK

bill_amount = int(input("Enter your Total bill amount:"))
if bill_amount>500:
    discount = bill_amount*.2
    print(bill_amount-discount)
elif bill_amount>=200   and bill_amount<=500:
    discount = bill_amount*.1
    print(bill_amount-discount)
else:
    print(bill_amount)