"""Текст для функции play_chapter_4. Неожиданный поворот."""
from termcolor import colored

from texts import colored_text as clr

A = '''Но сон был недолог - неожиданно ты просыпаешься от громкого и резкого звука.
Вскочив от испуга с кровати, ты недоумённо уставился на входную дверь.
Запиравшая её изнутри щеколда была выбита сильным ударом, а на пороге стояли {}.'''.format(clr.BONES_BROTHERS)

B = (
    colored(
        'Выбери один из вариантов действий:\n'
        '-> Попытаться скрыться (введи 1) \n'
        '-> Попытаться атаковать (введи 2)',
        'blue'
    )
)

X_1 = '''Решив действовать, ты достал из-под кровати {} и тут же метнул его в незванных гостей, чтобы задержать их и выиграть для себя время.
Проскочив между костей {}, кинжал воткнулся в стену, не причинив им никакого вреда.'''.format(
    clr.DAGGER, colored('Бледных братьев', 'red')
)

X_2 = '''Решив действовать, ты достал из-под кровати самодельное оружие собственного изготовления - {} - и метнул ею
в незванных гостей, чтобы задержать их и выиграть для себя время.
Однако это, с позволения сказать, «оружие» было для них что для слона дробина - {} даже не пошатнулись.'''.format(
    clr.RAT_ON_STICK, clr.BONES_BROTHERS
)

C = '''У тебя тут же сработал инстинкт вечного беглеца и ты рванул было в сторону единственного окна.
Однако один из братьев метнул тебе под ноги {}, отчего ты тут же замер на месте.
"Стой где стоишь, {}!" - проговорили они в унисон зловещим голосом.'''.format(clr.GLUE, clr.CHAR_NAME)

D = '''В этот момент ты горько пожалел о том, что за несколько дней до этого обменял у странствующего барда свою {},
которая неоднократно спасала твою шкуру от неприятностей, прибавляя каждый раз +3 к смывке, на {} и {}.
А ведь она ой как пригодилась бы сейчас против твоих незванных гостей.'''.format(
    colored('Чарующую дуду', 'green'), clr.DAGGER, clr.CHEET_DICE
)

E = '''Ты знал, что эта парочка Андедов с того света являются профессиональными наёмниками, обладающими невероятной силой и ловкостью.
Лишь только у {}, обладавших особой силой против Андедов, были хоть какие-то шансы противостоять им.
Поэтому без {} нечего было и думать скрыться от них.'''.format(colored('Клириков', 'yellow'), colored('Чарующей дуды', 'green'))

F = '''Осознав всю безвыходность ситуации, ты решил не сопротивляться, чтобы не провоцировать их на силовые действия.
Однако, ты никак не мог понять, почему они пришли за тобой.
Тебе было известно, что {} очень дорого оценивают свои услуги и берутся только за самую трудную работёнку -
вступить в схватку с {}...'''.format(clr.BONES_BROTHERS, colored('Плутониевым драконом', 'red'))

G = 'Или, например, пересадить ужасную и непобедимую {} в ёмкость попросторней...'.format(colored('Огорошенную траву', 'red'))

H = '''"Вряд ли их появление связано с моими вчерашними проделками",- подумал ты,- "я для них слишком мелкая сошка."
Подняв руки вверх, ты робко сказал: "Ребята, мне не нужны неприятности. Давайте жить дружно!"'''

IA = '''"Тоже мне кот Леопольд нашёлся! Веди себя смирно и без глупостей",- ответили хором {}.
Они связали тебе руки и вывели на улицу, где их уже поджидал {}.
Храня молчание, Братья погрузили тебя на круп коня, набросили на голову мешок и повезли в неизвестном направлении.'''.format(clr.BONES_BROTHERS, clr.DEAD_HORSE)

J = '''Находясь в тревожной неизвестности, ты ломал голову над тем, за что мог быть похищен и куда вы направлялись,
однако не находил никакого рационального объяснения происходящему.
Мешок на голове не сулил ничего хорошего, а звук гремящих костей твоих конвоиров лишь усиливал чувство отчаяния...'''
