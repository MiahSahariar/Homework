fname = "Miah"
lname = "Sahariar"
age = 14

print(fname + lname)
# print(fname + age) # can only concentrate str to str, (not str to int)
print(fname, age) # this is OK

# cannot concentrate str to "int"
# print("My name: " + fname + " " + lname + ", age" + age))

# Python format string
fname = "Miah"
lname = "Sahariar"
age = 14
salary = 140000

# by formatting text, we can get an outcome of string and other data type
# {} is called placeholder
outcome = f"My Name is {fname} {lname}, my age {age} and my salary {salary}" 
print(outcome)

cost1 = 4
print(f"fuel price {cost1:.2f}$")

cost2 = 5
total1 = f"Gas price {cost2:.3f}$"
print(total1)

cost3 = 6
total2 = f"Gas price {cost1*cost2+cost3}"
print(total2)

# {} is a placeholder, which holds the variable
# we can call string methods inside it
# we can do arithmetic function inside code. Ex: price + (price * tax)
# we can display the price with 2 or 3 decimals
# it's possible to use comma as the divider between thousandths
product = "gold"
price = 438642
tax = 0.10

x = f"The price of {product.title()} is {price + (price * tax):,.3f}"
print(x)

# if we want to use " " around a name, we have to use a single quotation around the double quotations
x = f"The price of \"{product.title()}\" is {price + (price * tax):,.3f}"
print(x)