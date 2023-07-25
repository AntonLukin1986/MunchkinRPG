"""Логика игры, сгруппированная в функциях."""

TIGHTS = '''У тебя в рюкзаке как раз лежат Колготки великанской силы (20 den)
Ты давно хотел их примерять, но настоящим Воинам одевать такое не по статусу...
С помощью Чита ты наплевал на все приличия и с радостью натянул колготы
на свои тощие ляшки: они дают тебе +2 к боевой силе.'''
ILLUSION = '''Ты обнаружил древний свиток с необычным заклинанием. Следующий
монстр, с которым ты столкнёшься, будет заменён на Огорошенную траву.'''
GOD = '''Внезапно таинственная трансцендентная сущность вмешивается в
обычный порядок вещей и ты непостижимым образом проскакиваешь через
следующий уровень.'''


def create_events(floors=5, show=True):
    '''Создание схемы уровня со случайным расположением событий за дверями.'''
    from random import randint

    level_events = list()
    for _ in range(floors):
        level_events.append([])
    for floor in level_events:
        events = ['monster', 'free', 'curse']
        for _ in range(3):
            floor.append(events.pop(randint(0, len(events) - 1)))
    if show:
        for floor in level_events:
            print(floor)
    return level_events


def create_character(race, klass, level):
    '''Создание персонажа и его экипировка в зависимости от уровня, расы
    и класса. Возвращает не использованные шмотки.'''
    from classes import Cleric, Warrior, Wizard
    import items as item

    klasses_set = {'Воин': Warrior, 'Волшебник': Wizard, 'Клирик': Cleric}
    kwargs = {  # экипировка при уровне персонажа 0
        'helmet': item.HELM_COURAGE,
        'armor': item.SLIMY_ARMOR,
        'footgear': item.SANDALS,
        'left_arm': item.LONG_POLE,
        'right_arm': item.NO_ITEM
    }
    if level >= 1:
        if klass == 'Воин':
            weapon = item.SHIELD_UBIQUITY
        elif klass == 'Волшебник':
            weapon = item.STAFF_NAPALM
        elif klass == 'Клирик':
            weapon = item.MACE_SHARPNESS
        item.treasures_for_level.remove(weapon)
        kwargs['right_arm'] = weapon  # в левой руке базовое оружие
    if level >= 2:
        if klass == 'Воин':
            special = item.DOPPLEGANGER
            kwargs['doppleganger'] = True
        elif klass == 'Волшебник':
            special = item.POLLYMORPH_POTION
            kwargs['pollymorph'] = True
        elif klass == 'Клирик':
            special = item.WISHING_RING
            kwargs['wishing_ring'] = 1
        item.treasures_for_level.remove(special)
    if level == 3:
        if race == 'Эльф':
            stuff = item.HORNY_HELMET
            kwargs['helmet'] = stuff
        elif race == 'Дварф':
            stuff = item.SHORT_WIDE_ARMOR
            kwargs['armor'] = stuff
        elif race == 'Халфлинг':
            stuff = item.STEPLADDER
            kwargs['footgear'] = stuff
        item.treasures_for_level.remove(stuff)
    return klasses_set[klass](race, **kwargs), item.treasures_for_level


def prepare_game(race, klass, level, show=True):
    '''Подготовка персонажа и стартовых наборов карт.'''
    from items import (
        door_cards_base, door_cards_specific,
        monster_treasures_base, monster_treasures_specific
    )

    door_cards = door_cards_base
    door_cards.extend(
        [card for card in door_cards_specific if card.require == klass]
    )
    monster_treasures = monster_treasures_base
    monster_treasures.extend(
        [staff for staff in monster_treasures_specific if staff.require
         in (race, klass)]
    )
    character, rest_treasures_for_level = create_character(
        race, klass, level
    )
    # добавление шмоток и бафов, оставшихся после распределения уровней
    monster_treasures.extend(
        [staff for staff in rest_treasures_for_level
         if staff.require in (race, klass)]
    )
    if show:
        print(f'Уровень {level} |', character)
        print('=' * 10)
        print(f'Количество {len(monster_treasures)}:')
        print(*monster_treasures, sep='\n')
        print('*' * 10)
        print(f'Количество {len(door_cards)}:')
        print(*door_cards, sep='\n')
        print('*' * 10)
    return character, monster_treasures, door_cards


def weak_or_strong_arm(char, weak=True):
    '''Определяет, в какой руке самое слабое/сильное оружие.'''
    if weak:
        return (
            'left_arm' if
            char.left_arm.value <= char.right_arm.value else 'right_arm'
        )
    return (
        'left_arm' if
        char.left_arm.value >= char.right_arm.value else 'right_arm'
    )


def get_random_card(cards_set, show=True):
    '''Перемещает случайную карту из набора в игру.'''
    from random import randint

    card = cards_set.pop(randint(0, len(cards_set)-1))
    if show:
        print(card)
    return card


def free_or_monster_event(character, cards_set):
    '''Отрабатывает открытие свободной двери или двери с монстром.'''
    from classes import Boost, Buff, Item

    card = get_random_card(cards_set)
    if isinstance(card, Boost):
        character.boost += card.value
    elif isinstance(card, Item):
        if card.kind == 'arm':
            # определяется, в какой руке самое слабое оружие
            card.kind = weak_or_strong_arm(character)
        have_item = getattr(character, card.kind)
        if have_item.value <= card.value:
            setattr(character, card.kind, card)
            print(f'{have_item} заменено на {card}!')
    elif isinstance(card, Buff):
        setattr(character, card.kind, True)
    print(character)


def curse_event(character, cards_set):
    '''Отрабатывает открытие двери с проклятьем.'''
    from items import NO_ITEM

    card = get_random_card(cards_set)
    if card.kind == 'doom':
        print('Поймал утку. Откатись на первый уровень.')
        return
    if card.kind == 'lose':
        if card.lose not in ('min_arm', 'max_arm'):
            lose = card.lose
        else:
            weak_arm = weak_or_strong_arm(character)
            strong_arm = weak_or_strong_arm(character, False)
            if (card.lose == 'min_arm' and getattr(character, weak_arm)
               is not NO_ITEM):
                lose = weak_arm
            else:
                lose = strong_arm
        value = NO_ITEM
    else:
        lose = card.kind
        value = True
    (setattr(character, lose, value)
     if character.klass != 'Клирик' or character.use_wishing_ring(lose, value)
     else print('Ты используешь Хотельное кольцо: проклятье отменяется!'))
    print(character)
