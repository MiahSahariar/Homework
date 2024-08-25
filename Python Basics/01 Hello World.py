# Python Comment
# This is an example of a single line comment
# Shortcut: control/command + /
# Another type is multi line comments, how to do that?

"""
When we use 3 double quotation or 3 single quotation, it creates multi line comments
@Author Miah Sahariar
Version 1.1
Date: 7/19/2024
"""

'''
Here we used, a 3 single quatation
'''

# print () is called a function
# more specifically a library function because it came from Python library
print("Hello World!")
print("Good Morning!") # single quotation is okay too
# We will use double quotation in Python

print("Miah")
print(14)
print(3.78)

# the variables hold the data
print("- - - - - - - - - - -")
name = "Miah"
age = 134
grade = 3.7832
usCitizen = True
# Above 4 data is not same
print(name)
print(age)
print(grade)
print(usCitizen)

print("-------------------------")
print(type(name))# str represent string/text type, represent by double quatation
print(type(age))# int represent integer/numeric type, represent by no quotation
print(type(grade))# float represent float/numeric type, represent by no quotation
print(type(usCitizen))# bool represent boolean type [True/False], represent by no quotation

print("------------------------")
# naming convention of variable
# we have to assign a value for a variable
employee = 12

x = 512
y = 488
_ = True

print(_)

print("_________________________")
# Variables are case sensitive, myName and MYname is not the same
myName = "Jamal"
MYname = "James"
print(myName)
print(MYname)

# alpha-numeric characters means alphabet and number both allowed
# A variable cannot start with a number
my1var = "Michael"

# How to write Multi Worlds Variables Names
# CamelCase, Snake case and pascal case
# Example of camel case - myName
# Generally variables start in lowercase, but this is not a rule, but we will follow this
myName = "Michele"
myAge = 234
myGradeScore = 3.01


# Example of pascal case -- MyName
MyName = "Michele"
MyAge = 234
MyGradeScore = 3.01

# Example of snake case -- my_name
my_name = "Jake"
my_age = 89
my_grade_score = 4.1

# Camelcase and snakecase is most popular in industry

print("---------------")
# Variables can change type after they have been set
x = 483 # int type
x = 483.0 # float type
print(x)
print(type(x))

y = 510 # int type 
y = "Bill"
print(y)
print(type(y))
# because interpreter covert source code to binary code line by line,
# last line will be executed

print("---------------------------------")
# What is casting
x = 4
print(x)
print(type(x))

y = str(4) # we cast string type for an int type
print(type(y))

z = bool("Miah")
print(type(z))

# although the data type is different but casting allows us to get a new data type

