myString=input("phrase:")

#method 1
for i in range(len(myString)-1, -1, -1):
    print(myString[i], end="")
print()

#method 2
myList= list(reversed(myString))
for letter in myList:
    print(letter, end="")
print()

#method 3
myList= list(reversed(myString))
print("".join(myList))
