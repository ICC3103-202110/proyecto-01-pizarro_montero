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

    @cards.setter
    def cards(self, cards):
        self.__cards = cards
    
    def loseInfluence(self):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        cont = len(self.cards)
        chosenCard = int(input('Seleccione una de sus cartas: '))
        card = self.cards[chosenCard].val
        self.cards.pop(chosenCard)
        return card

    def loseInfluence(self, selectedCard):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        cont = len(self.cards)
        card = self.cards[selectedCard].val
        self.cards.pop(selectedCard)
        return card

    def pickAction(self):
        action = Printer().menu(self.name)
        return action
    
    def counterAttack(self):
        counterattack = Printer().counterattack(self.name)
        return counterattack

    def Challenge(self):
        challenge = Printer().challenge(self.name)
        return challenge

    def modifyCoins(self, amount):
        self.coins += amount
    
    def changeCard(self, card):
        self.cards.append(card)