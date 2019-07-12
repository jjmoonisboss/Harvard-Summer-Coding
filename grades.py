myList= []





while True:
    grade=input("What was your assignment grade? (type done to finish): ")
    if grade == "done":
        break
    else:
        myList.append(int(grade))
     
final = sum(myList)
print(final / len(myList))

