#Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print(f'Боец наносит удар мечом')

class Bow(Weapon):
    def attack(self):
        print(f'Боец наноcит удар из лука')

class Monster():
    def loss(self):
        print('Монстр побежден')

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon
    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        weapon_type = ''
        if isinstance(weapon, Sword):
            weapon_type = 'меч'
        elif isinstance(weapon, Bow):
            weapon_type = 'лук'
        print(f'Боец выбирает {weapon_type}')

    def attack(self, monster: Monster):
        self.weapon.attack()
        monster.loss()


s = Sword()
b = Bow()
f = Fighter(s)
m = Monster()

f.change_weapon(s)
f.attack(m)
f.change_weapon(b)
f.attack(m)
