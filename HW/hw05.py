def voter(age):
    if age == 18:
        print("I am a Voter")
    elif age < 18:
        print("I am not a Voter")
    elif age > 18:
        print("I've been a voter")
    else: 
        print("Please add a valid age")
        
    voter(19)
    
    