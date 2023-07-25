"""Карты предметов, способностей, проклятий и т.п.
Списки с каратми, сгруппированными по категориям."""
from classes import Item, Buff, Boost, Curse

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
POLLYMORPH_POTION = Buff(
    'Зелье попуморфа - превращает монстра в попугая, который тут же улетает, оставляя сокровища.',
    'pollymorph', require='Волшебник'
)
DOPPLEGANGER = Buff(
    'Дупельгангер - увеличивает силу в текущем бою вдвое???', 'doppleganger', require='Воин'
)
WISHING_RING = Buff(
    'Хотельное кольцо - отменяет любое проклятие', 'wishing_ring', require='Клирик'
)
# специфическая шмотка расы при стартовом уровне 3
HORNY_HELMET = Item('Шлем-рогач +3 (головняк)', 'helmet', 3, require='Эльф')
SHORT_WIDE_ARMOR = Item('Коротоширокие латы +3 (броник)', 'armor', 3, require='Дварф')
STEPLADDER = Item('Боевая стремянка +3 (обувка)', 'footgear', 3, require='Халфлинг')
treasures_for_level = [
    STAFF_NAPALM, SHIELD_UBIQUITY, MACE_SHARPNESS,
    POLLYMORPH_POTION, DOPPLEGANGER, WISHING_RING,
    HORNY_HELMET, SHORT_WIDE_ARMOR, STEPLADDER
]

# базовые сокровища монстров
IMPRESSIVE_TITLE = Buff('Реально впечатляющий титул - делает из тебя персону голубых кровей. Получаешь +3 к боевой силе.', 'title')
INVISIBILITY_POTION = Buff('Зелье невидимости - позволит автоматически убежать от монстра, если провалишь смывку.', 'invisibility')
PRETTY_BALLOONS = Boost('Клёвые шарики: увеличивают специальную атаку на 5', 5)
MAGIC_MISSILE = Boost('Ракета магического назначения: увеличивает специальную атаку на 5', 5)
EL_RAD_ACID_POTION = Boost('Электро-ксилотно-радиационное зелье: увеличивает специальную атаку на 5', 5)
monster_treasures_base = [
    IMPRESSIVE_TITLE, INVISIBILITY_POTION, PRETTY_BALLOONS, MAGIC_MISSILE,
    EL_RAD_ACID_POTION
]

# сокровища монстров, специфичные для расы и класса
ELF_BOW = Item('Лучок с ленточками +4 (в руке)', 'arm', 4, require='Эльф')
DVARF_HUMMER = Item('Коленоотбойный молот +4 (в руке)', 'arm', 4, require='Дварф')
HALFLING_SANDWICH = Item('Сэндвич «Душистая смерть» +4 (в руке)', 'arm', 4, require='Халфлинг')
# ещё одно хотельное кольцо
FRIENDSHIP_POTION = Buff(
    'Зелье дружбы - подружись с монстром и он пропустит тебя без битвы', 'friendship', require='Волшебник'
)
SPIKY_KNEES = Buff(
    'Шипастые коленки - дают тебе дополнительную силу +2', 'knees', require='Воин'
)
monster_treasures_specific = [
    ELF_BOW, DVARF_HUMMER, HALFLING_SANDWICH,
    FRIENDSHIP_POTION, SPIKY_KNEES, WISHING_RING
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
CHANGE_SEX = Curse('Смена пола - стань женщиной! Из-за смятения получаешь -5 в следующем бою.',  'woman')
DUCK_DOOM = Curse('Роковой нырок. Откатись на самый первый этаж. Без вариантов!', 'doom')
door_cards_base = [
    LOSE_HELMET, LOSE_ARMOR, LOSE_FOOTGEAR,
    LOSE_MIN_ARM, LOSE_MIN_ARM, LOSE_MAX_ARM,
    MALING_MIRROR, CHANGE_SEX, DUCK_DOOM
]

# карты комнаты с проклятьями, специфичные для расы и класса
CHEAT = Buff('Чит. Можешь носить запрещённую шмотку.', 'tights', require='Воин')
ILLUSION = Buff('Морок: следующий монстр будет заменён на Огорошенную траву.', 'illusion', require='Волшебник')
DIVINE_INTERDICTION = Buff('Божественное вмешательство. Автоматически проходишь следующий уровень.', 'god', require='Клирик')
door_cards_specific = [CHEAT, ILLUSION, DIVINE_INTERDICTION]
