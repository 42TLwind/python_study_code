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

# change the value in a dictionary
alien_0 = {"color": "green"}
print(f"The alien is {alien_0["color"]}")
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}")

# tracking an alien's position
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0['x_position']}")
# move the alien to the right
speed = (alien_0["speed"]).lower()
if speed == "slow":
    x_increment = 1
elif speed == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] += x_increment
print(f"New position: {alien_0['x_position']}")
