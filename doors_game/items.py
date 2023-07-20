"""Карты предметов, способностей, проклятий и т.п.
Списки с каратми, сгруппированными по категориям."""
from classes import Item, Buff, Boost, Curse

# базовый набор шмотки при стартовом уровне 0
HELM_COURAGE = Item('helmet', 1, 'Шлем отваги +1 (головняк)')
SLIMY_ARMOR = Item('armor', 1, 'Слизистая оболочка +1 (броник)')
SANDALS = Item('footgear', 1, 'Сандалеты протекторы +1 (обувка)')
LONG_POLE = Item('arm', 1, 'Одиннадцатифутовый шест +1 (в руке)')
NO_ITEM = Item(None, 0, 'отсутствует')
# входят в аргументы по умолчанию в классе персонажа

# специфическая шмотка класса при стартовом уровне 1
STAFF_NAPALM = Item('arm', 3, 'Посох напалма +3 (в руке)', 'Волшебник')
SHIELD_UBIQUITY = Item('arm', 3, 'Вездешний щит +3 (в руке)', 'Воин')
MACE_SHARPNESS = Item('arm', 3, 'Палица остроты +3 (в руке)', 'Клирик')
# специфическая способность класса при статровом уровне 2
POLLYMORPH_POTION = Buff(
    'Зелье попуморфа - превращает монстра в попугая, который тут же улетает, '
    'оставляя сокровища.', 'Волшебник'
)
DOPPLEGANGER = Buff(
    'Дупельгангер - увеличивает силу в текущем бою вдвое???', 'Воин'
)
WISHING_RING = Buff(
    'Хотельное кольцо - отменяет любое действующее проклятие или следующее, '
    'с которым столкнёшься.', 'Клирик'
)
# специфическая шмотка расы при стартовом уровне 3
HORNY_HELMET = Item('helmet', 3, 'Шлем-рогач +3 (головняк)', 'Эльф')
SHORT_WIDE_ARMOR = Item('armor', 3, 'Коротоширокие латы +3 (броник)', 'Дварф')
STEPLADDER = Item('footgear', 3, 'Боевая стремянка +3 (обувка)', 'Халфлинг')
treasures_for_level = [
    STAFF_NAPALM, SHIELD_UBIQUITY, MACE_SHARPNESS,
    POLLYMORPH_POTION, DOPPLEGANGER, WISHING_RING,
    HORNY_HELMET, SHORT_WIDE_ARMOR, STEPLADDER
]

# базовые сокровища монстров
IMPRESSIVE_TITLE = Buff(
    'Реально впечатляющий титул - делает из тебя персону голубых кровей. '
    'Получаешь +3 к боевой силе.'
)
INVISIBILITY_POTION = Buff(
    'Зелье невидимости - позволит автоматически убежать от монстра, '
    'если провалишь смывку.'
)
PRETTY_BALLOONS = Boost('Клёвые шарики: увеличивают специальную атаку на 5', 5)
MAGIC_MISSILE = Boost(
    'Ракета магического назначения: увеличивает специальную атаку на 5', 5
)
EL_RAD_ACID_POTION = Boost(
    'Электро-ксилотно-радиационное зелье: увеличивает специальную атаку на 5',
    5
)
monster_treasures_base = [
    IMPRESSIVE_TITLE, INVISIBILITY_POTION, PRETTY_BALLOONS, MAGIC_MISSILE,
    EL_RAD_ACID_POTION
]

