#author : Ananthakrishnan K V
#date : 06-10-2024
#calculator

number1 = float(input("Enter 1st number"))
number2 = float(input("Enter 2nd number"))
operator = input("Enter an operator (+,-,*,/)")

if operator =="+":
    result=(number1+number2)
    print(result)

elif operator=="-":
    result=(number1-number2)
    print(result)

elif operator=="*":
    result=(number1*number2)
    print(result)

elif operator=="/":
    result=(number1/number2)
    print(round(result, 3))
else: print(f"{operator} is not valid operator")
