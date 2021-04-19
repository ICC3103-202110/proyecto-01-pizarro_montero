from deck import Deck

class Players:

    def __init__(self, name):
        self.name = name
        self.coins = 0
        self.__cards = Deck().deal_cards()

    @property
    def cards(self):
        return self.__cards
    
#Trabajar esta funcion pq no funciona...
    def loseInfluence(self):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        #la carta es elegida
        chosenCard = input('Seleccione influencia: ')
        self.cards.remove(chosenCard)
        return chosenCard #entregar esta carta a lostInfluence en game.


    def pickAction(self):
        self.action = int(input('Que desea hacer?: '))
        if self.action == 1:
            pass



    def blockAction(self):
        
        pass

    def Challenge(self):
        pass

    def modifyCoins(self, amount):
        self.coins += amount
    
    
def main():
    k = Players('Juan')
    for i in k.cards:
        print(i.getVal())
    
    
if __name__ == "__main__":
    main() 
