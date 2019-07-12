import time
f = open("script.txt", "r")

for line in f:
    print(line)
    time.sleep(1)
    
