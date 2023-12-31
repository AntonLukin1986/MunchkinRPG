"""Текст для функции play_chapter_2. Погоня."""
from termcolor import colored

from texts import colored_text as clr

CHAR_NAME_1 = colored('Знатного Вонючки', 'yellow')
GIPPOGRIF_1 = colored('Гиппогрифа', 'red')

A = '''Выйдя на площадь, ты обнаружил, что пришёл в самый разгар веселья: здесь было яблоку негде упасть.
Городские жители всех мастей, полов и возрастов заполнили всё свободное пространство. Они толкались
и бранились друг на друга, пытаясь протиснуться как можно ближе к арене. Везде, откуда было возможно
наблюдать за поединком, находились люди: на крышах ближащих домов, фонарных столбах и даже груда бочек
с элем служила своеобразной трибуной для нескольких зевак. Вокруг сновали торовцы чурчхелой и шаурмой,
добавляя свою лепту в общую какафонию звуков. Возбуждённая толпа с интересом наблюдала за главным
поединком этого утра, в котором сошлись {} и {}.'''.format(clr.GOBLIN, clr.DUCKBILL)

A_2 = '''Последний был явным фаворитом поединка и большая часть зрителей делала ставки на его победу, предвкушая
возможность лёгкого зароботка. Ещё бы - нужно было сильно постараться, чтобы проиграть калеке на костылях.
Однако же и гоблин был не из робкого десятка: подбадриваемый своими немногочисленными болельщиками, он не
упускал возможности доставить неприятности сопернику, ловко орудуя своим костылём и справкой от травматолога.'''

B = '''{0} сражался отчаянно. Дело в том, что с самого детства он ненавидел свой несуразный нос и мечтал
поскорее от него избавиться. Но, так как денег на операцию по пластике носа у него не было, то ему пришлось
участвовать в данном турнире, где главным призом победителю был бесплатный купон в Клинику Ринопластики
доктора И.П.Носогубкина. Воодушевлённый своей целью, {0} мало-помалому одерживал верх над своим
соперником и уже был готов окончательно с ним расправиться...'''.format(clr.DUCKBILL)

C = '''В этот момент твоей никчёмной воровской душёнке, наблюдавшей за поединком, захотелось напакостить и ты,
пользуясь умением Вора, подрезаешь {}, уменьшая его боевую силу на два. Просто так - от скуки и из-за
своего скверного характера. Этой небольшой пакости хватило, чтобы баланс сил изменился и {}, применив
коронный удар костылём по темечку с разворота в прыжке, неожиданно для всех положил противника на лопатки.'''.format(clr.DUCKBILL, clr.GOBLIN)

C_2 = '''Оглушённый {0} осознал, что ему ничего не остаётся, как попытаться смыться из проигранного боя, чтобы
избежать унизительного и болезненного непотребства от победителя.
Однако хотя {1} и был на костылях, но у него имелись при себе новенькие {2}
фирмы Абибас, которые придавали своему обладателю невероятную прыткость.'''.format(clr.DUCKBILL, clr.GOBLIN, clr.FAST_BOOTS)

C_3 = '''Надев их, калека на глазах у изумлённой публики, как заправский спринтер, помчался вдогонку за {0},
колотя его по пяткам и осыпая отборной гоблинской бранью.
Того и гляди пропал бы {0}, если бы вовремя не воспользовался волшебным заклинанием {1}.
Благодаря этому за спиной беглеца вмиг выросла кирпичная стена, в которую со всего размаху влетел лбом гоблин,
поплатившийся таким образом за излишнее усердие в погоне.'''.format(clr.DUCKBILL, clr.WALL)

D = '''От такого неожиданного развития событий зрители притихли в недоумении, удивлённо оглядываясь друг на друга.
Кто-то в толпе предположил, что здесь явно не обошлось без проделок известного маргинала и пакостника
{}. Поддержав справедливость этого предположения, собравшиеся начали рыскать глазами по сторонам,
пытаясь обнаружить предполагаемого виновника происшествия.'''.format(CHAR_NAME_1)

