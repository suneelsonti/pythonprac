# This program calculates the age of a person based on the date of birth provided !

name = input("Your name please:   ")
print("hello, " + name)
dob = input("What is your year of birth: ") # This input functions records received data as a string
age = 2021 - int(dob) # We are converting the string variable into integer
print(name + ", you are " + str(age) + " years old")
