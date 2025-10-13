# 1. List consist of multiple items in a single variable
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)

# 2. you can use the index to access a specific item in the list
print(bicycles[0])  # prints the first item in the list
print(bicycles[1])  # prints the second item in the list

# 3. if you want, you can use the 2.4 string_method to modify the item in the list
print(bicycles[0].title())
print(bicycles[1].upper())

# also you can use -1 to access the last item in the list
print(bicycles[-1])  # prints the last item in the list
# this is very useful when you don't know the length of the list

# 4. you can use f-strings to create a message with the item from the list
message = f"My first bicycle was a {bicycles[0].title()}, but my favorite is a {bicycles[3].title()}."
print(message, "\n")

# exercise
# 1. put some friends names in a list, and named it as "friends", print the all friends names
friends = ["big bing", "wang zi", "jb gege", "lin haowen"]
for i in friends:
    print(i.title())

# 2. keep use the list "friends", print a message for each friend.
for i in friends:
    print(f"Hi, My fcuking friend {i.title()}, long time no see!")

# 3. which way of the commute u like the most? put some commute ways in a list, and print a message for each way.
commute_ways = ["bike", "bus", "subway", "walk", "drive"]
for i in commute_ways:
    print(f"I would like to commute by {i}.")