# сокровища монстров, специфичные для расы и класса
ELF_BOW = Item('arm', 4, 'Лучок с ленточками +4 (в руке)', 'Эльф')
DVARF_HUMMER = Item('arm', 4, 'Коленоотбойный молот +4 (в руке)', 'Дварф')
HALFLING_SANDWICH = Item(
    'arm', 4, 'Сэндвич «Душистая смерть» +4 (в руке)', 'Халфлинг'
)
WISHING_RING = Buff(
    'Хотельное кольцо - отменяет любое действующее проклятие или следующее, '
    'с которым столкнёшься', 'Клирик'
)
FRIENDSHIP_POTION = Buff(
    'Зелье дружбы - подружись с монстром и он пропустит тебя без битвы',
    'Волшебник'
)
SPIKY_KNEES = Buff(
    'Шипастые коленки - дают тебе дополнительную силу +2', 'Воин'
)
monster_treasures_specific = [
    ELF_BOW, DVARF_HUMMER, HALFLING_SANDWICH,
    FRIENDSHIP_POTION, SPIKY_KNEES, WISHING_RING
]

# сокровища свободной комнаты
SLEEP_POTION = Boost('Спячечное зелье: увеличивает специальную атаку на 2', 2)
BRAVERY_POTION = Boost(
    'Зелье идиотской храбрости: увеличивает специальную атаку на 2', 2
)
COTION_PONFUSION = Boost(
    'Пелье зутаницы: увеличивает специальную атаку на 2', 2
)
FLAMING_POTION = Boost(
    'Зелье пламенной отравы: увеличивает специальную атаку на 3', 3
)
FREEZING_POTION = Boost(
    'Зелье холодильного взрыва: увеличивает специальную атаку на 3', 3
)
SING_DANCE_SWORD = Item('arm', 2, 'Меч песни и пляски +2 (в руке)')
SWISS_POLEARM = Item('arm', 2, 'Швейцарская армейская алебарда +2 (в руке)')
BANDANA = Item('helmet', 2, 'Бандана сволочизма +2 (головняк)')
FLAMING_ARMOR = Item('armor', 2, 'Пылающие латы +2 (броник)')
KICKING_BOOTS = Item('footgear', 2, 'Башмаки могучего пенделя +2 (обувка)')
free_way_treasures = [
    SLEEP_POTION, BRAVERY_POTION, COTION_PONFUSION, FLAMING_POTION,
    FREEZING_POTION, SING_DANCE_SWORD, SWISS_POLEARM, BANDANA,
    FLAMING_ARMOR, KICKING_BOOTS
]

# карты комнаты с проклятьями общие
LOSE_FOOTGEAR = Curse('Потеряй обувку. Если её нет, то и терять нечего.')
LOSE_ARMOR = Curse('Потеряй броник. Нет броника - нет проблем.')
LOSE_HEADGEAR = Curse('Потеряй головняк. Если нет головняка - потеряй волосы.')
LOSE_arm = Curse(  # в список передаётся 2 штуки
    'Потеряй мелкую шмотку (оружие в руках): скинь самое слабое.'
)
LOSE_arm_MAX = Curse(
    'Невыносимо гнусное проклятье: потеряй самую сильную из своих шмоток '
    '(оружие в руках).'
)
MALING_MIRROR = Curse(
    'Кривое зеркало. В следующем бою бонус будет только у броника.'
)
DUCK_DOOM = Curse(
    'Роковой нырок. Откатись на самый первый этаж. Без вариантов!'
)
CHANGE_SEX = Curse(
    'Смена пола - стань женщиной! Из-за смятения получаешь -5 в следующем бою.'
)
door_cards_base = [
    LOSE_FOOTGEAR, LOSE_ARMOR, LOSE_HEADGEAR, LOSE_arm, LOSE_arm,
    LOSE_arm_MAX, MALING_MIRROR, DUCK_DOOM, CHANGE_SEX
]

# карты комнаты с проклятьями, специфичные для расы и класса
DIVINE_INTERDICTION = Curse(
    'Божественное вмешательство. Автоматически проходишь следующий уровень.',
    'Клирик'
)
CHEAT = Curse(
    'Чит. Можешь носить запрещённую шмотку.', 'Воин'
)  # Колготы великанской силы +2
ILLUSION = Curse(
    'Морок: следующий монстр будет заменён на Огорошенную траву.', 'Волшебник'
)
door_cards_specific = [DIVINE_INTERDICTION, CHEAT, ILLUSION]
