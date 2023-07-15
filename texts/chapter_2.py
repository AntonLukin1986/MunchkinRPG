"""Текст для функции play_chapter_2. Погоня."""
from termcolor import colored

from texts import colored_text as clr

CHAR_NAME_1 = colored('Знатного Вонючки', 'yellow')
GIPPOGRIF_1 = colored('Гиппогрифа', 'red')

A = '''Выйдя на площадь, ты понял, что пришёл в самый разгар веселья. Вокруг кричала возбуждённая толпа,
наблюдавшая за главным поединком этого утра, в котором сошлись {} и {}.'''.format(clr.GOBLIN, clr.DUCKBILL)

A_2 = '''Последний был явным фаворитом поединка и большая часть зрителей делала ставки на его победу, предчувствуя возможность
лёгкого зароботка. Ещё бы - нужно было сильно постараться, чтобы проиграть калеке на костылях.
Однако же и гоблин был не из робкого десятка: подбадриваемый своими немногочисленными болельщиками,
он не упускал возможности доставить неприятности сопернику, ловко орудуя своим костылём.'''

B = '''{0} сражался отчаянно. С самого детства он ненавидел свой несуразный нос и мечтал поскорее от него избавиться.
Но, так как денег на операцию по пластике носа у него не было, ему пришлось участвовать в данном турнире,
чтобы попытаться выиграть главный приз - бесплатный купон в Клинику Ринопластики доктора И.П.Носовского.
Воодушевлённый своей целью, {0} мало-помалому одерживал верх над своим соперником и уже был готов окончательно
с ним расправиться...'''.format(clr.DUCKBILL)

C = '''Однако, твоей никчёмной воровской душёнке, наблюдающей за поединком, захотелось напакостить и ты, пользуясь умением Вора,
подрезаешь {}, уменьшив его боевую силу.\nПросто так. От скуки и из-за своего скверного характера.
Этой пакости хватило, чтобы баланс сил изменился и {}, применив свой коронный удар костылём по темечку
с разворота в прыжке, неожиданно одержал верх над противником.'''.format(clr.DUCKBILL, clr.GOBLIN)

C_2 = '''Оглушённый {0} понял, что ему ничего не остаётся, как попытаться смыться из боя.
Однако, хотя {1} и был на костылях, но у него имелись при себе новенькие {2}
фирмы Абибас, которые придавали своему обладателю невероятную прыткость!'''.format(clr.DUCKBILL, clr.GOBLIN, clr.FAST_BOOTS)

C_3 = '''Надев их, калека на глазах у изумлённой публики помчался вдогонку за {0}, колотя его по пяткам.
Того и гляди пропал бы {0}, если бы не воспользовался волшебным заклинанием {1}.
Благодаря ему за спиной беглеца неожиданно выросла кирпичная стена, в которую со всего лёту врезался
лбом гоблин, поплатившийся таким образом за излишнее усердие в погоне.'''.format(clr.DUCKBILL, clr.WALL)

D = '''От такого неожиданного развития событий зрители притихли в недоумении.
Кто-то в толпе предположил, что здесь явно не обошлось без проделок {}.
Поддержав справеливость это предположения, наблюдавшие за поединком зрители стали рыскать глазами по сторонам,
пытаясь обнаружить виновника происшествия...'''.format(CHAR_NAME_1)

E = 'Осознав, что дело пахнет жареным, ты поспешно закутываешься в свой {} и произносишь: '.format(clr.CLOAK)

F = 'Этой кодовой фразой ты активировал специальную маскировочную функцию своего плаща и превратился в холщёвый мешок с гнилым луком.'

G = '''Ты вовремя сориентировался и пока мог чувствовать себя в безопасности, поскольку искавшие тебя люди просто проходили мимо
и не обращали никакого внимания на мешок.
Успокоившись, ты уже начал раздумывать, как бы незаметно улизнуть с площади, как вдруг двое странного вида {}
остановились возле тебя.'''.format(GIPPOGRIF_1)

H_1 = '"От этого мешка с гнилым луком несёт прям как от {}",- сказал один из них.'.format(CHAR_NAME_1)

H_2 = 'Ты замер, затаив дыхание и боясь пошевелиться. Лишь только звук колотившегося от страха сердца мог выдать твоё присутствие.'

H_3 = '''"Ну уж нет",- ответил его товарищ,- "{} смердит гораздо противнее!".
"И то правда",- заключил первый и с отвращением пнул мешок, после чего оба пошли дальше.'''.format(clr.CHAR_NAME)

IA = '''"Опять мне повезло",- выдохнул ты с облегчением, вытирая холодный пот со лба и морщась от боли в боку после пинка {}.
Как вдруг до тебя донеслось чьё-то восклицание: "Смотрите, это же {}!".'''.format(GIPPOGRIF_1, clr.NOSE)

J = '''И действительно, посмотрев сквозь щель в мешке на центр площади, ты увидел злобный {}, который забрался
на повозку с бочками и внимательно осматривал окерсности.
Его ноздри гневно раздувались в такт с дыханием, выдавая серьёзный настрой и сосредоточенность.
"Меня нанял продавец колбасы",- громогласно заявил Нос,- "у которого {} сегодня утром украл палку Докторской.
И я намерен поймать этого дерзкого воришку и навешать ему тумаков.
Все вокруг - замрите, сейчас я попытаюсь учуять его запах!"'''.format(clr.NOSE, clr.CHAR_NAME)

K = '''"А вто это уже серьёзно",- подумал ты и затаился.
{} закрыл глаза и стал принюхиваться...
"Я чувствую запах колбасы от того мешка с гнилым луком",- сказал Нос, указывая в твою сторону,- "той самой колбасы,
которую украл {}!"'''.format(clr.NOSE, clr.CHAR_NAME)

L = '''Толпа с удивлением посмотрела в твою сторону.
Внезапно ты вспомнил про остатки недоеденной колбасы в кармане и горько пожалел, что не избавился от этой улики.
Тем временем {} начал стремительно приближаться, угрожающе сопя своими огромными ноздрями.'''.format(clr.NOSE)

M = '''Понимая, что медлить дальше нельзя, ты вскакиваешь, теряя свою маскировку, и пускаешься наутёк, воспользовавшись общим замешательством.
"А ведь я сразу почуял в этом мешке что-то неладное!"- злобно прорычал {}.
Уже через пару секунд гневная улюлюкающая толпа с криками "держи вора!" бросилась за тобой.
Воскликнув: "От меня ещё никому не удавалось скрыться!", к погоне присоединился {}.'''.format(clr.GIPPOGRIF, clr.NOSE)
