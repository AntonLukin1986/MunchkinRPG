"""Игровые классы."""
from random import randint

from doors_game.text import (
    BASE_STRENGTH, CHICKEN, COMBAT_STRENGTH, DUPPEL, FRIENDSHIPcol,
    ILLUSIONcol, INVISIBILITY, MIRROR, NAME, POLLYMORPHcol, RING,
    USE_RING, WOMAN
)


class Card():
    '''Базовый класс карты.'''
    def __init__(self, description, require=None, image=None):
        self.description = description
        self.require = require
        self.image = image

    def __str__(self):
        return self.description


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
    DEFAULT_POWER = 10
    STRONG_ATTACK_RATIO = 2  # коэффициент для сильной атаки
    MIN_STRONG_RATIO = 0.9  # коэффициент мин. предела тяж. атаки
    MAX_STRONG_RATIO = 1.3  # коэффициент макс. предела тяж. атаки
    MIN_RATIO = 0.8  # коэффициенты минимального и максимального
    MAX_RATIO = 1.2  # пределов случайной величины для урона и защиты
    stamina = 10  # выносливость
    health = 100

    def __init__(
        self, race, rank, helmet, armor, footgear, left_arm, right_arm
    ):
        self.race = race
        if self.race == 'Эльф':
            self.DEFAULT_ATTACK = 8
            self.health = 110
        elif self.race == 'Дварф':
            self.DEFAULT_ATTACK = 12
            self.health = 90
        # Халфлинг - здоровье и атака по дефолту
        self.rank = rank
        self.helmet = helmet
        self.armor = armor
        self.footgear = footgear
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.boost = 0  # дальнобойная атака
        self.title = False  # Впечатляющий титул
        self.invisibility = False  # Зелье невидимости
        self.only_armor = False  # проклятье Кривое зеркало
        self.woman = False  # проклятье Смена пола
        self.chicken = False  # проклятье Курица на башке

    def items_strength(self):
        '''Рассчитывает силу шмоток персонажа с учётом проклятья.'''
        if self.only_armor:
            return self.armor.value
        return sum(
            (self.helmet.value, self.armor.value, self.footgear.value,
             self.left_arm.value, self.right_arm.value)
        )

    def strength(self):
        '''Рассчитывает итоговую силу персонажа с учётом проклятья и титула.'''
        strength = 3 if self.title else 0
        strength += self.items_strength()
        strength += self.DEFAULT_POWER
        if self.woman:
            return strength - 5
        return strength

    def attack(self):
        '''Обычная атака противника.'''
        attack = self.strength()
        value = randint(
            round(self.MIN_RATIO * attack), round(self.MAX_RATIO * attack)
        )
        self.stamina -= 10
        print(f'Противнику нанесён урон {value}')
        return value

    def strong_attack(self):
        '''Мощная атака противника.'''
        attack = self.strength() * self.STRONG_ATTACK_RATIO
        value = randint(
            round(self.MIN_STRONG_RATIO * attack),
            round(self.MAX_STRONG_RATIO * attack)
        )
        self.stamina -= 20
        print(f'В результате тяжёлой атаки противнику нанесён урон {value}')
        return value

    def boost_attack(self):
        '''Дальнобойная атака бустами.'''
        print(f'Дальнобойная атака нанесла монстру {self.boost} урона')
        self.stamina += 10
        return self.boost

    def defence(self):
        '''Блокирование урона от атаки противника.'''
        defence = self.strength()
        self.stamina += 10
        if defence < 0:
            return 0
        return randint(
            round(self.MIN_RATIO * defence),
            round(self.MAX_RATIO * defence)
        )

    def show_weapon(self):
        '''Отображает надетое вооружение персонажа и титул при наличии.'''
        return (
            ('Реально впечатляющий титул [+3]\n' if self.title else '') +
            f'\tВооружение:\nГоловняк → {self.helmet}\nБроник → {self.armor}\n'
            f'Обувка → {self.footgear}\nЛевая рука → {self.left_arm}\n'
            f'Правая рука → {self.right_arm}\n'
        )

    def show_curses(self):
        '''Отображает действующие проклятия.'''
        return (
            ('\nДействующие проклятия:' +
             (f' {MIRROR}' if self.only_armor else '') +
             (f' {CHICKEN}' if self.chicken else '') +
             (f' {WOMAN}' if self.woman else ''))
            if self.only_armor or self.woman or self.chicken else ''
        )

    def show_boost(self):
        '''Отображает бусты и Зелье невидимости при наличии.'''
        return (
            (f'\nДальнобойная атака: {self.boost}' if self.boost else '') +
            (f'\n{INVISIBILITY}' if self.invisibility else '')
        )

    def show_health(self):
        '''Отображает здоровье персонажа.'''
        return f'\nЗдоровье: {self.health}'

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
        dopple = 2 if self.doppleganger else 1
        if self.only_armor:
            return self.armor.value * dopple
        return sum(
                (self.helmet.value, self.armor.value, self.footgear.value,
                 self.left_arm.value, self.right_arm.value,
                 2 if self.knees else 0, 2 if self.tights else 0)
            ) * dopple

    def show_unique(self):
        '''Отображает уникальные шмотки для Воина.'''
        return (
            ('Колени → Шипастые коленки [+2]\n' if self.knees else '') +
            ('Бёдра → Колготы великанской силы [+2]\n' if self.tights else '')
            + (f'{DUPPEL} (увеличивает силу шмоток в 2 раза)'
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
            self.line() + BASE_STRENGTH.format(self.DEFAULT_POWER) + '\n' +
            self.show_weapon() + self.show_unique() +
            COMBAT_STRENGTH.format(self.strength()) +
            self.show_health() + self.show_boost() + self.show_curses()
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
            ('\nЧародейство:' +
             (f' {ILLUSIONcol}' if self.illusion else '') +
             (f' {POLLYMORPHcol}' if self.pollymorph else '') +
             (f' {FRIENDSHIPcol}' if self.friendship else ''))
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
            self.line() + BASE_STRENGTH.format(self.DEFAULT_POWER) + '\n' +
            self.show_weapon() + COMBAT_STRENGTH.format(self.strength()) +
            self.show_health() + self.show_boost() + self.show_unique() +
            self.show_curses()
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
            self.line() + BASE_STRENGTH.format(self.DEFAULT_POWER) + '\n' +
            self.show_weapon() +
            COMBAT_STRENGTH.format(self.strength()) +
            self.show_health() + self.show_boost() +
            (f'\n{RING} {self.wishing_ring} шт.'
             if self.wishing_ring else '') + self.show_curses()
        )


class Monster():
    '''Базовый класс монстра.'''
    DEFAULT_ATTACK = 10
    MIN_RATIO = 0.8  # коэффициенты минимального и максимального
    MAX_RATIO = 1.2  # пределов случайной величины урона
    health = 100

    def __init__(self, name, level, detail, image):
        self.name = name
        self.level = level
        self.detail = detail
        self.image = image

    def strength(self):
        '''Боевая сила монстра.'''
        return round(self.DEFAULT_ATTACK * self.level)

    def attack(self, defence):
        '''Наносимый монстром урон с учётом его боевой силы и защиты игрока.'''
        strength = self.strength()
        attack = randint(
            round(self.MIN_RATIO * strength), round(self.MAX_RATIO * strength)
        )
        print(f'{self.name} атаковал с силой {attack}')
        damage = 0 if defence >= attack else attack - defence
        print(f'Блокировано {defence} урона от атаки противника\n'
              f'Получено повреждений {damage}')
        return damage

    def __str__(self):
        return f'{self.name} (боевая сила {self.strength()})'
