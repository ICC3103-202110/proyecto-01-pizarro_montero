from cards import Cards
from numpy import random


class Deck:
    def __init__(self):
        self.__cards = self.generate_deck()


    @property
    def cards(self):
         return self.__cards
    
    def generate_deck(self):
        influenceCard = ['Duke','Assasin','Captain','Ambassador',
        'Contessa']
        cards = []
        for i in influenceCard:
            for k in range(3):
                cards.append(Cards(i))
        random.shuffle(cards)
        return cards
    

    def deal_cards(self):
        deal = []
        for i in range(2):
            card = self.cards[i]
            deal.append(card)
            self.cards.pop(i)
        return deal


    def remove_card_of_deck(self, card):
        self.cards.remove(card)