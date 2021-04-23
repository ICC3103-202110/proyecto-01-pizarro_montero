from numpy import random
from players import Players
from actions import Action
from deck import Deck

class Game:
    def __init__(self):
        self.players = []
        self.lostInfluences = []
        self.action = Action()
        self.deck = Deck()

    #turno va de 0-3
    #condicion para cantidad de jugadores
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
                    challenging = []
                    counterattacking = []
                    for player in self.players:
                        if player != self.currentPlayer:
                            answer = self.player.counterAttack()
                            if answer == 1:
                                counterattacking.append(player)
                            else:
                                continue
                        
                    if len(counterattacking) != 0:
                        i = random.randint(len(counterattacking))
                        caPlayer = counterattacking[i]

                        for player in self.players:
                            if player != self.caPlayer:
                                answer = self.player.Challenge()
                                if answer == 1:
                                    challenging.append(player)
                                else:
                                    continue

                        if len(challenging) != 0:
                            k = random.randint(len(counterattacking))
                            chPlayer = challenging[i]
                            
                            #se lleva a cabo el desafio
                            
                            'el jugador desafiado muestra su duque'

                        else:
                            #se lleva a cabo el contraataque
                            self.currentPlayer.modifyCoins(0)

                    else:
                        #se lleva a cabo la accion
                        self.action.ForeignAid(self.currentPlayer)
                
                elif action == 3:
                    target = input('quien: ')
                    target = self.players.index(target)
                    self.lostInfluences.append(self.action.Coup(
                        self.currentPlayer, target))

                            # if counterattack= 1:#si
                            #     #preguntar si alguien desafia el contraataque
                            #     if challenge == 1: #si
                            #         #seleccionar carta
                            #         # if self.caPlayer.cards.getVal() == 'Duke':
                            #         #     self.currentPlayer.modifyCoins(0)
                            #         #     self.caPlayer.changeCard()
                            #         # else:
                            #         #     self.action.ForeignAid(self.currentPlayer)
                            #         #     self.lostInfluences.append(
                            #         #         self.caPlayer.loseInfluence())

            #Acciones de Personaje
            else:
                challenging = []
                counterattacking = []
                for player in self.players:
                    if player != self.currentPlayer:
                        #preguntar si quiere desafiar
                        answer = self.player.Challenge()
                            if answer == 1:
                                challenging.append(player)
                            else:
                                continue
                
                if len(challenging) != 0:
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
                        for player in self.players:
                            if player != self.currentPlayer:
                                answer = self.player.counterAttack()
                                if answer == 1:
                                    counterattacking.append(player)
                                else:
                                    continue
                            
                        if len(counterattacking) != 0:
                            i = random.randint(len(counterattacking))
                            caPlayer = counterattacking[i]

                            for player in self.players:
                                if player != self.caPlayer:
                                    answer = self.player.Challenge()
                                    if answer == 1:
                                        challenging.append(player)
                                    else:
                                        continue

                            if len(challenging) != 0:
                                k = random.randint(len(counterattacking))
                                chPlayer = challenging[i]
                                
                                #se lleva a cabo el desafio
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
                                #se lleva a cabo el contraataque
                                elif action == 5:
                                    self.currentPlayer.modifyCoins(-3)
                                elif action == 7:
                                    self.currentPlayer.modifyCoins(0)

                        else:
                            #se lleva a cabo la accion
                            if action == 5:
                                target = input('as: ')
                                target = self.players.index(target)
                                self.action.Assassinate(
                                    self.currentPlayer, target)
                            elif action == 7:
                                #steal
                                pass
        
                    else:
                        #ejecuta accion
                        if action == 4:
                            target = input('f: ')
                            target = self.players.index(target)
                            self.action.Tax(self.currentPlayer, 
                            target)
                        elif action == 6:
                            #exchange
                            pass
                            
            
            if len(self.players) == 1:
                self.GameOver()
            else:
                #cambio de turno


    def GameOver(self):
        return True

#Crear condiciones para cuando los jugadores se quedan sin cartas