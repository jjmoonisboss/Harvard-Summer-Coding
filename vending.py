drinks ={"yeye juice":10.00,"water":1.00,"Coke": 1.99, "Arizona Tea": 0.99}

class vendingMachine():
    def __init__(self, myDrinks):
        self.myDrinks = myDrinks
    
    def info(self):
        print(self.myDrinks)
    
    def getDrink(self):
        gulp = input("What do you want: ")
        while True:
            if gulp in self.myDrinks:
                print(gulp)
                break
            else:
                print("Not available")
                gulp = input("What do you want: ")
                   


floor1_drinks=vendingMachine(drinks)
floor1_drinks.getDrink()
floor1_drinks.info()

# print("As you reach in to grab the last bottle of water, a hot anime dude reaches in at the same time")
# print("Pay 30 gems to find share the bottle")
# print("Or tell him to get his own bottle")
