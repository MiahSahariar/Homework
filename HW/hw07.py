def diabeticCondition(hbA1c):
    input(int(hbA1c))
    if hbA1c > 6.4:
        print("I am a diabetic patient")
    elif hbA1c <= 6.4:
        if hbA1c >= 5.7:
            print("I am a pre-diabetic patient")
        elif hbA1c < 5.7:
            print("I am a healthy person")
    else:
        print("Please enter a valid hbA1c")
        
    