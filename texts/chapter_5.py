"""Текст для функции play_chapter_5. Таинственное место."""
from termcolor import colored

from texts import colored_text as clr

A = '''Примерно через час, насколько ты мог судить о пройденном времени, {} остановился и тебя грубо спустили на землю.
Ты с удовольствием немного размял затёкшие конечности и поинтересовался у Братьев, нельзя ли снять мешок с твоей головы?
Однако ответа не последовало. Храня молчание, тебя завели в какое-то здание - ты услышал скрип открывающейся двери
и почувствовал, что идёшь по деревянному полу.
Вы шли долго, петляя по коридорам, пока, наконец, тебя не усадили на стул в одном из помещений.
Затем {} сняли с твоей головы мешок и встали у тебя за спиной.
Ты огляделся. В комнате царил полумрак. Рядом со стулом горела небольшая масляная лампа,
света которой хватало лишь на то, чтобы осветить пространство в паре метров вокруг тебя.'''.format(clr.DEAD_HORSE, clr.BONES_BROTHERS)

B = '''Приглядевшись, тебе удалось заметить перед собой четыре стоявшие в тени фигуры, которые молча смотрели на тебя.
Ты не мог разглядеть их лица, скрытые темнотой и надетыми на головы капюшонами. Зато тебя они видели хорошо.
Все находившиеся в комнате хранили зловещее молчание...
Не выдерживая затянувшейся паузы, ты решаешь заговорить первым.'''

C = (
    colored(
        'Выбери один из вариантов реплики:\n'
        '-> Я требую объяснений! (введи 1) \n'
        '-> Простите меня грешного! (введи 2)',
        'blue'
    )
)

D_1 = '''"Я надеюсь, это какой-то розыгрыш! Не бывает такого, чтобы ни в чём неповинного добропорядочного гражданина
вот так просто взяли дома посреди ночи, накинкули на голову мешок и увезли в неизвестном нарпавлении.
Это же самое настоящее похищение! За которое, между  прочим, предусмотрена уголовная ответственность по статье 126 УК РФ,
чтобы это ни значило.
Я требую объяснений! Я буду жаловаться в Международный суд по правам человека в Стразбурге, чтобы это ни было.
И вообще у меня дядя прокурор и вам всем кабздец!!!"- завопил ты, как потерпевший.
"Немедленно меня отпустите, иначе..."'''

D_2 = '''"Граждане-товарищи,- замолил ты, - Я правда не понимаю, почему и за что здесь оказался, но вся эта зловещая торжественность
пугает меня до чёртиков. Простите, если я кого-то когда-либо обидел - я больше так не буду, честное пионерское!
Если всё это из-за вчерашней колбасы, так вот, знайте: она была уже подпорченной и я, получается, даже уберёг от отравления кого-то из её
потенциальных покупателей. Погодите... А может быть дело в том, что я намедни легонько пнул того милого белого пуделя? Так я не хотел!
Это я просто перепутал его с футбольным мячом, который..."'''

E = '''Твой истерический монолог был бесцеремонно прерван смачным подзатыльником от одного из {} из-за спины.
Метод оказался действенным и ты тут же умолк, ожидая, что будет дальше...'''.format(colored('Бледных братьев', 'red'))

F = '''"А это точно тот, кто нам нужен?"- спросил один из незнакомцев перед тобой.
"Я уже сам начинаю сомневаться",- ответил другой.
"Такова его реакция на стресс на фоне крайней степени испуга",- подытожил третий.
Из этого небольшого обсуждения твоей персоны ты понял, что все говорившие были мужчинами.'''

G = '''В этот момент из-за их спин вышла вперёд ещё одна фигура и подошла к тебе поближе.
Оказавшись на свету, таинственная персона сняла с головы капюшон. Это оказалась красивая молодая девушка.
Её роскошные светлые волосы обрамляла изящная диадема, украшенная драгоценными камнями,
ярко поблёскивавшими при свете лампы. Уж ты-то, воришка, знал толк в драгоценностях!
Одеяние незнакомки, её украшения, а так же правильные, красивые черты лица, вкупе с благородной осанкой,
выдавали особу знатного происхождения.
Присмотревшись повнимательней, ты обомлел, отказываясь верить своим глазам: прямо перед тобой стояла прекрасная
эльфийская принцесса из вчерашнего сна...'''