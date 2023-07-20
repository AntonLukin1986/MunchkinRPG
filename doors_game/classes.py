"""Игровые классы."""  # сделать наследование: Card -> ItemCard...


class Item():
    '''Для создания обычной шмотки.'''
    def __init__(self, kind, value, description, require=None):
        self.kind = kind
        self.value = value
        self.description = description
        self.require = require
        # добавить картинку как свойство?

    def __str__(self):
        return (
            self.description +
            (f'({self.require})' if self.require is not None else '')
        )


class Buff():
    '''Для создания особой способности.'''
    def __init__(self, description, require=None):
        self.description = description
        self.require = require
        # добавить картинку как свойство?

    def __str__(self):
        return (
            self.description +
            (f'({self.require})' if self.require is not None else '')
        )


class Boost():
    '''Для создания разового усилителя.'''
    def __init__(self, description, value):
        self.description = description
        self.value = value
        # добавить картинку как свойство?

    def __str__(self):
        return self.description


class Curse():
    '''Для создания проклятья или специфичной карты-бонуса.'''
    def __init__(self, description, require=None):
        self.description = description
        self.require = require
        # добавить картинку как свойство?
        # можно установить свойство lose: helmet, armor и т.п.

    def __str__(self):
        return self.description


class Character():
    '''Для создания персонажа.'''
    from items import (
        HELM_COURAGE, SLIMY_ARMOR, SANDALS, LONG_POLE, NO_ITEM
    )

    def __init__(
            self, race, klass,
            helmet=HELM_COURAGE,
            armor=SLIMY_ARMOR,
            footgear=SANDALS,
            left_arm=LONG_POLE,
            right_arm=NO_ITEM,
            special=[]
    ):
        self.race = race
        self.klass = klass
        self.helmet = helmet
        self.armor = armor
        self.footgear = footgear
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.knees = 0  # только для воина
        self.tights = 0  # только для воина
        self.title = 0
        self.boost = 0
        self.special = special

    def total_strength(self):
        return sum(
            (self.helmet.value, self.armor.value, self.footgear.value,
             self.left_arm.value, self.right_arm.value,
             self.knees, self.tights, self.title)
        )

    def __str__(self):
        specials = [buff.description for buff in self.special]
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Боевая сила: {self.total_strength()}\n'
            f'Разовый усилитель: {self.boost}\n'
            'Специальные приёмы класса: ' +
            ('\n' + '\n'.join(specials) if self.special else 'нет')
        )
