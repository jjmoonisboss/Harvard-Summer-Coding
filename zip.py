def zip(myList):
    myDict={}
    for i in myList:
        if i in myDict:
            myDict[i] += 1
        #myDict[i] = myDict[i]+ 1
        else:
            myDict[i]= 1
            

        
        
    #loop over your list
    #check if each element already is in your dictionary 
    #if element in dictionary,update counter
    #if not , add it to Dictionary
    #return dictionary
    
    return myDict
    
    
    
    
print(zip([1,2,2,3,4,5,5,5,6,6,7]))    
