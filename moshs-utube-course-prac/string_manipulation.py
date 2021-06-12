# String manipulation functions, methods & operators

# len function: Counts the characters in a string

course = "Python for beginners"
print(len(course))

# find method: Finds and prints the index of first occurance of the character

print(course.find('f')) # output is 7 - index 7 is f in the string above variable value

# Print lowercase or upper case variable:

print(course.lower())
print(course.upper())

# Replace and printing a string. This does not change the original value of the variable.

print(course.replace('for', 'is awesome for'))

# in operator is a boolean operator and returns true or false values.

print("Python" in course)
print("python" in course)

