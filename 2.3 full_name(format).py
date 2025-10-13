# f-strings can be used to format strings
first_name = 'JONn'
last_name = 'dOe'
full_name = f'{first_name.lower()} {last_name.lower()}'
print(full_name.title())

# use the f-string to create a message
first_name = 'ada'
last_name = 'wang'
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# also, you can use the format method to create a formatted string
first_name = 'TomMY'
last_name = 'looNG'
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# \t adds a tab space
print("Python")
print("\tPython")

# \n adds a new line
print("Languages:\nPython\nC\nJavaScript")
# \n can be used multiple times to create multiple lines
print("Languages:\n\tPython\n\tC\n\tJavaScript")
print()

# the rstrip method can remove whitespace at the end of a string 
ex1 = '42TLwind       '
print(ex1)
print(ex1.rstrip())
# but this method can't change the original string
print(ex1)

# the lstrip method that can remove whitespace at the beginning of a string
ex2 = '       42TLwind'
print(ex2)
print(ex2.lstrip())

# and the strip method that can remove whitespace at both ends of a string
ex3 = '       42TLwind       '
print(ex3)
print(ex3.strip())

# however, these methods only remove whitespace, not spaces between words
ex4 = '   Hello   World   '
print(ex4.strip())

# in order to save changes, you need to assign the result to a variable
ex5 = '   Hello   World   '
ex5 = ex5.strip()
print(ex5)

# show the difference between rstrip, lstrip, and strip
ex6 = '   Hello   World   '
print(f"'{ex6}'")
print(f"'{ex6.rstrip()}'")
print(f"'{ex6.lstrip()}'")
print(f"'{ex6.strip()}'")