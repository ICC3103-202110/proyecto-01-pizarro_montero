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
        pass

    def remove_card_of_deck(self):
        pass 