#from players import Players

class Action:
    
    def __init__(self):
        # self.action_name = ''
        # self.action = ''
        self.coinsGained = 0

    def Income(self):
        return self.coinsGained = 1

    def ForeignAid(self):
        return self.coinsGained = 2


    def Coup(Action):
        self.coinsGained = -7
        target = input("Which player do you want to take away a card?:")
        coins = self.coinsGained
        coup = []
        coup.append(target)
        coup.append(coins)
        return coup 
        #lista que tiene la persona que pierda influencia y monedas perdida

    
    def Duke(self):
        self.coinsGained = 3
        coins = self.coinsGained
        person = input("Who do you want to take coins from?:")
        duke = []
        duke.append(person)
        duke.append(coins)
        return duke
        #lista que tiene a la persona que se le quita las monedas y la cantidad de monedas
        
    

    def Assasin(self):
        self.coinsGained = -3
        coins = self.coinsGained
        person = input("Who do you want to kill?:")
        assasin = []
        assasin.append(person)
        assasin.append(coins)
        return assasin
         #paga 3 mmonedas y asesina una influencia
         #Players.loseInfluence(target)
    
    def Captain(self):
        self.coinsGained = 2
        coins = self.coinsGained
        person = input("From whom would you like to steal?:")
        captain = []
        captain.append(person)
        captain.append(coins)
        return captain 


    def Ambassador(self):
        card = input("Which card would you like to change?:")
        person = input("Which player do you want to change with?:")
        ambassador = []
        ambassador.append(card)
        ambassador.append(person)
        return ambassador

