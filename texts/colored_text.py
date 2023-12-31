"""Цветные (и не только) слова и фразы для импорта."""
from termcolor import colored

RACES = {'а': 'Эльф', 'б': 'Дварф', 'в': 'Хафлинг'}
KLASSES = {'а': 'Воин', 'б': 'Волшебник', 'в': 'Клирик'}
FILES_RACES = {'а': 'elf', 'б': 'dwarf', 'в': 'halfling'}
FILES_CLASSES = {'а': 'warrior', 'б': 'wizard', 'в': 'cleric'}

AGAIN_OR_NEW_PERS = colored('Попробовать ещё раз  (введи 1)\nПоменять персонажа   (введи 2)', 'blue')
ATTENTION = '''
{attention} В игре тебе потребуется вводить различный текст.
Кнопка {enter} служит для подтверждения ввода.
Руководствуйся подсказками на экране.
Для выхода из игры нажми {ctrl}+{c} или закрой основное окно.
Играй СО ЗВУКОМ для полного погружения!
'''.format(
    attention=colored('Внимание!', 'red'),
    enter=colored('[Enter]', 'blue', attrs=['bold', 'underline']),
    ctrl=colored('[Ctrl]', 'blue', attrs=['bold', 'underline']),
    c=colored('[C]', 'blue', attrs=['bold', 'underline'])
)
PUSH_ENTER = '{} {} \n'.format(
    colored('Для продолжения нажми', 'blue'),
    colored('[Enter]', 'blue', attrs=['bold', 'underline'])
)

# --- Для функций ---
ANSWER_OPTION = colored('Введи один вариант ответа >>> ', 'blue')
ATAS = colored('Введи фразу активации плаща "Атас, меня спалили!" >>> ', 'blue')
CHAR_DESCR = colored('Введи описание персонажа >>> ', 'blue')
CHOICE = colored('Сделай выбор 1 или 2 >>> ', 'blue')
ENTER_LETTER = colored('Введи букву >>> ', 'blue')
FORGIVE_ME = colored('Введи "Простите меня, я больше так не буду" >>> ', 'blue')
PRINT_NAME = colored('Придумай и напиши имя для персонажа >>> ', 'blue')
RATING_LEGEND = '''Зелёным цветом в таблице выделены персонажи, с которыми ты одерживал победу над Ктулху,
и заработанные очки рейтинга («Итого»). За победу над Ктулху без использования волшебной фразы
«последнего шанса» получаешь «Бонус», увеличивающий в 2 раза положенные очки («Очки»).
Чтобы получить максимальный рейтинг, необходимо победить Ктулху всеми уникальными персонажами с
«Бонусом». Если каким-то из персонажей ты не смог получить «Бонус», то можешь попытаться снова.
В случае успеха значения в графах «Бонус» и «Итого» будут обновлены.
'''
ROLL_DICE = colored('Введи "бросаю кубик" >>> ', 'blue')
SHOW_DAGGER = colored('Введи "Отдать кинжал" >>> ', 'blue')
START_GAME = colored('Для начала игры введи "Начать" >>> ', 'blue')
USE_CHEET_DICE = colored('Введи "Использовать читерский кубик" >>> ', 'blue')
WHAT_FILM = colored('Помнишь, что за фильм? >>> ', 'blue')
YES_OR_NO = colored('Введи «Да» или «Нет» >>> ', 'blue')
CHALLENGE = '''\nОднажды ты уже победил Великого Ктулху. Но если хочешь больше славы - повтори свой успех,
управляя персонажем другой расы, класса и ранга. Собери полную коллекцию достижений и получи
максимальный рейтинг. Стань главным задротом этой игры!'''

# --- Для импорта в тексты разных глав ---
BONES_BROTHERS = colored('Бледные братья', 'red')
CHAR_NAME = colored('Знатный Вонючка', 'yellow')
CHEET_DICE = colored('Читерский кубик', 'green')
CLOAK = colored('Плащ замутнённости', 'green')
CTHULHU = colored('Великий и Ужасный Ктулху', 'red')
DAGGER = colored('Кинжал измены', 'green')
DEAD_HORSE = colored('Конь Андедный', 'red')
DUCKBILL = colored('Утконтикора', 'red')
FAST_BOOTS = colored('Башмаки реально быстрого бега', 'green')
FRUSTLAND = colored('Фрустландия', 'yellow')
GIPPOGRIF = colored('Гиппогриф', 'red')
GLUE = colored('Тюбик клея', 'green')
GOBLIN = colored('Увечный гоблин', 'red')
KALMADZILLA = colored('Кальмадзилла', 'red')
MADEMONUAZELI = colored('Мадемонуазели', 'red')
COUNTRY = colored('Вымышляндия', 'yellow')
NOSE = colored('Блуждающий нос', 'red')
OCTAEDRON = colored('Желатиновый октаэдр', 'red')
PRINCESS = colored('Ариэлла', 'yellow')
RAT_ON_STICK = colored('Крыса на палочке', 'green')
STINK_POTION = colored('Зелье ротовой вони', 'green')
THE_END = colored('Игра создана по мотивам настолки «Манчкин» её преданным поклонником shahter86@mail.ru', 'green')
WALL = colored('Стенка-мгновенка', 'green')
