# if usually be followed by an else statement

cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("hold the anchovies!")

# if result is boolean value, u can use that value directly in an if statement.
# u can use if to check two value are equal or not equal
answer = 17
if answer != 42:
    print("\nThat is not the correct answer. Please try again!")

# u also can ues lower() method to make sure the value u are checking is in lowercase
# this is useful when u are accepting input from users, because u dont know how they will
# format their input.
requested_topping = "Mushrooms"
if requested_topping.lower() != "anchovies":
    print("\nHold the anchovies!")

# and, or, not, in, not in
# and: both conditions must be true
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print("\nBoth are old enough to drink.")
else:
    print("\nAt least one is not old enough to drink.")

# or: at least one condition must be true
age_0 = 22
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print("\nAt least one is old enough to drink.")
else:
    print("\nNeither is old enough to drink.")

# not: reverse the result, if the result is true, it becomes false

# in: check if a value is in a list
requested_toppings = ["mushrooms", "onions", "pineapple"]
if "mushrooms" in requested_toppings:
    print("\nMushrooms is in the list.")

# not in: check if a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"\n{user.title()}, you can post a response if you wish.")

# if-if-if use multiple if statements, all the conditions are checked, and all the true
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("\nAdding mushrooms.")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni.")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# exercise
# 1. create a alien_color variable and assign it a value of 'green', 'yellow', or 'red'
alien_color = "red"
# write an if statement to test whether the alien's color is green. if it is, print a message that the player just earned 5 points.
if alien_color.lower() == "green":
    print("You just earned 5 points.")
else:
    print("The alien is not green.")

if alien_color.lower() == "red":
    print("\nYou just earned 5 points.")

# 2. if the alien's color is green, print a message that the player earned 5 points for shooting the alien.
# if the alien's color is yellow, print a message that the player earned 10 points
if alien_color.lower() == "green":
    print("You just earned 5 points.")
else:
    print("You just earned 10 points.")

# 3. if the alien's color is green, print a message that the player earned 5 points.
# if the alien's color is yellow, print a message that the player earned 10 points
# if the alien's color is red, print a message that the player earned 15 points
if alien_color.lower() == "green":
    print("You just earned 5 points.")
elif alien_color.lower() == "yellow":
    print("You just earned 10 points.")
else:
    print("You just earned 15 points.")

# 4. the age variable stores a person's age. write an if-elif-else chain that
import random

age = random.randint(1, 100)
if age < 2:
    stage = "a baby"
elif age < 4:
    stage = "a toddler"
elif age < 13:
    stage = "a kid"
elif age < 18:
    stage = "a teenager"
elif age < 65:
    stage = "an adult"
else:
    stage = "an elder"
print(f"You are {stage}.", age)

# if and list
# this pizzeria make pizza add toppings will print a message
# but the green pepers are out of stock
requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# make sure the list is not empty before u run a for loop
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are u sure u want a plain pizza?")

# more lists
available_toppings = [
    "mushrooms",
    "olives",
    "green peppers",
    "pepperoni",
    "pineapple",
    "extra cheese",
]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# exercise
# 1. make a list of 5 or more usernames, including the name 'admin.
usernames = ["alice", "bob", "admin", "carol", "dave"]
del usernames[:]
# loop through the list, and print a greeting to each user.
if usernames:
    for username in usernames:
        if username.lower() == "admin":
            print(f"Hello {username.title()}, would u like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# 2. checking user names: make a list of 5 or more usernames, named new_users.
# make another list of 5 usernames, named current_users. make sure one or two
# of the new usernames are also in the current_users list.
new_users = ["Su Jiaxuan", "wang Zi", "BIG BING", "Lin Haowen", "JB Gege"]
current_users = ["Big bing", "Wang Zi", "Alice", "Bob", "Carol"]
# loop through the new_users list to see if each new username has already been used.
if new_users:
    for new_user in new_users:
        if new_user.lower() in [current_user.lower() for current_user in current_users]:
            print(
                f"Sorry, the username {new_user} is already taken. Please enter a new username."
            )
        else:
            print(f"The username {new_user} is available.")
else:
    print("We need to find some users!")

# 3. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
# Most ordinal numbers end in th, except 1, 2, and 3.
# Store the numbers 1 through 9 in a list. Loop through the list.
# Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
numbers = list(range(1, 10))
numbers = [i for i in range(1, 10)]
print(numbers, type(numbers))
for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
