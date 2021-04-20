#from players import Players

class Action:
    
    def __init__(self):
        # self.action_name = ''
        # self.action = ''
        self.coinsGained = 0

    def play_action(self):
        return self.coinsGained

class Income(Action):
    def __init__(self):
        self.coinsGained = 1
        print('listo')

class ForeignAid(Action):
    def __init__(self):
        self.coinsGained = 2


class Coup(Action):
    def __init__(self):
        self.coinsGained = -7
    """
    Players.loseInfluence()
    """

# class Duke(self):
#     def tax(self):
#         #obtiene 3 monedas
#         self.coinsGained = 3
        
    

# class Assasin(self):
#     def assessinate(self, target):
#         self.coinsNeeded = -3
#         #paga 3 mmonedas y asesina una influencia
#         #Players.loseInfluence(target)
    

# class Captain(self):
#     def steel(self):
#         #quita max 2 monedas
#         pass
#     pass

# class Ambassador(self):
#     def exchange(self):
#         #cambia cartas
#         pass
#     pass

# class Contessa(self):
#     pass