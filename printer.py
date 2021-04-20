class Printer:

    def menu(self, name):
        print("1. Income","2. Foreign Aid", "3. Coup","4. Tax","5. Addassinate"
            ,"6. Exchange","7. Steal", sep="\n")
        print(name, end='')
        return int(input(" ,what would you like to do?: "))
        
    def challenge(self):
        print("Does someone want to Challenge?")
        print("1. Yes")
        print("2. No")
        answer = int(input())
        if answer != 2:
            name = input('Your name: ')
            ans = []
            target = input("Name of the player you are challenging: ")
            ans.append(name)
            ans.append(target)
        #entrega una lista con el jugador que desafio y el que esta desafiando
        return ans

    def counterattack(self):
        print("Does someone want to counterattack?")
        print("1. Yes")
        print("2. No")
        answer = int(input())
        if answer != 2:
            name = input('Your name: ')
            ans = []
            target = input("Name of the player you are counterattacking: ")
            ans.append(name)
            ans.append(target)
        #entrega una lista con el jugador que contra ataco y el que esta desafiando
        return ans

    def blockAction(self):
        print("Does someone want to block the action?")
        print("1. Yes")
        print("2. No")
        answer = int(input())
        if answer != 2:
            name = input('Your name: ')
            ans = []
            target = input("Name of the player you are blocking: ")
            ans.append(name)
            ans.append(target)
        return ans
