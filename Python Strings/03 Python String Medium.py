# String Methods
x = "A quick brown FOX jumps over the lazy DOG"
txt = "Pack My Box With Five Dozen Liquor Jugs"
# To modify the strings, we have some methods
print(x.upper())
print(x)

print(x.isupper)

# The center method will align the strings

# The startswith() method returns True if thr string starts with the specified value, otherwise False.
x = "A quick brown FOX jumps over A lazy DOG"
txt = "Pack My Box With Five Dozen Liquor Jugs"


text = "I love apples, apples are my favorite fruit"
print(text.count("a"))
print(text.count("apples"))

print(x.startswith("A"));
print(x.startswith("B"));
print(x.startswith("A qui"));

print(x.len())
print(x.startwith("A", 0, 25)); # True
print(x.startswith("A", 1, 40)); # False
print(x.startswith("q", 2, 40)); # True
print(x.startswith("Q", 2, 40)); # False, String is case sensitive

print(x.endswith("DOG")) # True
print(x.endswith("G")) # True
print(x.endswith("G"))

txt = "Pack My Box With Five Dozen Liquor Jugs"
print(txt.find("a"))
print(txt.find("o"))
print(txt.find("S"))
print(txt.find("Box"))
print(txt.find("Box", 10, 30))
print(txt.find("a", 10, 39))

# The index() method finds the first occurence of the specified value.
# The index() methodn is almost the same as the find() method, the only difference is that the find () method returns a -1 if value is not found. The index method raises an exception.
print(txt.index("A", 10, 39))
print(txt.find("o"))

x = "A quick brown FOX jumps over A lazy DOG"
print(x.isalnum())

fruit = "Apple483"
print(fruit.isalnum())

fruit = "483Apple"
print(fruit.isalpha()) # Numeric number present

fruit = "Apple" 
print(fruit.isnumeric) # False