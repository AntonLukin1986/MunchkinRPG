"""Ролевая игра по мотивам настолки "Манчкин"."""
import time
import shelve

from asciimatics.screen import Screen
from colorama import just_fix_windows_console
from termcolor import colored, cprint

from functions import (
    animation, check_have_dagger, game_begins, playsound, save_dagger,
    save_game, SAVES_PATH, show_image, teleprint
)
from texts import colored_txt as clr
from texts import chapter_1
from texts import chapter_2
from texts import chapter_3
from texts import chapter_4
from texts import chapter_5
from texts import chapter_6
from texts import chapter_7
from texts import character_creation
from texts.intro import INTRO_1, INTRO_2

just_fix_windows_console()  # use Colorama to make Termcolor work on Windows


def start_game():
    """Стартовое меню игры."""
    print('╤' * 63, clr.ATTENTION, '╧' * 63, '\n', sep='\n')
    cprint('► Г Л А В Н О Е   М Е Н Ю ◄', 'black', attrs=['bold'])
    print('▬' * 27)
    db = shelve.open(SAVES_PATH)
    progress = db.get('IN_PROGRESS')
    if progress is None:
        db.close()
        while input(clr.START_GAME).lower() != 'начать':
            pass
        intro()
    else:
        cprint('Введи "Заново" - начать игру с самого начала', 'blue', end='')
        cprint(' (последнее сохранение будет сброшено!)', 'red')
        cprint('Введи "Продолжить" - загрузить последнее сохранение ', 'blue')
        while (
            (decision := input(colored('>>> ', 'blue')).lower())
            not in ('заново', 'продолжить')
        ):
            pass
        if decision == 'продолжить':
            db.close()
            print()
            GAME_STAGES[progress]()
        if decision == 'заново':
            del db['IN_PROGRESS']
            db.close()
            intro()


def intro():
    """Введение."""
    print()
    cprint('§ Введение', 'black', attrs=['bold'])
    print('•' * 27)
    teleprint(INTRO_1)
    input(clr.PUSH_ENTER)
    show_image('country', 'Манчикистания')
    teleprint(INTRO_2)
    input(clr.PUSH_ENTER)
    character_creation_func()


def character_creation_func():
    """Создание персонажа."""
    cprint('§ Создание персонажа', 'black', attrs=['bold'])
    save_game('character_creation')
    teleprint(character_creation.A)
    input(clr.PUSH_ENTER)
    print(character_creation.DESCRIBE_CHARACTER, sep='\n')
    while len(input(clr.CHAR_DESCR)) < 101:
        print(character_creation.DETAILED_DESCRIPTION)
    cprint('\n► Автоматическая генерация персонажа по описанию...\n', 'blue')
    time.sleep(3)
    show_image('character', character_creation.B)
    teleprint(character_creation.CHAR_CREATED)
    print()
    while not input(clr.PRINT_NAME):
        pass
    print()
    teleprint(character_creation.D)
    print()
    while input(clr.YES_OR_NO).lower() not in ('да', 'нет'):
        pass
    print()
    teleprint(character_creation.E)
    input(clr.PUSH_ENTER)
    teleprint(character_creation.F)
    time.sleep(2)
    Screen.wrapper(game_begins)
    print()
    chapter_1_func()


