# "if" is the first condition
# "else" is the last condition
# "elif" is between
# else has no condition
# if not true, statement inside will be executed

# We can use input function so that the user can be able to input data as we wish
a = input("Please provide value of a: ")
b = input("Please provide value of b: ")

if a>b:
    print(a, "is greater than", b)
    # Not a function, it's a condition
elif a<b :
    print(a, "is smaller than", b)
    # condition is complete
elif a==b:
    print(a,"is equal to", b)
# else function has no condition, basically the none of the above
else:
    print("Not gonna work")
    
# compareTwoNumber is a user defined function
# a and b are considered parameters
def compareTwoNumbers(a, b):
    if a>b:
        print(a, "is greater than", b)
    # Not a function, it's a condition
    elif a<b :
        print(a, "is smaller than", b)
    # condition is complete
    elif a==b:
        print(a,"is equal to", b)
    # else function has no condition, basically the none of the above
    else:
        print("Not gonna work")
        
    compareTwoNumber()
    