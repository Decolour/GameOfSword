from abc import ABC, abstractmethod
import random

class Warrior:
    def __init__(self, luck, weapon):
        self.luck = luck
        self.weapon = weapon

class Fighter(Warrior):
    def __init__(self, name, luck, weapon, Strength, Defense, Health):
        super().__init__(luck, weapon)
        self.name = name
        self.Strength = Strength
        self.Defense = Defense
        self.Health = Health

class Monster(Warrior):
    def __init__(self, name, luck, weapon, Strength, Defense, Health):
        super().__init__(luck, weapon)
        self.name = name
        self.Strength = Strength
        self.Defense = Defense
        self.Health = Health

class Weapon(ABC):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self, name, damage, weight):
        super().__init__(name, damage)
        self.weight = weight

    def attack(self):
        print("Sword attack")

class Axe(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self):
        print("Axe attack")

class Dagger(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)

    def attack(self):
        print("Dagger attack")

# Создание объектов оружия
Kladinec = Sword("Кладинец", 10, 10) # Create a sword object
Fang = Dagger("Клык", 5) # Create a dagger object
Kirdyk = Axe("Кирдык", 7) # Create an axe object

# Создание объектов бойцов и монстров
Vanya = Fighter("Ваня", 4, Kladinec, 10, 11, 100) # Create a fighter object
Ilyusha = Fighter("Илюша", 7, Kirdyk, 15, 7, 70) # Create a fighter object
Petrovich = Fighter("Петрович", 15, Fang, 7, 10, 50) # Create a fighter object

Babay = Monster("Бабай", 10, Kladinec, 10, 10, 40) # Create a monster object
Byaka = Monster("Бяка", 5, Fang, 6, 5, 60) # Create a monster object

def damage_calculation(attacking, defending):
    damage = attacking.weapon.damage + attacking.Strength - defending.Defense + random.randint(0, 10) * attacking.luck
    return max(damage, 0)  # Чтобы не было отрицательного урона

def fight(attacking, defending):
    # Сохранение начальных значений
    initial_attacking_health = attacking.Health
    initial_defending_health = defending.Health

    while attacking.Health > 0 and defending.Health > 0:
        damage = damage_calculation(attacking, defending)
        defending.Health -= damage
        print(f"{attacking.name} наносит {damage} урона оружием {attacking.weapon.name} персонажу {defending.name}")
        if defending.Health <= 0:
            print(f"{attacking.name} победил {defending.name}")
            break
        damage = damage_calculation(defending, attacking)
        attacking.Health -= damage
        print(f"{defending.name} наносит {damage} урона {attacking.name}")
        if attacking.Health <= 0:
            print(f"{defending.name} победил {attacking.name}")

        # Сброс параметров объектов до начальных значений
    attacking.Health = initial_attacking_health
    defending.Health = initial_defending_health


fight(Vanya, Babay)
fight(Ilyusha, Byaka)

fight(Petrovich, Babay)
