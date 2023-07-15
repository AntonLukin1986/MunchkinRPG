"""Текст для функции play_chapter_7. Радужные перспективы."""
from termcolor import colored

from texts import colored_text as clr

A = '''Заключив с принцессой официальный договор под заголовком "Миссия невыполнима 14", скреплённый её гербовой печатью с одной стороны
 и твоим "честным пионерским" с другой, ты твёрдо решаешь, что с этого момента твоя жизнь кардинально изменится.
Предаваясь мечтаниям, ты начал воображать, как уже завтра прогоняешь из {} всех монстров;
после чего благодарная принцесса предлагает тебе взять её в жёны; ты становишься почётным принцем,
героем эльфийского королевства и поселяешься вместе с ней в собственном роскошном замке!
От таких мыслей у тебя даже потекли слюнки изо рта... В общем, жалкое зрелище!'''.format(colored('Фрустландии', 'yellow'))

B = '''Но твоим сладким грёзам было суждено рассыпаться о суровую реальность - внезапно тебе в голову пришло осознание того
что ты, вообще-то, ни разу не отважный рыцарь, а всего-навсего мелкий воришка, которого сможет одолеть даже {}.
А всё, что ты умеешь - пакостить исподтишка, да шарить по чужим карманам...'''.format(clr.OCTAEDRON)

C = '''"Товарищи",- робко промолвил ты,- "я конечно дико извиняюсь, но, кажется, я немного поспешил с принятием решения!
Я тут подумал: а каким образом мне удастся победить всех этих ужасных монстров? Боец из меня тот ещё! Я бокс
только по телевизору смотерл, да и то ничего не понял.
А из магических заклинаний владею лишь "вонючарами", которыми разве что приличных господ на улице отпугивать.
И вообще, с чего вдруг вы все так уверены, что я справлюсь с этим вашими монстрами?"'''

D = '''"Ну вот - посыпался",- разочарованно сказал Бард.
"Только зря потратим на него время",- в сердцах произнёс Паладин.
"А что ж ты сам не пойдёшь сражаться?"- обиженно спросил ты у Паладина,- "Ты же вон какой здоровый. И меч у тебя есть. И доспехи модные."'''

E = '''"Он не может туда отправиться",- поспешила вмешаться {},- "так как среди этих монстров есть {} - его бывшая жена..."'''.format(
    clr.PRINCESS, clr.KALMADZILLA
)

E_1 = '''"...Видишь ли",- в пол голоса продолжила принцесса, чтобы её не смог услышать Паладин,- "они расстались пару лет назад с грандиозным скандалом.
Она отсудила у мужа большую часть имущества, да ищё и навешала на него алиментов. И если эти двое вновь встретятся лицом к лицу,
то произойдёт катастрофа поистине вселенского масштаба - похуже ядерной войны, что бы это ни было. В общем, больная тема..."
Ты понимающе кивнул, вспомнив свою бывшую, и решил больше не ворошить это осиное гнездо.'''

F = '''"Наш выбор",- вмешался в разговор престарелый Друид,- "пал на тебя потому что у меня было видение!"
При этом Друид принял пафосную позу и зажёг правой рукой фаейрбол - неизменный атрибут разного рода чародеев.
Сделав глубокий вздох, он поведал присутствующим своё пророчество...'''

G = '''"Мне привидилось, что в начале двадцать первого века",- торжественно начал он,- "НЕКТО из далёкой, холодной и таинственной страны {},
находясь по ту сторону монитора, начнёт играть в "Манчкин RPG": сгенерирует странного вида персонажа по своему образу и подобию;
выберет для него самый неинтересный и скучный класс из всех возможных; после чего решит присвоить получившемуся герою глупейшее из имён,
когда-либо встречавшихся в компьютерных играх!
И, несмотря на такое несерьёзное отношение к делу, НЕКТУ всё-таки удастся достичь главной цели - пройти всю игру до самого конца!'''.format(colored('Россия', 'yellow'))

