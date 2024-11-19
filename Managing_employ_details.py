information=[
    ('Jack','Finance',10000.00),
    ('Rose','Advertising',20000.0),
    ('Daniel','Networking',15000.0),
    ('Hugie','Hiring',8000.0),
    ('Fred','Technical',12000.0)
]
salary_threshold=float(input("Enter the salary_threshold: "))
total_annual_payroll=0
for employ in information:
    name,department,salary=employ
    total_annual_payroll+=salary*12
    if salary>salary_threshold:
        print(f"Employ who have Monthly salary greater than {salary_threshold}=\t{name}\t{department}\t{salary}")
print(f"Total annual payroll={total_annual_payroll}")