def chapter_1_func():
    """Начало."""
    cprint('§ Начало', 'black', attrs=['bold'])
    save_game('chapter_1')
    print(chapter_1.A)
    input(clr.PUSH_ENTER)
    playsound('birds_song')
    show_image('city', 'город Токийск Алтайского края')
    print(chapter_1.A_2)
    input(clr.PUSH_ENTER)
    print(chapter_1.A_3)
    input(clr.PUSH_ENTER)
    show_image('thief', 'класс Вор')
    print(chapter_1.B_1)
    input(clr.PUSH_ENTER)
    show_image('dagger', 'Кинжал измены')
    show_image('cloak', 'Плащ замутнённости')
    print(chapter_1.B_2)
    input(clr.PUSH_ENTER)
    print(chapter_1.C)
    input(clr.PUSH_ENTER)
    playsound('shatunov')
    show_image('market', 'Белые розы, белые розы - беззащитны шипы...')
    print(chapter_1.D)
    input(clr.PUSH_ENTER)
    cprint(chapter_1.TRY_TO_THIEF, 'blue')
    while input(clr.ROLL_DICE).lower() != 'бросаю кубик':
        pass
    print()
    time.sleep(1)
    show_image('dice_six', 'На кубике выпало ШЕСТЬ')
    print(chapter_1.THEFT_SUCCESS)
    input(clr.PUSH_ENTER)
    print(chapter_1.E)
    input(clr.PUSH_ENTER)
    print(chapter_1.OTHER_THEFT, '\n')
    while input(clr.ROLL_DICE).lower() != 'бросаю кубик':
        pass
    print()
    time.sleep(1)
    show_image('dice_one', 'На кубике выпало ОДИН')
    print(chapter_1.OTHER_THEFT_FAIL)
    input(clr.PUSH_ENTER)
    print(chapter_1.DANGER)
    print(chapter_1.CHEET_DICE)
    print()
    while input(clr.USE_CHEET_DICE).lower() != 'использовать читерский кубик':
        pass
    print()
    show_image('cheet_dice', 'Читерский кубик')
    print(chapter_1.OTHER_THEFT_SUCCESS)
    input(clr.PUSH_ENTER)
    print(chapter_1.F)
    input(clr.PUSH_ENTER)
    print(chapter_1.F_2)
    print()
    while input(
        clr.FORGIVE_ME
    ).lower() != 'простите меня, я больше так не буду':
        pass
    print()
    print(chapter_1.G)
    input(clr.PUSH_ENTER)
    show_image('market_fight', 'Самое "уютное" местечко в городке...')
    chapter_2_func()


def chapter_2_func():
    """Погоня."""
    cprint('§ Погоня', 'black', attrs=['bold'])
    save_game('chapter_2')
    print(chapter_2.A)
    input(clr.PUSH_ENTER)
    show_image('lame_goblin', 'Увечный гоблин')
    show_image('platycore', 'Утконтикора')
    print(chapter_2.A_2)
    input(clr.PUSH_ENTER)
    print(chapter_2.B)
    input(clr.PUSH_ENTER)
    print(chapter_2.C)
    input(clr.PUSH_ENTER)
    print(chapter_2.C_2)
    input(clr.PUSH_ENTER)
    show_image('fast_boots', 'Башмаки реально быстрого бега')
    print(chapter_2.C_3)
    input(clr.PUSH_ENTER)
    show_image('instant_wall', 'Стенка-мгновенка')
    print(chapter_2.D)
    input(clr.PUSH_ENTER)
    print(chapter_2.E)
    print()
    while input(clr.ATAS).lower() != 'атас, меня спалили!':
        pass
    print()
    print(chapter_2.F)
    input(clr.PUSH_ENTER)
    show_image('onion_bag', 'Маскировка восьмидесятого левела')
    print(chapter_2.G)
    input(clr.PUSH_ENTER)
    show_image('gippogrif', 'Гиппогриф (второй за кадром)')
    print(chapter_2.H_1)
    input(clr.PUSH_ENTER)
    print(chapter_2.H_2)
    input(clr.PUSH_ENTER)
    print(chapter_2.H_3)
    input(clr.PUSH_ENTER)
    print(chapter_2.IA)
    input(clr.PUSH_ENTER)
    playsound('danger')
    show_image('floating_nose', 'Блуждающий нос')
    print(chapter_2.J)
    input(clr.PUSH_ENTER)
    print(chapter_2.K)
    input(clr.PUSH_ENTER)
    print(chapter_2.L)
    input(clr.PUSH_ENTER)
    print(chapter_2.M)
    input(clr.PUSH_ENTER)
    chapter_3_func()


