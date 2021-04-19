from players import Players


class Game:
    def __init__(self):
        self.players = []
        self.lostInfluences = []

    #turno va de 0-3
    #condicion para cantidad de jugadores
    def play(self):
        self.currentPlayer = 0
        num_of_players = int(input('Cuantos jugadores?: '))
        while num_of_players < 3 or num_of_players > 4:
            print('Cantidad invalida')
            num_of_players = int(input('Cuantos jugadores?: '))
        for i in range(num_of_players):
            name = input('Nombre jugador: ')
            self.players.append(Players(name))
        pass