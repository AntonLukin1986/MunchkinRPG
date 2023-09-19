"""Модуль с дополнительными функциями для игры."""
from pathlib import Path
import sys
from typing import Union

# путь для exe-шника одним файлом
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    DIRNAME = 'Munchkin RPG'
    SAVES_FILE = 'game_progress'
    SAVES_DIR = Path.home() / DIRNAME
    if not SAVES_DIR.exists():
        SAVES_DIR.mkdir()
    SAVES_PATH = str(SAVES_DIR / SAVES_FILE)
else:
    SAVES_PATH = str(Path(__file__).resolve().parent / 'saves/game_progress')


def teleprint(*args, delay=0.05, str_join=' ') -> None:
    """Имитация печатания в терминале."""
    import sys
    import time

    text = str_join.join(str(x) for x in args)
    n = len(text)
    for i, char in enumerate(text, 1):
        if i == n:
            char = f'{char}\n'
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def save_game(current_stage: str) -> None:
    """Сохранение текущего прогресса игры."""
    import shelve
    from termcolor import cprint

    with shelve.open(SAVES_PATH) as db:
        db['LAST_SAVE'] = current_stage
    cprint('¶ Контрольная точка сохранения ¶', 'blue')
    print('•' * 32)


def show_image(image_name: str, description: str) -> None:
    """Показать окно с картинкой."""
    import re
    import tkinter as tk

    IMAGES_DIR = Path(__file__).resolve().parent / 'images/text_game'
    NO_IMAGE = ('Здесь должна была быть\nкрасивая картинка,\n'
                'но её украли гномы...')

    window = tk.Tk()
    window.bind('<Escape>', lambda event: window.destroy())
    window.title('Манчкин РПГ')
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
        text='Для продолжения нажми Esc',
        font='Calibri 14',
        foreground='black',
        background='yellow'
    )
    label.pack()
    window.mainloop()


def custom_handler(event) -> None:
    """Обработчик нажатия кнопок, прерывающих анимацию."""
    from asciimatics.event import KeyboardEvent
    from asciimatics.exceptions import StopApplication
    from asciimatics.screen import Screen

    if (isinstance(event, KeyboardEvent) and
       event.key_code == Screen.KEY_ESCAPE):
        raise StopApplication("User quit")


def game_begins(screen) -> None:
    """Анимация после создания персонажа."""
    from asciimatics.effects import Cycle, Print, Stars
    from asciimatics.renderers import FigletText, SpeechBubble
    from asciimatics.scene import Scene

    effects = [
        Cycle(
            screen,
            FigletText('the   game   begins', font='big'),
            int(screen.height / 2 - 8)
        ),
        Stars(screen, 200),
        Print(
            screen,
            SpeechBubble('Нажми Esc для продолжения'),
            screen.height-5,
            speed=1,
            transparent=False
        )
    ]
    screen.play([Scene(effects, 500)], unhandled_input=custom_handler)


def animation(screen) -> None:
    """Анимационная заставка игры."""
    from asciimatics.renderers import FigletText, Fire, SpeechBubble
    from asciimatics.scene import Scene
    from asciimatics.screen import Screen
    from asciimatics.effects import Print
    from pyfiglet import Figlet

    scenes = []
    text = Figlet(font='banner', width=200).renderText('Munchkin RPG')
    print(text)
    effects = [
        Print(
            screen,
            Fire(screen.height, 80, text, 0.4, 40, screen.colours),
            0,
            speed=1,
            transparent=False,
        ),
        Print(
            screen,
            FigletText("Munchkin RPG", "banner"),
            screen.height - 15,
            colour=Screen.COLOUR_WHITE,
            bg=Screen.COLOUR_WHITE,
            speed=1
        ),
        Print(
            screen,
            SpeechBubble('Нажми Esc чтобы начать'),
            screen.height-5,
            speed=1,
            transparent=False
        )
    ]
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=False, unhandled_input=custom_handler)


def playsound(filename: str, sync=False) -> None:
    """Проигрывание звуков в игре."""
    from playsound import playsound
    MP3_PATH = str(Path(__file__).resolve().parent / f'mp3/{filename}.mp3')
    playsound(MP3_PATH, sync)  # False - выполнять асинхронно


def save_dagger(have_dagger: bool) -> None:
    """Сохранение информации о наличии у персонажа Кинжала измены."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        db['HAVE_DAGGER'] = have_dagger


def check_have_dagger() -> bool:
    """Проверка информации о наличии у персонажа Кинажала измены."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        return bool(db['HAVE_DAGGER'])


