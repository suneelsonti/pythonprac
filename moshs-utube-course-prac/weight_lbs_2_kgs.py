# In this program we are trying to convert user's input weight (in lbs) to kilos and print it to terminal
# There are always multiple ways to achieve an output, below are four ways to do so

'''
weight = input("Hello, please enter your weight in pounds:   ")
weight_in_pounds = int(weight)
weight_in_kilos = str( weight_in_pounds*0.453592)
print('\n'+"You currently weigh " + weight_in_kilos + " kilos")
'''
'''
weight = int(input("Hello, please enter your weight in pounds:   "))*0.45
weight_in_kilos = str(weight * 0.453592)
print('\n')
print("you weigh " + weight_in_kilos + " kilos")
'''
# Less is always more in programming.
"""
weight_in_kilos = int(input("Please enter you weight in lbs: "))*0.45
print("your weight in kilos: " + str(int((weight_in_kilos))))"""

#Shortest one line code for solving the statment. Yet not a very clean code

print("Your weight in kilos: " + str((weight_in_kilos := int(input("Please enter you weight in lbs: "))*0.45)))