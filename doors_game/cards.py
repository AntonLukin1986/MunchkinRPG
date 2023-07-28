"""Карты предметов, способностей, проклятий и т.п. Списки с каратми, сгруппированными по категориям."""
from classes import Item, Buff, Boost, Curse

# тексты для карт
FRIENDSHIP = '''Применено Зелье Дружбы! Внезапно монстр становится дружелюбным.
Вы жмёте друг другу руки, обмениваетесь номерами телефонов и договариваетесь
сходить как-нибудь вместе в бар попить пивка. Монстр уходит, унося с собой свои сокровища...'''
GOD = '''Внезапно таинственная трансцендентная сущность вмешивается в обычный
порядок вещей и ты непостижимым образом проскакиваешь этот уровень.'''
ILLUSION = '''Ты обнаружил древний свиток с необычным заклинанием. Следующий
монстр, с которым ты столкнёшься, будет заменён на Огорошенную траву.'''
POLLYMORPH = '''Ты применяешь Зелье Попуморфа: монстр тут же превращается в разноцветного волнистого попугайчика.
Очумев от такой трансформации, он взмывает вверх, размахивая крыльями, и улетает, оставив свои сокровища!
Монстр улетел, но обещал вернуться...'''
TIGHTS = '''У тебя в рюкзаке как раз лежат Колготки великанской силы (20 den)
Ты давно хотел их примерять, но настоящим Воинам одевать такое не по статусу.
С помощью Чита ты наплевал на все приличия и с радостью натянул колготы
на свои тощие ляшки: они дают тебе +2 к боевой силе.'''

# базовый набор шмотки при стартовом уровне 0
HELM_COURAGE = Item('Шлем отваги +1 (головняк)', 'helmet', 1)
SLIMY_ARMOR = Item('Слизистая оболочка +1 (броник)', 'armor', 1)
SANDALS = Item('Сандалеты протекторы +1 (обувка)', 'footgear', 1)
LONG_POLE = Item('Одиннадцатифутовый шест +1 (в руке)', 'arm', 1)
NO_ITEM = Item('отсутствует', None, 0)

# специфическая шмотка класса при стартовом уровне 1
STAFF_NAPALM = Item('Посох напалма +3 (в руке)', 'arm', 3, require='Волшебник')
SHIELD_UBIQUITY = Item('Вездешний щит +3 (в руке)', 'arm', 3, require='Воин')
MACE_SHARPNESS = Item('Палица остроты +3 (в руке)', 'arm', 3, require='Клирик')
# специфическая способность класса при статровом уровне 2
FRIENDSHIP_POTION = Buff(
    'Зелье дружбы - подружись с монстром и он пропустит тебя без битвы.', 'friendship',
    FRIENDSHIP, require='Волшебник'
)
SPIKY_KNEES = Buff('Шипастые коленки - дают тебе дополнительную силу +2', 'knees', require='Воин')
WISHING_RING = Buff('Хотельное кольцо - отменяет любое проклятие', 'wishing_ring', require='Клирик')
# специфическая шмотка расы при стартовом уровне 3
HORNY_HELMET = Item('Шлем-рогач +3 (головняк)', 'helmet', 3, require='Эльф')
SHORT_WIDE_ARMOR = Item('Коротоширокие латы +3 (броник)', 'armor', 3, require='Дварф')
STEPLADDER = Item('Боевая стремянка +3 (обувка)', 'footgear', 3, require='Халфлинг')
treasures_for_level = [
    STAFF_NAPALM, SHIELD_UBIQUITY, MACE_SHARPNESS,
    FRIENDSHIP_POTION, SPIKY_KNEES, WISHING_RING,
    HORNY_HELMET, SHORT_WIDE_ARMOR, STEPLADDER
]

# базовые сокровища монстров
IMPRESSIVE_TITLE = Buff('Реально впечатляющий титул - делает из тебя персону голубых кровей. Получаешь +3 к боевой силе.', 'title')
INVISIBILITY_POTION = Buff('Зелье невидимости - позволит автоматически убежать от монстра, если провалишь смывку.', 'invisibility')
PRETTY_BALLOONS = Boost('Клёвые шарики: увеличивают специальную атаку на 5', 5)
MAGIC_MISSILE = Boost('Ракета магического назначения: увеличивает специальную атаку на 5', 5)
EL_RAD_ACID_POTION = Boost('Электро-ксилотно-радиационное зелье: увеличивает специальную атаку на 5', 5)
# буст-заглушка для заполнения опустевшего списка сокровищ монстров (если игрок уровня 3 победил 7 монстров)
PLUG = Boost('Бесполезный буст: ничего не даёт - ты и так уже Рэмбо...', 0)
monster_treasures_base = [
    IMPRESSIVE_TITLE, INVISIBILITY_POTION, PRETTY_BALLOONS, MAGIC_MISSILE, EL_RAD_ACID_POTION
]

