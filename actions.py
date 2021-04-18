from players import Players

class action:
    
    def __init__(self):
        self.action_name = ''
        self.action = ''
        self.coinsNeeded = 0
        self.coinsGained = 0

    def play(self):
        Players.modifyCoins(coinsNeeded) 
        Players.modifyCoins(coinsGained) 

class income(action):
    self.coinsGained = 1

class ForeignAid(action):



class Coup(action):
    pass

class Duke(action):
    def tax(self):
        #obtiene 3 monedas
        pass
    pass

class Assasin(action):
    def assessinate(self, target):
        self.coinsNeeded = -3
        #paga 3 mmonedas y asesina una influencia
        #Players.loseInfluence(target)
    

class Captain(action):
    def steel(self):
        #quita max 2 monedas
        pass
    pass

class Ambassador(action):
    def exchange(self):
        #cambia cartas
        pass
    pass

class Contessa(action):
    pass