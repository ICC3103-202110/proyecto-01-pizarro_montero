class Printer:

    def menu(self, name):
        print('\n', "1. Income","2. Foreign Aid", "3. Coup","4. Tax",
        "5. Assassinate","6. Exchange","7. Steal", sep="\n")
        print('\n', '['+name+']', '\n')
        return int(input("What would you like to do? > "))
        
    def challenge(self, name):
        print('\n', '['+name+']', '\n')
        print("Do you want to Challenge?")
        print("1. Yes")
        print("2. No")
        answer = int(input('> '))
        return answer

    def counterattack(self, name):
        print('\n', '['+name+']', '\n')
        print("Do you want to counterattack?")
        print("1. Yes")
        print("2. No")
        answer = int(input('> '))
        return answer