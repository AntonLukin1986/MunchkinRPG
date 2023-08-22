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


def create_events(floors=10, show=True):
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
        print('*' * 10)
        for floor in level_events:
            print(floor)
        print('*' * 10)
    return level_events


def create_character(race, klass, rank):
    '''Создание персонажа и его экипировка в зависимости от уровня, расы
    и класса. Возвращает не использованные шмотки.'''
    import doors_game.cards as item
    from doors_game.cards import treasures_for_rank
    from doors_game.classes import Cleric, Warrior, Wizard
    from doors_game.text import PUSH_ENTER

    treasures_for_rank = treasures_for_rank.copy()
    klasses_set = {'Воин': Warrior, 'Волшебник': Wizard, 'Клирик': Cleric}
    kwargs = {  # экипировка при уровне персонажа 0
        'helmet': item.HELM_COURAGE,
        'armor': item.SLIMY_ARMOR,
        'footgear': item.SANDALS,
        'left_arm': item.LONG_POLE,
        'right_arm': item.NO_ITEM
    }
    print('Персонаж нулевого ранга обладает следующей экипировкой...')
    input(PUSH_ENTER)
    for stuff in [
        item.HELM_COURAGE, item.SLIMY_ARMOR, item.SANDALS, item.LONG_POLE
    ]:
        show_image(stuff.image, stuff)
    if rank >= 1:
        if klass == 'Воин':
            weapon = item.SHIELD_UBIQUITY
        elif klass == 'Волшебник':
            weapon = item.STAFF_NAPALM
        elif klass == 'Клирик':
            weapon = item.MACE_SHARPNESS
        treasures_for_rank.remove(weapon)
        kwargs['right_arm'] = weapon  # в левой руке базовое оружие
        print(f'За первый ранг дополнительно получаешь особое оружие {klass}а '
              f'- {weapon}.')
        input(PUSH_ENTER)
        show_image(weapon.image, weapon)
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
        treasures_for_rank.remove(special)
        print(f'За второй ранг держи {special}.')
        input(PUSH_ENTER)
        show_image(special.image, special)
    if rank == 3:
        if race == 'Эльф':
            stuff = item.HORNY_HELMET
            kwargs['helmet'] = stuff
        elif race == 'Дварф':
            stuff = item.SHORT_WIDE_ARMOR
            kwargs['armor'] = stuff
        elif race == 'Хафлинг':
            stuff = item.STEPLADDER
            kwargs['footgear'] = stuff
        treasures_for_rank.remove(stuff)
        print(f'За третий ранг уникальный для {race}а {stuff} заменит '
              'стандартный элемент экипировки.')
        input(PUSH_ENTER)
        show_image(stuff.image, stuff)
    return klasses_set[klass](race, rank, **kwargs), treasures_for_rank


def prepare_game(race, klass, rank, show=True):
    '''Подготовка персонажа и стартовых наборов карт.'''
    from doors_game.cards import (
        door_cards_base, door_cards_specific,
        free_room_treasures,
        monster_treasures_base, monster_treasures_specific
    )

    door_cards = door_cards_base.copy()
    door_cards.extend(
        [card for card in door_cards_specific if card.require == klass]
    )
    monster_treasures = monster_treasures_base.copy()
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
    free_treasures = free_room_treasures.copy()
    if show:
        print('----- before game -----')
        print(f'Всего сокровищ монстров {len(monster_treasures)}:')
        print(*monster_treasures, sep='\n')
        print('*' * 10)
        print(f'Всего карт дверей {len(door_cards)}:')
        print(*door_cards, sep='\n')
        print('*' * 10)
        print(f'Всего свободных сокровищ {len(free_treasures)}:')
        print(*free_treasures, sep='\n')
        print('----- before game -----\n')
    return character, monster_treasures, door_cards, free_treasures


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
    from doors_game.cards import PLUG

    if len(cards_set) == 0:  # для сокровищ монстра
        cards_set.extend([PLUG, PLUG, PLUG])  # заглушки
    card = cards_set.pop(randint(0, len(cards_set)-1))
    show_image(card.image, card)
    if show:
        print(card)
        print('*' * 10)
        print(f'Осталось в наборе {len(cards_set)}:')
        print(*cards_set, sep='\n')
        print('*' * 10)
    return card


