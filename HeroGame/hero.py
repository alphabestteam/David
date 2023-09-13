import math


class Hero:
    heal_percent = 0.20  # 10%
    level_up_benefits_percent = 0.50  # 20%
    level_up_threshold = 3

    def __init__(self, name):
        self._name = name
        self._level = 1
        self._damage = 2
        self._hp = 10
        self._max_health = 10
        self._coins = 0
        self.defending = False

    @property
    def defending(self) -> bool:
        return self._defending

    @defending.setter
    def defending(self, is_defending: bool) -> None:
        self._defending = is_defending

    def heal(self) -> None:
        healing = math.ceil(self.hp * Hero.heal_percent)
        if healing > self.max_health:
            self.hp = self.max_health
        else:
            self.hp += healing

    def level_up(self):
        if self.coins >= Hero.level_up_threshold * (self.level+1):
            self.level += 1
            self.damage += math.ceil(self.damage / 10)
            self.max_health += math.ceil(self.damage / 10)
            self.hp = self.max_health
            self.coins -= Hero.level_up_threshold * self.level+1

    def attack(self, monster: object):
        monster.reduce_health(self)

    def reduce_health(self, monster: object) -> None:
        if self.defending:
            self.hp = self.hp - monster.damage * 0.20
            self.defending = False
            print("You dodged 80% of the damage")
        else:
            self.hp = self.hp - monster.damage

    def increase_coins(self, coins: int) -> None:
        self.coins = coins + self.coins

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, value):
        self._coins = value

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, value):
        self._max_health = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
