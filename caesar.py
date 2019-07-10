key=int(input("key:"))
plaintxt=input("insert text:")
ciphertxt=""




for i in plaintxt:
    if i == " ":
        print(i,end="")
#         ciphertxt += " "
        #this is to add on a space to your code.
    elif i.isupper():    
#         ciphertxt +=chr(ord(i) + key)
       ciphertxt=(ord(i)-65 + key)% 26 + 65
       print(chr(ciphertxt),end="")
    elif i.islower(): 
#         
       ciphertxt=(ord(i)-97 + key)% 26 + 97
       print(chr(ciphertxt),end="")
#         ciphertxt += chr(ord(i) + key) 
        # TO EXPLAIN MY COdE , what you do is you take the number of i + your key and convert it to a chr to get the letter
    
# ciphertxt=(ord(i)-97)% 
                
# print(ciphertxt)                
