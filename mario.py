
height = int(input("Put in a height for a pyramid: "))



for x in range(height):   
    for y in range(x+2):
        print(" ", end="")
    for y in range(height - x - 1):
        print("#", end="")
        print()


