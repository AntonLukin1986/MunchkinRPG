from random import randint
import time
from typing import Union

from termcolor import colored, cprint

ATTACK = '{0} → урон от 1 до 5\n{1}  → урон от 10 до 20\n{2} → урон от 30 до 40'.format(
        colored('Лёгкая', 'green', attrs=['bold']),
        colored('Средняя', 'green', attrs=['bold']),
        colored('Тяжёлая', 'green', attrs=['bold']),
)
RANK = '''<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n
Тренировки закончены. Начинаются {} в зачёт.
Сейчас у твоего персонажа {}. За каждую победу ты получишь дополнительный ранг.\n'''.format(
    colored('три битвы', 'blue'), colored('нулевой ранг', 'blue')
)
RULES_1 = '''{0}
Твоя цель — за {1} набрать такое количество очков урона своему противнику, которое попадёт
в диапазон {2} от его изначального здоровья. Здоровье противника каждый раз генерируется случайным
образом в диапазоне {3} единиц. {4} если противник получил 100 здоровья, то для победы
необходимо за 5 атак нанести ему суммарный урон от 95 до 105. Перед каждой битвой отобразится
подсказка - количество цифр в значении здоровья твоего противника.
{4} для 92 единиц отобразится ХХ, а для 107 - ХХХ.
В твоём распоряжении три вида атак, урон от которых выбирается случайным образом в заданных пределах:
{attack}'''.format(
    colored('↓ Правила поединка ↓', 'green', attrs=['bold']),
    colored('5 атак', 'blue', attrs=['bold']),
    colored('± 5', 'blue', attrs=['bold']),
    colored('от 80 до 120', 'blue', attrs=['bold']),
    colored('Пример:', 'black', attrs=['bold']),
    attack=ATTACK
)
RULES_2 = '''Сперва ты можешь немного попрактиковаться - тренировочные бои не влияют на итоговый результат.
Когда посчитаешь нужным, переходи к трём зачётным сражениям. Приступай, как только будешь готов.'''

TRAIN = (
    '-> Как-то боязно - хочу ещё потренить (введи {})\n'
    '-> Мортал комбат!!! (введи {})\n>>> '.format(
        colored('Тренировка', 'blue', attrs=['bold']), colored('Бой', 'blue', attrs=['bold'])
    )
)


def get_lite_attack() -> int:
    return randint(1, 5)


def get_mid_attack() -> int:
    return randint(10, 20)


def get_hard_attack() -> int:
    return randint(30, 40)


def get_user_attack() -> int:
    '''Вычисляет совокупный урон от атак игрока.'''
    damage = 0
    attacks_types = {
        'лёгкая': get_lite_attack,
        'средняя': get_mid_attack,
        'тяжёлая': get_hard_attack,
    }
    for number in range(1, 6):
        print(ATTACK)
        while ((input_attack := input(colored('Введи тип атаки: ', 'blue')).lower())
                not in attacks_types):
            pass
        time.sleep(1)
        attack_value = attacks_types[input_attack]()
        damage += attack_value
        print(f'\nУрон от текущей атаки: {attack_value}')
        print(f'Проведено атак: {number}\nСовокупный урон противнику: {damage}\n')
    return damage


def run_game(fight: bool = False) -> Union[bool, int]:
    '''Запускает мини-игру.'''
    enemy_health = randint(80, 120)
    hint = 'ХХ' if len(str(enemy_health)) == 2 else 'ХХХ'
    print(f'‼ Противник получает {hint} ♥')
    user_total_damage = get_user_attack()
    time.sleep(1)
    print('*' * 51)
    print(
        'В ходе боя противнику был нанесён урон, равный {}.\n'
        'Очки здоровья противника до боя: {}.'.format(
            colored(f'{user_total_damage}', 'green', attrs=['bold']),
            colored(f'{enemy_health}', 'red', attrs=['bold']),
        )
    )
    print('*' * 51)
    point_difference = abs(enemy_health - user_total_damage)
    if 0 <= point_difference <= 5:
        cprint('Победа за тобой!\n', 'green')
        winning = 1
    else:
        cprint('Бой проигран...\n', 'red')
        winning = 0
    if not fight:
        train_quit = {'тренировка': True, 'бой': False}
        while (replay := input(TRAIN).lower()) not in train_quit:
            pass
        print()
        return train_quit[replay]
    return winning


def start() -> int:
    '''Запускает цикл тренировки, после чего три битвы в зачёт.'''
    replay = True
    while replay:
        replay = run_game()
    print(RANK)
    wins = 0
    for _ in range(3):
        wins += run_game(fight=True)
    return wins


if __name__ == '__main__':
    start()
