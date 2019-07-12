fruits ={"apples":1,"pears":2}

class fruitMachine():
    def __init__(self, myFruits):
        self.myFruits = myFruits
    
    def info(self):
        print(self.myFruits)
    
    def getFruit(self,fruitName):
         self.myFruits[fruitName] -= 1


floor1_fruits=fruitMachine(fruits)
floor1_fruits.info()
floor1_fruits.getFruit("apples")
floor1_fruits.info()