def chapter_3_func():
    """Развязка."""
    cprint('§ Развязка', 'black', attrs=['bold'])
    save_game('chapter_3')
    print(chapter_3.A)
    input(clr.PUSH_ENTER)
    print(chapter_3.EXP_1)
    input(clr.PUSH_ENTER)
    print(chapter_3.EXP_2)
    input(clr.PUSH_ENTER)
    show_image('pursuit', 'Без преувеличения - эпическая погоня!')
    show_image('plasmic_gun', 'Эка диковина приблуда')
    print(chapter_3.EXP_3)
    print()
    while input(clr.WHAT_FILM) == '':
        pass
    print()
    print(chapter_3.EXP_4)
    input(clr.PUSH_ENTER)
    print(chapter_3.B)
    input(clr.PUSH_ENTER)
    show_image('stink_potion', 'Зелье ротовой вони')
    print(chapter_3.C)
    input(clr.PUSH_ENTER)
    print(chapter_3.DECISION)
    while ((choise := input(clr.CHOICE))not in ('1', '2')):
        pass
    print()
    if choise == '2':
        print(chapter_3.D)
        input(clr.PUSH_ENTER)
        show_image('monster_killed', 'Типа победил Носа...')
        print(chapter_3.E)
        have_dagger = True
    if choise == '1':
        print(chapter_3.F)
        print()
        while input(clr.SHOW_DAGGER).lower() != 'отдать кинжал':
            pass
        print()
        print(chapter_3.G)
        input(clr.PUSH_ENTER)
        show_image('dagger', 'Кинжал измены')
        print(chapter_3.H)
        have_dagger = False
    input(clr.PUSH_ENTER)
    print(chapter_3.IA)
    input(clr.PUSH_ENTER)
    save_dagger(have_dagger)
    chapter_4_func()


def chapter_4_func():
    """Неожиданный поворот."""
    cprint('§ Неожиданный поворот', 'black', attrs=['bold'])
    save_game('chapter_4')
    print(chapter_4.A)
    input(clr.PUSH_ENTER)
    show_image('bones_brothers', 'Бледные Братья')
    print(chapter_4.B)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    if result == '2':
        print()
        if check_have_dagger():
            print(chapter_4.X_1)
        else:
            print(chapter_4.X_2)
            show_image('rat_on_stick', 'Крыса на палочке')
        input(clr.PUSH_ENTER)
    else:
        print()
    print(chapter_4.C)
    input(clr.PUSH_ENTER)
    show_image('glue', 'Тюбик клея')
    print(chapter_4.D)
    input(clr.PUSH_ENTER)
    print(chapter_4.E)
    input(clr.PUSH_ENTER)
    show_image('tuba_of_charm', 'Чарующая дуда')
    print(chapter_4.F)
    input(clr.PUSH_ENTER)
    show_image('dragon', 'Плутониевый дракон')
    print(chapter_4.G)
    input(clr.PUSH_ENTER)
    show_image('plant', 'Огорошенная трава')
    print(chapter_4.H)
    input(clr.PUSH_ENTER)
    print(chapter_4.IA)
    input(clr.PUSH_ENTER)
    show_image('dead_horse', 'Конь андедный')
    print(chapter_4.J)
    input(clr.PUSH_ENTER)
    chapter_5_func()


def chapter_5_func():
    """Таинственное место."""
    cprint('§ Таинственное место', 'black', attrs=['bold'])
    save_game('chapter_5')
    print(chapter_5.A)
    input(clr.PUSH_ENTER)
    show_image('oil_lamp', 'Та самая лампа...')
    print(chapter_5.B)
    input(clr.PUSH_ENTER)
    print(chapter_5.C)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        print(chapter_5.D_1)
        input(clr.PUSH_ENTER)
    if result == '2':
        print(chapter_5.D_2)
        input(clr.PUSH_ENTER)
    print(chapter_5.E)
    input(clr.PUSH_ENTER)
    print(chapter_5.F)
    input(clr.PUSH_ENTER)
    print(chapter_5.G)
    input(clr.PUSH_ENTER)
    show_image('princess_kenny', 'Принцесса Кенни')
    chapter_6_func()


