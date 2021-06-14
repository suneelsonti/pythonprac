# This example demos logical operators 'and' 'or' that can combine multiple conditions#
print('\n')
price = 1000000

has_good_credit = True
has_high_income = True

if has_high_income and has_good_credit:
    down_payment = price * .1
    print(f"You are eligible for a loan, and your down payment is: ₹ {down_payment}")
elif has_good_credit or has_high_income:
    down_payment = price * .1
    print('\n' f"Your down-payment for this property is, ₹ {down_payment}")
else:
    down_payment = price * .2
    print('\n' f"Your down-payment for this property is, ₹ {down_payment}")

