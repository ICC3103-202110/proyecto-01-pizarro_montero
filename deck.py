from cards import Cards
from numpy import random


class Deck:
    def __init__(self):
        self.generate_deck()

    @property
    def cards(self):
         return self.__cards

    @cards.setter
    def cards(self, cards):
        self.__cards = cards
    

    def generate_deck(self):
        influenceCard = ['Duke','Assasin','Captain','Ambassador',
        'Contessa']
        self.cards = []
        for i in influenceCard:
            for k in range(3):
                self.cards.append(Cards(i))
        random.shuffle(self.cards)
    
    def deal_cards(self):
        deal = []
        for i in range(2):
            card = self.cards[i]
            deal.append(card)
            self.cards.pop(i)
        return deal

    def return_card(self, card):
        self.cards.append(card)

    def deal_one_card(self):
        for i in range(len(self.cards)):
            card = self.cards[i]
            self.cards.pop(i)
        return card
