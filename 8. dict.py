# in python, the dict is a series of key-value pairs
# a simple dictionary example
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])

# now you can get the value associated with a key
new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

# you can add new key-value pairs to a dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# empty dictionary
alien_1 = {}
alien_1["color"] = "green"
alien_1["points"] = 5
print(alien_1)