def get_treasure(character, cards_set):
    '''Отрабатывает найденную шмотку при открытии свободной двери или после
    победы над монстром.'''
    from doors_game.cards import WISHING_RING
    from doors_game.classes import Boost, Buff, Item
    from doors_game.text import WEAK_ITEM

    card = get_random_card(cards_set)
    if isinstance(card, Boost):
        character.boost += card.value
    elif isinstance(card, Item):
        if card.kind == 'arm':
            # определяется, в какой руке самое слабое оружие
            card.kind = weak_or_strong_arm(character)
        have_item = getattr(character, card.kind)
        if have_item.value < card.value:
            setattr(character, card.kind, card)
            print(f'{have_item} заменено на {card}')
        else:
            print(WEAK_ITEM.format(card))
            character.boost += card.value
    elif isinstance(card, Buff):
        if card is WISHING_RING:
            character.wishing_ring += 1
        else:
            setattr(character, card.kind, True)


def get_curse(character, cards_set):
    '''Отрабатывает открытие двери с проклятьем.'''
    from doors_game.classes import Curse
    from doors_game.cards import CHEAT, NO_ITEM, TIGHTS
    from doors_game.text import PUSH_ENTER

    card = get_random_card(cards_set)
    if card.kind == 'cheat':
        character.tights = True
        print(CHEAT.after_use)
        input(PUSH_ENTER)
        show_image(TIGHTS.image, TIGHTS.description)
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
        to_lose = getattr(character, lose)
        if to_lose is not NO_ITEM:
            print(f'Ты вынужден потерять {to_lose}')
            input(PUSH_ENTER)
            show_image(f'{to_lose.image}', 'Попрощайся с этой шмоткой')
        else:
            print('Терять нечего - проклятье не подействовало!')
            input(PUSH_ENTER)
            return
    else:
        lose = card.kind
        value = True
    if (isinstance(card, Curse) and character.klass == 'Клирик'
       and character.use_wishing_ring(lose, value)):
        print('Ты используешь Хотельное кольцо: проклятье отменяется!')
        input(PUSH_ENTER)
        return
    setattr(character, lose, value)  # в том числе для Бафа
    if card.kind != 'lose':
        input(PUSH_ENTER)


def fight_command(character):
    '''Ввод команды игроком и проверка возможности её выполнения.'''
    from doors_game.text import COMBAT, COMBAT_CHECK

    confirmed = False
    while not confirmed:
        while (command := input(COMBAT).lower()) not in COMBAT_CHECK:
            pass
        if ((command == 'атака' and character.stamina < 10)
           or (command == 'мощная' and character.stamina < 20)):
            print('Недостаточно выносливости!')
        elif command == 'дальняя' and character.boost == 0:
            print('Бустов пока нет - применять нечего!')
        else:
            confirmed = True
    return command


def prepare_monster(level, character):
    '''Подготавливает монстра для битвы.'''
    from random import choice
    from doors_game.cards import ILLUSION
    from doors_game.monsters import MONSTERS, PLANT
    from doors_game.text import PUSH_ENTER

    if character.klass == 'Волшебник' and character.illusion:
        character.illusion = False
        monster = PLANT
        print(ILLUSION.after_use)
        input(PUSH_ENTER)
    else:
        monster = choice(MONSTERS[level])
    show_image(monster.image, monster.detail)
    return monster


def wizard_spells(character):
    '''Предоставление волшебнику возможности усмирить монстра вместо боя.'''
    from doors_game.cards import POLLYMORPH_POTION, FRIENDSHIP_POTION
    from doors_game.text import PUSH_ENTER, SPELL_CHOSE

    morph = (
        '\n' + POLLYMORPH_POTION.description if character.pollymorph else ''
    )
    friend = (
        '\n' + FRIENDSHIP_POTION.description if character.friendship else ''
    )
    print(
        f'У тебя есть заклинания для усмирения монстров:{morph}{friend}'
        '\nМожешь воспользоваться, чтобы избежать боя!'
    )
    while (
        (decision := input(SPELL_CHOSE).lower())
        not in ('прогнать монстра', 'бой')
    ):
        pass
    print()
    if decision == 'бой':
        return False
    if character.pollymorph:  # в приоритете первым используется Попуморф
        character.pollymorph = False
        print(POLLYMORPH_POTION.after_use)
        input(PUSH_ENTER)
        return True
    character.friendship = False
    print(FRIENDSHIP_POTION.after_use)
    input(PUSH_ENTER)
    return None


def change_to_default(character):
    '''После боя сбрасывает здоровье и выносливость персонажа к первоначальным
    значениям. Убирает проклятья следующего боя.'''
    setattr(character, 'woman', False)
    setattr(character, 'only_armor', False)
    health = {'Эльф': 110, 'Дварф': 90, 'Хафлинг': 100}
    character.health = health[character.race]
    character.stamina = 10


