"""Основной файл для запуска игры."""


def run_doors_game(race, klass, rank):
    '''Запускает прохождение уровней с дверями.'''
    import cards as item
    from funcs import (
        create_events, doors_progress, get_curse, get_treasure, prepare_game,
        run_away, show_image, start_fight
    )
    from text import CHOOSE_DOOR, DOORS_INDEXES

    table = None
    index = None
    event = None
    character, monster_treasures, door_cards = prepare_game(
        race, klass, rank
    )
    for level, floor in enumerate(create_events(), 1):
        if hasattr(character, 'god') and character.god:
            character.god = False
            print(item.DIVINE_INTERDICTION.after_use + f'{level}')
            continue
        # show_image('levels/level_1', 'Сейчас ты находишься на...')
        table = doors_progress(level, table, index, event)
        while (choice := input(CHOOSE_DOOR).lower()) not in DOORS_INDEXES:
            pass
        index = DOORS_INDEXES[choice]
        event = floor[index]
        if event == 'monster':
            result = start_fight(character)
            if result is True:  # победил в битве или использовал попуморфа
                get_treasure(character, monster_treasures)
            elif result is False and run_away(character) is False:
                return False
            # вариант c None (использовал зелье дружбы) не обрабатывается
        elif event == 'curse':
            get_curse(character, door_cards)
        elif event == 'free':
            get_treasure(character, item.free_room_treasures)
    doors_progress(level + 1, table, index, event, finish=True)
    # ####################################################################
    print('*' * 10)
    print(f'Осталось сокровищ монстров {len(monster_treasures)}:')
    print(*monster_treasures, sep='\n')
    print('*' * 10)
    print(f'Осталось проклятий {len(door_cards)}:')
    print(*door_cards, sep='\n')
    print('*' * 10)
    print(f'Осталось свободных сокровищ {len(item.free_room_treasures)}:')
    print(*item.free_room_treasures, sep='\n')
    print('*' * 10)
    # ####################################################################
    return True


if __name__ == '__main__':
    race = 'Эльф'
    # race = 'Дварф'
    # race = 'Халфлинг'
    klass = 'Воин'
    # klass = 'Клирик'
    # klass = 'Волшебник'
    rank = 0
    run_doors_game(race, klass, rank)
