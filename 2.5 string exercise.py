# 1. use the string to show one guys name and print a message to him
name = "eric"
print(f'Hello {name.title()}, would you like to learn some Python today?')

# 2. use a variable to represent a person's name ,and then print that person's name in lowercase, uppercase, and titlecase
full_name = "eRIc MAttheS"
print(full_name.lower())
print(full_name.upper())
print(full_name.title())

# 3. to find ur favorite celebrity, and then use a variable to represent that person's name.
celebrity = "albert einstein"
message = f'{celebrity.title()} once said, "A person who nerver made a mistake never tried anything new."'
print(message)

# 4. delete any whitespace characters from the beginning and the end of the name,must use the \t and \n characters at least once
name = "\t\n  eric mattes  \n\t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# 5. filename extension exercise,use the removesuffix() method to remove the .txt suffix from the filename and print the result
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))