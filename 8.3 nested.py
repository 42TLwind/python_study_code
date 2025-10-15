# nested can be used to store lots of things.
# you can store some list in a dictionary.
# also can store another dictionary in a dictionary.
# you can even store a dictionary in a list

# list store dicts.
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

# three dicts in one list
aliens = [alien_0, alien_1, alien_2]

# use loop to print it
for alien in aliens:
    print(alien)

# but if u have lots of aliens, u can use range() and a loop to make 30 aliens
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

# aliens.py
# create a empty list for storing aliens
aliens = []

# create 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# change the first 3 aliens to yellow
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print(f"Total number of aliens: {len(aliens)}")

# you also can expand this loop
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

# pizza.py
# nested dict in a list
# store pizza info
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"],
}

# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(f"\t{topping}")

# when dict have many value in a key, you can nested a list in dict
# favorite_languages.py
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# many_users.py
# nested dict in a dict
users = {
    "aeinstein": {
        "first_name": "albert",
        "last_name": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first_name": "marie",
        "last_name": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info["first_name"]} {user_info["last_name"]}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# exercise
# 1.use 6.1 program add two person's dict and store them in a list
person_name = {"first_name": "ou", "last_name": "yangjian"}
person_age = {
    "age": 23,
}
person_other = {"city": "shenzhen", "language": "chinese"}

person = [person_name, person_age, person_other]

for info in person:
    for i in info.values():
        print(i)

# 2.create many pets dict, every single dict include the pet's type and master.
# sotre these dicts in a list named pets.

pets = [
    {"type": "dog", "master": "ou"},
    {"type": "cat", "master": "lin"},
    {"type": "fish", "master": "matt"},
]

for pet in pets:
    for i in pet.values():
        print(i)

# 3. create a dict name favorite_places, use three names as keys, store everyone
# favorite places in a list as values. print each person's name and their favorite places.
favorite_places = {
    "Ou Yangian": ["Xin jiang", "Shan xi"],
    "Lin Wenhao": ["shenzhen", "guangzhou", "hunan"],
    "Matt": ["beijing", "shanghai"],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()} 's favorite place is:")
    else:
        print(f"\n{name.title()} 's favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

# 4. use 6.2 program make everyone can have more than one favorite number
favorite_numbers = {
    "eric": [24, 42],
    "matt": [98, 77],
    "jb": [78],
    "lin": [45, 2123],
    "big bing": [250, 45],
}

for name, num in favorite_numbers.items():
    if len(num) == 1:
        print(f"\n{name.title()}'s favorite number is:")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
    for n in num:
        print(f"\t{n}")

# 5. city: create a cities dict, use the name of three cities as keys.
# create a dict of information about each city and include the country,
# population, and one fact. the value for each city should be a dict.
# print the name of each city and all its info.

cities = {
    "shenzhen": {
        "country": "china",
        "population": 20_000_000,
        "fact": "the first special economic zone in china",
    },
    "tokyo": {
        "country": "japan",
        "population": 14_000_000,
        "fact": "the capital city of japan",
    },
    "new york": {
        "country": "usa",
        "population": 8_000_000,
        "fact": "known as the big apple",
    },
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    country, population, fact = info.values()
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")
