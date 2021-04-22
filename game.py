from players import Players
from actions import Action

class Game:
    def __init__(self):
        self.players = []
        self.lostInfluences = []
        self.action = Action()
    #self.lostInfluences.append(self.players[algo].loseInfluence())

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
            self.players.append(Players(name))
        #crear condicion para que no se repitan nombres

        while not self.GameOver():
            self.currentPlayer = self.players[self.turn]
            action = self.currentPlayer.pickAction()
            #Acciones Generales
            if action == 1 or action == 2 or action == 3:
                if action == 1:
                    self.action.Income(self.currentPlayer)
                elif action == 2:
                    self.action.ForeignAid(self.currentPlayer)
                elif action == 3:
                    target = input('quien: ')
                    target = self.players.index(target)
                    self.lostInfluences.append(self.action.Coup(
                        self.currentPlayer, target))
            #Acciones de Personaje
            else:
                for player in self.players:
                    if player != self.currentPlayer:
                        #preguntar si quiere desafiar
                        player.Challenge()
                        if challenge == 1:#si
                            #desafia
                            '''
                            si gana el que desafia el jugador actual pierde una
                            carta y no se ejecuta la accion.
                            si gana el desafio se ejecuta la accion, el jugador
                            actual devuelve su carta al mazo y saca otra y el 
                            jugador de desafia pierde la influencia.
                            '''
                            #condiciones accion/carta
                        elif challenge == 2:#no
                            #preguntar si desea contraatacar
                            if counterattack == 1: #si
                                #preguntar si alguien desafia el contraataque
                                if challenge == 1:#si
                                    #desafia al contraataque
                                    '''
                                si gana el que desafia el jugador que 
                                contraataca pierde una carta, el jugador actual
                                ejecuta la accion
                                si gana el desafio se ejecuta el contraataque, 
                                el jugador que contraataca devuelve su carta
                                al mazo y saca otra y el jugador de desafia 
                                pierde una influencia.
                                '''
                                #condiciones contraataque/carta
                                elif challenge = 2:#no
                                    #contraataca
                            elif counterattack == 2:#no
                                #ejecuta accion
                                if action == 4:
                                    target = input('f: ')
                                    target = self.players.index(target)
                                    self.action.Tax(self.currentPlayer, target)
                                elif action == 5:
                                    target = input('as: ')
                                    target = self.players.index(target)
                                    self.action.Assassinate(self.currentPlayer,
                                     target)
                                elif action == 6:
                                    pass
                                elif action == 7:
                                    pass
            
            if len(self.players) == 1:
                GameOver()
            else:
                #cambio de turno


    def GameOver(self):
        return True

#Crear condiciones para cuando los jugadores se quedan sin cartas