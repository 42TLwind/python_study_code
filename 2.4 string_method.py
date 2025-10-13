# the rstrip(right strip) method can remove whitespace at the end of a string 
ex1 = '42TLwind       '
print(ex1)
print(ex1.rstrip())
# but this method can't change the original string
print(ex1)
print()

# the lstrip(left strip) method that can remove whitespace at the beginning of a string
ex2 = '       42TLwind'
print(ex2)
print(ex2.lstrip())
print()

# and the strip method that can remove whitespace at both ends of a string
ex3 = '       42TLwind       '
print(ex3)
print(ex3.strip())
print()

# however, these methods only remove whitespace, not spaces between words
ex4 = '   Hello   World   '
print(ex4.strip())
print()

# in order to save changes, you need to assign the result to a variable
ex5 = '   Hello   World   '
ex5 = ex5.strip()
print(ex5)
print()

# show the difference between rstrip, lstrip, and strip
ex6 = '   Hello   World   '
print(f"'{ex6}'")
print(f"'{ex6.rstrip()}'")
print(f"'{ex6.lstrip()}'")
print(f"'{ex6.strip()}'")
print()

# removeprefix method can remove a specified prefix from a string
ex7 = 'https://www.42tlwind.com'
print(ex7)
print(ex7.removeprefix('https://'))
# like the previous methods, this method doesn't change the original string
print(ex7)
# if u wanna save the change, assign the result to a variable
ex7 = ex7.removeprefix('https://')
print(ex7)


