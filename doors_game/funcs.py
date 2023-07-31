"""Логика игры, сгруппированная в функциях."""


def show_image(image_name: str, description: str) -> None:
    """Показать окно с картинкой."""
    import re
    from pathlib import Path
    import tkinter as tk

    IMAGES_DIR = Path(__file__).resolve().parent / 'images/'
    NO_IMAGE = ('Здесь должна была быть\nкрасивая картинка,\n'
                'но её украли гномы...')

    window = tk.Tk()
    window.title('Манчкин RPG')
    window.resizable(False, False)  # без регулировки размера
    window.attributes('-topmost', True)  # на передний план
    frame_1 = tk.Frame(master=window, bg='green')  # задний фон вокруг
    frame_1.pack(fill=tk.X)                        # следующего лэйбла
    label = tk.Label(
        master=frame_1,
        text=f'{description}',
        font=('Comic Sans MS', 16, 'italic'),
        foreground='white',
        background='green'
    )
    label.pack()
    try:
        image = tk.PhotoImage(file=Path(IMAGES_DIR, f'{image_name}.png'))
    except tk.TclError:
        label = tk.Label(
            master=window,
            text=NO_IMAGE,
            font='Gabriola 20'
        )
    else:
        label = tk.Label(master=window, image=image)
    label.pack()
    # --- отображение окна по центру экрана ---
    window.update_idletasks()
    w, h, sx, sy = map(int, re.split('x|\+', window.winfo_geometry()))
    sw = (window.winfo_rootx() - sx) * 2 + w
    sh = (window.winfo_rooty() - sy) + (window.winfo_rootx() - sx) + h
    sx = (window.winfo_screenwidth() - sw) // 2
    sy = (window.winfo_screenheight() - sh) // 2
    window.wm_geometry('+%d+%d' % (sx, sy))
    # --- окончание ---
    frame_2 = tk.Frame(master=window, bg='yellow')
    frame_2.pack(fill=tk.X)
    label = tk.Label(
        master=frame_2,
        text='Для продолжения закрой это окно',
        font='Calibri 14',
        foreground='black',
        background='yellow'
    )
    label.pack()
    window.mainloop()


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


def create_character(race, klass, rank):
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
    if rank >= 1:
        if klass == 'Воин':
            weapon = item.SHIELD_UBIQUITY
        elif klass == 'Волшебник':
            weapon = item.STAFF_NAPALM
        elif klass == 'Клирик':
            weapon = item.MACE_SHARPNESS
        item.treasures_for_rank.remove(weapon)
        kwargs['right_arm'] = weapon  # в левой руке базовое оружие
    if rank >= 2:
        if klass == 'Воин':
            special = item.SPIKY_KNEES
            kwargs['knees'] = True
        elif klass == 'Волшебник':
            special = item.FRIENDSHIP_POTION
            kwargs['friendship'] = True
        elif klass == 'Клирик':
            special = item.WISHING_RING
            kwargs['wishing_ring'] = 1
        item.treasures_for_rank.remove(special)
    if rank == 3:
        if race == 'Эльф':
            stuff = item.HORNY_HELMET
            kwargs['helmet'] = stuff
        elif race == 'Дварф':
            stuff = item.SHORT_WIDE_ARMOR
            kwargs['armor'] = stuff
        elif race == 'Халфлинг':
            stuff = item.STEPLADDER
            kwargs['footgear'] = stuff
        item.treasures_for_rank.remove(stuff)
    return klasses_set[klass](race, rank, **kwargs), item.treasures_for_rank


def prepare_game(race, klass, rank, show=True):
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
    character, rest_treasures_for_rank = create_character(
        race, klass, rank
    )
    # добавление шмоток и бафов, оставшихся после распределения уровней
    monster_treasures.extend(
        [staff for staff in rest_treasures_for_rank
         if staff.require in (race, klass)]
    )
    print(character)
    if show:
        print('----- prepare_game func -----')
        print(f'Всего {len(monster_treasures)}:')
        print(*monster_treasures, sep='\n')
        print('*' * 10)
        print(f'Всего {len(door_cards)}:')
        print(*door_cards, sep='\n')
        print('*' * 10)
        print('----- end prepare_game func -----\n')
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
        show_image(card.image, card)
        print(card)
    return card


def get_treasure(character, cards_set):
    '''Отрабатывает найденную шмотку при открытии свободной двери или после
    победы над монстром.'''
    from cards import WISHING_RING
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
        if card is WISHING_RING:
            character.wishing_ring += 1
        else:
            setattr(character, card.kind, True)
    print(character)


def get_curse(character, cards_set):
    '''Отрабатывает открытие двери с проклятьем.'''
    from classes import Curse
    from cards import CHEAT, NO_ITEM

    card = get_random_card(cards_set)
    if card.kind == 'cheat':
        print(CHEAT.after_use)
        show_image(
            'curses/tights', 'Колготы великанской силы: +2 к боевой силе!'
        )
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
    if (isinstance(card, Curse) and character.klass == 'Клирик'
       and character.use_wishing_ring(lose, value)):
        print('Ты используешь Хотельное кольцо: проклятье отменяется!')
    else:
        setattr(character, lose, value)  # в том числе для Бафа
    print(character)


