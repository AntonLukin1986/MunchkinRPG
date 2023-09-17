"""Ролевая игра по мотивам настолки «Манчкин»."""
import time
import shelve

from asciimatics.screen import Screen
from colorama import just_fix_windows_console
from termcolor import colored, cprint

from functions import (
    animation, check_have_dagger, game_begins, game_passed, # game_passed_by,
    new_character, playsound, save_dagger, save_game, SAVES_PATH, save_rank,
    save_race_klass, show_image, teleprint, tower_assault
)
from doors_game.text import DOORS_INTRO
import mini_game
from texts import (
    chapter_1, chapter_2, chapter_3, chapter_4, chapter_5, chapter_6,
    chapter_7, chapter_8, chapter_9, chapter_10, chapter_12,
    character_creation, colored_text as clr
)
from texts.intro import INTRO_1, INTRO_2

just_fix_windows_console()  # use Colorama to make Termcolor work on Windows


def start_game():
    """Стартовое меню игры."""
    print('╤' * 63, clr.ATTENTION, '╧' * 63, '\n', sep='\n')
    cprint('► Г Л А В Н О Е   М Е Н Ю ◄', 'black', attrs=['bold'])
    print('▬' * 27)
    with shelve.open(SAVES_PATH) as db:
        last_save = db.get('LAST_SAVE')
        game_passed = db.get('GAME_PASSED')
    if last_save is None:
        while input(clr.START_GAME).lower() != 'начать':
            pass
        return play_intro()
    cprint('Введи "Заново" - начать игру с самого начала', 'blue', end='')
    cprint(' (последнее сохранение будет сброшено!)', 'red')
    cprint('Введи "Продолжить" - загрузить последнее сохранение', 'blue')
    checking = ['заново', 'продолжить']
    if game_passed is not None:
        cprint('Введи "Рейтинг" - покоряй башню повторно и получи '
               'максимальный рейтинг', 'blue')
        checking.append('рейтинг')
    while (decision := input(colored('>>> ', 'blue')).lower()) not in checking:
        pass
    if decision == 'заново':
        print()
        return play_intro()
    if decision == 'продолжить':
        print()
        return GAME_STAGES[last_save]()
    if decision == 'рейтинг':
        print()
        teleprint(clr.CHALLENGE)
        input(clr.PUSH_ENTER)
        #функция отображения таблицы со статой на основе game_passed_by()
        teleprint('Вперёд, к победе!')
        input(clr.PUSH_ENTER)
        new_character()
        tower_assault()
        #изменение рейтинга на основании текущего класса, расы и ранга
        return start_game()


def play_intro():
    """Введение."""
    cprint('§ Введение', 'black', attrs=['bold'])
    print('•' * 27)
    teleprint(INTRO_1)
    input(clr.PUSH_ENTER)
    show_image('country', 'Вымышляндия')
    teleprint(INTRO_2)
    input(clr.PUSH_ENTER)
    return play_character_creation()


def play_character_creation():
    """Создание персонажа."""
    cprint('§ Создание персонажа', 'black', attrs=['bold'])
    save_game('character_creation')
    time.sleep(1)
    teleprint(character_creation.A)
    input(clr.PUSH_ENTER)
    teleprint(character_creation.DESCRIBE_CHARACTER)
    while len(input(clr.CHAR_DESCR)) < 100:
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
    return play_chapter_1()


