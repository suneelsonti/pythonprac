# arthematic operations supported in python

# Basic math opertors

print(10+10)
print(10-1)
print(10*2)
print(10/6) # output can be either int or float based on the numbers being divided
print(10//6) # output is always an integer
print(10%3) # % sign denotes modulus, basically reminder of the division. the value should be 1 in this case
print(2**3) # to the power off. ** denotes exponent value.

#Augument assignment operator
# used to enhance the code

#regular code:
x = 5
x = x+3 # incremented x's value
print(x)

x += 3 # += is the enhancement
print(x)

x -= 6
print(x)

# Operator precedence: Python applies the same basic math rules - BODMAS - paranthesis, exponent, division,
# multiplication, addition, subtraction

print(x := 4 + 8**2 * (30 / 5))