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
Kladinec = Sword("Кладинец", 10, 10)
Fang = Dagger("Клык", 5)
Kirdyk = Axe("Кирдык", 7)

# Создание объектов бойцов и монстров
Vanya = Fighter("Ваня", 4, Kladinec, 10, 11, 100)
Ilyusha = Fighter("Илюша", 7, Kirdyk, 15, 7, 70)
Petrovich = Fighter("Петрович", 20, Fang, 7, 10, 50)

Babay = Monster("Бабай", 10, Kladinec, 10, 10, 100)
Byaka = Monster("Бяка", 5, Fang, 13, 53, 60)

def change_warrior():
    print("Имеющиеся бойцы:")
    print("1. Ваня")
    print("2. Илюша")
    print("3. Петрович")
    choice = input("Выберите бойца (Введите его номер): ")
    if choice == "1":
        warrior = Vanya
        print("Вы выбрали Ваню")
    elif choice == "2":
        warrior = Ilyusha
        print("Вы выбрали Илюшу")
    elif choice == "3":
        warrior = Petrovich
        print("Вы выбрали Петровича")
    else:
        print("Неверный выбор")
        return None
    return warrior

def change_weapon(warrior):
    print("Имеющееся оружие:")
    print("1. Кладинец")
    print("2. Клык")
    print("3. Кирдык")
    choice = input("Выберите новое оружие (Введите его номер): ")
    if choice == "1":
        warrior.weapon = Kladinec
        print("Вы выбрали Кладинец")
    elif choice == "2":
        warrior.weapon = Fang
        print("Вы выбрали Клык")
    elif choice == "3":
        warrior.weapon = Kirdyk
        print("Вы выбрали Кирдык")
    else:
        print("Неверный выбор")

def damage_calculation(attacking, defending):
    damage = attacking.weapon.damage + attacking.Strength - defending.Defense + random.randint(0, 3) * attacking.luck
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

# Выбор бойца и смена оружия
selected_warrior = change_warrior()
if selected_warrior:
    change_weapon(selected_warrior)

# Запуск боя
fight(selected_warrior, Babay)