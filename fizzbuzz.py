counter=0
while True:
    counter+=1
    if counter>100:
        break     
    elif counter % 3 is 0:
        print("fizz")
    elif counter % 5 is 0:
         print("buzz")
    else:
         print(counter)
            

