# logical, not operator, reverse the result, returns False if the result is true

def outcome(val1, val2):
    if val1%2==0 and val1>val2:
        print(val1, "is an even number and is greater than", val2)
    elif not (val1%2==0 and val1>val2):
        print(val1, "is not an even number and", val1, "is not greater than", val2)
    else:
        print("Please provide sufficient value")
        
outcome(11,9)