from random import randrange
from robots import Robot, Aggressive, Defensive, Zombie, Lucky

class War:
    
    def __init__(self, a, b):
        """Create class war between two given robots - a and b"""
        self.robot_A = a
        self.robot_B = b
        self.score_A = 0
        self.score_B = 0

    def round(self):
        """Realises one round of battle of two robots.
        The robot, which stay alive longer, become a winner"""
        self.robot_A.lifes = self.robot_A.max_lifes
        self.robot_B.lifes = self.robot_B.max_lifes

        while True:
            self.robot_A.attack(self.robot_B)
            print('{}: {}'.format(self.robot_B.name, self.robot_B.lifes))
            if not self.robot_B.is_alive():
                print('{} won this round.'.format(self.robot_A.name))
                self.score_A += 1
                break
    
            self.robot_B.attack(self.robot_A)
            print('{}: {}'.format(self.robot_A.name, self.robot_A.lifes))   
            if not self.robot_A.is_alive():
                print('{} won this round.'.format(self.robot_B.name))
                self.score_B += 1
                break

    def battle(self, number_of_rounds):
        """Repeat round in given number of times and print the winner of battle."""
        for _ in range(number_of_rounds):
            self.round()
        if self.score_A > self.score_B:
            print('{} won battle'.format(self.robot_A.name))
        elif self.score_A < self.score_B:
            print('{} won battle'.format(self.robot_B.name))
        else:
            print('Fifty fifty - nobody won')


aggr = Aggressive('Fred')
deff = Defensive('George')
zomb = Zombie('Jane')
luck = Lucky('Luke')


war = War(deff, luck)
war.battle(4)