def save_race_klass(race: str, klass: str) -> None:
    """Сохранение информации о расе и классе персонажа."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        db['RACE'] = race
        db['KLASS'] = klass


def save_rank(rank: int) -> None:
    """Сохранение значения ранга персонажа."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        db['RANK'] = rank


def load_race_klass_rank() -> Union[str, str, int]:
    """Получение данных о расе, классе и ранге персонажа."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        race = db['RACE']
        klass = db['KLASS']
        rank = db['RANK']
    return race, klass, int(rank)


def new_character() -> None:
    """Создаёт персонажа вне текстовой части и запускает уровень с башней."""
    from termcolor import colored, cprint
    import mini_game
    from texts import colored_text as clr

    cprint('Выбери одну из рас: эльф (а), дварф (б) или хафлинг (в)')
    while (choice_1 := input(clr.ENTER_LETTER)).lower() not in ('а', 'б', 'в'):
        pass
    cprint('Выбери один из классов: воин (а), волшебник (б) или клирик (в)')
    while (choice_2 := input(clr.ENTER_LETTER)).lower() not in ('а', 'б', 'в'):
        pass
    race = clr.RACES[choice_1.lower()]
    klass = clr.KLASSES[choice_2.lower()]
    print()
    print('Теперь твой персонаж {}'.format(colored(f'{race}-{klass}',
          'green')))
    input(clr.PUSH_ENTER)
    show_image(clr.FILES_RACES[choice_1], 'раса ' + race)
    show_image(clr.FILES_CLASSES[choice_2], 'класс ' + klass)
    print('Определение ранга. Первый бой - разминка.\n')
    rank = mini_game.start()
    save_race_klass(race, klass)
    save_rank(rank)


def tower_assault() -> None:
    """Запускает прохождение башни Ктулху."""
    from doors_game.main import run_doors_game
    from texts import colored_text as clr

    while run_doors_game(*load_race_klass_rank()) is False:
        print(clr.AGAIN_OR_NEW_PERS)
        while (result := input(clr.CHOICE)) not in ('1', '2'):
            pass
        print()
        if result == '2':
            new_character()


def game_passed() -> None:
    """Сохранение отметки о прохождении игры."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        db['GAME_PASSED'] = True


def change_rating_table(bonus_ratio: bool) -> None:
    """Создаёт и обновляет таблицу рейтинга. Записывает полученные очки за
    последнюю победу над Ктулху."""
    import shelve

    RANKS_POINTS = {0: 40, 1: 30, 2: 25, 3: 20}
    race, klass, rank = load_race_klass_rank()
    total_points = RANKS_POINTS[rank] * (2 if bonus_ratio else 1)
    with shelve.open(SAVES_PATH) as db:
        if 'RATING_TABLE' not in db:
            db['RATING_TABLE'] = [
                ['Дварф', 'Воин', 0, RANKS_POINTS[0], None, 0],
                ['Дварф', 'Воин', 1, RANKS_POINTS[1], None, 0],
                ['Дварф', 'Воин', 2, RANKS_POINTS[2], None, 0],
                ['Дварф', 'Воин', 3, RANKS_POINTS[3], None, 0],
                ['Дварф', 'Волшебник', 0, RANKS_POINTS[0], None, 0],
                ['Дварф', 'Волшебник', 1, RANKS_POINTS[1], None, 0],
                ['Дварф', 'Волшебник', 2, RANKS_POINTS[2], None, 0],
                ['Дварф', 'Волшебник', 3, RANKS_POINTS[3], None, 0],
                ['Дварф', 'Клирик', 0, RANKS_POINTS[0], None, 0],
                ['Дварф', 'Клирик', 1, RANKS_POINTS[1], None, 0],
                ['Дварф', 'Клирик', 2, RANKS_POINTS[2], None, 0],
                ['Дварф', 'Клирик', 3, RANKS_POINTS[3], None, 0],
                ['Хафлинг', 'Воин', 0, RANKS_POINTS[0], None, 0],
                ['Хафлинг', 'Воин', 1, RANKS_POINTS[1], None, 0],
                ['Хафлинг', 'Воин', 2, RANKS_POINTS[2], None, 0],
                ['Хафлинг', 'Воин', 3, RANKS_POINTS[3], None, 0],
                ['Хафлинг', 'Волшебник', 0, RANKS_POINTS[0], None, 0],
                ['Хафлинг', 'Волшебник', 1, RANKS_POINTS[1], None, 0],
                ['Хафлинг', 'Волшебник', 2, RANKS_POINTS[2], None, 0],
                ['Хафлинг', 'Волшебник', 3, RANKS_POINTS[3], None, 0],
                ['Хафлинг', 'Клирик', 0, RANKS_POINTS[0], None, 0],
                ['Хафлинг', 'Клирик', 1, RANKS_POINTS[1], None, 0],
                ['Хафлинг', 'Клирик', 2, RANKS_POINTS[2], None, 0],
                ['Хафлинг', 'Клирик', 3, RANKS_POINTS[3], None, 0],
                ['Эльф', 'Воин', 0, RANKS_POINTS[0], None, 0],
                ['Эльф', 'Воин', 1, RANKS_POINTS[1], None, 0],
                ['Эльф', 'Воин', 2, RANKS_POINTS[2], None, 0],
                ['Эльф', 'Воин', 3, RANKS_POINTS[3], None, 0],
                ['Эльф', 'Волшебник', 0, RANKS_POINTS[0], None, 0],
                ['Эльф', 'Волшебник', 1, RANKS_POINTS[1], None, 0],
                ['Эльф', 'Волшебник', 2, RANKS_POINTS[2], None, 0],
                ['Эльф', 'Волшебник', 3, RANKS_POINTS[3], None, 0],
                ['Эльф', 'Клирик', 0, RANKS_POINTS[0], None, 0],
                ['Эльф', 'Клирик', 1, RANKS_POINTS[1], None, 0],
                ['Эльф', 'Клирик', 2, RANKS_POINTS[2], None, 0],
                ['Эльф', 'Клирик', 3, RANKS_POINTS[3], None, 0]
            ]
        rating_table = db['RATING_TABLE']
        for index, string in enumerate(rating_table):
            if string[0] == race and string[1] == klass and string[2] == rank:
                if string[5] < total_points:
                    rating_table[index][4] = bonus_ratio
                    rating_table[index][5] = total_points
                    db['LAST_POINTS'] = total_points
                else:
                    db['LAST_POINTS'] = False
                break
        db['RATING_TABLE'] = rating_table


