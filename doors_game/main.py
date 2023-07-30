"""Основной файл для запуска игры."""


def run_doors_game(race, klass, level):
    '''Запускает прохождение уровней с дверями.'''
    import cards as item
    from funcs import (
        create_events, get_curse, get_treasure, prepare_game, run_away,
        start_fight
    )
    from text import CHOOSE_DOOR

    character, monster_treasures, door_cards = prepare_game(
        race, klass, level
    )
    doors_indexes = {'слева': 0, 'центр': 1, 'справа': 2}
    for i, floor in enumerate(create_events(), 1):
        if hasattr(character, 'god') and character.god:
            character.god = False
            print(item.DIVINE_INTERDICTION.after_use + f'{i}')
            continue
        print(f'<-> <-> <-> <-> <-> Уровень №{i} <-> <-> <-> <-> <->')
        while (result := input(CHOOSE_DOOR).lower()) not in doors_indexes:
            pass
        event = floor[doors_indexes[result]]
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
    # ####################################################################
    print('^' * 10)
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
    # race = 'Эльф'
    race = 'Дварф'
    # race = 'Халфлинг'
    # klass = 'Воин'
    # klass = 'Клирик'
    klass = 'Волшебник'
    level = 0
    run_doors_game(race, klass, level)
