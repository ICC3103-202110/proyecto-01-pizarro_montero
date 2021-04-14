from cards import Cards
from numpy import random


class Deck:

    def __init__(self):
        self.influencia = ['Duke','Assasin','Captain','Ambassador','Contessa']
        self.cards = []
        for i in range(len(self.influencia)):
            self.cards.append(Cards(self.influencia[i]))
            self.cards.append(Cards(self.influencia[i]))
            self.cards.append(Cards(self.influencia[i]))
        
    
    def shuffle(self):
        random.shuffle(self.cards)
    