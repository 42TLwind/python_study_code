# tuple very similar to list but they are immutable
# tuple is a collection which is ordered and unchangeable

dimensions = (200, 50)
print(dimensions[0], dimensions[1])
# if u want to modify the tuple, u can't
# dimensions[0] = 250
# 'tuple' object does not support item assignment

# be careful when using tuple you need use dot notation
a_tuple = (3,)
print(type(a_tuple))

# also, you can use for loop to loop through a tuple
for dimension in dimensions:
    print(dimension)

# although, you can't change the value of a tuple, but you can reassign it
dimensions = (200, 50, 160)
print("Original dimensions:")
for i in dimensions:
    print(i)

dimensions = (400, 100, 500)
print("\nModified dimensions:")
for i in dimensions:
    print(i)

# exercise
# buffet menu: a buffet-style restaurant offers only five dishes.
# create a tuple containing these five dishes, and use a for loop to print each dish.
buffet_menu = ("steak", "chicken", "fish", "beef", "pork")
for i in buffet_menu:
    print(i.title())

print()

# change the tuple
buffet_menu = ("steak", "chicken", "fish", "beef", "pork", "shrimp")
for i in buffet_menu:
    print(i.title())
