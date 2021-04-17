from cards import Cards
from numpy import random


class Deck:
    #elimina las que no estan
    def __init__(self):
        self.deck = []
        self.influenceCard = ['Duke','Assasin','Captain','Ambassador',
        'Contessa']
        for i in self.influenceCard:
            for k in range(3):
                self.deck.append(Cards(i))
        random.shuffle(self.deck)

    def deal_cards(self):
        pass 