class Cards:
    def __init__(self, val):
        self.val = val
        self.isFaceUp = False
        self.inGame = True

    def getVal(self):
        return  self.val

    def flipCard(self):
        return True
        