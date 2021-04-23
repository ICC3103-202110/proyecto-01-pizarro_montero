from printer import Printer
from deck import Deck

class Players:

    def __init__(self, name, deck):
        self.__name = name
        self.__coins = 2
        self.__cards = deck.deal_cards()

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
    
    def loseInfluence(self):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        chosenCard = int(input('Seleccione una de sus cartas: '))
        card = self.cards[chosenCard].getVal()
        self.cards.pop(chosenCard)
        return card
    
    # def loseInfluence(self, cardSelected):
    #     #el jugador pierde una carta y esta debe quedar visible para todos los
    #     #jugadores, no vuelve al mazo
    #     card = self.cards[cardSelected].getVal()
    #     self.cards.pop(chosenCard)
    #     return card


    def pickAction(self):
        action = Printer().menu(self.name)
        return action
    
    def counterAttack(self):
        counterattack = Printer().counterattack()
        return counterattack

    def Challenge(self):
        challenge = Printer().challenge()
        return challenge

    def modifyCoins(self, amount):
        self.coins += amount
    
    def changeCard(self, card):
        pass


def main():
    k = Players('Juan')
    for i in k.cards:
        print(i.getVal())
    k.loseInfluence()
    #k.pickAction()
    #print(k.coins)
    
    
if __name__ == "__main__":
    main() 
