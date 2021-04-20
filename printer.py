


class Printer:

    def menu(self, numero):
        print("Player", numero,  ",what would you like to do?")
        print("1. Income"
            ,"2. Foreign Aid"
            ,"3. Coup"
            ,"4. Tax"
            ,"5. Addassinate"
            ,"6. Exchange"
            ,"7. Steal"
            , sep="\n")
        return input()
        
    def challenge(self, Jugador):
        print("Does someone want to Challenge?")
        print("Yes, then identify your self (Your number):")
        print("No, then enter 0")
        return input()

    def counterattack(self, Jugador):
        print("Does someone want to counterattack?")
        print("Yes, then identify your self (Your number):")
        print("No, then enter 0")
        return input()
        
