from cs50 import get_int

temp = get_int("What temperature is it today ")

if temp >= 80:
    print("Wear a t-shirt")
    #else if is elif in python
elif temp <= 60:
    print("Wear a sweater")
elif temp <=50:
    print("Wear a jacket")
elif temp <= 40:
    print("Wear a coat")
            
            