def play_chapter_1():
    """Начало."""
    cprint('§ Начало', 'black', attrs=['bold'])
    save_game('chapter_1')
    time.sleep(1)
    teleprint(chapter_1.A)
    input(clr.PUSH_ENTER)
    playsound('birds_song')
    show_image('city', 'городок Токийск Алтайского края')
    teleprint(chapter_1.A_2)
    input(clr.PUSH_ENTER)
    show_image('thief', 'класс Вор')
    teleprint(chapter_1.B_1)
    input(clr.PUSH_ENTER)
    show_image('dagger', 'Кинжал измены')
    show_image('cloak', 'Плащ замутнённости')
    teleprint(chapter_1.B_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.C)
    input(clr.PUSH_ENTER)
    playsound('shatunov')
    show_image('market', 'Белые розы, белые розы - беззащитны шипы...')
    teleprint(chapter_1.D)
    input(clr.PUSH_ENTER)
    cprint(chapter_1.TRY_TO_THIEF, 'blue')
    while input(clr.ROLL_DICE).lower() != 'бросаю кубик':
        pass
    print()
    playsound('dice')
    time.sleep(2)
    show_image('dice_six', 'На кубике выпало...')
    teleprint(chapter_1.THEFT_SUCCESS)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.E)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.OTHER_THEFT, '\n')
    while input(clr.ROLL_DICE).lower() != 'бросаю кубик':
        pass
    print()
    playsound('dice')
    time.sleep(2)
    show_image('dice_one', 'На кубике выпало...')
    teleprint(chapter_1.OTHER_THEFT_FAIL)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.DANGER)
    teleprint(chapter_1.CHEET_DICE)
    print()
    while input(clr.USE_CHEET_DICE).lower() != 'использовать читерский кубик':
        pass
    print()
    time.sleep(1)
    show_image('cheet_dice', 'Читерский кубик')
    teleprint(chapter_1.OTHER_THEFT_SUCCESS)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.F)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.F_2)
    print()
    while input(
        clr.FORGIVE_ME
    ).lower() != 'простите меня, я больше так не буду':
        pass
    print()
    teleprint(chapter_1.G)
    input(clr.PUSH_ENTER)
    teleprint(chapter_1.H)
    input(clr.PUSH_ENTER)
    show_image('market_fight', 'Самое "уютное" местечко в городке...')
    return play_chapter_2()


def play_chapter_2():
    """Погоня."""
    cprint('§ Погоня', 'black', attrs=['bold'])
    save_game('chapter_2')
    time.sleep(1)
    teleprint(chapter_2.A)
    input(clr.PUSH_ENTER)
    show_image('lame_goblin', 'Увечный гоблин')
    show_image('platycore', 'Утконтикора')
    teleprint(chapter_2.A_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.B)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.C)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.C_2)
    input(clr.PUSH_ENTER)
    show_image('fast_boots', 'Башмаки реально быстрого бега')
    teleprint(chapter_2.C_3)
    input(clr.PUSH_ENTER)
    show_image('instant_wall', 'Стенка-мгновенка')
    teleprint(chapter_2.D)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.E)
    print()
    while input(clr.ATAS).lower() != 'атас, меня спалили!':
        pass
    print()
    teleprint(chapter_2.F)
    input(clr.PUSH_ENTER)
    show_image('onion_bag', 'Маскировка восьмидесятого левела')
    teleprint(chapter_2.G)
    input(clr.PUSH_ENTER)
    show_image('gippogrif', 'Гиппогриф (второй за кадром)')
    teleprint(chapter_2.H_1)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.H_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.H_3)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.IA)
    input(clr.PUSH_ENTER)
    playsound('danger')
    show_image('floating_nose', 'Блуждающий нос')
    teleprint(chapter_2.J)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.K)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.L)
    input(clr.PUSH_ENTER)
    teleprint(chapter_2.M)
    input(clr.PUSH_ENTER)
    return play_chapter_3()


def play_chapter_3():
    """Развязка."""
    cprint('§ Развязка', 'black', attrs=['bold'])
    save_game('chapter_3')
    time.sleep(1)
    teleprint(chapter_3.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_3.EXP_1)
    input(clr.PUSH_ENTER)
    teleprint(chapter_3.EXP_2)
    input(clr.PUSH_ENTER)
    show_image('pursuit', 'Без преувеличения - эпическая погоня!')
    show_image('plasmic_gun', 'Эка диковина приблуда')
    teleprint(chapter_3.EXP_3)
    print()
    while input(clr.WHAT_FILM) == '':
        pass
    print()
    teleprint(chapter_3.EXP_4)
    input(clr.PUSH_ENTER)
    teleprint(chapter_3.B)
    input(clr.PUSH_ENTER)
    show_image('stink_potion', 'Зелье ротовой вони')
    teleprint(chapter_3.C)
    input(clr.PUSH_ENTER)
    print(chapter_3.DECISION)
    while ((choise := input(clr.CHOICE))not in ('1', '2')):
        pass
    print()
    if choise == '2':
        teleprint(chapter_3.D)
        input(clr.PUSH_ENTER)
        show_image('monster_killed', 'Типа победил Носа...')
        teleprint(chapter_3.E)
        have_dagger = True
    elif choise == '1':
        teleprint(chapter_3.F)
        print()
        while input(clr.SHOW_DAGGER).lower() != 'отдать кинжал':
            pass
        print()
        teleprint(chapter_3.G)
        input(clr.PUSH_ENTER)
        show_image('dagger', 'Кинжал измены')
        teleprint(chapter_3.H)
        have_dagger = False
    input(clr.PUSH_ENTER)
    teleprint(chapter_3.IA)
    input(clr.PUSH_ENTER)
    save_dagger(have_dagger)
    return play_chapter_4()


