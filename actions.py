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

class income(self):
    self.coinsNeeded = 0
    self.coinsGained = 1

class ForeignAid(self):
    self.coinsNeeded = 0
    self.coinsGained = 2


class Coup(self):
    self.coinsneed = 7
    """
    Players.loseInfluence()
    """

class Duke(self):
    def tax(self):
        #obtiene 3 monedas
        self.coinsGained = 3
        
    

class Assasin(self):
    def assessinate(self, target):
        self.coinsNeeded = -3
        #paga 3 mmonedas y asesina una influencia
        #Players.loseInfluence(target)
    

class Captain(self):
    def steel(self):
        #quita max 2 monedas
        pass
    pass

class Ambassador(self):
    def exchange(self):
        #cambia cartas
        pass
    pass

class Contessa(self):
    pass