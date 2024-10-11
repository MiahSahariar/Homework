# This is a tuple
# A tuple is a collection which is ordered and unchanganle.
# Written with parenthesis

fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
print(fruits[3:6])

# indes start with 0

if "Orange" in fruits:
    print("Orange is in Tuple")
else:
    print("Orange is not")
    
# Update tuple?
# We convert it into lists
fruits = ("Apple", "Orange", "Grapes", "Kiwi", "Cherry", "Fig", "Blueberry")
fruitsAsList = list(fruits)
print(fruitsAsList)

print(type(fruitsAsList))
fruitsAsList[2] = "Raspberry"
fruitsAsTuple = tuple(fruitsAsList)
print(fruitsAsTuple)

# Python allows us to extrasct values via unpacking

# packed
fr = ("Apple", "Banana", "Grapes")
(green, yellow, violet) = fr

print(green)
print(yellow)
print(violet)