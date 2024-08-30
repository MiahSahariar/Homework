temp = input(todaysTemperature)

if temp < 32:
    print("Freezing")
elif temp < 55:
    print("Pleasant")
elif temp < 73:
    print("Getting Warmer")
elif temp < 101:
    print("Very Hot")
else:
    print("Please input a valid temperature")
    
