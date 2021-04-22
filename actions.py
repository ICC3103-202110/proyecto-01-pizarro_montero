from players import Players
from deck import Deck

class Action:
    
    def __init__(self):
        self.coinsGained = 0

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
#Ver desafio
    def Tax(self, player1, player2):
        player1.modifyCoins(3)
        #depende de las monedas que tiene player2
        player2.modifyCoins(-3)
        
        
    def Assassinate(self, player1, player2):
        player1.modifyCoins(-3)
        selectedCard = int(input('Which card do you want to delete?: '))
        #ver lo de la cantidad de cartas
        #leer enunciado
        deadCard = self.player2.loseInfluence(selectedCard)
        return deadCard 
        #paga 3 mmonedas y asesina una influencia
    
    def Steal(self, player1, player2):
        #condiciones monedas player2
        player1.modifyCoins(2)
        player2.modifyCoins(-2)
 


    def Exchange(self, player1, deck):
        newCards = deck.deal_cards()
        oldCards = player1.cards()
        #seleccionar una carta para quedarse devolver dos
        
        #cambia sus cartas
        

