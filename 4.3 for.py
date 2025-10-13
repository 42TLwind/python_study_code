print(range(1, 40))
a = range(1, 40)
print(a, type(a))

# exercise

# 1. think of at least 3 pizzas you like, and store them in a list.
pizzas = ["pepperoni", "mushroom", "cheese"]

# use a for loop to print each pizza flavor.
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# add a code line at the end of ur program, outside the for loop, that states how much u like pizza.
print("I really love pizza!")

# range() function and for loop
# range function generates a sequence of numbers, which is commonly used in for loops to iterate over a specific range of values.
for i in range(1, 6):
    print(i)

# if u wanna translate the range object into a list, u can use the list() function.
number = list(range(6))
print(number)

number = list(range(2, 11, 2))
print(number)

# you can
squares = []
for i in range(1, 11):
    square = i**2
    squares.append(square)
print(squares)

ex = []
for i in range(1, 11):
    ex.append(i**2)
print(ex)

# they have some function to use
# max min sum
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print()

# list comprehension
# use one line code to create a number list
sqiares = [value**2 for value in range(1, 11)]
print(squares)

# exercise
# 1. use for loop print 1~20
for i in range(1, 21):
    # end can be use to set the end of the line
    print(i, end="  ")
print()

# 2. create a list include 1~1 000 000, then use min() and max() check this list
# start at 1 end of 1 000 000, at last use sum() watch how many time to deal this result
numbers = [a for a in range(1, 1_000_001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 3. print the odd numbers from 1 to 20
jishu = [i for i in range(1, 21) if i % 2 != 0]
print(jishu)
for i in jishu:
    print(i, end=" ")
print()

# 4. print the numbers that can be divided by 3 from 3 to 30
a_list = [i for i in range(3, 31) if i % 3 == 0]
for i in a_list:
    print(i, end=" ")
print()

# 5. print the cube of the numbers from 1 to 10
b_list = [i**3 for i in range(1, 11)]
for i in b_list:
    print(i, end=" ")  # end=" " can not use \n
