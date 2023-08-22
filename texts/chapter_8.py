"""Текст для функции play_chapter_8. Специальная подготовка."""
from termcolor import colored

from texts import colored_text as clr

A = '''Поздравляю, {}! Ты стоишь на пороге великих свершений!
Судьба, а так же больное воображение сценариста, предоставили тебе великолепный шанс изменить
своё жалкое существование и вписать собственное имя золотыми буквами {}-ом на доску почёта
Выдающихся задротов ролевых игр.'''.format(clr.CHAR_NAME, colored('CAPS LOCK', 'black', attrs=['underline']))

B = '''Перед тем, как начать денацификацию и демилитаризацию {}, тебя нужно основательно подготовить.
Сейчас ты пройдёшь специальный лингво-генетический тест, который определит, какой фэнтезийной рассе
соответствует твоя ментальная сущность. Сосредоточься и ответь на следующие вопросы:'''.format(colored('Фрустландии', 'yellow'))

C_1 = '''1. Я никогда не замечал на клавиатуре компьютера клавишу с надписью "SysRq":
а) да   б) нет   в) R2D2   г) трололо'''

C_2 = '''2. Я иногда обращаюсь за советом к своей кошке (собаке, попугайчику):
а) да   б) нет   в) шикака   г) тсссс!'''

C_3 = '''3. Я считаю, что инопланетяне живут среди нас:
а) да   б) нет   в) Оумуамуа   г) я прибыл из далёкой галактики...'''

C_4 = '''4. Како бресно jармилjевка развjалки чмошка?
а) Бркма   б) Жжко   в) Трквja   г) Чфрчко'''

C_5 = '''5. Просыпаясь утром ты первым делом думаешь о том, что:
   а) Как жаль, что я не родился {}. Ведь они такие крутые: обладают длинными, заострёнными ушами;
   всегда находятся в единении с природой и являются непревзойдёнными лучниками и долгожителями.
   б) Как бы мне хотелось однажды проснуться и бонаружить, что я {}. Я был бы низкорослым, коренастым
   и бородатым; жил под землёй и искусно орудовал боевым топором. Время от времени помогал бы искать
   хоббитам их волшебные кольца.
   в) Вот бы мне хотя бы денёк побыть {}. Я был бы похож на маленького волосатого человчка; обладал
   бы выдающейся ловкостью и обожал собирать и прятать в заначки золото.'''.format(
    colored('Эльфом', 'green'),
    colored('Дварф', 'green'),
    colored('Хафлингом', 'green')
)

D = '''Следующий тест определит, навыки какого боевого класса подходят для твоего уровня интеллектуально-
техногенного развития. Постарайся дать правильные ответы на следующие вопросы:'''

E_1 = '''1. Чему равен Икс в уравнении
(6A + 4B)cos3x + (4A - 6B)sin3x + x((-5A)sin3x + (12A - 5B)cos3x) + (25A*sin3x + 25B*cosX) = sinx:
a) 1   б) 11   в) 111'''

E_2 = '''2. К вам подбегает очумевший учёный и кричит: «Я всажу свой квантовый гармонизатор в вашу фотонно-резонаторную камеру!»
Что ты ответишь?
а) Но, доктор, это же вызовет параболическую дестабилизацию сингулярности расщепления!
б) А как же тогда наша Лазерно-интерферометрическая гравитационно-волновая обсерватория?
в) Кажется, вы забыли вовремя принять селективный ингибитор обратного захвата серотонина.'''

F = '''3. Если бы ты мог выбрать, какое оружие ты бы предпочёл всем остальным?
а) двуручный меч и боевой щит;
б) волшебный посох и магические заклинания;
в) святая вода и вмешательство божественных сил.'''

G = '''Аппарат начинает громко жужжать и трястись, мигая разноцветными огоньками, после чего выдаёт
маленький флакон с малинового цвета жидкостью, на котором написано «Выпей меня!».
"Надеюсь это с алкоголем",- подумал ты, после чего взял флакон и, зажмурившись от страха,
залпом выпил всё его содержимое. По вкусу оно напоминало бабушкин ягодный кисель.'''

H = '''Вдруг с тобой начинают происходить таинственные мистические метаморфозы.
Ты чувствуешь лёгкое головокружение и покалывание в животе.
Тебя окутывает белое искрящееся облако и кажется, что все части тела будо-бы выкручиваются наизнанку.
Через несколько секунд облако рассеивается и, открыв глаза, ты с удивлением обнаруживаешь, что
непостижимым образом трансформировался из человека-вора в {result}.
Хотя и по-прежнему остался {char} - теперь это имя с тобой до самого конца. Смирись!'''

IA = '''"Ну ничего себе!- воскликнул ты, рассматривая нового себя,- такого эффекта я точно не ожидал!"
"А можно мне с помощью этого чудо аппарата превратиться в Брэда Пита? Или хотя бы в Дольфа Лундгрена?"
"Максимум - в Михаила Пореченкова, кто бы это ни был",- ухмыльнулся бард...'''

J = '''"На следующем этапе тебе предстоит сдать нормативы общей физической подготовки, на основании которых
будут определены твои персональные характеристики силы, ловкости, выносливости и здоровья",- сказал Паладин,
после чего вы отправились на тренировочную площадку.'''
