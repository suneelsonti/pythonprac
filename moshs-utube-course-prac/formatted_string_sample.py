# Formatted strings

first = 'Suneel'
last = 'Sonti'
print(first + ' [' + last + '] is learning to code')

# The above way to printing output to screen need a lot of moving parts and formatting. Cleaner way to get the same
# output is to use formatted string as below.

first = 'Suneel'
last = 'Sonti'
language = 'python'
print(f"{first} [{last}] is learning to code in {language}]")