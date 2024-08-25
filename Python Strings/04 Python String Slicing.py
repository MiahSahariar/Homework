# [] called square bracket
# The first character has index 0
# Specify the start index and end index, with an end colon, to return a part (slice) of the string. Note: The first character has index 0 and the end string is not included
x = "Pack my box with five dozen liquor jugs"
print(len(x))
print(x[2:10]) # end index is not counted

print(x[0:39]) # Why the entire string?
# Beause 0-38 is 39, as it starts from 0

print(x[:10]) # This represents start from 0, and end index is excluded
print(x[5:]) # Starts from index 5 and ends with end index, which is excluded 

print(x[0:60]) # although we know length is 39, we wrote 60

# Negative indexing
# first index: 0
# last index: -1
# negative indexes are for starting the slice from the end of the string
print(x[-10:-1])