# input make program stop temporarily, and wait user input text.
# parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# greeter.py
# when you use input() you should give user a prompt
name = input("Please enter ur name: ")
print(f"\nHello, {name}!")

# sometime, the prompt will be too long, so u can use
prompt = "If you share ur name, we can personalize the message you see."
prompt += "\nWhat is ur name? "

name = input(prompt)
print(f"\nHello, {name}!")

# use int() to get number from user
age = int(input("How old are you? "))
print(age)
age >= 18

# you also can use int after input().
# rollercoaster.py
height = int(input("How tall are you, in inches? "))
if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# % operator to get the remainder of a division
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
# this is useful when u want to know if a number is even or odd
# even_or_odd.py
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

# exercise
# 1. ask the user what car they want to rent, and print a message
car = input("What car do you want to rent? ")
print(f"Let me see if I can find you a {car}.")

# 2. ask the user how many people are in their dinner group,
# if more than 8 ppls, will print a message:no empty table
ppls_num = int(input("How many people are in your dinner group? "))
if ppls_num > 8:
    print("Sorry, there is no empty table.")
else:
    print("There is an empty table.")

# 3. ask the user for a number, and tell them if it's a multiple of 10
num = int(input("Enter a number, and I'll tell you if it's a multiple of 10: "))
if num % 10 == 0:
    print(f"\nThe number {num} is a multiple of 10.")
else:
    print(f"\nThe number {num} is not a multiple of 10.")
