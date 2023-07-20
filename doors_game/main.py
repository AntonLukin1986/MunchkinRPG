"""Основной файл для запуска игры."""
from classes import Item, Boost
from funcs import create_level_events, prepare_character_cards
import items as item

race = 'Эльф'
# race = 'Дварф'
# race = 'Халфлинг'
klass = 'Воин'
# klass = 'Клирик'
# klass = 'Волшебник'
level = 0
character, monster_treasures, door_cards = prepare_character_cards(
    race, klass, level
)
# #################################################################

got_monster_tresuares = []
got_curses = []
got_free_way_treasures = []


from random import randint
doors_indexes = {'слева': 0, 'центр': 1, 'справа': 2}
for floor in create_level_events():
    while (result := input('Выбери дверь: слева, центр, справа >>> ')) not in doors_indexes:
        pass
    event = floor[doors_indexes[result]]
    if event == 'monster':
        card = monster_treasures.pop(randint(0, len(monster_treasures)-1)); print(card)
        got_monster_tresuares.append(card)
    elif event == 'curse':
        card = door_cards.pop(randint(0, len(door_cards)-1)); print(card)
        got_curses.append(card)
    elif event == 'free':
        def weak_or_strong_arm(character, weak=True):
            '''Определяет, в какой руке самое слабое или сильное оружие.'''
            if weak:
                return 'left_arm' if character.left_arm.value <= character.right_arm.value else 'right_arm'
            return 'left_arm' if character.left_arm.value >= character.right_arm.value else 'right_arm'

        def get_random_card(cards_set, show=True):
            '''Перемещает случайную карту из переданного набора в игру.'''
            card = cards_set.pop(randint(0, len(cards_set)-1))
            if show: print(card)
            return card

        def free_event():
            '''Отрабатывает ситуацию открытия свободной двери.'''
            card = get_random_card(item.free_way_treasures)
            got_free_way_treasures.append(card)
            if isinstance(card, Boost):
                character.boost += card.value
                print(character)
            elif isinstance(card, Item):
                if card.kind == 'arm':
                    card.kind = weak_or_strong_arm(character)
                have_item = getattr(character, card.kind)
                if have_item.value < card.value:
                    setattr(character, card.kind, card)
                    print(f'{have_item} заменено на {card}!')
                    print(character)
        
        free_event()

print('^' * 10)
print(f'Количество {len(got_monster_tresuares)}:')
print(*got_monster_tresuares, sep='\n')
print('*' * 10)
print(f'Количество {len(monster_treasures)}:')
print(*monster_treasures, sep='\n')
print('=' * 10)
print(f'Количество {len(got_curses)}:')
print(*got_curses, sep='\n')
print('*' * 10)
print(f'Количество {len(door_cards)}:')
print(*door_cards, sep='\n')
print('=' * 10)
print(f'Количество {len(got_free_way_treasures)}:')
print(*got_free_way_treasures, sep='\n')
print('*' * 10)
print(f'Количество {len(item.free_way_treasures)}:')
print(*item.free_way_treasures, sep='\n')
print('=' * 10)
