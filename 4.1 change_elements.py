import random

# if u wanna modify the elements of a list, you can use direct assignment
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# use append() to add elements to the end of a list
motorcycles.append("ducati")
print(motorcycles)

# of course, you can append any object to a list, even another list.
motorcycles.append(["harley", "bmw"])
print(motorcycles)

# you can create an empty list and then use append() to add elements to the list.
motorcycles = []
print(motorcycles)
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# insert() method can add an element at any position in a list.
# inster(index, value)
motorcycles.insert(0, "ducati")
print(motorcycles)
motorcycles.insert(2, "harley")
print(motorcycles, "\n")

# delet elements from a list
# 1. del statement, if you know the position of the element you want to delete, you can use the del statement to remove that element.
print(motorcycles)
del motorcycles[4]
print(motorcycles, "\n")

# 2. pop() method
# pop() method removes the last element in a list, but it lets you work with that element after removing it.
# so u need to create a variable to hold the popped element.
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles, "\n")

# what pop method is useful for?
# when u want to use the value of an element that u are removing from a list.
# example:
motorcycles = ["honda", "yamaha", "suzuki"]
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.\n")

# actually pop method can remove an element from any position in a list, not just the last element.
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.\n")
print(motorcycles, "\n")

# if u dont know which method to use to remove an element from a list, there have a simple way to decide.
# u can use del statement when u dont need the value of the removed element.
# u can use pop() method when u need to use the value of the removed element.

# 3. remove() method
# if u know the value of the element u want to remove from a list, u can use the remove() method to remove the first occurrence of that value.
motorcycles = ["honda", "yamaha", "suzuki"]
motorcycles.remove("yamaha")
print(motorcycles)

# u can also use the remove() method to work with the value u are removing.
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
too_expensive = "ducati"
a = motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print(a, "\n")  # None, because remove() method does not return any value

# move() method only removes the first occurrence of a value.
# if u want to remove all occurrences of a value, u can use a while loop to do this.

# exercise
# 1. the guest list: if u could invite anyone, living or deceased, to dinner, who would u invite?
# make a list and include at least three people u'd like to invite.
guest_list = ["big bing", "su jiaxuan", "xiao jiji"]
print(
    f"I would like to invite {guest_list[0].title()}, "
    f"{guest_list[1].title()}, and {guest_list[2].title()} to dinner."
)

# 2. modifying the guest list: u just heard that one of ur guess cant make the dinner, so u need to invite someone else.
# u need to print a message talk who cant make it
# modify ur list, replacing the name of the guest who cant make it with the name of the new person.
# print a message to each person, letting them know they are still invited.
cant_make_it = guest_list.pop(1)
print(f"{cant_make_it.title()} cant make the appointment.")
guest_list.append("jacky chen")
print(
    f"new guess list have been complicted."
    f"I would invite {guest_list[0].title()}, {guest_list[1].title()} and {guest_list[2].title()}"
)

# 3. add guest: use insert() method add a new guest in the start of the list
# use insert() method make a new guest in the middle of the list
# use append() make a new guest in the end of the list
guest_list.insert(0, "tommy long")
guest_list.insert(len(guest_list) // 2, "zhang shuang")
guest_list.append("new life")
for i in guest_list:
    print(f"I would invite {i.title()} to join my dinner")

# 4. shorten the guest list: print message which u just can invite two guests to the dinner
# use the pop() method to delet the guest in the list, till the two guests.


for i in range(4):
    del_guest = guest_list.pop(random.randint(0, len(guest_list) - 1))
    print(f"sorry, {del_guest.title()}, I cant invite u to the dinner.")
print(
    f"I would invite {guest_list[0].title()} and {guest_list[1].title()} to the dinner."
)

del guest_list[0]
del guest_list[0]
print(guest_list)
