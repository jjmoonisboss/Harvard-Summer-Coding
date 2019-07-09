#try to create a guessinng game
import random
x = random.randint(0,10)
from cs50 import get_int
guess = get_int("Guess a number, any number:")

if guess > x:
    print("Too low!")
elif guess < x:
    print("Too high!")
else:
    print("You've got it!")  
