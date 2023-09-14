import random


def init_monster_level(hero_level):
    return random.choice([hero_level - 1, hero_level, hero_level + 1])


class Monster:
    monster_damage = 2
    monster_health = 6
    level_buff_percent = 0.50

    def __init__(self, name, hero_level):
        self._name = name
        self._level = init_monster_level(hero_level)
        self._hp = Monster.monster_health + (self.level * Monster.level_buff_percent)
        self._damage = Monster.monster_damage + (self.level * Monster.level_buff_percent)

    def attack(self, hero: object):
        hero.reduce_health(self)

    def reduce_health(self, hero: object) -> None:
        self.hp = self.hp - hero.damage
        if self.hp < 0:
            self.hp = 0

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        self._damage = value

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