# сокровища монстров, специфичные для расы и класса
ELF_BOW = Item('Лучок с ленточками +4 (в руке)', 'arm', 4, require='Эльф')
DVARF_HUMMER = Item('Коленоотбойный молот +4 (в руке)', 'arm', 4, require='Дварф')
HALFLING_SANDWICH = Item('Сэндвич «Душистая смерть» +4 (в руке)', 'arm', 4, require='Халфлинг')
# ещё одно хотельное кольцо
POLLYMORPH_POTION = Buff(
    'Зелье попуморфа - превращает монстра в попугая, который тут же улетает, оставляя свои сокровища.', 'pollymorph',
    POLLYMORPH, require='Волшебник'
)
DOPPLEGANGER = Buff('Дупельгангер: увеличивает силу твоих шмоток в два раза!', 'doppleganger', require='Воин')
monster_treasures_specific = [
    ELF_BOW, DVARF_HUMMER, HALFLING_SANDWICH,
    POLLYMORPH_POTION, DOPPLEGANGER, WISHING_RING
]

# сокровища свободной комнаты
SLEEP_POTION = Boost('Спячечное зелье: увеличивает специальную атаку на 2', 2)
BRAVERY_POTION = Boost('Зелье идиотской храбрости: увеличивает специальную атаку на 2', 2)
COTION_PONFUSION = Boost('Пелье зутаницы: увеличивает специальную атаку на 2', 2)
FLAMING_POTION = Boost('Зелье пламенной отравы: увеличивает специальную атаку на 3', 3)
FREEZING_POTION = Boost('Зелье холодильного взрыва: увеличивает специальную атаку на 3', 3)
SING_DANCE_SWORD = Item('Меч песни и пляски +2 (в руке)', 'arm', 2)
SWISS_POLEARM = Item('Швейцарская армейская алебарда +2 (в руке)', 'arm', 2)
BANDANA = Item('Бандана сволочизма +2 (головняк)', 'helmet', 2)
FLAMING_ARMOR = Item('Пылающие латы +2 (броник)', 'armor', 2)
KICKING_BOOTS = Item('Башмаки могучего пенделя +2 (обувка)', 'footgear', 2)
free_room_treasures = [
    SLEEP_POTION, BRAVERY_POTION, COTION_PONFUSION, FLAMING_POTION, FREEZING_POTION,
    SING_DANCE_SWORD, SWISS_POLEARM, BANDANA, FLAMING_ARMOR, KICKING_BOOTS
]

# карты комнаты с проклятьями общие
LOSE_HELMET = Curse('Потеряй головняк. Если нет головняка - потеряй волосы.', 'lose', lose='helmet')
LOSE_ARMOR = Curse('Потеряй броник. Нет броника - нет проблем.', 'lose', lose='armor')
LOSE_FOOTGEAR = Curse('Потеряй обувку. Если её нет, то и терять нечего.', 'lose', lose='footgear')
LOSE_MIN_ARM = Curse('Потеряй мелкую шмотку (оружие в руках): скинь самое слабое.', 'lose', lose='min_arm')
LOSE_MAX_ARM = Curse('Невыносимо гнусное проклятье: потеряй самую сильную из своих шмоток (оружие в руках).', 'lose', lose='max_arm')
MALING_MIRROR = Curse('Кривое зеркало. В следующем бою бонус будет только у броника.', 'only_armor')
CHANGE_SEX = Curse('Смена пола - стань женщиной! Из-за смятения получаешь -5 в следующем бою.', 'woman')
CHICKEN = Curse('Проклятье: курица на башке. Получаешь минус один ко всем броскам кубика!', 'chicken')
door_cards_base = [
    LOSE_HELMET, LOSE_ARMOR, LOSE_FOOTGEAR,
    LOSE_MIN_ARM, LOSE_MIN_ARM, LOSE_MAX_ARM,
    MALING_MIRROR, CHANGE_SEX, CHICKEN
]

# карты комнаты с проклятьями, специфичные для расы и класса
CHEAT = Buff('Чит. Можешь носить запрещённую шмотку.', 'tights', TIGHTS, require='Воин')
ILLUSION = Buff(
    ILLUSION, 'illusion',
    'Ужасный, огромный, непобедимый монстр за дверью был заменён на Огорошенную траву при помощи заклинания «Иллюзия».',
    require='Волшебник'
)
DIVINE_INTERDICTION = Buff('Божественное вмешательство. Автоматически проходишь следующий уровень.', 'god', GOD, require='Клирик')
door_cards_specific = [CHEAT, ILLUSION, DIVINE_INTERDICTION]
