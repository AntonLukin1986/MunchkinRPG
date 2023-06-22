"""Текст для функции pursuit_final."""
from termcolor import colored

AAAA = (
    'Ты изо всех сил бежишь по {}, сворачивая в самые тесные улочки, переворачивая за собой всё, что попадается на пути,\n'
    'пытаясь таким образом оторваться от преследователей.\n'
    'Благодаря твоей ловкой воровской натуре и изрядной доли выброшенного в кровь адреналина,\n'
    'подкреплённый опасением за целостность собственной шкуры, тебе мало-помалу удаётся оставить преследователей позади.\n'
    'И лишь только {}, кажется, и не собирался сдаваться, постепенно сокращая дистанцию.'
).format(colored('Токийску', 'yellow'), colored('Блуждающий Нос', 'red'))

EXP_1 = (
    'Казалось бы всё пропало и тебе не удастся сбежать от Носа, как вдруг ты замечаешь припаркованный у обочины пикап.\n'
    'Ты сходу запрыгиваешь в кабину и садишься за руль.\n'
    'На удачу автомобиль оказывается заведённым и ты тут же даёшь по газам, срываясь с места под визг колёс...'
)
EXP_2 = (
    'Промчавшись на пикапе пару кварталов, маневрируя между телегами с лошадьми,\n'
    'валяющимися повсюду корзинами фруктов и навозными кучами, ты уже было решил, что оторвался от {}.\n'
    'Как вдруг тот выскакивает из переулка за рулём огромного 30-тонного автокрана, сметая и руша всё на своём пути.\n'
    'Одновременно он стреляет в тебя плазменными зарядами из какой-то футуристической пушки, вмонтированной в руку...'
).format(colored('Блуждающего носа', 'red'))
EXP_3 = (
    'Так, стоп! Это же сцена из одного голливудского фильма с брутальным качком в главной роли.\n'
    'Он ещё после этого губернатором стал. Терми-манчкин, кажется...'
)
EXP_4 = (
    'Точно - Терминатор 3. Умели же снимать боевики раньше...\n'
    'Впрочем, на чём мы там остановились? Ах, да!\n'
    '...И лишь только {}, кажется, и не собирался сдаваться, постепенно сокращая дистанцию...'
).format(colored('Блуждающий Нос', 'red'))
BBBB = (
    'Понимая, что от Носа просто так не скрыться, ты решаешь договориться с ним мирным путём.\n'
    'А на случай неудачи у тебя в кармане лежит {}, которое, по слухам, может сразить {} наповал.'
).format(colored('Зелье ротовой вони', 'green'), colored('Блуждающего Носа', 'red'))
CCCC = (
    'С этими мыслями ты остановился и, обернувшись, крикнул Носу: "Всё, я сдаюсь! Давай поговорим."\n'
    'Приблизившись к тебе вплотную, Нос злобно прорычал:\n'
    '"Нам не о чём с тобой разговаривать, {}. Мы с детства терпеть не можем таких, как ты! Я и Мойдодыр Чуковского."\n'
    '"Окей, я всё понял, - отвечаешь ты, - Я не стану сейчас плакаться о том, что это не я такой плохой,\n'
    'а всему виной трудное детство и дорогой гель для душа..."\n'
    '"Ни слова больше, - ответил Нос, - руки за голову и мордой в пол - работает ОМОН!"'
).format(colored('Знатный Вонючка', 'yellow'))
DECISION = (
    colored(
        'Сейчас тебе предстоит сделать выбор:\n'
        '-> предложить Носу сделку (введи 1)\n'
        '-> попытаться победить Носа, применив Зелье ротовой вони (введи 2)',
        'blue'
    )
)
DDDD = (
    'В этот момент ты решаешь вероломно атаковать противника. А что ещё можно было ожидать от такого бесчестного персонажа?\n'
    'Ты достаёшь из-за пазухи {} и бросаешь его под {}.\n'
    'Бутылёк разбивается и Нос оказывается в плотном облаке едкой вонючей субстанции, отчего он тут же начинает кашлять и задыхаться.\n'
    'Для пущего эффекта ты выдохнул в него нечищенным две недели ртом... Ну ясно, {}!'
).format(colored('Зелье ротовой вони', 'green'), colored('Блуждающего носа', 'red'), colored('Знатная Вонючка', 'yellow'))
EEEE = (
    '"Так тебе и надо наглый Нос! Будешь знать, как со мной связываться", - сказал ты и, довольный собой, побрёл домой окольными путями,\n'
    'запутывая следы от возможной слежки. Трудный выдался денёк, однако!'
)
FFFF = (
    '"Глубокоуважаемый мистер Нос, - говоришь ты, - я предлагаю Вам сделку.\n'
    'Я отдам Вам в качестве подкупа свой эксклюзивный коллекционный {},\n'
    'а Вы за это меня отпустите и сообщите своему нанимателю, что не смогли меня поймать.\n'
    'И при этом я обещаю больше никогда не попадаться Вам на глаза. Ну как, по рукам?"\n'
    '"А ну-ка, покажи мне этот кинжал", - ответил {}.'
).format(colored('Кинжал измены', 'green'), colored('Блуждающий Нос', 'red'))
GGGG = ('Ты достаёшь из-за пояса свой новенький блестящий {} и протягиваешь его Носу.').format(colored('Кинжал измены', 'green'))
HHHH = (
    'У того сразу загорелись глаза и, недолго думая, он согласился на твоё предложение.\n'
    'А всё потому, что с детства у Носа был навязчивый фетишь к эксклюзивному коллекционному барахлу, стоимостью не меньше 400 голдов,\n'
    'которое он складировал в своём сундуке. Психиатр, осматривавший его однажды, сделал неутешительное заключение: синдром Плюшкина...\n'
    'С неохотой отдав Носу свой кинжал, ты грустно побрёл окольными путями домой, заметая таким образом следы.\n'
    'Можно сказать, что ты ещё довольно дёшево отделался сегодня - везучий засранец!'
)
IIII = (
    'Вернувшись под вечер в свою лачугу, ты запер за собой дверь, небрежно кинул плащ на стол и повалился без сил на кровать.\n'
    'Не прошло и минуты, как ты заснул крепким сном, изнурённый событиями этого дня...'
)
