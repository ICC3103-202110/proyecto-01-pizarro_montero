from deck import Deck


class Players:

    def __init__(self, name):
        self.name = name
        self.coins=0
        self.cards = Deck.deal_cards()

    def pickAction(self):
        self.action = input('Que desea hacer?: ')
        if self.action = '':
            pass
        pass

    def blockAction(self):
        
        pass

    def modify_coins(self, amount):
        self.coins += amount

    
    
    
