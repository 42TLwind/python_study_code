# in python, number can be classified into several types, including:
# int: integer, represents whole numbers without decimal points, such as 1, -5
# float: floating-point number, represents numbers with decimal points, such as 3.14, -0.001
# complex: complex number, represents numbers with a real part and an imaginary part, such as
# 2 + 3j, -1 + 0.5j
# bool: boolean, represents truth values, either True or False
# Python also supports various operations and functions for working with numbers, such as arithmetic operations (+, -, *, /, //, %, **), comparison operations (==, !=, >, <,
# >=, <=), and built-in functions (abs(), round(), pow(), etc.).
# Here are some examples of using numbers in Python:

# integer
a = 10
b = -5
print(a + b)  # output: 5
print(a * b)  # output: -50
print(a // 3)  # output: 3
print(a % 3)  # output: 1
print(a**2)  # output: 100
print()

# float
print(0.1 + 0.1)
print(0.2 + 0.2)
print(0.2 * 2)
print()

# some unexpected results due to floating-point precision issues
print(0.2 * 3)
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)  # output
print()

# when you use the float to do arithmetic operations, you may get some unexpected results due to floating-point precision issues.
# to avoid this problem, you can use the decimal module to perform decimal arithmetic operations.
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # output: True
print()

# use float and int together in arithmetic operations the int will be converted to float
c = 5.5
d = 11
print(c + d)  # output: 16.5
print(c * 4)
print(d / c)

# when input the large number, u can use underscores(_) to make it more readable
universe_age = 14_000_000_000
print(universe_age)

# constant is a variable that its value should not be changed
# in python, we use uppercase letters to represent constants
MAX_CONNECTIONS = 5000

# exercise
# 1. write 4 expressions that use the +, -, *, and / operators, and print the results of each expression
print(2 + 6)
print(10 - 2)
print(1.25 * 6)
print(16.0 / 2)

# 2. use a variable to represent ur favorite number, and use that to create a message that reveals ur favorite number. Print that message
FAVORITE_NUMBER = 42
print(f"My favorite number is {FAVORITE_NUMBER}")
