from players import Players
from deck import Deck

class Action:
    
    # def __init__(self):
    #     self.coinsGained = 0

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
        oldCards = player.cards()
        exchangeCards = []


        for i in newCards:
            print(index(i),'.',i)
        for i in oldCards:
            print((index(i)+2),'.', i)


        for i in len(newCards):
            x = int(input("Choose a card:"))
            if x == 1 or x ==2:
                exchangeCards.append(newCards[x])
                newCards.remove(newCards[x])
            if x == 3 or x ==2:
                exchangeCards.append(oldCards[x])
                oldCards.remove(oldCards[x])

        
        Deck.return_card(newCards)
        

        #elige 2 cartas y devuelve las otras 2

    def Steal(self, player1, player2):
        #condiciones monedas player2
        if player2.coins >= 2 :
            player1.modifyCoins(2)
            player2.modifyCoins(-2)
        elif player2.coins == 1:
            player1.modifyCoins(1)
            player2.modifyCoins(-1)
            