def show_last_points() -> str:
    """Отображает полученные очки за победу над Ктулху."""
    import shelve

    POINTS_YES = ('За победу над Ктулху ты получаешь {} очков! '
                  '(рейтинг доступен в главном меню)\n')
    POINTS_NO = (
        'Очки рейтинга не получены! С данным сочетанием расы, класса и '
        'ранга ты уже получал такое же или меньшее количество очков.\n')
    with shelve.open(SAVES_PATH) as db:
        if points := db['LAST_POINTS'] is False:
            return POINTS_NO
        return POINTS_YES.format(points)


def show_rating_table() -> None:
    """Отображает таблицу рейтинга."""
    import shelve
    from prettytable import PrettyTable
    from termcolor import colored
    from texts.colored_text import RATING_LEGEND

    with shelve.open(SAVES_PATH) as db:
        rating = db['RATING_TABLE']
    TEXT_1 = ('У тебя максимально возможный рейтинг {} очков.\n'
              'Неужели ты и вправду существуешь?!\n')
    TEXT_2 = 'Твой текущий рейтинг: {} очков из {} | {}%\n'
    TITLE = [
        colored('Раса', 'blue', attrs=['bold']),
        colored('Класс', 'blue', attrs=['bold']),
        colored('Ранг', 'blue', attrs=['bold']),
        colored('Очки', 'blue', attrs=['bold']),
        colored('Бонус', 'blue', attrs=['bold']),
        colored('Итого', 'blue', attrs=['bold'])
    ]
    table = PrettyTable()
    table.field_names = TITLE
    total_rating_points = 0
    counter = 0
    for string in rating:
        if string[-1] == 0:
            string[-1] = '---'
            string[-2] = '---'
        else:
            total_rating_points += string[-1]
            string[-2] = 'x2' if string[-2] else 'нет'
            string = [colored(cell, 'green', attrs=['bold'])
                      for cell in string]
        if counter == 3:
            table.add_row(string, divider=True)
            counter = 0
        else:
            table.add_row(string)
            counter += 1
    max_rating_points = sum([string[3] for string in rating]) * 2
    if total_rating_points == max_rating_points:
        TEXT_1 = TEXT_1.format(max_rating_points)
        print(colored(TEXT_1, 'green', attrs=['bold']))
    else:
        TEXT_2 = TEXT_2.format(
            total_rating_points, max_rating_points,
            round(total_rating_points / max_rating_points * 100, 2)
        )
        print(colored(TEXT_2, 'green', attrs=['bold']))
    print(RATING_LEGEND)
    print(table)
    return None
