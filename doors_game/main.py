"""Основной файл для запуска игры."""
from classes import *
from funcs import create_events, curse_event, free_or_monster_event, get_random_card, prepare_game, weak_or_strong_arm
import items as item

race = 'Эльф'
# race = 'Дварф'
# race = 'Халфлинг'
klass = 'Воин'
# klass = 'Клирик'
# klass = 'Волшебник'
level = 2
character, monster_treasures, door_cards = prepare_game(
    race, klass, level
)
# #################################################################

got_monster_tresuares = []

doors_indexes = {'слева': 0, 'центр': 1, 'справа': 2}
for i, floor in enumerate(create_events(), 1):
    print(f'<-> <-> <-> <-> <-> Уровень {i} <-> <-> <-> <-> <->')
    while (result := input('Выбери дверь: слева, центр, справа >>> ')) not in doors_indexes:
        pass
    event = floor[doors_indexes[result]]
    if event == 'monster':
        print('...Битва с монстром...')
        # если победа, то получаешь его сокровище
        free_or_monster_event(character, monster_treasures)
    if event == 'curse':
        curse_event(character, door_cards)
    elif event == 'free':
        free_or_monster_event(character, item.free_room_treasures)
    # оптимизировать только в получение карты и функции а вызывать в конце

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