def play_chapter_4():
    """Неожиданный поворот."""
    cprint('§ Неожиданный поворот', 'black', attrs=['bold'])
    save_game('chapter_4')
    time.sleep(1)
    teleprint(chapter_4.A)
    input(clr.PUSH_ENTER)
    show_image('bones_brothers', 'Бледные Братья')
    print(chapter_4.B_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    if result == '2':
        print()
        if check_have_dagger():
            teleprint(chapter_4.X_1)
            input(clr.PUSH_ENTER)
        else:
            teleprint(chapter_4.X_2)
            input(clr.PUSH_ENTER)
            show_image('rat_on_stick', 'Крыса на палочке')
    elif result == '1':
        print()
        teleprint(chapter_4.C)
        input(clr.PUSH_ENTER)
        show_image('glue', 'Тюбик клея')
    teleprint(chapter_4.D)
    input(clr.PUSH_ENTER)
    teleprint(chapter_4.E)
    input(clr.PUSH_ENTER)
    show_image('tuba_of_charm', 'Чарующая дуда')
    teleprint(chapter_4.F)
    input(clr.PUSH_ENTER)
    show_image('dragon', 'Плутониевый дракон')
    teleprint(chapter_4.G)
    input(clr.PUSH_ENTER)
    show_image('plant', 'Огорошенная трава')
    teleprint(chapter_4.H)
    input(clr.PUSH_ENTER)
    teleprint(chapter_4.IA)
    input(clr.PUSH_ENTER)
    show_image('dead_horse', 'Конь андедный')
    teleprint(chapter_4.J)
    input(clr.PUSH_ENTER)
    return play_chapter_5()


def play_chapter_5():
    """Таинственное место."""
    cprint('§ Таинственное место', 'black', attrs=['bold'])
    save_game('chapter_5')
    time.sleep(1)
    teleprint(chapter_5.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_5.A_1)
    input(clr.PUSH_ENTER)
    show_image('oil_lamp', 'Та самая лампа...')
    teleprint(chapter_5.B)
    input(clr.PUSH_ENTER)
    print(chapter_5.CHOISE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        teleprint(chapter_5.D_1)
    elif result == '2':
        teleprint(chapter_5.D_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_5.E)
    input(clr.PUSH_ENTER)
    teleprint(chapter_5.F)
    input(clr.PUSH_ENTER)
    teleprint(chapter_5.G)
    input(clr.PUSH_ENTER)
    show_image('princess_kenny', 'Принцесса Кенни')
    return play_chapter_6()


def play_chapter_6():
    """Серьёзный разговор."""
    cprint('§ Серьёзный разговор', 'black', attrs=['bold'])
    save_game('chapter_6')
    time.sleep(1)
    teleprint(chapter_6.MISTAKE)
    input(clr.PUSH_ENTER)
    playsound('skrimer')
    time.sleep(0.2)
    show_image('princess_terrible', 'Буууууууууу!')
    teleprint(chapter_6.MISTAKE_1)
    input(clr.PUSH_ENTER)
    show_image('princess_ugly', 'О, какая красотка! Как тебе?')
    teleprint(chapter_6.MISTAKE_2)
    input(clr.PUSH_ENTER)
    show_image('princess', 'Теперь-то доволен? Всё устраивает?')
    teleprint(chapter_6.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.B)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.C)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.D)
    input(clr.PUSH_ENTER)
    playsound('kirkorov')
    show_image('kirkorov', 'Истинный король эстрады!!!')
    teleprint(chapter_6.E)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.F)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.G)
    input(clr.PUSH_ENTER)
    playsound('star_wars')
    show_image('star_wars', 'Гонятся за Дартом Вейдером')
    teleprint(chapter_6.G_1)
    input(clr.PUSH_ENTER)
    show_image('mademonuazeli', 'Мадемонуазели')
    teleprint(chapter_6.G_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.H)
    input(clr.PUSH_ENTER)
    print(chapter_6.H_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        teleprint(chapter_6.H_1)
    elif result == '2':
        teleprint(chapter_6.H_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.IA)
    input(clr.PUSH_ENTER)
    show_image('cthulhu', 'Великий и ужасный Ктулху')
    teleprint(chapter_6.J)
    input(clr.PUSH_ENTER)
    teleprint(chapter_6.K)
    input(clr.PUSH_ENTER)
    return play_chapter_7()


def play_chapter_7():
    """Радужные перспективы."""
    cprint('§ Радужные перспективы', 'black', attrs=['bold'])
    save_game('chapter_7')
    time.sleep(1)
    teleprint(chapter_7.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.B)
    input(clr.PUSH_ENTER)
    show_image('octaedron', 'Желатиновый октаэдр')
    teleprint(chapter_7.C)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.D)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.E)
    input(clr.PUSH_ENTER)
    show_image('kalmadzilla', 'Кальмадзилла\n от кальмар и годзилла')
    teleprint(chapter_7.E_1)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.F)
    input(clr.PUSH_ENTER)
    show_image('druid', 'Чародей из любой RPG игры')
    teleprint(chapter_7.G)
    input(clr.PUSH_ENTER)
    print(chapter_7.G_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        teleprint(chapter_7.G_1)
    elif result == '2':
        teleprint(chapter_7.G_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.H)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.IA)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.J)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.K)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.L)
    input(clr.PUSH_ENTER)
    while input(chapter_7.M).lower() != chapter_7.M_1.lower():
        pass
    print()
    teleprint(chapter_7.N)
    input(clr.PUSH_ENTER)
    teleprint(chapter_7.OA)
    input(clr.PUSH_ENTER)
    show_image('tester', 'Эта штука изменит твою жизнь навсегда!')
    teleprint(chapter_7.OA_1)
    input(clr.PUSH_ENTER)
    return play_chapter_8()