def chapter_6_func():
    """Серьёзный разговор."""
    cprint('§ Серьёзный разговор', 'black', attrs=['bold'])
    save_game('chapter_6')
    print(chapter_6.MISTAKE)
    input(clr.PUSH_ENTER)
    playsound('skrimer')
    time.sleep(0.2)
    show_image('princess_terrible', 'Буууууууууу!')
    print(chapter_6.MISTAKE_1)
    input(clr.PUSH_ENTER)
    show_image('princess_ugly', 'О, какая красотка! Как тебе?')
    print(chapter_6.MISTAKE_2)
    input(clr.PUSH_ENTER)
    show_image('princess', 'Теперь-то доволен? Всё устраивает?')
    print(chapter_6.A)
    input(clr.PUSH_ENTER)
    print(chapter_6.B)
    input(clr.PUSH_ENTER)
    print(chapter_6.C)
    input(clr.PUSH_ENTER)
    print(chapter_6.D)
    input(clr.PUSH_ENTER)
    playsound('kirkorov')
    show_image('kirkorov', 'Истинный король эстрады!!!')
    print(chapter_6.E)
    input(clr.PUSH_ENTER)
    print(chapter_6.F)
    input(clr.PUSH_ENTER)
    print(chapter_6.G)
    input(clr.PUSH_ENTER)
    playsound('star_wars')
    show_image('star_wars', 'Гонятся за Дартом Вейдером')
    print(chapter_6.G_1)
    input(clr.PUSH_ENTER)
    show_image('mademonuazeli', 'Мадемонуазели')
    print(chapter_6.G_2)
    input(clr.PUSH_ENTER)
    print(chapter_6.H)
    input(clr.PUSH_ENTER)
    print(chapter_6.H_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        print(chapter_6.H_1)
        input(clr.PUSH_ENTER)
    if result == '2':
        print(chapter_6.H_2)
        input(clr.PUSH_ENTER)
    print(chapter_6.IA)
    input(clr.PUSH_ENTER)
    print(chapter_6.J)
    input(clr.PUSH_ENTER)
    print(chapter_6.K)
    input(clr.PUSH_ENTER)


def chapter_7_func():
    """Радужные перспективы."""
    cprint('§ Радужные перспективы', 'black', attrs=['bold'])
    save_game('chapter_7')
    print(chapter_7.A)
    input(clr.PUSH_ENTER)
    print(chapter_7.B)
    input(clr.PUSH_ENTER)
    show_image('octaedron', 'Желатиновый октаэдр')
    print(chapter_7.C)
    input(clr.PUSH_ENTER)
    print(chapter_7.D)
    input(clr.PUSH_ENTER)
    print(chapter_7.E)
    input(clr.PUSH_ENTER)
    show_image('kalmadzilla', 'Кальмадзилла\n от кальмар и годзилла')
    print(chapter_7.E_1)
    input(clr.PUSH_ENTER)
    print(chapter_7.F)
    input(clr.PUSH_ENTER)
    show_image('druid', 'Чародей из любой RPG игры')
    print(chapter_7.G)
    input(clr.PUSH_ENTER)
    print(chapter_7.G_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        print(chapter_7.G_1)
        input(clr.PUSH_ENTER)
    if result == '2':
        print(chapter_7.G_2)
        input(clr.PUSH_ENTER)
    print(chapter_7.H)
    input(clr.PUSH_ENTER)
    print(chapter_7.IA)
    input(clr.PUSH_ENTER)
    print(chapter_7.J)
    input(clr.PUSH_ENTER)


if __name__ == '__main__':
    GAME_STAGES = {
        'character_creation': character_creation_func,
        'chapter_1': chapter_1_func,
        'chapter_2': chapter_2_func,
        'chapter_3': chapter_3_func,
        'chapter_4': chapter_4_func,
        'chapter_5': chapter_5_func,
        'chapter_6': chapter_6_func,
        'chapter_7': chapter_7_func
    }
    # Screen.wrapper(animation)
    start_game()
    # chapter_7_func()
