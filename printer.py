class Printer:

    def menu(self, numero):
        print("Player", numero,  ",what would you like to do?")
        print("1. Income","2. Foreign Aid", "3. Coup","4. Tax","5. Addassinate"
            ,"6. Exchange","7. Steal", sep="\n")
        return int(input())
        
    def challenge(self):
        print("Does someone want to Challenge?")
        print("Yes, then identify your self (Your players name):")
        print("No, then enter 0")
        answer = input()
        if answer != 0 :
            ans = []
            print("Name of the player you are challenging:")
            target = input()
            ans.append(answer)
            ans.append(target)
        #entrega una lista con el jugador que desafio y el que esta desafiando
        return ans

    def counterattack(self):
        print("Does someone want to counterattack?")
        print("Yes, then identify your self (Your players name):")
        print("No, then enter 0")
        answer = input()
        if answer != 0:
            ans = []
            print("Name of the player you are counterattacking:")
            target = input()
            ans.append(answer)
            ans.append(target)
        #entrega una lista con el jugador que contra ataco y el que esta desafiando
        return ans

    def blockAction(self):
        print("Does someone want to block the action?")
        print("Yes, then identify your self (Your players name):")
        print("No, then enter 0")
        answer = input()
        if answer != 0:
            ans = []
            print("Name of the player you are blocking:")
            target = input()
            ans.append(answer)
            ans.append(target)
        return ans

        
