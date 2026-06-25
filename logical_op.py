# and
#or
#not
high_income = False
good_credit = True
if high_income and good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
age = 22
if age >= 18 or age <= 65:
    print("Eligible for work")
high_income = True
good_credit = False 
if not high_income or not good_credit:
    print("Not eligible for loan")