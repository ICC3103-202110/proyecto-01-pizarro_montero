from printer import Printer
from deck import Deck
from actions import Action, Income


class Players:

    def __init__(self, name):
        self.name = name
        self.coins = 2
        self.__cards = Deck().deal_cards()

    @property
    def cards(self):
        return self.__cards
    
#Trabajar esta funcion pq no funciona...
    def loseInfluence(self):
        #el jugador pierde una carta y esta debe quedar visible para todos los
        #jugadores, no vuelve al mazo
        #la carta es elegida
        chosenCard = int(input('Seleccione una carta (0 o 1): '))
        card = self.cards(chosenCard).getVal()
        print('hola')
        print(card)
        #self.cards.pop(i)
         #entregar esta carta a lostInfluence en game.


    def pickAction(self):
        action = Printer().menu(self.name)
        if action == 1:
            print('income')
            #print(income().play_action())
            x = income().play_action()
            self.modifyCoins(x)
        elif action == 2:
            print('foreign help')
        elif action == 3:
            print('coup')
        elif action == 4:
            print('tax')
        elif action == 5:
            print('assesinate')
        elif action == 6:
            print('exchange')
        elif action == 7:
            print('steal')


    def blockAction(self):
        block = Printer().blockAction()
        pass

    def Challenge(self):
        pass

    def modifyCoins(self, amount):
        self.coins += amount
    
    
def main():
    k = Players('Juan')
    for i in k.cards:
        print(i.getVal())
    #k.loseInfluence()
    k.pickAction()
    print(k.coins)
    
    
if __name__ == "__main__":
    main() 
