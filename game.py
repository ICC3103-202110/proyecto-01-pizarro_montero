from players import Players
from actions import Action

class Game:
    def __init__(self):
        self.players = []
        self.lostInfluences = []

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
    

        while not self.GameOver():
            self.currentPlayer = self.players[self.turn]
            action = self.currentPlayer.pickAction()
            
            if action == 1 or action == 2 or action == 3:
                if action == 1:
                    print('income')
                    amount = Action().Income()
                    self.currentPlayer.modifyCoins(amount)
                elif action == 2:
                    print('foreign aid')
                    amount = Action().ForeignAid()
                    self.currentPlayer.modifyCoins(amount)
                elif action == 3:
                    print('coup')
                    self.currentPlayer.modifyCoins(amount)
                    (self.lostInfluences.append(self.target.
                    loseInfluence(selectedCard))

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
                        elif challenge == 2:#no
                            #preguntar si desea contraatacar
                            if counterattack == 1: #si
                                "preguntar si alguien desafia el contraataque"
                                if challenge == 1:
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
                                elif challenge = 2:
                                    #contraataca
                            elif counterattack == 2:
                                #ejecuta accion
            
            #cambio de turno


    def GameOver(self):
        return True
