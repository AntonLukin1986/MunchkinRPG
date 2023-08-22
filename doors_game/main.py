"""Основной файл для запуска игры."""


def run_doors_game(race, klass, rank):
    '''Запускает прохождение игры с вышибанием дверей.'''
    from doors_game import cards as item
    from doors_game.funcs import (
        boss_fight, create_events, doors_progress, get_curse, get_treasure,
        prepare_game, run_away, start_fight
    )
    from doors_game.text import CHOOSE_DOOR, DOORS_INDEXES, PUSH_ENTER

    table = None
    index = None
    event = None
    character, monster_treasures, door_cards, free_treasures = prepare_game(
        race, klass, rank, show=True
    )
    for level, doors in enumerate(create_events(show=True), 1):
        print(character)
        input(PUSH_ENTER)
        table = doors_progress(level, table, index, event)
        if hasattr(character, 'god') and character.god:
            character.god = False
            print(item.DIVINE_INTERDICTION.after_use.format(level))
            input(PUSH_ENTER)
            event = 'god'
            continue
        while (choice := input(CHOOSE_DOOR).lower()) not in DOORS_INDEXES:
            pass
        print()
        index = DOORS_INDEXES[choice]
        event = doors[index]
        if event == 'monster':
            print('За дверью притаился монстр!')
            input(PUSH_ENTER)
            result = start_fight(level, character)
            if result is True:  # победил в битве или использовал попуморфа
                get_treasure(character, monster_treasures)
                input(PUSH_ENTER)
            elif result is False and run_away(character) is False:
                return False
            # вариант c None (использовал зелье дружбы) не обрабатывается
        elif event == 'curse':
            print('Ты открыл дверь с проклятьем...')
            input(PUSH_ENTER)
            get_curse(character, door_cards)
        elif event == 'free':
            print('Проход свободен. На полу лежат бесхозные вещи...')
            input(PUSH_ENTER)
            get_treasure(character, free_treasures)
            input(PUSH_ENTER)
    doors_progress(level + 1, table, index, event, finish=True)
    print(character)
    input(PUSH_ENTER)
    print('----- after game -----')
    print(f'Всего сокровищ монстров {len(monster_treasures)}:')
    print(*monster_treasures, sep='\n')
    print('*' * 10)
    print(f'Всего карт дверей {len(door_cards)}:')
    print(*door_cards, sep='\n')
    print('*' * 10)
    print(f'Всего свободных сокровищ {len(free_treasures)}:')
    print(*free_treasures, sep='\n')
    print('----- after game -----\n')
    return boss_fight(character)


if __name__ == '__main__':
    # race = 'Эльф'
    # race = 'Дварф'
    race = 'Халфлинг'
    klass = 'Воин'
    # klass = 'Клирик'
    # klass = 'Волшебник'
    rank = 0
    run_doors_game(race, klass, rank)
