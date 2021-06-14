# Weight converter:

weight = float(input("Please enter your weight: "))
type = input("Please mention if the weight is in lbs(L) or kgs(K): ")

if type.upper() == 'L':
    print(f"You weigh {weight / 2.20462} kilos")
elif type.upper() == 'K':
    print(f"You weigh is {weight * 2.20462} pounds")
else:
    print("This calculator only accepts L or K for unit representation")