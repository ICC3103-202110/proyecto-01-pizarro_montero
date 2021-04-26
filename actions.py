from players import Players
from deck import Deck

class Action:

#Acciones Generales
    def Income(self, player):
        player.modifyCoins(1)   

    def ForeignAid(self, player):
        player.modifyCoins(2)

    def Coup(self, player1, player2):
        player1.modifyCoins(-7)
        selectedCard = int(input('Which card do you want to delete?: '))
        #ver lo de la cantidad de cartas
        #leer enunciado
        deadCard = self.player2.loseInfluence(selectedCard)
        return deadCard 

#Acciones de Personaje
    def Tax(self, player1):
        player1.modifyCoins(3)
        
    def Assassinate(self, player1, player2):
        #paga 3 monedas y asesina una influencia
        player1.modifyCoins(-3)
        deadCard = self.player2.loseInfluence()
        return deadCard

    def Exchange(self, player, deck):
        newCards = deck.deal_cards()
        oldCards = player.cards
        exchangeCards = []
        returnCards = []
        for i in newCards:
            print(newCards.index(i),'.',i.val)
        for i in oldCards:
            print((oldCards.index(i)+2),'.', i.val)

        print('\n')
        for i in range(len(newCards)):
            x = int(input("Choose a card:"))
            if x == 0 or x == 1:
                exchangeCards.append(newCards[x])
                newCards.pop(x)
            if x == 2 or x == 3:
                exchangeCards.append(oldCards[x-2])
                oldCards.pop(x - 2)

        for i in newCards:
            returnCards.append(i)
        for i in oldCards:
            returnCards.append(i)
        for i in returnCards:
            deck.return_card(i)
    
        player.cards = exchangeCards


        #elige 2 cartas y devuelve las otras 2

    def Steal(self, player1, player2):
        #condiciones monedas player2
        if player2.coins >= 2 :
            player1.modifyCoins(2)
            player2.modifyCoins(-2)
        elif player2.coins == 1:
            player1.modifyCoins(1)
            player2.modifyCoins(-1)