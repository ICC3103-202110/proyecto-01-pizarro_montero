from numpy import random
from players import Players
from actions import Action
from deck import Deck

class Game:
    def __init__(self):
        self.__players = []
        self.__lostInfluences = []
        self.__action = Action()
        self.__deck = Deck()

    @property
    def players(self):
        return self.__players
    
    @players.setter
    def players(self, players):
        self.__players = players

    @property
    def lostInfluences(self):
        return self.__lostInfluences
    
    @lostInfluences.setter
    def lostInfluences(self, lostInfluences):
        self.__lostInfluences = lostInfluences
    
    @property
    def action(self):
        return self.__action
    
    @action.setter
    def action(self, action):
        self.__action = action
    
    @property
    def deck(self):
        return self.__deck
    
    @deck.setter
    def deck(self, deck):
        self.__deck = deck

    def askcounterattack(self):
        counterattacking = []
        for player in self.players:
            if player != self.currentPlayer:
                answer = self.player.counterAttack()
                if answer == 1:
                    counterattacking.append(player)
            
        if len(counterattacking) != 0:
            i = random.randint(len(counterattacking))
            caPlayer = counterattacking[i]
            return caPlayer
        else:
            return False  

    def askchallenge(self, challengedPlayer):
        challenging = []
        for player in self.players:
            if player != self.challengedPlayer:
                answer = self.player.Challenge()
                if answer == 1:
                    challenging.append(player)

        if len(challenging) != 0:
            k = random.randint(len(counterattacking))
            chPlayer = challenging[i]
            return chPlayer
        else:
            return False
        

    def play(self):
        self.turn = 0
        num_of_players = int(input('Cuantos jugadores?: '))
        while num_of_players < 3 or num_of_players > 4:
            print('Cantidad invalida')
            num_of_players = int(input('Cuantos jugadores?: '))
        for i in range(num_of_players):
            name = input('Nombre jugador: ')
            self.players.append(Players(name, self.deck))
        #crear condicion para que no se repitan nombres

        while not self.GameOver():
            self.currentPlayer = self.players[self.turn]
            action = self.currentPlayer.pickAction()

            #Acciones Generales
            if action == 1 or action == 2 or action == 3:
                if action == 1:
                    self.action.Income(self.currentPlayer)
                elif action == 2:
                    ca = self.askcounterattack()
                    if ca != False:
                        #se pregunta si se quiere desafiar
                        ch = self.askchallenge(ca)
                        if ch != False:
                            #se desafia
                            '''
                            si gana el que desafia el jugador que 
                            contraataca pierde una carta, el jugador 
                            actual ejecuta la accion si gana el desafio
                            se ejecuta el contraataque, el jugador que
                            contraataca devuelve su carta al mazo y 
                            saca otra y el jugador que desafia pierde
                            una influencia.
                            '''
                        else:
                            #se contraataca
                            self.currentPlayer.modifyCoins(0)
                    else:
                        #ejecuta accion
                        self.action.ForeignAid(self.currentPlayer)
                
                elif action == 3:
                    target = input('Target: ')
                    target = self.players.index(target)
                    self.lostInfluences.append(self.action.Coup(
                        self.currentPlayer, target))

            #Acciones de Personaje
            else:
                ch = self.askchallenge(self.currentPlayer)
                if ch != False:
                    #ejecutar desafio
                    '''
                    si gana el que desafia el jugador actual pierde una
                    carta y no se ejecuta la accion.
                    si gana el desafio se ejecuta la accion, el jugador
                    actual devuelve su carta al mazo y saca otra y el 
                    jugador de desafia pierde la influencia.
                    '''   
                else:
                    if action == 5 or action == 7:
                        ca = self.askcounterattack()
                        if ca != False:
                            ch = self.askchallenge(ca)
                            if ch != False:
                                #se desafia
                                '''
                                si gana el que desafia el jugador que 
                                contraataca pierde una carta, el jugador 
                                actual ejecuta la accion si gana el desafio
                                se ejecuta el contraataque, el jugador que
                                contraataca devuelve su carta al mazo y 
                                saca otra y el jugador que desafia pierde
                                una influencia.
                                '''
                            else:
                                #se contraataca
                                if action == 5:
                                    self.currentPlayer.modifyCoins(-3)
                                elif action == 7:
                                    self.currentPlayer.modifyCoins(0)
                                
                        else:
                            #ejecuta accion
                            if action == 5:
                                target = input('Target: ')
                                target = self.players.index(target)
                                self.action.Assassinate(
                                    self.currentPlayer, target)
                            elif action == 7:
                                #steal
                                pass

                    else:
                        #ejecuta accion
                        if action == 4:
                            target = input('Target: ')
                            target = self.players.index(target)
                            self.action.Tax(self.currentPlayer, 
                            target)
                        elif action == 6:
                            #exchange
                            pass
                            
            
            if len(self.players) == 1:
                self.GameOver()
            else:
                if self.turn < num_of_players:
                    self.turn += 1
                else:
                    self.turn = 0


    def GameOver(self):
        return True

#Crear condiciones para cuando los jugadores se quedan sin cartas

def main():
    g = Game().play()
    
    
if __name__ == "__main__":
    main() 