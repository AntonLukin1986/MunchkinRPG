"""Ролевая игра по мотивам настолки "Манчкин"."""
import time
import shelve

from asciimatics.screen import Screen
from colorama import just_fix_windows_console
from termcolor import colored, cprint

from functions import animation, game_begins, save_game, SAVES_PATH, show_image, teleprint
from texts.begining import *
from texts.captured_at_home import *
from texts.character_creation import *
from texts.common import *
from texts.intro import *
from texts.pursuit import *
from texts.pursuit_final import *

just_fix_windows_console()  # use Colorama to make Termcolor work on Windows


def start_game():
    """Меню: начать игру заново или продолжить с последнего сохранения."""
    print('╤' * 63, ATTENTION, '╧' * 63, sep='\n')
    print()
    cprint('► Г Л А В Н О Е   М Е Н Ю ◄', 'black', attrs=['bold'])
    print('▬' * 27)
    db = shelve.open(SAVES_PATH)
    progress = db.get('IN_PROGRESS')
    if progress is None:
        db.close()
        while input(
            colored('Для начала игры введи "Начать" >>> ', 'blue')
        ).lower() != 'начать':
            pass
        print('•' * 27)
        intro()
    else:
        cprint('Чтобы начать игру с самого начала введи "Заново" ', 'blue', end='')
        cprint('(последнее сохранение будет сброшено ‼)', 'red')
        cprint('Чтобы загрузить последнее сохранение введи "Продолжить"', 'blue')
        while (
            (decision := input(colored('>>> ', 'blue')).lower())
            not in ('заново', 'продолжить')
        ):
            pass
        if decision == 'продолжить':
            db.close()
            GAME_STAGES[progress]()
        if decision == 'заново':
            del db['IN_PROGRESS']
            db.close()
            print('•' * 27)
            intro()


def intro():
    """Введение в игру."""
    teleprint(INTRO_1); input(PUSH_ENTER); print()
    show_image('country', 'Манчикистания')
    teleprint(INTRO_2); input(PUSH_ENTER); print()
    character_creation()


def character_creation():
    """Создание персонажа, имитация выбора имени."""
    save_game('character_creation')
    teleprint(A); input(PUSH_ENTER); print()
    print('▼ ' * 15)
    print(DESCRIBE_CHARACTER, sep='\n')
    while len(input(colored('Введи описание персонажа >>> ', 'blue'))) < 101:
        cprint(NEED_DETAILED_DESCRIPTION, 'red', attrs=['bold'])
    cprint('¶ Автоматическая генерация персонажа по описанию...', 'blue')
    time.sleep(3)
    show_image('character', B)
    teleprint(CHARACTER_NAME)
    while not input(colored('Придумай и напиши имя для персонажа >>> ', 'blue')):
        pass
    teleprint(D)
    input(colored('Введите ДА или НЕТ >>> ', 'blue'))
    teleprint(E); input(PUSH_ENTER); print()
    teleprint(F); time.sleep(2)
    Screen.wrapper(game_begins)
    begining()


def begining():
    """Начало повествования. Вор пытается подкрепиться."""
    save_game('begining')
    print(AA); input(PUSH_ENTER); print()
    show_image('city', 'город Токийск Алтайского края')
    print(AA_2); input(PUSH_ENTER); print()
    print(AA_3); input(PUSH_ENTER); print()
    show_image('thief', 'класс Вор')
    print(BB_1); input(PUSH_ENTER); print()
    show_image('dagger', 'Кинжал измены')
    show_image('cloak', 'Плащ замутнённости')
    print(BB_2); input(PUSH_ENTER); print()
    print(CC); input(PUSH_ENTER); print()
    show_image('market', 'Токийский рынок. Белые розы, белые розы - беззащитны шипы...')
    print(DD); input(PUSH_ENTER); print()
    cprint(TRY_TO_THIEF, 'blue')
    while input(
        colored('Введи "бросаю кубик" >>> ', 'blue')
    ).lower() != 'бросаю кубик':
        pass
    time.sleep(1)
    show_image('dice_six', 'На кубике выпало ШЕСТЬ')
    print(THEFT_SUCCESS); input(PUSH_ENTER); print()
    print(EE); input(PUSH_ENTER); print()
    print(OTHER_THEFT)
    while input(
        colored('Введи "бросаю кубик" >>> ', 'blue')
    ).lower() != 'бросаю кубик':
        pass
    time.sleep(1)
    show_image('dice_one', 'На кубике выпало ОДИН')
    print(OTHER_THEFT_FAIL); input(PUSH_ENTER); print()
    print(DANGER); print(CHEET_DICE)
    while input(
        colored('Введи "Использовать читерский кубик" >>> ', 'blue')
    ).lower() != 'использовать читерский кубик':
        pass
    show_image('cheet_dice', 'Читерский кубик')
    print(OTHER_THEFT_SUCCESS); input(PUSH_ENTER); print()
    print(FF); input(PUSH_ENTER); print()
    print(FF_2)
    while input(
        colored('Введи "Простите меня, я больше так не буду" >>> ', 'blue')
    ).lower() != 'простите меня, я больше так не буду':
        pass
    print(GG); input(PUSH_ENTER); print()
    show_image('market_fight', 'Самое "уютное" местечко в городке...')
    pursuit()


