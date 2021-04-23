class Cards:
    def __init__(self, val):
        self.__val = val

    @property
    def val(self):
        return  self.__val