'''
Author : Ananthakrishnan K V
date : 19-11-2024
1.create 2 empty list
2.input elements from user
3.Merge 2 list
4.sort even and odd number

'''

list1=[]
list2=[]
list1_size=int(input("Enter the number of elements in list 1: "))
print("Enter the elements for the first list: ")
for i in range(list1_size):
    print(list1.append(int(input())))
list2_size=int(input("Enter the number of elements in list 2: "))
print("Enter the elements for the second list: ")
for i in range(list2_size):
    print(list2.append(int(input())))
print(list1,list2)

list3=list1+list2
print(f"Merged list{list3}")

even_list=[]
odd_list=[]
for i in list3:
    if i % 2 ==0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
print(f"Final list = {even_list+odd_list}")
