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
        for i in range(len(newCards)):
            print(i,'.', newCards(i))
        for i in range(len(newCards)):
            print(i,'.', oldCards(i))
        
        #elige 2 cartas y devuelve las otras 2

    def Steal(self, player1, player2):
        #condiciones monedas player2
        if player2.coins() >= 2 :
            player1.modifyCoins(2)
            player2.modifyCoins(-2)
        elif player2.coins == 1:
            player1.modifyCoins(1)
            player2.modifyCoins(-1)
            

