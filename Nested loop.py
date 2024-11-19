row = int(input("enter the number of row: "))
print("\nIncreasing Pattern")
for i in range(row+1):
    for j in range(i):
        print('*\t',end='')
    print()
print("\nDecreasing Pattern")
for i in range(row,0,-1):
    for j in range(i):
        print('*\t',end='')
    print()

print("\nHill Pattern")
for i in range(1,row+1):
        for j in range(row-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print('*',end=" ")
        print()
print("\nReverse Hill pattern")
for i in range(row,0,-1):
        for j in range(row-i):
            print(" ",end=" ")
        for k in range(2*i-1):
            print('*',end=" ")
        print()