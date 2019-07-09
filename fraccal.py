from fractions import Fraction
firstNum=input("Write a fraction: ")
secondNum=input("Write another fraction: ")
#get split

operation=input("Insert your operation a= addition, s=subtraction, m=multiplication, d=division and e=exponent: ")

if operation is"a":
    print(Fraction(firstNum) + Fraction(secondNum))
elif operation is "s":
    print(Fraction(firstNum) - Fraction(secondNum))
elif operation is "m":
    print(Fraction(firstNum) *Fraction(secondNum))
elif operation is "d":
    print(Fraction(firstNum) / Fraction(secondNum))
elif operation is "e":
    print(Fraction(firstNum) ** Fraction(secondNum))
    
 

