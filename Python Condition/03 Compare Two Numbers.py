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
        
# Advantage?
# you can reuse the numbers by many different arguments
# Two values is called argument
compareTwoNumbers(2312, 324)
compareTwoNumbers(11, 85)    
