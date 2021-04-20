class Cards:
    def __init__(self, val):
        self.__val = val
        self.__isFaceUp = False
        self.__inGame = True

    @property
    def val(self):
        return  self.__val
    


    @property
    def isFaceUp(self):
        return self.__isFaceUp

    @isFaceUp.setter
    def isFaceUp(self):
        if self.__isFaceUp:
            self.__isFaceUp = False
        else:
            self.__isFaceUp = True

    @property
    def inGame(self):
        return self.__inGame

    @inGame.setter
    def inGame(self):
        
        