def fight_command(character):
    '''Ввод команды игроком и проверка возможности её выполнения.'''
    from text import COMBAT, COMBAT_CHECK

    confirmed = False
    while not confirmed:
        while (command := input(COMBAT).lower()) not in COMBAT_CHECK:
            pass
        if ((command == 'атака' and character.stamina < 10)
           or (command == 'тяжёлая атака' and character.stamina < 20)):
            print('Недостаточно выносливости!')
        elif command == 'бусты' and character.boost == 0:
            print('Бустов пока нет. Применять нечего!')
        else:
            confirmed = True
    return command


def prepare_monster(character):
    '''Подготавливает монстра для битвы.'''
    from classes import Monster
    from cards import ILLUSION
    from monsters import PLANT

    if character.klass == 'Волшебник' and character.illusion:
        character.illusion = False
        print(ILLUSION.after_use)
        show_image(PLANT.image, PLANT.detail)
        return PLANT
    return Monster('Ужасный монстр!', 100, 'Непобедимый', None)


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
    while (
        (decision := input('Введи «Прогнать монстра» или «Бой» >>> ').lower())
        not in ('прогнать монстра', 'бой')
    ):
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


def change_to_default(character):
    '''После боя сбрасывает здоровье и выносливость персонажа к первоначальным
    значениям. Убирает действие проклятий Смена пола и Кривое зеркало.'''
    setattr(character, 'woman', False)
    setattr(character, 'only_armor', False)
    character.health = 100
    character.stamina = 20


def start_fight(character):
    '''Запускает битву персонажа с монстром.'''
    monster = prepare_monster(character)
    print(f'За дверью тебя встретил {monster}. Приготовься к битве!')
    if (character.klass == 'Волшебник'
       and (character.pollymorph or character.friendship)):
        if (result := wizard_spells(character)) is not False:
            return result  # True или None
    attacks = {'атака': character.attack,
               'тяжёлая атака': character.strong_attack,
               'бусты': character.boost_attack}
    total_damage = 0
    print('Боевая сила >>>', character.strength())
    while True:
        print('Нанесено урона >>>', total_damage)
        print('Осталось жизней у монстра >>>', monster.health)
        print('Здоровье >>>', character.health)
        print('Выносливость >>>', character.stamina)
        command = fight_command(character)
        if command in attacks:
            defence = 0
            damage = attacks[command]()
            total_damage += damage
            monster.health -= damage
        else:
            defence = character.defence()
        if monster.health <= 0:
            print('Ты победил!')
            change_to_default(character)
            return True
        character.health -= monster.attack(defence)
        if character.health <= 0:
            print('Монстр победил!')
            change_to_default(character)
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
    while input('Введи «Бросаю кубик» >>> ').lower() != 'бросаю кубик':
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


def doors_progress(level, table, index, event, finish=False):
    '''Отобразить текущий уровень и закрытые двери для выбора.
    А так же результат уже пройденных уровней.'''
    from prettytable import PrettyTable, DOUBLE_BORDER
    from termcolor import colored

    CLOSED_DOOR = '▓▓▓▓▓▓\n▓▓▒▒▓▓\n▓▓▓▓▓▓\n▓▓▓▓▓▓\n───────'
    CLOSED_DOORS = [CLOSED_DOOR, CLOSED_DOOR, CLOSED_DOOR]
    CURRENT_LEVEl = [f'Уровень\n« {level} »\n\n\n───────', *CLOSED_DOORS]
    OPENED_CURSE = '┌────┐\n │ПРОК│\n │ ЛЯТ│\n└────┘\n───────'
    OPENED_FREE = '┌────┐\n │СВО │\n │ БОД│\n└────┘\n───────'
    OPENED_MONSTER = '┌────┐\n │МОН │\n │ СТР│\n└────┘\n───────'
    OPENED_DOORS = {'monster': OPENED_MONSTER,
                    'curse': OPENED_CURSE,
                    'free': OPENED_FREE}
    PASSED = colored('пройден', 'green', attrs=['bold'])
    TITLE = ['', colored('СЛЕВА', 'blue', attrs=['bold']),
             colored('ЦЕНТР', 'blue', attrs=['bold']),
             colored('СПРАВА', 'blue', attrs=['bold'])]

    if level == 1:
        table = PrettyTable()
        table.set_style(DOUBLE_BORDER)
        table.field_names = TITLE
        table.add_row(CURRENT_LEVEl)
        print(table)
        return table[:0]  # возврат только заголовка
    closed_doors = CLOSED_DOORS.copy()
    closed_doors.pop(index)
    closed_doors.insert(index, OPENED_DOORS[event])
    table.add_row(
        [f'Уровень\n« {level - 1} »\n' + PASSED + '\n\n───────', *closed_doors]
    )
    if finish:
        print(table)
        return
    table.add_row(CURRENT_LEVEl)
    print(table)
    return table[:-1]
