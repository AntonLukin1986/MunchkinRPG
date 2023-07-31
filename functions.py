"""Модуль с дополнительными функциями для игры."""
from pathlib import Path

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
        db['IN_PROGRESS'] = current_stage
    cprint('¶ Контрольная точка сохранения ¶', 'blue')
    print('•' * 32)


def show_image(image_name: str, description: str) -> None:
    """Показать окно с картинкой."""
    import re
    import tkinter as tk

    IMAGES_DIR = Path(__file__).resolve().parent / 'images/'
    NO_IMAGE = ('Здесь должна была быть\nкрасивая картинка,\n'
                'но её украли гномы...')

    window = tk.Tk()
    window.title('Манчкин RPG')
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
        text='Для продолжения закрой это окно',
        font='Calibri 14',
        foreground='black',
        background='yellow'
    )
    label.pack()
    window.mainloop()


def game_begins(screen) -> None:
    """Анимация начала игры после создания персонажа."""
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
            SpeechBubble('Нажми Q для продолжения'),
            screen.height-5,
            speed=1,
            transparent=False
        )
    ]
    screen.play([Scene(effects, 500)])


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
            SpeechBubble('Нажми Q чтобы начать'),
            screen.height-5,
            speed=1,
            transparent=False
        )
    ]
    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


def playsound(filename: str) -> None:
    '''Проигрывание звуков в игре.'''
    from playsound import playsound
    MP3_PATH = str(Path(__file__).resolve().parent / f'mp3/{filename}.mp3')
    playsound(MP3_PATH, False)  # False - выполнять асинхронно


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


def save_race_klass(race_klass: str) -> None:
    """Сохранение информации о расе и классе персонажа."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        db['RACE_KLASS'] = race_klass  # строка в формате "Раса-Класс"


def save_rank(rank: int) -> None:
    """Сохранение значения ранга персонажа."""
    import shelve

    with shelve.open(SAVES_PATH) as db:
        db['RANK'] = rank
