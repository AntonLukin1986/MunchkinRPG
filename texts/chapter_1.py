"""Текст для функции play_chapter_1. Начало."""
import datetime as dt

from termcolor import colored

from texts import colored_text as clr

SUCCESS = colored('Кража удалась!', 'green')
MONTHS = {
    '01': 'января', '02': 'февраля', '03': 'марта', '04': 'апреля',
    '05': 'мая', '06': 'июня', '07': 'июля', '08': 'августа', '09': 'сентября',
    '10': 'октября', '11': 'ноября', '12': 'декабря'
}
today = dt.date.today().strftime("%d.%m.%Y")
day = today[:2]
month = MONTHS[today[3:5]]
year = int(today[-4:]) + 1894  # год основания Вавилона 1894 до н.э.

A = '''Утром {} года от основания Вавилона ты просыпаешься в своей серой лачуге
на окраине маленького средневекового городка {}.
За окном уже ярко светит улыбчивое солнце; птички радостно заливаются во весь голос;
гномики дружно идут на работу, насвистывая свою любимую песенку;
проходящие по улице горожане, мило улыбаясь, желают друг другу доброго утра и хорошего дня.
Ну прямо идилия какая-то - нарочно и не придумаешь!'''.format(
    colored(f'{day} {month} {year}', 'yellow'), colored('Токийска', 'yellow')
)

A_2 = '''Потерев руками глаза и прогнав остатки дремоты, ты постепенно осознаёшь, что это был
всего лишь сон и никакой ты не храбрый принц, сражавшийся с огромным и ужасным драконом за
сердце прекрасной эльфийской принцессы, а всего лишь обычный, никому ненужный, невзрачный,
скучный человечек. Да к тому же ещё презренный Вор и {}!'''.format(clr.CHAR_NAME)

B_1 = '''"И кто только придумал эти предательские сновидения,- пробормотал ты,- только расстраиваешься утром."
Услышав урчание в животе, ты грустно вздохнул, подумав, что неплохо бы и подкрепиться.
Взглянув на стол и обнаружив там лишь огрызок яблока, да крошки от вчерашнего сворованного пирога,
ты вставил за пояс {dagger}, накинул на плечи {cloak}...'''.format(dagger=clr.DAGGER, cloak=clr.CLOAK)

B_2 = '''...вышел на улицу и неспеша побрёл на местный рынок, намереваясь поживиться чем-нибудь съестным
у зазевавшихся лоточников. Благо за годы бродяжничества и общения со всевозможными антисоциальными
элементами ты неплохо прокачал свои навыки воровства и пакостничества.
Путь был неблизкий и всю дорогу ты развлекал себя тем, что пинал ногами всё, что плохо лежало:
от пустых банок из под пива и цветочных горшков, до задремашего на солнышке старого облезлого пуделя.'''

C = '''Как обычно, утром на рынке было непротолкнуться. Со всех сторон слышалась какафония звуков.
Торговцы старались перекричать друг друга, завлекая покупателей.
Где-то громко мяукнула кошка - продавец рыбы отвесил ей пендаля, чтобы та не зарилась на прилавок.
Совсем рядом кузнец звонко бил молотом о наковальню, ремонтируя плуг для какого-то хлебопашца.
Вдобавок непонятно откуда фоном играла странная песня с незамысловатой мелодией, в которой неведомый
исполнитель пел что-то о белых розах и их беззащитных шипах.
Вяло блуждая вдоль рядов, ты, наконец, добираешься до лавки местного булочника.'''

D = '''Как раз в это время булочник увлечённо выкладывал на прилавок свежеиспечённые калачи и ватрушки.
Воспользовавшись царящей вокруг суетой и дождавшись, когда лавочник отвлечётся на одного
из покупателя, ты пытаешься украсть с прилавка большой и ароматный тердельник с маком...'''

TRY_TO_THIEF = '''Ты собираешься воспользоваться особым умением Вора - воровство (неожиданно!).
Брось кубик: выпадет 4, 5 или 6 - кража удалась. Меньше - тебе несдобровать!'''

THEFT_SUCCESS = f'''Затаив дыхание, ты ждал, каким будет результат твоего броска.
В этот раз тебе улыбнулась удача - на кубике выпало 6. {SUCCESS}'''

E = '''"Проще пареной репы," - подумал ты, спешно отоходя от лотка с тердельником за пазухой.
Отойдя в безопасное место, ты принялся уплетать свою добычу за обе щёки.
Но от этого твой аппетит только разыгрался и ты решаешь раздобыть немного колбасы - для разнообразия
рациона, так сказать...'''

OTHER_THEFT = '''Подойдя к лавке с колбасой и уверившись в своей сегодняшней удаче, наплевав на всякую осторожность,
ты сходу пытаешься стащить аппетитную палочку Докторской, несмотря на то, что торговец как-то искоса
и с недоверием на тебя поглядывает...'''

OTHER_THEFT_FAIL = 'В этот раз на кубике выпало 1. {}'.format(colored('Попытка кражи провалилась...', 'red'))

DANGER = '''Протянув руку за колбасой, ты неуклюже задеваешь прилавок, отчего тот начинает шататься и несколько
палок с грохотом валятся на землю. Все вокруг оборачиваются в твою сторону. Казалось, даже птицы перестали
щебетать, выжидая, чем же всё закончится.'''

CHEET_DICE = '''"Уууупс",- робко прошептал ты.
Понимая, что тебя сейчас же схватят и накажут, ты решаешь воспользоваться специальным {},
который всегда держал в кармане плаща на случай подобной неудачи. Твои пальцы начали лихорадочно его искать,
так как медлить в этой ситуации было нельзя.'''.format(colored('Читерским кубиком', 'green'))

OTHER_THEFT_SUCCESS = '''С помощью {} ты меняешь неудачный результат своего прошлого броска на удачный. {}
Все вокруг, как ни в чём не бывало, тут же забывают о тебе и продолжают заниматься своими делами.
Как будто им стёрли память. Прямо как в фильме "Люди в чёрном" - любая часть. Ну а что ты хотел?
Это же фэнтэзийная игра...'''.format(colored('Читерского кубика', 'green'), SUCCESS)

F = '''"Уфф!- подумал ты,- Это было опасно. Если бы не {}, меня бы точно схватили и поколотили...
Как хорошо, что я нахожусь в компьютерной игре и здесь можно читерить. Хвала криворуким разработчикам,
оставляющим различные лазейки для таких засранцев, как я."'''.format(clr.CHEET_DICE)

F_2 = 'Вор, {}, да ещё и читак! И не стыдно тебе?! Да за такое при Сталине в ГУЛАГ отправляли!'.format(clr.CHAR_NAME)

G = '''Да кто тебе вообще поверит после такого! Забанить бы тебя по-хорошему за использование читов.
Ну да ладно, на первый раз прощаю, но буду пристально за тобой следить. Не вздумай больше хитрить.
Продолжаем...'''

H = '''Насытившись, ты убираешь остатки колбасы в карман, мастеришь из валявшейся на земле соломы и
каких-то тряпок импровизированную подстилку и довольный собой ложишься вздремнуть на солнышке...
Однако уже через 10 минут такое праздное времяпровождение тебе наскучило и ты подумал, что неплохо
было бы чем-то развлечь себя. С этой целью ты решил направиться на центральную площадь городка,
где в эти часы обычно проводятся уличные бои разного сорта упырей и маргинальных личностей.
Ну и ещё сладкой ватой торгуют.'''
