# 1. Problem 1
has_high_income = True
has_good_credit = True

# and operation
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


# or operation
if has_high_income or has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# 2. Problem 2
has_good_cred = True
has_criminal_record = False

if has_good_cred and not has_criminal_record:
    print("No Criminal record and has good cred so eligible for loan")
