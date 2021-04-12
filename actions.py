
#CLASE PADRE
class Action:
    
    def __init__(self):
        name = ''
        action = ''
        coinsNeeded = 0

    def play(self):
        pass

#SUBCLASES
class Income(Action):
    pass

class ForeignAid(Action):
    pass

class Coup(Action):
    pass

class Duke(Action):
    def tax(self):
        #obtiene 3 monedas
        pass
    pass

class Assasin(Action):
    def assessinate(self):
        #paga 3 mmonedas y asesina una influencia
        pass
    pass

class Captain(Action):
    def steel(self):
        #quita max 2 monedas
        pass
    pass

class Ambassador(Action):
    def exchange(self):
        #cambia cartas
        pass
    pass

class Contessa(Action):
    pass