def play_chapter_8():
    """Специальная подготовка."""
    cprint('§ Специальная подготовка', 'black', attrs=['bold'])
    save_game('chapter_8')
    time.sleep(1)
    teleprint(chapter_8.A)
    input(clr.PUSH_ENTER)
    playsound('fanfars')
    show_image('fanfars', 'Фанфары в твою честь')
    teleprint(chapter_8.B)
    input(clr.PUSH_ENTER)
    for question in (
        chapter_8.C_1, chapter_8.C_2, chapter_8.C_3, chapter_8.C_4
    ):
        print(question)
        while input(clr.ANSWER_OPTION).lower() not in ('а', 'б', 'в', 'г'):
            pass
        print()
    print(chapter_8.C_5)
    while (choice_1 := input(clr.ANSWER_OPTION)).lower() not in (
        'а', 'б', 'в'
    ):
        pass
    print()
    teleprint(chapter_8.D)
    input(clr.PUSH_ENTER)
    print(chapter_8.E_1)
    while input(clr.ANSWER_OPTION).lower() not in ('а', 'б', 'в'):
        pass
    print()
    show_image('fallout', 'Из теста К.О.З.А.')
    print(chapter_8.E_2)
    while input(clr.ANSWER_OPTION).lower() not in ('а', 'б', 'в'):
        pass
    print()
    print(chapter_8.F)
    while (choice_2 := input(clr.ANSWER_OPTION)).lower() not in (
        'а', 'б', 'в'
    ):
        pass
    cprint('\n► Тестирование успешно завершено! Обработка результатов...\n',
           'blue')
    time.sleep(3)
    teleprint(chapter_8.G)
    input(clr.PUSH_ENTER)
    race = clr.RACES[choice_1.lower()]
    klass = clr.KLASSES[choice_2.lower()]
    teleprint(chapter_8.H.format(char=clr.CHAR_NAME,
                                 result=colored(f'{race}-{klass}', 'green')))
    input(clr.PUSH_ENTER)
    show_image(clr.FILES_RACES[choice_1], 'раса ' + race)
    show_image(clr.FILES_CLASSES[choice_2], 'класс ' + klass)
    teleprint(chapter_8.IA)
    input(clr.PUSH_ENTER)
    teleprint(chapter_8.J)
    input(clr.PUSH_ENTER)
    save_race_klass(race, klass)
    return play_chapter_9()


