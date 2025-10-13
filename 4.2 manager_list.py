# sort method can sort a list permanently
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars)

# if u want to reverse the order of a list, u can use reverse=True as an argument to the sort() method.
cars.sort(reverse=True)
print(cars, "\n")

# sorted method can sort a list temporarily
# sorted() function takes a list as an argument and returns a new list that is sorted, leaving the original list unchanged.
cars = ["bmw", "audi", "toyota", "subaru"]
print(cars)
print(sorted(cars))
print(cars)
# u can also sort in reverse order using sorted() function
print(sorted(cars, reverse=True))
print(cars, "\n")

# reverse method can reverse the order of a list permanently
# reverse() method reverses the order of a list, but it does not sort the list
cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)

# len function can find the length of a list
print(len(cars), "\n")

# exercise
# 1. think of at least five places in the world u would like to visit
# store the locations in a list. make sure the list is not in alphabetical order.
place = ["london", "tokyo", "hunan", "amsterdam"]
print(place)
# user sorted() method to print this list
print(sorted(place))
# print the list again to show that it is still in its original order
print(place)
# use sorted() method to print the list in reverse alphabetical order without modifying.
print(sorted(place, reverse=True))
# show that the list is still in its original order by printing it again
print(place)
# use reverse() method to change the order of the list. print the list to show that
place.reverse()
print(place)
# use sort() method to change the list make it alphabetical order.
place.sort()
print(place)
# use sort() method to change the list make it reverse alphabetical order.
place.sort(reverse=True)
print(place)

# 2. think of can storge in the list u like to have,like mountain bike, car, home, etc.
# write a program that stores these items in a list. make sure the list is not in
like_sth = ["car", "china", "huangshan mountain", "bike", "house", "money", "family"]
for i in like_sth:
    print(f"I like to have a {i.title()}.")
    print(f"I like to have a {i.upper()}.")
    print(f"I like to have a {i.lower()}.")

# pop, remove, del, append, insert, sort, sorted, reverse, len