def show_statistics(character, monster) -> None:
    '''Отображение статистики во время боя.'''
    from termcolor import colored, cprint
    from doors_game.text import NAME
    total_power = character.strength()
    print(NAME, '¶', f'Боевая сила {total_power}')
    min_attack = round(character.MIN_RATIO * total_power)
    max_attack = round(character.MAX_RATIO * total_power)
    print(f'Атака: {min_attack}-{max_attack} '
          f'(-10 выносливости | блокирует {character.items_strength()} урона)')
    min_hard = round(
        total_power * character.STRONG_ATTACK_RATIO *
        character.MIN_STRONG_RATIO
    )
    max_hard = round(
        total_power * character.STRONG_ATTACK_RATIO *
        character.MAX_STRONG_RATIO
    )
    print(f'Мощная: {min_hard}-{max_hard} (-20 выносливости)')
    min_defence = round(character.MIN_RATIO * total_power)
    max_defence = round(character.MAX_RATIO * total_power)
    print(f'Защита: блокирует {min_defence}-{max_defence} '
          'урона (+10 выносливости)')
    print(f'Дальнобойная: {character.boost} (+10 выносливости)')
    print(
        colored('► Выносливость', attrs=['bold']) + f' [{character.stamina}]'
    )
    if character.health <= 20:
        color = 'red'
    elif character.health <= 50:
        color = 'yellow'
    else:
        color = 'green'
    print(colored('► Здоровье', attrs=['bold']) +
          colored(f' [{character.health}]', color))
    print('><' * 15)
    cprint(monster.name, 'red', attrs=['bold'], end=' ¶ ')
    print(f'Боевая сила {monster.strength()}')
    min_damage = round(monster.MIN_RATIO * monster.strength())
    max_damage = round(monster.MAX_RATIO * monster.strength())
    print(f'Наносимый урон: {min_damage}-{max_damage}')
    if monster.health <= 20:
        color = 'red'
    elif monster.health <= 50:
        color = 'yellow'
    else:
        color = 'green'
    print(colored('► Здоровье', attrs=['bold']) +
          colored(f' [{monster.health}]', color))


def start_fight(level, character):
    '''Запускает битву персонажа с монстром.'''
    from termcolor import colored
    from doors_game.text import MONSTER_DEAD, MONSTER_WIN, PUSH_ENTER

    monster = prepare_monster(level, character)
    print(
        f'Ты столкнулся с {colored(monster, "red")}. Приготовься к битве!',
        '\n'
    )
    if (character.klass == 'Волшебник'
       and (character.pollymorph or character.friendship)):
        if (result := wizard_spells(character)) is not False:
            return result  # True или None
    attacks = {'атака': character.attack,
               'мощная': character.strong_attack,
               'дальняя': character.boost_attack}
    while True:
        show_statistics(character, monster)
        print()
        command = fight_command(character)
        print()
        if command in attacks:
            defence = character.items_strength() if command == 'атака' else 0
            damage = attacks[command]()
            monster.health -= damage
        else:
            defence = character.defence()
        if monster.health <= 0:
            input(PUSH_ENTER)
            change_to_default(character)
            print(MONSTER_DEAD)
            input(PUSH_ENTER)
            monster.health = 100
            return True
        character.health -= monster.attack(defence)
        if character.health <= 0:
            input(PUSH_ENTER)
            change_to_default(character)
            print(MONSTER_WIN)
            input(PUSH_ENTER)
            monster.health = 100
            return False
        input(PUSH_ENTER)


def monster_get_item(character):
    '''Монстр забирает случайную шмотку при неудачной смывке.'''
    from random import choice
    from doors_game.cards import NO_ITEM, SPIKY_KNEES, TIGHTS
    from doors_game.text import PUSH_ENTER

    item_types = [
        'helmet', 'armor', 'footgear', 'left_arm', 'right_arm',
        'knees', 'tights'
    ]
    if character.klass != 'Воин':
        item_types.remove('knees')
        item_types.remove('tights')
    for type_ in item_types.copy():
        stuff = getattr(character, type_)
        if stuff is False or stuff is NO_ITEM:
            item_types.remove(type_)
    if item_types:
        lose_type = choice(item_types)
        if lose_type in ('knees', 'tights'):
            new_value = False
        else:
            new_value = NO_ITEM
        # для отображения информации
        if lose_type == 'knees':
            to_lose = SPIKY_KNEES
        elif lose_type == 'tights':
            to_lose = TIGHTS
        else:
            to_lose = getattr(character, lose_type)
        print(f'Ты потерял: {to_lose}')
        input(PUSH_ENTER)
        show_image(f'{to_lose.image}', 'Попрощайся с этой шмоткой')
        setattr(character, lose_type, new_value)
    else:
        print('Так как экипировки у тебя нет, то пришлось сбросить штаны... ')


