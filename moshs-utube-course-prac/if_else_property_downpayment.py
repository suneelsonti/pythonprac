# conditional code:
# Exercise is to print the downpayment of a house worth 1$ dollars.
# Conditions : If buyer has good credit score, downpayment is 10% of property value, else it is 20%
'''
for_good = 1000000 * .1
others = 1000000 * .2

is_goodcredit = False

if is_goodcredit:
    print("Your downpayment is, " + str(for_good))
else:
    print("Your downpayment is, " + str(others))
'''

# Another way around

price = 1000000

has_good_credit = False

if has_good_credit:
    down_payment = price * .1
else:
    down_payment = price * .2
print("Your downpayment for this property is, " + str(int(down_payment)))

print(f"Your down-payment is, {down_payment}")