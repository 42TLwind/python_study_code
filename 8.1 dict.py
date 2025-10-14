# in python, the dict is a series of key-value pairs
# a simple dictionary example
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# now you can get the value associated with a key
new_points = alien_0["points"]
print(f"\nYou just earned {new_points} points!")

# you can add new key-value pairs to a dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# empty dictionary
alien_1 = {}
alien_1["color"] = "green"
alien_1["points"] = 5
print(alien_1)

# change the value in a dictionary
alien_0 = {"color": "green"}
print(f"The alien is {alien_0["color"]}")
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}")

# tracking an alien's position
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")
# move the alien to the right
speed = (alien_0["speed"]).lower()
if speed == "slow":
    x_increment = 1
elif speed == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] += x_increment
print(f"New position: {alien_0['x_position']}")

# removing key-value pairs
names_dict = {"name": "eric", "age": 25, "city": "beijing"}
print(names_dict)
del names_dict["age"]
print(names_dict)

# you also can storge many values in a dictionary
# favorite_languages.py
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
print("\n", favorite_languages)

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")

# if the key does not exist, you get an error
# KeyError: 'phil123'
# print(f"Phil's favorite language is {favorite_languages['phil123'].title()}")

# you can use get() method to avoid this error
hobby = favorite_languages.get("endless")
print(hobby)
# if the key does not exist, get() method returns None
# in get() method, the second argument is the value to return if the key is not found

# exercise
# 1.use a dictionary to store ppl's info inclde name, age, city
person = {"fist_name": "ou", "last_name": "yangjian", "age": 23, "city": "shenzhen"}
# then print the all info
for info in person:
    print(person[info], end="")

# 2. use a dict store some number of ppl's favorite
# think of five ppls names, and use these names as keys in your dict
# each person should have a list of favorite numbers
favorite_numbers = {
    "eric": 24,
    "matt": 98,
    "jb": 78,
    "lin": 45,
    "big bing": 250,
}
for num in favorite_numbers:
    print(num.title(), favorite_numbers[num])

# 3.think of five programming languages, and store each language in a list
# in your dict use these lang as keys, and store the list of languages as values
# print all the values, not the keys
programming_glossary = {
    "variable": "A placeholder for storing data.",
    "function": "A block of organized, reusable code.",
    "loop": "A programming construct that repeats a block of code.",
    "list": "A collection of items in a particular order.",
    "dictionary": "A collection of key-value pairs.",
}

print("\nProgramming Glossary:")
for term, definition in programming_glossary.items():
    print(f"{term}: {definition}\n")
