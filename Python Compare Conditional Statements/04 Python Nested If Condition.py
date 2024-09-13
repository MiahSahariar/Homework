# You can have if statements inside if statements, this is called nested if

def outcome(val1, val2):
    if val1%2==0:
        if val1>val2:
            print(val1, "is an even number and", val1, "is greater than", val2)
        elif val1<val2:
            print(val1, "is an even number and", val1, "is less than", val2)
        elif val1==val2:
            print(val1, "is an even number and", val1, "is equal to", val2)
        elif val1<=val2:
            print(val1, "is an even number and", val1, "is less than or equal to", val2)
        elif val1>=val2:
            print(print(val1, "is an even number and", val1, "is greater than or equal to", val2))
        print(val1, "is am even number")
    elif not val1%2==0:
        if val1>val2:
            print(val1, "is an odd number and", val1, "is greater than", val2)
        elif val1<val2:
            print(val1, "is an odd number and", val1, "is less than", val2)
        elif val1==val2:
            print(val1, "is an odd number and", val1, "is equal to", val2)
        elif val1<=val2:
            print(val1, "is an odd number and", val1, "is less than or equal to", val2)
        elif val1>=val2:
            print(print(val1, "is an odd number and", val1, "is greater than or equal to", val2))
        print(val1, "is an odd number")
    else:
        print("Please provide a valid number")
        
        