G_CHOICE = (
    colored(
        'Выбери один из вариантов реплики:\n'
        '-> Звучит туманно... (введи 1) \n'
        '-> Ну и бред... (введи 2)',
        'blue'
    )
)

G_1 = '"Ничего не понятно, но очень интересно",- пробормотал ты, недоумённо посмотрев на принцессу.'

G_2 = '''"Кажется, у нашего старичка галлюцинации",- воскликнул ты. "Может быть на него смирительную рубашку накинуть?
А то ведь, чего доброго, ещё и кусаться начнёт..."'''

H = '''"Не обращай внимания. Просто старик недавно пристрастился к нашему знаменитому Эльфийскому элю и после этого
у него периодически стали возникать подобные "видения"",- закатывая глаза пояснила {}.
Ты предположил, что с такими темпами у Друида того и гляди может случиться белая горячка
и попросил эльфийку рассказать, как обстояли дела на самом деле.'''.format(clr.PRINCESS)

IA = '''{} пояснила, что прочие кандидаты, к кототрым они обращались, отказались участвовать в подобной авантюре.
И так как ты производил впечатление самого глупого и отчаянного человека, которого им доводилось встречать,
то было принято решение сделать ставку именно на тебя. К тому же ты оказался настолько недалёким,
что даже не удосужился прочитать подписанный только что договор.
А ведь в нём указано, что если ты не выполнишь его условия, то тебя бросят в чан с маленькими пандами и ты умрёшь от умиления.
Таким образом, обратного пути у тебя нет, подытожила молодая эльфийка.'''.format(clr.PRINCESS)

J = 'Поблагодарив принцессу за столь лестное мнение о твоей персоне, ты поинтересовался у присутствующих, каков теперь дальнейший план действий?'

K = '''Принцесса {} сообщила, что прежде чем отправиться во {}, тебе предстоит пройти курс специальной подготовки,
по окончании которого ты станешь крутым Манчкином и сможешь навалять люлей любому противнику. Но это не точно!'''.format(clr.PRINCESS, colored('Фрустландию', 'yellow'))

L = '''"А что такое «Манчкин»?"- спросил ты.
"Так во вселенной, откуда прибыли эти монстры, называют отважного героя, который должен им противостоять",- пояснил Бард.
В результате этой подготовки ты из обычного человека превратишься в представителя какой-либо фэнтезийной рассы.
А так же обучишься особым умениям одного из боевых классов, значащихся в Фрустландском Трудовом Кодексе.'''

M = colored('Введи реплику: Я и человеком себя неплохо чувствую\n>>> ', 'blue')
M_1 = 'Я и человеком себя неплохо чувствую'

N = '''"Так уж сложилось, что доступ представителю человеческой рассы во {} закрыт волщебным фейсконтролем,
что бы это ни было. А без наличия боевого класса ни один уважающий себя монстр не станет с тобой сражаться,
так как у них это считается дурным тоном",- ответил Паладин.
"Ок, я всё понял! Когда приступаем к тренировкам?"- поинтересовался ты.
"Да прямо сейчас и начнём",- ответила принцесса,- "Твоими фитнесс-тренерами станут Друид и Паладин, а Бард будет отвечать
за мотивирующую фоновую музыку, как в любом уважающем себя модном фитнесс клубе."'''.format(colored('Фрустландию', 'yellow'))

OA = 'С этими словами тебя отводят в соседнее помещение, где стоит очень странного вида агрегат.'

OA_1 = '''Друид пояснил, что этот аппарат привезли с собой Хан Соло, Люк Скайуокер и Чубакка и подарили его эльфийскому народу.
Работает он следующим образом: любая антисоциальная личность может пройти на нём тестирование, по результатам которого
аппарат создаёт некую генно-модифицированную жидкость, выпив которую, тестируемый трансформируется в Эпического героя
и Хорошего парня. А как это всё работает Друид и понятия не имеет...
"Отлично! Тогда встречайте нового меня",- торжественно заявил ты и уселся за аппарат,- "Надеюсь онсделает мне причёску помодней?!"'''