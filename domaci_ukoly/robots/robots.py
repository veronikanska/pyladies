# Modul with predefined classes of different kinds of robots with special features.

from random import randrange

class Robot():
    max_damage = 5
    max_lifes = 20

    def __init__(self, name):
        """Create robot with max count of lifes and with given name."""
        self.lifes = self.max_lifes
        self.name = 'Basic {}'.format(name)

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

    def __init__(self, name):
        super().__init__(name)
        self.name = 'Aggresive {}'.format(name)

    def attack(self, target_robot):
        """Makes damage to the other robot twice. Special for aggresive robot."""
        for _ in range(2):
            self._make_damage(target_robot)

class Defensive(Robot):
    max_damage = 3    
    max_lifes = 40

    def __init__(self, name):
        super().__init__(name)
        self.name = 'Defensive {}'.format(name)

    def defend(self, damage):
        """Special for deffensive robot, takes only half damage."""
        self._take_damage(damage // 2)

class Zombie(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Zombie {}'.format(name)

    def is_alive(self):
        """Special for Zombie robot - can't be killed."""
        return True

class Lucky(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.name = 'Lucky {}'.format(name)

    def defend(self, damage):
        """Takes damage only if number of damage is divisible by 2."""
        if damage % 2 == 0:
            self._take_damage(damage)
        else:
            print('{}: Ha, you missed.'.format(self.name))