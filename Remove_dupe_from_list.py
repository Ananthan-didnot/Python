'''
Author : Ananthakrishnan K V
date : 19-11-2024
'''
list=[50,66,95,66,70,50,43,66]
empty_list =[]
for number in list:
    if number not in empty_list:
        empty_list.append(number)
print("First list=",list)
print("Unique list=",empty_list)