E = 'Осознав, что дело пахнет жареным, ты поспешно закутываешься в свой {} и произносишь: '.format(clr.CLOAK)

F = '''Плащ этот является экспериментальной разработкой НИИ ОКБ «УралВагонМаш» и был приобретён тобой в Чёрную пятницу
на Алиэкспресс. Данная кодовая фраза значилась в Инструкции по применению изделия. Произнеся её, ты активировал
специальную маскировочную функцию плаща и в мгновение ока превратился в холщёвый мешок с гнилым луком.'''

G = '''Ты вовремя сориентировался и пока мог чувствовать себя в относительной безопасности, поскольку искавшие
тебя люди, ничего не подозревая, проходили мимо и не обращали никакого внимания на ничем не примечательный
мешок. Немного успокоившись, ты уже начал раздумывать, как бы попытаться незаметно улизнуть с площади и
убраться куда подальше, как вдруг двое странного вида {} остановились возле тебя.'''.format(GIPPOGRIF_1)

H_1 = '''"Посмотри-ка,- сказал один другому,- от этого мешка несёт прямо как от {}."
Тот, к кому обращались, с удивлением посмотрел на мешок.'''.format(CHAR_NAME_1)

H_2 = '''Ты замер, затаив дыхание и боясь пошевелиться. Лишь только звук колотившегося от страха сердца мог выдать
твоё присутствие. Казалось ещё чуть-чуть и тебя разоблачат и схватят...'''

H_3 = '''"Ну уж нет,- ответил его товарищ,- {} смердит гораздо противнее!"
"И то правда",- заключил первый и с отвращением пнул ногой мешок, после чего оба пошли дальше.'''.format(clr.CHAR_NAME)

IA = '''"Опять мне повезло",- выдохнул ты с облегчением, вытирая холодный пот со лба и морщась от боли в боку
после пинка {}. В этот момент до тебя донеслось чьё-то восклицание:
"Смотрите, это же {}!"'''.format(GIPPOGRIF_1, clr.NOSE)

J = '''И действительно, посмотрев сквозь щель в мешке на центр площади, ты увидел злобный {}, который
забрался на повозку с пивными бочками, пристально осматривая окресности.
Его ноздри гневно раздувались в такт с дыханием, выдавая серьёзный настрой и сосредоточенность.
"Меня нанял продавец колбасы,- громогласно заявил Нос,- у которого {} сегодня утром украл палку
Докторской. И я намерен поймать этого дерзкого воришку и наказать его по всей строгости закона.
Все замрите - сейчас я попробую учуять его запах!"'''.format(clr.NOSE, clr.CHAR_NAME)

K = '''"А вто это уже серьёзно",- подумал ты и затаился, с тревогой ожидая, что будет дальше.
{} закрыл глаза и стал принюхиваться. Предательский ветерок как раз подул от тебя в его сторону...
"Я чувствую запах колбасы от того мешка с гнилым луком,- сказал Нос, указывая в твоём направлении,- Той самой
колбасы, которую стащил {}!"'''.format(clr.NOSE, clr.CHAR_NAME)

L = '''Толпа с удивлением посмотрела в твою сторону, не понимая, как Докторская могла оказаться в мешке с гнилым луком.
В этот момент ты вспомнил про остатки недоеденной колбасы в кармане и горько пожалел, что не избавился от этой
улики. Тем временем {} начал стремительно приближаться, угрожающе сопя своими огромными ноздрями.'''.format(clr.NOSE)

M = '''Понимая, что медлить дальше нельзя, воспользовавшись всеобщим замешательством, ты вскакиваешь на ноги, теряя
при этом свою маскировку, и пускаешься наутёк в узкий безлюдный переулок.
"А ведь я сразу почуял, что с этим мешком что-то неладное!"- злобно прорычал {}.
И уже через пару секунд гневная улюлюкающая толпа с криками "держи вора!" бросилась за тобой.
Воскликнув: "От меня ещё никому не удавалось скрыться!", к погоне присоединился {}.'''.format(clr.GIPPOGRIF, clr.NOSE)
