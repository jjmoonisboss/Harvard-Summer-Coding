from cs50 import get_float
firstNum=get_float("Write a number: ")
secondNum=get_float("Write another number: ")
# This isnnt gonnnna work so hardcode it
# add=("+")
# sub=("-")
# mult=("*")
# div=("/")
# exp=("**")

operation=input("Insert your operation a= addition, s=subtraction, m=multiplication, d=division and e=exponent: ")

if operation is"a":
    print(firstNum + secondNum)
elif operation is "s":
    print(firstNum - secondNum)
elif operation is "m":
    print(firstNum * secondNum)
elif operation is "d":
    print(firstNum / secondNum)
elif operation is "e":
    print(firstNum ** secondNum)
