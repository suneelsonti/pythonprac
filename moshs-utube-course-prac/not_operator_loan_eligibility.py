
#not operator reverses the read of true boolean value of a variable to False. False stays the same.
'''in the below example not has_criminal_record translates to
if has_criminal_record is false
'''
#Loan eligibility:
#Use case 1: expectation is to print second iteration of the command

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print("You are eligible for a loan !!!")
else:
    print("Sorry your loan application has been declined !")

#Use case 2: expectation is to print first iteration of the command

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('\n'"You are eligible for a loan !!!")
else:
    print("Sorry your loan application has been declined !")