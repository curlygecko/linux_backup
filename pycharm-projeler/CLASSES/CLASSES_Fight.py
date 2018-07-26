import random

class Player1:
    def __init__(self):
        self.hp = random.randint(0, 20)
        self.dmg = 5
    def health(self):
        return "Can: ",self.hp


p1 = Player1()

class Player2:
    def __init__(self):
        self.hp = random.randint(0, 20)
        self.dmg = 5
    def health(self):
        return "Can: ",self.hp


p2 = Player2()

class Game:
    def __init__(self):
        self.p1 = p1
        self.p2 = p2

    def combat(self):
        p1.hp = self.p1.hp-self.p2.dmg
        p2.hp = self.p2.hp-self.p1.dmg
        return p1.hp, p2.hp

game = Game()

while p1.hp or p2.hp > 0:
    if p1.hp > p2.hp:
        print("KAZANAN PLAYER 1 !!")
    else:
        print("KAZANAN PLAYER 2 !!")
    print("FIGHT!")
    print(game.combat())


