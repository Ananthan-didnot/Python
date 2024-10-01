'''Auther : Ananthakrishnan K V
Date : 01-10-2024
Python programe to get student details'''


name=input("Enter the student name:")
roll_number=int(input("Enter your roll number:"))
roll_number=roll_number+1
cgpa=float(input("Enter your CGPA:"))
percentage=cgpa*10


print("Your name is",name)
print("Your roll number is",roll_number)
print("Marks Percentage is",percentage,"%")