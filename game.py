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
                answer = player.counterAttack()
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
            if player != challengedPlayer:
                answer = player.Challenge()
                if answer == 1:
                    challenging.append(player)

        if len(challenging) != 0:
            k = random.randint(len(challenging))
            chPlayer = challenging[k]
            return chPlayer
        else:
            return False
        
    def Challenge_(self, challenged, player, influence):
        i = 0
        while i < len(challenged.cards):
            if challenged.cards[i] == influence:
                #gana el desafio
                #el jugador desafiado cambia su carta
                deck.return_card(challenged.cards[i])
                challenged.cards.pop(i)
                challenged.changeCard(deck.deal_one_card())
                # jugador que desafia pierde influencia
                player.loseInfluence()
                return True
            else:
                i += 1
                if i == len(challenged.cards):
                    #pierde el desafio
                    #el jugador desafiado pierde una influencia
                    challenged.loseInfluence()
                    return False


    def game_status(self):
        for i in self.players:
            print(i.name, ":", i.coins)


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
            self.game_status()
            action = self.currentPlayer.pickAction()

            #Acciones Generales
            if action == 1 or action == 2 or action == 3:
                if action == 1:
                    self.action.Income(self.currentPlayer)
                elif action == 2:
                    #se pregunta si se quiere contraatacar
                    ca = self.askcounterattack()
                    if ca != False:
                        #se pregunta si se quiere desafiar
                        ch = self.askchallenge(ca)
                        if ch != False:
                            #se desafia
                            challenge = self.Challenge_(ca, ch, 'Duke')
                            if challenge == True:
                                # se contraataca
                                self.currentPlayer.modifyCoins(0)
                            elif challenge == False:
                                # currentPlayer ejecuta accion
                                self.action.ForeignAid(self.currentPlayer)                                 

                        else:
                            #se contraataca
                            self.currentPlayer.modifyCoins(0)
                    else:
                        #ejecuta accion
                        self.action.ForeignAid(self.currentPlayer)
                
                elif action == 3:
                    print('\n')
                    target = input('Target: ')
                    ind = self.players.index(target)
                    target = self.players[ind]
                    self.lostInfluences.append(self.action.Coup(
                        self.currentPlayer, target))

            #Acciones de Personaje
            else:
                ch = self.askchallenge(self.currentPlayer)
                if ch != False:
                    #ejecutar desafio
                    if action == 4:
                        inf = 'Duke'
                    elif action == 5:
                        inf = 'Assasin'
                    elif action == 6:
                        inf = 'Ambassador'
                    elif action == 7:
                        inf = 'Captain'
                    challenge = self.Challenge_(self.currentPlayer, ch, inf)
                    if challenge == True:
                        #ejecutar accion 
                        if action == 4:
                            self.action.Tax(self.currentPlayer)
                        elif action == 5:
                            print('\n')
                            target = input('Target: ')
                            ind = self.players.index(target)
                            target = self.players[ind]
                            self.action.Assassinate(self.currentPlayer, target)
                        elif action == 6:
                            self.action.Exchange(self.currentPlayer, self.deck)
                        elif action == 7:
                            print('\n')
                            target = input('Target: ')
                            ind = self.players.index(target)
                            target = self.players[ind]
                            self.action.Steal(self.currentPlayer, target)  
                else:
                    if action == 5 or action == 7:
                        #se pregunta si se quiere contraatacar
                        ca = self.askcounterattack()
                        if ca != False:
                            #se pregunta si se quiere desafiar el contraataque
                            ch = self.askchallenge(ca)
                            if ch != False:
                                #se desafia
                                if action == 5:
                                    inf = 'Contessa'
                                elif action == 7:
                                    inf = 'Captain'
                                    challenge = self.Challenge_(ca, ch, inf)
                                    if challenge == False:
                                        inf = 'Ambassador'

                                challenge = self.Challenge_(ca, ch, inf)

                                if challenge == True:
                                    #se contraataca
                                    if action == 5:
                                        self.currentPlayer.modifyCoins(-3)
                                    elif action == 7:
                                        self.currentPlayer.modifyCoins(0)
                                elif challenge == False:
                                    #ejecutar accion 
                                    if action == 5:
                                        print('\n')
                                        target = input('Target: ')
                                        ind = self.players.index(target)
                                        target = self.players[ind]
                                        self.action.Assassinate(
                                            self.currentPlayer, target)
                                    elif action == 7:
                                        print('\n')
                                        target = input('Target: ')
                                        ind = self.players.index(target)
                                        target = self.players[ind]
                                        self.action.Steal(
                                            self.currentPlayer, target) 

                            else:
                                #no hay desafio y se contraataca
                                if action == 5:
                                    self.currentPlayer.modifyCoins(-3)
                                elif action == 7:
                                    self.currentPlayer.modifyCoins(0)
                                
                        else:
                            #ejecuta accion
                            if action == 5:
                                print('\n')
                                target = str(input('Target: '))
                                ind = self.players.index(target)
                                target = self.players[ind]
                                self.action.Assassinate(
                                    self.currentPlayer, target)
                            elif action == 7:
                                print('\n')
                                target = input('Target: ')
                                ind = self.players.index(target)
                                target = self.players[ind]
                                self.action.Steal(self.currentPlayer, target)

                    else:
                        #ejecuta accion
                        if action == 4:
                            self.action.Tax(self.currentPlayer)
                        elif action == 6:
                            self.action.Exchange(self.currentPlayer, self.deck)
                            pass

            #verifica que los jugadores tengan cartas
            for i in self.players:
                if len(i.cards) == 0:
                    k = self.players.index(i)
                    self.players.pop(k)
            
            if self.turn < num_of_players:
                self.turn += 1
            else:
                self.turn = 0


    def GameOver(self):
        if len(self.players) == 1:
            return True