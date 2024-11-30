"""
Author:Ananthakrishnan KV
Date:30/11/2024
Upper case and lower case
"""
def case_count():
    upper_case=0
    lower_case=0
    sample_string = "The quick Brow Fox"
    for i in range(0,len(sample_string)):
        if sample_string[i].isupper():
            upper_case+=1
        elif sample_string[i].islower():
            lower_case+=1
    return  upper_case,lower_case
upper_case,lower_case=case_count()

print(f"No of upper case:{upper_case} ")
print(f"no of lower case:{lower_case}")