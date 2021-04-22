from printer import Printer
from deck import Deck


class Players:

    def __init__(self, name):
        self.__name = name
        self.__coins = 2
        self.__cards = Deck().deal_cards()

    @property
    def name(self):
        return self.__name
    
    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, newCoins):
        self.__coins = newCoins

    @property
    def cards(self):
        return self.__cards
    
#Trabajar esta funcion pq no funciona...
    def loseInfluence(self):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        #la carta es elegida
        chosenCard = int(input('Seleccione una carta (0 o 1): '))
        card = self.cards[chosenCard].getVal()
        self.cards.pop(chosenCard)
        print('hola')
        return card
        #entregar esta carta a lostInfluence en game.
    
    def loseInfluence(self, cardSelected):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        #la carta es elegida
        card = self.cards[cardSelected].getVal()
        self.cards.pop(chosenCard)
        print('hola')
        return card
        #entregar esta carta a lostInfluence en game.


    def pickAction(self):
        action = Printer().menu(self.name)
        return action


    def counterAttack(self):
        block = Printer().counterattack()
        return block

    def Challenge(self):
        challenge = Printer().challenge()
        return challenge

    def modifyCoins(self, amount):
        self.coins += amount
    
    
def main():
    k = Players('Juan')
    for i in k.cards:
        print(i.getVal())
    k.loseInfluence()
    #k.pickAction()
    #print(k.coins)
    
    
if __name__ == "__main__":
    main() 