def play_chapter_9():
    """Чебуратор."""
    cprint('§ Чебуратор', 'black', attrs=['bold'])
    save_game('chapter_9')
    time.sleep(1)
    teleprint(chapter_9.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_9.Aa)
    input(clr.PUSH_ENTER)
    teleprint(chapter_9.B)
    input(clr.PUSH_ENTER)
    teleprint(chapter_9.C)
    input(clr.PUSH_ENTER)
    playsound('garmon')
    show_image('cheburator', 'Серьёзно? Он сделал из Гены гармошку?!!')
    teleprint(chapter_9.Cc)
    input(clr.PUSH_ENTER)
    print(chapter_9.D_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        teleprint(chapter_9.D_1)
    elif result == '2':
        teleprint(chapter_9.D_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_9.E)
    input(clr.PUSH_ENTER)
    teleprint(chapter_9.F)
    input(clr.PUSH_ENTER)
    teleprint(chapter_9.G)
    input(clr.PUSH_ENTER)
    print(mini_game.RULES_1)
    input(clr.PUSH_ENTER)
    print(mini_game.RULES_2)
    input(clr.PUSH_ENTER)
    rank = mini_game.start()
    save_rank(rank)
    print(chapter_9.H.format(rank, colored(f'{rank} ранг', 'green')))
    input(clr.PUSH_ENTER)
    return play_chapter_10()


def play_chapter_10():
    """Портал."""
    cprint('§ Портал', 'black', attrs=['bold'])
    save_game('chapter_10')
    time.sleep(1)
    teleprint(chapter_10.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_10.B)
    input(clr.PUSH_ENTER)
    teleprint(chapter_10.C)
    input(clr.PUSH_ENTER)
    teleprint(chapter_10.D)
    input(clr.PUSH_ENTER)
    show_image('portal', 'Порталус Маджификус')
    teleprint(chapter_10.E)
    input(clr.PUSH_ENTER)
    teleprint(chapter_10.F)
    input(clr.PUSH_ENTER)
    teleprint(chapter_10.G)
    input(clr.PUSH_ENTER)
    print(chapter_10.H_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        teleprint(chapter_10.H_1)
    elif result == '2':
        teleprint(chapter_10.H_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_10.J)
    input(clr.PUSH_ENTER)
    return play_chapter_11()


def play_chapter_11():
    """Башня Ктулху."""
    cprint('§ Башня Ктулху', 'black', attrs=['bold'])
    save_game('chapter_11')
    time.sleep(1)
    teleprint(DOORS_INTRO)
    input(clr.PUSH_ENTER)
    tower_assault()
    return play_chapter_12()


def play_chapter_12():
    """Хэппи энд."""
    cprint('§ Хэппи энд', 'black', attrs=['bold'])
    save_game('chapter_12')
    time.sleep(1)
    teleprint(chapter_12.A)
    input(clr.PUSH_ENTER)
    teleprint(chapter_12.B)
    input(clr.PUSH_ENTER)
    teleprint(chapter_12.C)
    input(clr.PUSH_ENTER)
    teleprint(chapter_12.D)
    input(clr.PUSH_ENTER)
    print(chapter_12.E_CHOICE)
    while (result := input(clr.CHOICE)) not in ('1', '2'):
        pass
    print()
    if result == '1':
        teleprint(chapter_12.E_1)
    elif result == '2':
        teleprint(chapter_12.E_2)
    input(clr.PUSH_ENTER)
    teleprint(chapter_12.F)
    input(clr.PUSH_ENTER)
    teleprint(chapter_12.G)
    input(clr.PUSH_ENTER)
    playsound('alarm_clock', True)
    time.sleep(1)
    teleprint(chapter_12.H)
    input(clr.PUSH_ENTER)
    teleprint(chapter_12.J)
    input(clr.PUSH_ENTER)
    print(f'{colored("Конец игры!", "blue", attrs=["bold"])}\n')
    game_passed()
    #записать в рейтинг и вывести полученные очки рейтинга за текущее прохождение
    teleprint(clr.THE_END)
    input(f'{colored("Для завершения нажми", "blue")} '
          f'{colored("[Enter]", "blue", attrs=["bold", "underline"])}')
    return None


if __name__ == '__main__':
    GAME_STAGES = {
        'character_creation': play_character_creation,
        'chapter_1': play_chapter_1,
        'chapter_2': play_chapter_2,
        'chapter_3': play_chapter_3,
        'chapter_4': play_chapter_4,
        'chapter_5': play_chapter_5,
        'chapter_6': play_chapter_6,
        'chapter_7': play_chapter_7,
        'chapter_8': play_chapter_8,
        'chapter_9': play_chapter_9,
        'chapter_10': play_chapter_10,
        'chapter_11': play_chapter_11,
        'chapter_12': play_chapter_12
    }
    try:
        #Screen.wrapper(animation)
        start_game()
    except Exception as error:
        print(f'{colored("!!! Критическая ошибка !!!", "red")}\n{error}')
        input('Нажатие Enter завершит работу программы...')
