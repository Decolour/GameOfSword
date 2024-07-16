import ABC

class Fighter:
    def __init__(self, name):
        self.name = name

class Monster:
    def __init__(self, name):
        self.name = name

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("Sword attack")

class Axe(Weapon):
    def attack(self):
        print("Axe attack")

class Bow(Weapon):
    def attack(self):
        print("Bow attack")

class Dagger(Weapon):
    def attack(self):
        print("Dagger attack")