from random import randrange

class Robot():
    max_damage = 5
    max_lifes = 20

    def __init__(self):
        self.lifes = self.max_lifes
        self.name = 'Name'

    def _make_damage(self, target_robot):
        """Generates random damage and forces the
        other robot to defend."""
        damage = randrange(0, self.max_damage)
        target_robot.defend(damage)

    def _take_damage(self, damage):
        """Sets new number of lifes when not already 0."""
        if self.lifes - damage <0:
            self.lifes = 0
        else:
            self.lifes -= damage
    
    def is_alive(self):
        """Returns True if robot has any lifes left."""
        return self.lifes > 0

    def defend(self, damage):
        """Default defend. Simply takes damage."""
        self._take_damage(damage)

    def attack(self, target_robot):
        """Default attack. Simply makes damage."""
        self._make_damage(target_robot)

class Aggressive(Robot):
    max_damage = 7
    max_lifes = 10

    def __init__(self):
        super().__init__()
        self.name = 'Aggresive'

    def attack(self, target_robot):
        """Makes damage to the other robot twice. Special for aggresive robot."""
        for _ in range(2):
            self._make_damage(target_robot)

class Defensive(Robot):
    max_damage = 3    
    max_lifes = 40

    def __init__(self):
        super().__init__()
        self.name = 'Deffensive'

    def defend(self, damage):
        """Special for deffensive robot, takes only half damage."""
        self._take_damage(damage // 2)

class Zombie(Robot):

    def __init__(self):
        super().__init__()
        self.name = 'Zombie'

    def is_alive(self):
        """Special for Zombie robot - can't be killed."""
        return True

class Lucky(Robot):

    def __init__(self):
        super().__init__()
        self.name = 'Lucky'

    def defend(self, damage):
        """Takes damage only if number of damage is divisible by 2."""
        if damage % 2 == 0:
            self._take_damage(damage)
        else:
            print('{}: Ha, you missed.'.format(self.name))

class War:

    def __init__(self, a, b):
        self.robot_A = a
        self.robot_B = b
        self.score_A = 0
        self.score_B = 0

    def round(self):
        
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
        for _ in range(number_of_rounds):
            self.round()
        if self.score_A > self.score_B:
            print('{} won battle'.format(self.robot_A.name))
        elif self.score_A < self.score_B:
            print('{} won battle'.format(self.robot_B.name))
        else:
            print('Fifty fifty - nobody won')


aggr = Aggressive()
deff = Defensive()
zomb = Zombie()
luck = Lucky()


war = War(deff, luck)
war.battle(4)