import datetime
currentTime = datetime.datetime.now()
currentTime.hour
 
name =input("Enter your Name: ")
 
if currentTime.hour < 12:
    print('\nGood morning', name)
elif 12 <= currentTime.hour < 18:
    print('\nGood afternoon', name)
else:
    print('\nGood evening', name)