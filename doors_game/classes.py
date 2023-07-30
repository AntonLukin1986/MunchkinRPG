"""Игровые классы."""
from random import randint
from text import USE_RING


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
    def __init__(
            self, description, kind, after_use=None, require=None, image=None
    ):
        super().__init__(description, require, image)
        self.kind = kind
        self.after_use = after_use


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
    DEFAULT_ATTACK = 10
    STRONG_ATTACK_RATIO = 2.5  # коэффициент для сильной атаки
    MIN_RATIO = 0.8  # коэффициенты минимального и максимального
    MAX_RATIO = 1.2  # пределов случайной величины для урона и защиты
    DEFAULT_DEFENCE = 10
    stamina = 20  # выносливость
    health = 100

    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm):
        self.race = race
        self.helmet = helmet
        self.armor = armor
        self.footgear = footgear
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.boost = 0  # разовый усилитель
        self.title = False  # Впечатляющий титул
        self.invisibility = False  # Зелье невидимости
        self.only_armor = False  # проклятье Кривое зеркало
        self.woman = False  # проклятье Смена пола
        self.chicken = False  # проклятье Курица на башке

    def items_strength(self):
        '''Рассчитывает силу шмоток персонажа.'''
        return sum(
            (self.helmet.value, self.armor.value, self.footgear.value,
             self.left_arm.value, self.right_arm.value,
             3 if self.title else 0)
        )

    def strength(self):
        '''Рассчитывает итоговую силу персонажа с учётом проклятий.'''
        if self.only_armor:
            strength = self.armor.value
        else:
            strength = self.items_strength()
        if self.woman:
            return strength - 5
        return strength

    def attack(self):
        '''Обычная атака противника.'''
        attack = self.DEFAULT_ATTACK + self.strength()
        value = randint(
            round(self.MIN_RATIO * attack), round(self.MAX_RATIO * attack)
        )
        self.stamina -= 10
        print(f'Ты нанёс противнику урон, равный {value}.')
        return value

    def strong_attack(self):
        '''Мощная атака противника.'''
        attack = (
            (self.DEFAULT_ATTACK + self.strength()) * self.STRONG_ATTACK_RATIO
        )
        value = randint(
            round(self.MIN_RATIO * attack), round(self.MAX_RATIO * attack)
        )
        self.stamina -= 20
        print(f'Мощная атака нанесла противнику урон, равный {value}.')
        return value

    def defence(self):
        '''Блокирование урона от атаки противника.'''
        defence = self.DEFAULT_DEFENCE + self.strength()
        value = randint(
            round(self.MIN_RATIO * defence), round(self.MAX_RATIO * defence)
        )
        self.stamina += 10
        print(f'Защищаясь, ты блокировал {value} урона от монстра.')
        return value

    def special(self):
        '''Специальная атака с использованием буста.'''
        print(
            f'Дальнобойная атака бустами нанесла монстру {self.boost} урона.'
        )
        self.stamina += 10
        return self.boost

    def __str__(self):
        return 'Базовый класс.'


class Warrior(Character):
    '''Класс Воин.'''
    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm,
                 knees=False):
        super().__init__(race, helmet, armor, footgear, left_arm, right_arm)
        self.klass = 'Воин'
        self.knees = knees
        self.doppleganger = False
        self.tights = False

    def items_strength(self):
        '''Рассчитывает силу шмоток персонажа. Переопределён от родительского с
        добавлением колгот и наколенников. Учитывается Дупельгангер.'''
        return sum(
                (self.helmet.value, self.armor.value, self.footgear.value,
                 self.left_arm.value, self.right_arm.value,
                 3 if self.title else 0,
                 2 if self.knees else 0, 2 if self.tights else 0)
            ) * (2 if self.doppleganger else 1)

    def __str__(self):
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Наколенники: {self.knees}\nКолготы: {self.tights}\n'
            f'Титул: {self.title}\n'
            f'Боевая сила: {self.strength()}\n'
            f'Разовый усилитель: {self.boost}\n'
            f'Бафы:\nЗелье невидимости {self.invisibility}\n'
            f'Дупельгангер {self.doppleganger}'
        )


class Wizard(Character):
    '''Класс Волшебник.'''
    def __init__(self, race, helmet, armor, footgear, left_arm, right_arm,
                 friendship=False):
        super().__init__(race, helmet, armor, footgear, left_arm, right_arm)
        self.klass = 'Волшебник'
        self.friendship = friendship
        self.pollymorph = False
        self.illusion = False

    def __str__(self):
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Титул: {self.title}\n'
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
        if self.wishing_ring and getattr(self, lose) != value:
            while (decision := input(USE_RING).lower()) not in ('да', 'нет'):
                pass
            if decision == 'да':
                self.wishing_ring -= 1
                return True
        return False

    def __str__(self):
        return (
            f'{self.race}-{self.klass}\n'
            f'Вооружение:\n{self.helmet}\n{self.armor}\n{self.footgear}\n'
            f'{self.left_arm}\n{self.right_arm}\n'
            f'Титул: {self.title}\n'
            f'Боевая сила: {self.strength()}\n'
            f'Разовый усилитель: {self.boost}\n'
            f'Бафы:\nЗелье невидимости {self.invisibility}\n'
            f'Хотельное кольцо {self.wishing_ring}\n'
            f'GOD {self.god}'
        )


class Monster():
    '''Базовый класс монстра.'''
    DEFAULT_ATTACK = 10
    MIN_RATIO = 0.8  # коэффициенты минимального и максимального
    MAX_RATIO = 1.2  # пределов случайной величины урона
    health = 10

    def __init__(self, name, level, detail, image):
        self.name = name
        self.level = level
        self.detail = detail
        self.image = image

    def strength(self):
        '''Боевая сила монстра.'''
        return self.DEFAULT_ATTACK * self.level

    def attack(self, defence):
        '''Наносимый монстром урон с учётом его боевой силы и защиты игрока.'''
        strength = self.strength()
        attack = randint(
            round(self.MIN_RATIO * strength), round(self.MAX_RATIO * strength)
        )
        print(f'{self.name} атаковал с силой {attack}')
        damage = 0 if defence >= attack else attack - defence
        print(f'Блокировано {defence} урона от атаки монстра.\n'
              f'Получено повреждений {damage}')
        return damage

    def __str__(self):
        return f'{self.name} Уровень {self.level}'