def run_away(character):
    '''Смывка при поражении в бою с монстром.'''
    from pathlib import Path
    from playsound import playsound
    from random import randint
    from doors_game.cards import INVISIBILITY_POTION
    from doors_game.text import (
        DICE, RUN_AWAY, PUSH_ENTER, RUN_AWAY_BAD, RUN_AWAY_OK, RUN_AWAY_SO_SO
    )
    MP3_PATH = str(Path(__file__).resolve().parent.parent / 'mp3/dice.mp3')
    DICE_IMAGES = {1: 'dice_one', 2: 'dice_two', 3: 'dice_three',
                   4: 'dice_four', 5: 'dice_five', 6: 'dice_six'}
    print(RUN_AWAY)
    while input(DICE).lower() != 'бросаю кубик':
        pass
    playsound(MP3_PATH)
    dice = randint(1, 6)
    show_image(f'dices/{DICE_IMAGES[dice]}', 'На кубике выпало...')
    if character.chicken and dice != 1:
        dice -= 1
        show_image(f'dices/{DICE_IMAGES[dice]}',
                   'Курица на твоей башке уменьшила результат броска на 1')
    print()
    if dice >= 5:
        print(RUN_AWAY_OK)
        input(PUSH_ENTER)
    elif dice >= 3:
        print(RUN_AWAY_SO_SO)
        input(PUSH_ENTER)
        monster_get_item(character)
    else:
        if character.invisibility:
            character.invisibility = False
            print(INVISIBILITY_POTION.after_use)
            input(PUSH_ENTER)
            show_image('monster_treasures/invisibility',
                       'Зелье невидимости. Полусладкое!')
        else:
            print(RUN_AWAY_BAD)
            input(PUSH_ENTER)
            show_image('common/angel', 'The end')
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
    if event == 'god':
        table.add_row(
            [f'Уровень\n« {level - 1} »\n' + PASSED + '\n\n───────',
             *CLOSED_DOORS]
            )
    else:
        closed_doors = CLOSED_DOORS.copy()
        closed_doors.pop(index)
        closed_doors.insert(index, OPENED_DOORS[event])
        table.add_row(
            [f'Уровень\n« {level - 1} »\n' + PASSED + '\n\n───────',
             *closed_doors]
        )
    if finish:
        print(table)
        return
    table.add_row(CURRENT_LEVEl)
    print(table)
    return table[:-1]


def magic_spell():
    '''Волшебное заклинание в битве с Ктулху.'''
    from doors_game.text import (
        MAGIC_SPELL, MAGIC_SPELL_OK, MAGIC_SPELL_WRONG, PUSH_ENTER
    )

    print(MAGIC_SPELL)
    input(PUSH_ENTER)
    if input('Введи волшебную фразу >>> ').lower() == 'vivus ercapus':
        print(MAGIC_SPELL_OK)
        return True
    print(MAGIC_SPELL_WRONG)
    return False


def boss_fight(character):
    '''Запускает битву с главным боссом - Ктулху.'''
    from termcolor import colored
    from doors_game.monsters import CTHULHU
    from doors_game.text import (
        CTHULHU_MEET_1, CTHULHU_MEET_2, CTHULHU_MEET_3, LOSE_CTHULHU,
        PUSH_ENTER, WIN_CTHULHU
    )

    monster = CTHULHU
    print('Тебе удалось пройти все уровни Башни.\n'
          f'Приготовься встретиться с {colored(monster.name, "red")}!')
    input(PUSH_ENTER)
    show_image(monster.image, monster.detail)
    print(CTHULHU_MEET_1)
    input(PUSH_ENTER)
    print(CTHULHU_MEET_2)
    input(PUSH_ENTER)
    print(CTHULHU_MEET_3)
    input(PUSH_ENTER)
    attacks = {'атака': character.attack,
               'мощная': character.strong_attack,
               'дальняя': character.boost_attack}
    last_chance = True
    while True:
        show_statistics(character, monster)
        print()
        command = fight_command(character)
        print()
        if command in attacks:
            defence = character.items_strength() if command == 'атака' else 0
            damage = attacks[command]()
            monster.health -= damage
        else:
            defence = character.defence()
        if monster.health <= 0:
            input(PUSH_ENTER)
            print(WIN_CTHULHU)
            input(PUSH_ENTER)
            return True
        character.health -= monster.attack(defence)
        if character.health <= 0:
            input(PUSH_ENTER)
            if last_chance and magic_spell():
                character.health = 30
                last_chance = False
            else:
                change_to_default(character)
                monster.health = 100
                last_chance = True
                print(LOSE_CTHULHU)
                input(PUSH_ENTER)
                return False
        input(PUSH_ENTER)
