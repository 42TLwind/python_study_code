# we can use while loop to change list or dict.
# confirmed_users.py

# create a not - dentifity list
# and a empty list
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

# confirm user until all user be done
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# in 4.1 change_elements.py we use the remove() function to remove an element from a list
# but if we have many the same value, we can use while loop to remove all the same value
# pets.py
pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")
print(pets)

# we can use while loop to prompt user input info.
# mountain_poll.py
responses = {}
# create a sign
polling_active = True

while True:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # store the response in a dict
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        break

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")

# exercise
# 1. create a list named sandwich_orders which will store the names of sandwiches
# and create a empty list named finished_sandwiches
sandwich_orders = ["veggie", "chicken", "steak"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)

    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 2. use exercise 1. list add pastrami at least 3 times.
sandwich_orders = [
    "pastrami",
    "veggie",
    "chicken",
    "beef",
    "pastrami",
    "steak",
    "pastrami",
]
finished_sandwiches = []
print("pastrami have been solded out.")
count = 0
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
    count += 1
    print("pastrami order have been removed.")
print(f"We have delete ur pastrami order {count} times.")
print(sandwich_orders)

# 3. survey user's dream vactation place.
user_responses = {}
while True:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would it be? ")
    user_responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == "no":
        break

print("\n--- Poll Results ---")
for name, response in user_responses.items():
    print(f"{name.title()} would like to visit {response.title()}")
