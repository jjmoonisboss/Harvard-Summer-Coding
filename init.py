from cs50 import get_string

word=get_string("What is your full name: ")
newList = word.split(" ")
print(word)

for i in newList:
    print(i[:1] ,end=" ")
 
