# counting.py
# use while to count to 5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# you can define a quit_value, if user not input this value, this program will run forever.
# parrot.py
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message.lower() != "quit":
    message = input(prompt)
    print(message)

# you also can add if() to make this program more comprehensive.
while message.lower() != "quit":
    message = input(prompt)
    if message.lower() != "quit":
        print(message)

# sign can be usedd to control the while loop
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message.lower() == "quit":
        active = False
    else:
        print(message)

# break() can quit the while loop
# cities.py
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city.lower() == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}!")

# if you wanna back to start of the loop, you can use continue()
# counting.py
# print the 1-10 odds.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# exercise
# 1. pizza toppoing. use while loop to prompt user to add topping. until user input 'quit'

while True:
    topping = input(
        "\nPlease enter a topping: " "\n Enter 'quit' when you are finished."
    )
    if topping.lower() == "quit":
        break
    else:
        print(topping)

# 2. movie ticket: use while loop to ask user to input age.
# if age < 3, the ticket is free
# if age 3-12, the ticket is $10
# if age > 12, the ticket is $15
while True:
    age = int(input("\nPlease enter your age: "))
    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age < 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
    break
