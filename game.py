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
                    x = AC
                    self.currentPlayer.modifyCoins(x)
                elif action == 2:
                    print('foreign aid')
                    x = ForeignAid().play_action()
                    self.currentPlayer.modifyCoins(x)
                elif action == 3:
                    print('coup')
                    x = Coup().play_action()
                    self.currentPlayer.modifyCoins(x)
                    self.loseInfluence()

            else:
                for player in self.players:
                    if player != self.currentPlayer:
                        #preguntar si quiere desafiar
                        if challenge == 1:#si
                            #desafia
                        elif challenge == 2:#no
                            #preguntar si desea contraatacar
                            if counterattack == 1: #si
                                "alguien pregunta si desafia el contraataque"
                                if challenge == 1:
                                    #desafia al contraataque
                                elif challenge = 2:
                                    #desafia


    def GameOver(self):
        return True

