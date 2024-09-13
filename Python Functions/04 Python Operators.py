# Operators are used to perform operations on variables and values
# In the example below, we use the + operator to add together two values

# Arithmetic operators
x = 20
y = 6 
# Addition
print(x + y)

# Subtraction 
print(x - y)

# Multipication
print(x * y)

# Division
print(x/y)
# above gave float number

# Floor division [new]
print(x//y)

# Modulus
print(x%y)

# Exponentiation
a = 2
b = 4
print(a**b)

# Python Comparison Operators
m = 6
n = 4

# Equal to
print(m==n)

# Not equal
print(m!=n)

# Greater than
print(m>n)

# Less than
print(m<n)

# Greater than or equal to
print(m>=n)

# Less than or equal to
print(m<=n)

# logical operator -----> 'and', 'or', 'not

# Built-in math func.
# max() finds the highest value
print(max(577867, 283646, 427493, 584835, 683938))

# min() finds the lowest value
print(min(577867, 283646, 427493, 584835, 683938))

# the abs() function brings the absolute positive value of an integer
print(abs(-34.6788765))
      

# the pow(x,y) function returns the value of x to the value of y (xy)
print(a**b)
print(pow, 2,3)

print(round(3.2))
print(round(3.4))
print(round(3.8))

# We are importing math library by below line
import math

# The math sqrt() method returns the square root of the value
print(math.sqrt(64))

# Rounds a square root number dowards to the nearest integer
print(math.isqrt(37))

# Rounds a number down to the nearest integer
print(math.floor(3.7))

# Rounds a number up to the nearest integer
print(math.ceil(3.1))

print(math.factorial(5))

# below one gave us remainder and modulus
print(x%y)

# method returns the remainder of x with respect to y
print(math.remainder(9,2))

import datetime
print(datetime.now())