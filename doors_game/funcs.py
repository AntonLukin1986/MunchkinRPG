"""Логика игры, сгруппированная в функциях."""


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
    import cards as item

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
    from cards import (
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
    from cards import PLUG

    card = cards_set.pop(randint(0, len(cards_set)-1))
    if len(cards_set) == 0:  # для сокровищ монстра
        cards_set.extend([PLUG, PLUG, PLUG])  # заглушки
    if show:
        print(card)
    return card


def get_treasure(character, cards_set):
    '''Отрабатывает найденную шмотку при открытии свободной двери или после
    победы над монстром.'''
def get_treasure(character, cards_set):
    '''Отрабатывает найденную шмотку при открытии свободной двери или после
    победы над монстром.'''
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


def get_curse(character, cards_set):
def get_curse(character, cards_set):
    '''Отрабатывает открытие двери с проклятьем.'''
    from classes import Curse
    from cards import CHEAT, NO_ITEM

    card = get_random_card(cards_set)
    if card.kind == 'tights':
        print(CHEAT.after_use)
    if card.kind == 'tights':
        print(CHEAT.after_use)
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
    if (card is Curse and character.klass == 'Клирик'
       and character.use_wishing_ring(lose, value)):
        print('Ты используешь Хотельное кольцо: проклятье отменяется!')
    else:
        setattr(character, lose, value)  # в том числе для Бафа
    if (card is Curse and character.klass == 'Клирик'
       and character.use_wishing_ring(lose, value)):
        print('Ты используешь Хотельное кольцо: проклятье отменяется!')
    else:
        setattr(character, lose, value)  # в том числе для Бафа
    print(character)


def action(character):
    '''Ввод команды игроком и проверка возможности её выполнения.'''
    command = input('Введи команду "attack"/"strong"/"defence"/"boost" ')
    if ((command == 'attack' and character.stamina < 10)
       or (command == 'strong' and character.stamina < 20)):
        print('Недостаточно выносливости!')
        return True
    if command == 'boost' and character.boost == 0:
        print('Бустов пока нет. Применять нечего!')
        return True
    return command


def prepare_monster(character):
    '''Подготавливает монстра для битвы.'''
    from classes import Monster
    from cards import ILLUSION
    from monsters import PLANT

    if character.klass == 'Волшебник' and character.illusion:
        character.illusion = False
        print(ILLUSION.after_use)
        return PLANT
    return Monster('Ужасный монстр!', 1, 'Непобедимый', None)


def wizard_spells(character):
    '''Предоставление волшебнику возможности усмирить монстра вместо боя.'''
    from cards import POLLYMORPH_POTION, FRIENDSHIP_POTION

    morph = (
        '\n' + POLLYMORPH_POTION.description if character.pollymorph else ''
    )
    friend = (
        '\n' + FRIENDSHIP_POTION.description if character.friendship else ''
    )
    print(
        f'У тебя есть специальные заклинания против монстров:{morph}{friend}'
        '\nМожешь воспользоваться, чтобы избежать боя!'
    )
    while ((decision := input('Выбери: «Прогнать монстра» или «Бой»').lower())
           not in ('прогнать монстра', 'бой')):
        pass
    if decision == 'бой':
        return False
    if character.pollymorph:  # в приоритете первым используется Попуморф
        character.pollymorph = False
        print(POLLYMORPH_POTION.after_use)
        return True
    character.friendship = False
    print(FRIENDSHIP_POTION.after_use)
    return None


def start_fight(character):
    '''Запускает битву персонажа с монстром.'''
    monster = prepare_monster(character)
    print(f'За дверью тебя встретил {monster}. Приготовься к битве!')
    if (character.klass == 'Волшебник'
       and character.pollymorph or character.friendship):
        if result := wizard_spells(character) is not False:
            return result  # True или None
    attacks = {'attack': character.attack,
               'strong': character.strong_attack,
               'boost': character.special}
    total_damage = 0
    print('Сила шмоток >>>', character.strength())
    while True:
        print('Нанесено урона >>>', total_damage)
        print('Осталось жизней у монстра >>>', monster.health)
        print('Здоровье >>>', character.health)
        print('Выносливость >>>', character.stamina)
        while (command := action(character)) is True:
            pass
        if command in attacks:
            defence = 0
            damage = attacks[command]()
            total_damage += damage
            monster.health -= damage
        else:
            defence = character.defence()
        if monster.health <= 0:
            print('Ты победил!')
            setattr(character.woman, False)
            setattr(character.only_armor, False)
            return True
        character.health -= monster.attack(defence)
        if character.health <= 0:
            print('Монстр победил!')
            setattr(character.woman, False)
            setattr(character.only_armor, False)
            return False


def monster_get_item(character):
    '''Монстр забирает случайную шмотку при неудачной смывке.'''
    from random import choice
    from cards import NO_ITEM

    item_types = [
        'helmet', 'armor', 'footgear', 'left_arm', 'right_arm',
        'knees', 'tights'
    ]
    if character.klass != 'Воин':
        item_types.remove('knees')
        item_types.remove('tights')
    for type_ in item_types:
        stuff = getattr(character, type_)
        if stuff is False or stuff is NO_ITEM:
            item_types.remove(type_)
    print('Имеющиеся шмотки: ', item_types)
    if item_types:
        lose_type = choice(item_types)
        if lose_type in ('knees', 'tights'):
            new_value = False
        else:
            new_value = NO_ITEM
        print(f'Ты потерял {getattr(character, lose_type)}.')
        setattr(character, lose_type, new_value)
    else:
        print('Так как экипировки у тебя нет, то пришлось сбросить штаны... ')


def run_away(character):
    '''Смывка при поражении в бою с монстром.'''
    from random import randint

    from text import (
        RUN_AWAY, RUN_AWAY_BAD, RUN_AWAY_OK, RUN_AWAY_SO_SO, USE_INVISIBLE
    )

    # DICE_IMAGES = {
    #     0: ..., 1: ..., 2: ..., 3: ..., 4: ..., 5: ..., 6: ...
    # }
    print(RUN_AWAY)
    while input('Введи «Бросаю кубик»: ').lower() != 'бросаю кубик':
        pass
    dice = randint(1, 6)
    # show_image('На кубике выпало...', DICE_IMAGES[dice])
    print(dice)
    if character.chicken:
        dice -= 1
        # show_image('Курица на башке уменьшила на 1 результат твоего броска', DICE_IMAGES[dice])
        print(dice, 'С курицей')
    if dice >= 5:
        print(RUN_AWAY_OK)
    elif dice >= 3:
        print(RUN_AWAY_SO_SO)
        monster_get_item(character)
    else:
        if character.invisibility:
            character.invisibility = False
            print(USE_INVISIBLE)
            # show_image('Зелье невидимости. С газиками!', image)
        else:
            print(RUN_AWAY_BAD)
            return False
    return True
