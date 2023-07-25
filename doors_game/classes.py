"""Игровые классы."""


class Card():
    '''Базовый класс карты.'''
    def __init__(self, description, require=None, image=None):
        self.description = description
        self.require = require
        self.image = image

    def __str__(self):
        return (
            self.description + (f'({self.require})' if self.require else '')
        )


class Item(Card):
    '''Карта носимой шмотки. Её категория и значение силы.'''
    def __init__(self, description, kind, value, require=None, image=None):
        super().__init__(description, require, image)
        self.kind = kind
        self.value = value


class Buff(Card):
    '''Карта особой способности класса или расы. Может быть универсальной.'''
    def __init__(self, description, kind, require=None, image=None):
        super().__init__(description, require, image)
        self.kind = kind


class Boost(Card):
    '''Карта разового усилителя. Его значение.'''
    def __init__(self, description, value, require=None, image=None):
        super().__init__(description, require, image)
        self.value = value


class Curse(Card):
    '''Карта проклятья.'''
    def __init__(self, description, kind, lose=None, require=None, image=None):
        super().__init__(description, require, image)
        self.kind = kind
        self.lose = lose


class Character():
    '''Базовый класс персонажа.'''
    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm):
        self.race = race
        self.helmet = helmet
        self.armor = armor
        self.footgear = footgear
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.boost = 0  # разовый усилитель
        self.title = False  # впечатляющий титул
        self.invisibility = False  # зелье Невидимости
        self.only_armor = False  # проклятье Кривое зеркало
        self.woman = False  # проклятье Смена пола

    def items_strength(self):
        return sum(
                (self.helmet.value, self.armor.value, self.footgear.value,
                 self.left_arm.value, self.right_arm.value,
                 3 if self.title else 0)
            )

    def strength(self):
        if self.only_armor:
            strength = self.armor.value
        else:
            strength = self.items_strength()
        if self.woman:
            return strength - 5
        return strength

    def __str__(self):
        return 'Базовый класс.'


class Warrior(Character):
    '''Класс Воин.'''
    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm,
                 doppleganger=False):
        super().__init__(race, helmet, armor, footgear, left_arm, right_arm)
        self.klass = 'Воин'
        self.doppleganger = doppleganger
        self.knees = False
        self.tights = False

    def items_strength(self):
        return sum(
                (self.helmet.value, self.armor.value, self.footgear.value,
                 self.left_arm.value, self.right_arm.value,
                 3 if self.title else 0,
                 2 if self.knees else 0, 2 if self.tights else 0)
            )

    def __str__(self):
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Наколенники: {self.knees}\nКолготы: {self.tights}\n'
            f'Боевая сила: {self.strength()}\n'
            f'Разовый усилитель: {self.boost}\n'
            f'Бафы:\nЗелье невидимости {self.invisibility}\n'
            f'Дупельгангер {self.doppleganger}'
        )


class Wizard(Character):
    '''Класс Волшебник.'''
    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm,
                 pollymorph=False):
        super().__init__(race, helmet, armor, footgear, left_arm, right_arm)
        self.klass = 'Волшебник'
        self.pollymorph = pollymorph
        self.illusion = False
        self.friendship = False

    def __str__(self):
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Боевая сила: {self.strength()}\n'
            f'Разовый усилитель: {self.boost}\n'
            f'Бафы:\nЗелье невидимости {self.invisibility}\n'
            f'Морок {self.illusion}\n'
            f'Попуморф {self.pollymorph}\n'
            f'Зелье дружбы {self.friendship}'
        )


class Cleric(Character):
    '''Класс Клирик.'''
    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm,
                 wishing_ring=0):
        super().__init__(race, helmet, armor, footgear, left_arm, right_arm)
        self.klass = 'Клирик'
        self.wishing_ring = wishing_ring
        self.god = False

    def use_wishing_ring(self, lose, value):
        '''Использовать Хотельное кольцо для отмены проклятья.'''
        if (self.wishing_ring and getattr(self, lose) != value
           and int(input('Использовать Хотельное кольцо? 0 или 1 '))):
            self.wishing_ring -= 1
            return False
        return True

    def __str__(self):
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Боевая сила: {self.strength()}\n'
            f'Разовый усилитель: {self.boost}\n'
            f'Бафы:\nЗелье невидимости {self.invisibility}\n'
            f'Хотельное кольцо {self.wishing_ring}'
        )
