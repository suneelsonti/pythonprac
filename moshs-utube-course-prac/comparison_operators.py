#Comparison operators:

# outside temp notification

temp = 29.5
print('\n'"Weather update:")
if temp >= 30:
    print("It is expected to be warm today. Stay indoors")
else:
    print("Outside temperature is expected to be less than 30. Enjoy ur day")


# Minimum and maximum allowed characters:
print('\n'"Character limitation:")
name = input("Please enter your name: ")

if len(name) < 3:
    print('\n'"Please make sure the name is atleast 3 characters !")
elif len(name) > 50:
    print("Maximum allowed characters in a name is 50 !")
else:
    print(f"Hello {name.capitalize()}, welcome to python programming !")