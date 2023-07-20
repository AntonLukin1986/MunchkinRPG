"""Логика игры, сгруппированная в функциях."""


def create_character(race, klass, level):
    '''Создание персонажа и его экипировка шмотками в зависимости от уровня,
    расы и класса.'''
    from classes import Character
    import items as item
    from items import treasures_for_level

    kwargs = dict()  # для персонажа уровня 0
    if level >= 1:
        if klass == 'Воин':
            weapon = item.SHIELD_UBIQUITY
        elif klass == 'Волшебник':
            weapon = item.STAFF_NAPALM
        elif klass == 'Клирик':
            weapon = item.MACE_SHARPNESS
        treasures_for_level.remove(weapon)
        kwargs['right_arm'] = weapon
    if level >= 2:
        if klass == 'Воин':
            special = item.DOPPLEGANGER
        elif klass == 'Волшебник':
            special = item.POLLYMORPH_POTION
        elif klass == 'Клирик':
            special = item.WISHING_RING
        treasures_for_level.remove(special)
        kwargs['special'] = [special]
    if level == 3:
        if race == 'Эльф':
            stuff = item.HORNY_HELMET
            kwargs['head'] = stuff
        elif race == 'Дварф':
            stuff = item.SHORT_WIDE_ARMOR
            kwargs['body'] = stuff
        elif race == 'Халфлинг':
            stuff = item.STEPLADDER
            kwargs['foot'] = stuff
        treasures_for_level.remove(stuff)
    return Character(race, klass, **kwargs), treasures_for_level


def create_level_events(floors=5, show=True):
    '''Создание карты уровня со случайным расположением событий за дверями.'''
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


def prepare_character_cards(race, klass, level, show=True):
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
    character, treasures_for_level_rest = create_character(
        race, klass, level
    )
    # добавление оставшихся после распределения уровней шмоток и бафов:
    monster_treasures.extend(
        [staff for staff in treasures_for_level_rest
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
