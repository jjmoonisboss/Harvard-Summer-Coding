class Pokemon():
    def __init__(self, name, level, moves, hp):
        self.name = name
        self.level= level
        self.moves = moves
        self.hp= hp
        
    def lvl_up(self):
        self.level += 1
        print("Your pokemon is level: " , self.level)
    
    def add_move(self, new_move):
        self.moves.append(new_move)
        print("Pokemon moves: " , self.moves)
    
    def attacked(self, damage):
        self.hp -=damage
        if self.hp <= 0:
            print("Your"+ self.name + "is dead")
        else:
            print("Pokemon hurt! New hp: " , self.hp)
    
pikachu = Pokemon("Pikachu",1,["tackle"],25) 
pikachu.lvl_up()
pikachu.add_move("thunderbolt")
pikachu.attacked(10)

jiggly = Pokemon("Jigglypuff",5,["tackle"],100) 
jiggly.lvl_up()
jiggly.add_move("lullaby ")
jiggly.attacked(10)