def pursuit():
    """Вор пользуется подрезкой и убегает от погони."""
    save_game('pursuit')
    print(AAA); input(PUSH_ENTER); print()
    show_image('lame_goblin', 'Увечный гоблин')
    show_image('platycore', 'Утконтикора')
    print(AAA_2); input(PUSH_ENTER); print()
    print(BBB); input(PUSH_ENTER); print()
    print(CCC); input(PUSH_ENTER); print()
    print(CCC_2); input(PUSH_ENTER); print()
    show_image('fast_boots', 'Башмаки реально быстрого бега')
    print(CCC_3); input(PUSH_ENTER); print()
    show_image('instant_wall', 'Стенка-мгновенка')
    print(DDD); input(PUSH_ENTER); print()
    print(EEE)
    while input(
        colored('Введи фразу активации плаща "Атас, меня спалили!" >>> ', 'blue')
    ).lower() != 'атас, меня спалили!':
        pass
    print(FFF); input(PUSH_ENTER); print()
    show_image('onion_bag', 'Маскировка восьмидесятого левела')
    print(GGG); input(PUSH_ENTER); print()
    show_image('gippogrif', 'Гиппогриф (второй за кадром)')
    print(HHH_1); input(PUSH_ENTER); print()
    print(HHH_2); input(PUSH_ENTER); print()
    print(HHH_3); input(PUSH_ENTER); print()
    print(III); input(PUSH_ENTER); print()
    show_image('floating_nose', 'Блуждающий нос')
    print(JJJ); input(PUSH_ENTER); print()
    print(KKK); input(PUSH_ENTER); print()
    print(LLL); input(PUSH_ENTER); print()
    print(MMM); input(PUSH_ENTER); print()
    pursuit_final()


def pursuit_final():
    """Вора догоняет Блуждающий нос. Диалог и возвращение домой."""
    save_game('pursuit_final')
    print(AAAA); input(PUSH_ENTER); print()
    print(EXP_1); input(PUSH_ENTER); print()
    print(EXP_2); input(PUSH_ENTER); print()
    show_image('pursuit', 'Без преувеличения - эпическая погоня!')
    show_image('plasmic_gun', 'Эка диковина приблуда')
    print(EXP_3)
    while input(colored('Помнишь, что за фильм? >>> ', 'blue')) == '':
        pass
    print(EXP_4); input(PUSH_ENTER); print()
    print(BBBB); input(PUSH_ENTER); print()
    show_image('stink_potion', 'Зелье ротовой вони')
    print(CCCC); input(PUSH_ENTER); print()
    print(DECISION)
    while (
        (choise := input(colored('Сделай выбор 1 или 2 >>> ', 'blue')))
        not in ('1', '2')
    ):
        pass
    if choise == '2':
        print(DDDD); input(PUSH_ENTER); print()
        show_image('monster_killed', 'Типа победил Носа...')
        print(EEEE)
    if choise == '1':
        print(FFFF)
        while input(
            colored('Введите "Показать кинжал" >>> ', 'blue')
        ).lower() != 'показать кинжал':
            pass
        print(GGGG); input(PUSH_ENTER); print()
        show_image('dagger', 'Кинжал измены')
        print(HHHH)
    input(PUSH_ENTER); print()
    print(IIII); input(PUSH_ENTER); print()
    captured_at_home()


def captured_at_home():
    """Возвращение домой. Персонаж схвачен."""
    save_game('captured_at_home')
    print(BBBBB); input(PUSH_ENTER); print()
    show_image('bones_brothers', 'Бледные Братья')
    print(CCCCC); input(PUSH_ENTER); print()
    show_image('glue', 'Тюбик клея'); print()
    print(DDDDD); input(PUSH_ENTER); print()
    print(EEEEE); input(PUSH_ENTER); print()
    show_image('tuba_of_charm', 'Чарующая дуда')
    print(FFFFF); input(PUSH_ENTER); print()
    show_image('dragon', 'Плутониевый дракон')
    print(GGGGG); input(PUSH_ENTER); print()
    show_image('plant', 'Огорошенная трава')
    print(HHHHH); input(PUSH_ENTER); print()
    print(IIIII); input(PUSH_ENTER); print()
    show_image('dead_horse', 'Конь андедный')
    print(JJJJJ); input(PUSH_ENTER); print()


if __name__ == '__main__':
    GAME_STAGES = {
        'character_creation': character_creation,
        'begining': begining,
        'pursuit': pursuit,
        'pursuit_final': pursuit_final,
        'captured_at_home': captured_at_home
    }
    Screen.wrapper(animation)
    start_game()
