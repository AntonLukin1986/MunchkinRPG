"""Игровые классы."""
from random import randint

from text import (
    COMBAT_STRENGTH, DUPPEL, FRIENDSHIPcol, ILLUSIONcol, INVISIBILITY, MIRROR,
    NAME, POLLYMORPHcol, RING, USE_RING, WOMAN
)


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

    def __init__(
        self, race, rank, helmet, armor, footgear, left_arm, right_arm
    ):
        self.race = race
        self.rank = rank
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
             self.left_arm.value, self.right_arm.value)
        )

    def strength(self):
        '''Рассчитывает итоговую силу персонажа с учётом проклятий
        и наличия титула.'''
        strength = 3 if self.title else 0
        if self.only_armor:
            strength += self.armor.value
        else:
            strength += self.items_strength()
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
        print(f'Противнику нанесён урон {value}.')
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
        print(f'Мощная атака нанесла противнику урон {value}.')
        return value

    def boost_attack(self):
        '''Дальнобойная атака бустами.'''
        print(f'Дальнобойная атака нанесла монстру {self.boost} урона. '
              'Восстановлено 10 выносливости.')
        self.stamina += 10
        return self.boost

    def defence(self):
        '''Блокирование урона от атаки противника.'''
        defence = self.DEFAULT_DEFENCE + self.strength()
        value = randint(
            round(self.MIN_RATIO * defence), round(self.MAX_RATIO * defence)
        )
        self.stamina += 10
        print(f'Защита блокировала {value} урона от монстра.'
              'Восстановлено 10 выносливости.')
        return value

    def show_weapon(self):
        '''Отображает надетое вооружение персонажа и титул при наличии.'''
        return (
            'Реально впечатляющий титул [+3]\n' if self.title else ''
            f'\tВооружение:\nГоловняк → {self.helmet}\nБроник → {self.armor}\n'
            f'Обувка → {self.footgear}\nЛевая рука → {self.left_arm}\n'
            f'Правая рука → {self.right_arm}\n'
        )

    def show_curses(self):
        '''Отображает проклятия следующего боя.'''
        return (
            ('Действующие проклятия:' +
             (f' {MIRROR}' if self.only_armor else '') +
             (f' {WOMAN}' if self.woman else '') + '\n')
            if self.only_armor or self.woman else ''
        )

    def show_boost(self):
        '''Отображает бусты и Зелье невидимости при наличии.'''
        return (
            f'Дальнобойные бусты: {self.boost}\n' if self.boost else ''
            f'{INVISIBILITY}\n' if self.invisibility else ''
        )

    def __str__(self):
        return f'{NAME} | Ранг: {self.rank} | Раса: {self.race} | '


class Warrior(Character):
    '''Класс Воин.'''
    def __init__(self, race, rank, helmet, armor, footgear, left_arm,
                 right_arm, knees=False):
        super().__init__(race, rank, helmet, armor, footgear, left_arm,
                         right_arm)
        self.klass = 'Воин'
        self.knees = knees
        self.doppleganger = False
        self.tights = False

    def items_strength(self):
        '''Рассчитывает силу шмоток персонажа. Переопределён от родительского
        с добавлением колгот и наколенников. Учитывает Дупельгангер.'''
        return sum(
                (self.helmet.value, self.armor.value, self.footgear.value,
                 self.left_arm.value, self.right_arm.value,
                 2 if self.knees else 0, 2 if self.tights else 0)
            ) * (2 if self.doppleganger else 1)

    def show_unique(self):
        '''Отображает уникальные шмотки для Воина.'''
        return (
            ('Колени → Шипастые коленки [+2]\n' if self.knees else '') +
            ('Бёдра → Колготы [+2]\n' if self.tights else '') +
            (f'{DUPPEL} (увеличивает силу шмоток в 2 раза)\n'
             if self.doppleganger else '')
        )

    def line(self):
        '''Отображает сплошную линию.'''
        return (
            '—' * (len(super().__str__() + f'Класс: {self.klass}\n') - 14) +
            '\n'  # 14 это компенсация длины окрашеного имени персонажа
        )

    def __str__(self):
        return (
            self.line() + super().__str__() + f'Класс: {self.klass}\n' +
            self.line() + self.show_weapon() + self.show_unique() +
            COMBAT_STRENGTH.format(self.strength()) + self.show_curses() +
            self.show_boost()
        )


class Wizard(Character):
    '''Класс Волшебник.'''
    def __init__(self, race, rank, helmet, armor, footgear, left_arm,
                 right_arm, friendship=False):
        super().__init__(race, rank, helmet, armor, footgear, left_arm,
                         right_arm)
        self.klass = 'Волшебник'
        self.friendship = friendship
        self.pollymorph = False
        self.illusion = False

    def show_unique(self):
        '''Отображает уникальные способности Волшебника.'''
        return (
            ('Чародейство:' +
             (f' {ILLUSIONcol}' if self.illusion else '') +
             (f' {POLLYMORPHcol}' if self.pollymorph else '') +
             (f' {FRIENDSHIPcol}' if self.friendship else '') + '\n')
            if self.illusion or self.pollymorph or self.friendship else ''
        )

    def line(self):
        '''Отображает сплошную линию.'''
        return (
            '—' * (len(super().__str__() + f'Класс: {self.klass}\n') - 14) +
            '\n'  # 14 это компенсация длины окрашеного имени персонажа
        )

    def __str__(self):
        return (
            self.line() + super().__str__() + f'Класс: {self.klass}\n' +
            self.line() + self.show_weapon() + self.show_curses() +
            COMBAT_STRENGTH.format(self.strength()) + self.show_boost()
            + self.show_unique()
        )


class Cleric(Character):
    '''Класс Клирик.'''
    def __init__(self, race, rank, helmet, armor, footgear, left_arm,
                 right_arm, wishing_ring=0):
        super().__init__(race, rank, helmet, armor, footgear, left_arm,
                         right_arm)
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

    def line(self):
        '''Отображает сплошную линию.'''
        return (
            '—' * (len(super().__str__() + f'Класс: {self.klass}\n') - 14) +
            '\n'  # 14 это компенсация длины окрашеного имени персонажа
        )

    def __str__(self):
        return (
            self.line() + super().__str__() + f'Класс: {self.klass}\n' +
            self.line() + self.show_weapon() + self.show_curses() +
            COMBAT_STRENGTH.format(self.strength()) + self.show_boost() +
            (f'{RING} {self.wishing_ring} шт.\n'
             if self.wishing_ring else '')
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
