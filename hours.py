from cs50 import get_int
hr=get_int("What hour is it: ")
past=get_int("How manny hrs will pass: ")
newTime=(hr + past) % 12

if newTime is 0:
    print("It is now 12 o clock")    
else:
    print("In " + str(past) + " hours it will be " +str(newTime) + " oclock")
    #convert into string sou can concatenate aka add onto the prinnt line which is a sting
