# a dict maybe include lots of key-value pairs
# so, use the for loop to get the key-value pairs

# loop of all key-value pairs
# user.py
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# the items() method returns a list of key-value pairs
# ex
ex = user_0.items()
print(ex, type(ex))

# favorite_languages.py enhanced version
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}.")

# if you dont wanna value, use keys() method
for name in favorite_languages.keys():
    print(name.title())

print()

# the keys() method is not necessary, because the for loop
# will loop through all the keys by default
for name in favorite_languages:
    print(name.title())
# but if you want to make it clear, you can use keys() method

friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# you also can use sorted() function to sort the keys
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# you can use values() method to get all the values in a dict
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# but if there are some same values, u can use set() to remove the duplicates
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# you also can use {} to creat a set
set_1 = {1, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8}
print(set_1)

# exercise
# 1.use 8.1 dict.py exercise 3 to print all the key-valus pairs for the loop
# and add five new python glossarys.
programming_glossary = {
    "variable": "A placeholder for storing data.",
    "function": "A block of organized, reusable code.",
    "loop": "A programming construct that repeats a block of code.",
    "list": "A collection of items in a particular order.",
    "dictionary": "A collection of key-value pairs.",
    "set": "A collection of unique items.",
    "tutple": "A collection of items.",
    "sort": "A method to arrange items in a particular order.",
    "title": "A method to capitalize the first letter of each word.",
    "upper": "A method to convert all letters to uppercase.",
}

print("\nProgramming Glossary:")
for glossary, definition in set(programming_glossary.items()):
    print(f"{glossary}: {definition}\n")

# 2. create a dict, store three rivers and the country they run through
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "yangtze": "china",
}
# use loop to print a message for every river
# ex: The Nile runs through Egypt.

for river, country in set(rivers.items()):
    print(f"The {river.title()} runs through {country.title()}.")

print()

# use loop to print all the rivers
for river in set(rivers):
    print(river)
# for river in set(rivers.keys())

# use loop to print all the countries
for country in set(rivers.values()):
    print(country)

# 3. use favorite_languages.py exercise to practice.
# create a need to accpet suvivers persons list,and someone in the dict, someone not in the dict.
a_list = ["jen", "phil"]
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for name, language in favorite_languages.items():
    if name in a_list:
        print(
            "\nHi "
            + name.title()
            + ", I see your favorite language is "
            + language.title()
            + "."
        )
    else:
        print("\n" + name.title() + ", I don't know your favorite language.")
