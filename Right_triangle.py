"""
Author:Ananthakrishnan KV
Date:30/11/2024
A program that accepts
the lengths of three sides of a triangle as inputs.
 The program should output whether or not the triangle is a right triangle
"""
def right_triangle():
    sides=[side1,side2,side3]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    return False



side1 = int(input("Enter the length of first side: "))
side2 = int(input("Enter the length of second side: "))
side3 = int(input("Enter the length of third side: "))
if right_triangle():
    print("The given triangle is a right triangle.")
else:
    print("The given triangle is not a right triangle.")



