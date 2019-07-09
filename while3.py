secretColor ="yellow"

userColor =input("Guess the color: ")

while True:
    if userColor == secretColor:
        print("you got it")
        break
    else:
        print("Try again" + "\n")
        userColor=input("Guess the color:")
