# if you wanna process some elements from a list, you can use lice
# to create a slice of a list or a portion of a list
# list[start:stop:step]

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])

# you can take any number of elements from a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:4])

# if you dont indicate a start index in the slice, it starts from the beginning
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[:4])

# also you can use -1 to indicate the last element
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[-1:])

# but if you wanna take a value in the list
print(players[-3])

# you can use step in a slice
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:5:2])

# also can use loop to print the list
players = ["charles", "martina", "michael", "florence", "eli"]
for player in players[:3]:
    print(player.title())

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
print(letters)
for i in letters[5:20:4]:
    print(i.title())

# copy list
my_foods = ["pizza", "falafel", "carrot cake"]
# falsey copy list
friend_foods = my_foods
print(my_foods)
friend_foods[0] = "sushi"
print(friend_foods, "\n")

# correct copy list
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print(my_foods)
my_foods[0] = "sushi"
print(friend_foods)

# another copy list method .copy
my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods.copy()
print(my_foods)
friends_foods.append("ice cream")
print(friends_foods)

# 如果你的列表很复杂，你可以使用deepcopy()方法来实现
import copy

student_original = ["Alice", ["Math", 90, "Science", 85]]

student_shallow_copy = copy.copy(student_original)

# 3. 使用 deepcopy (深复制) 创建副本
student_deep_copy = copy.deepcopy(student_original)
print("--- 修改浅复制 (Shallow Copy) ---")
student_shallow_copy[1][3] = 88  # 修改嵌套列表中的元素

print(f"原始数据:     {student_original}")
print(f"浅复制后的数据: {student_shallow_copy}")
print(f"深复制后的数据: {student_deep_copy}")
print("\n观察：修改浅复制副本时，原始数据也被一同修改了！\n")

# 5. 现在，我们把深复制副本中的数学成绩改为 95 分
print("--- 修改深复制 (Deep Copy) ---")
student_deep_copy[1][1] = 95  # 修改嵌套列表中的元素

print(f"原始数据:     {student_original}")
print(f"浅复制后的数据: {student_shallow_copy}")
print(f"深复制后的数据: {student_deep_copy}")
print("\n观察：修改深复制副本时，原始数据完全不受影响。\n")

# exercise
# 1. print the message: "The first three items in the list are." and use slice to print the first three items
list1 = ["a", "b", "c", "d", "e", "f", "g"]
print(f"The first three items in the list are: {list1[:3]}")

# 2. print the message: "Three items from the middle of the list are." and use slice to print the middle three items
print(
    f"Three items from the middle of the list are: {list1[(len(list1) // 2)-1:(len(list1) // 2) + 2]}"
)

# 3. print the message : " The last three items in the list are." and use slice to print the last three items
print(f" The last three items in the list are: {list1[-3:]}")

# 4. create a list called "my_pizzas", and copy this one named "friend_pizzas"
my_pizzas = ["pepperoni", "mushroom", "onion"]
friends_pizzas = my_pizzas[:]  # or my_pizzas.copy() and my_pizzas.deepcopy()
# add a new pizza to the original list
my_pizzas.append("bacon")
# add a new pizza to the friend's list
friends_pizzas.append("lucky")
# check list make sure they are two different lists
print(my_pizzas)
print(friends_pizzas)
# and print the message: "my favorite pizzas are:" and "my friend's favorite pizzas are:"
print("My favorite pizzas are:")
for i in my_pizzas:
    print(i.title())

print("\nMy friend's favorite pizzas are:")
for i in friends_pizzas:
    print(i.title())
