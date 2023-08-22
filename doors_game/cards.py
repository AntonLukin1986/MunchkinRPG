"""Карты предметов, способностей, проклятий и т.п. Списки с каратми, сгруппированными по категориям."""
from doors_game.classes import Item, Buff, Boost, Curse
from doors_game.text import FRIENDSHIP, GOD, ILLUSION, POLLYMORPH, TIGHTS, USE_INVISIBLE

# базовый набор шмотки при стартовом уровне 0
HELM_COURAGE = Item('Шлем отваги [+1]', 'helmet', 1, image='monster_treasures/helm_courage')
SLIMY_ARMOR = Item('Слизистая оболочка [+1]', 'armor', 1, image='monster_treasures/slime_armor')
SANDALS = Item('Сандалеты протекторы [+1]', 'footgear', 1, image='monster_treasures/protectors')
LONG_POLE = Item('Одиннадцатифутовый шест [+1]', 'arm', 1, image='monster_treasures/pole')
NO_ITEM = Item('ничего', None, 0)

# специфическая шмотка класса при стартовом уровне 1
STAFF_NAPALM = Item('Посох напалма [+3]', 'arm', 3, require='Волшебник', image='monster_treasures/napalm')
SHIELD_UBIQUITY = Item('Вездешний щит [+3]', 'arm', 3, require='Воин', image='monster_treasures/shield')
MACE_SHARPNESS = Item('Палица остроты [+3]', 'arm', 3, require='Клирик', image='monster_treasures/mace')
# специфическая способность класса при статровом уровне 2
FRIENDSHIP_POTION = Buff(
    'Зелье дружбы - подружись с монстром\nи он пропустит тебя без битвы.', 'friendship',
    after_use=FRIENDSHIP, require='Волшебник', image='monster_treasures/friendship'
)
SPIKY_KNEES = Buff('Шипастые коленки.\nПолучаешь дополнительную силу +2', 'knees', require='Воин', image='monster_treasures/knees')
WISHING_RING = Buff('Хотельное кольцо.\nОтменяет любое проклятие', 'wishing_ring', require='Клирик', image='monster_treasures/ring')
# специфическая шмотка расы при стартовом уровне 3
HORNY_HELMET = Item('Шлем-рогач [+3]', 'helmet', 3, require='Эльф', image='monster_treasures/helmet')
SHORT_WIDE_ARMOR = Item('Коротоширокие латы [+3]', 'armor', 3, require='Дварф', image='monster_treasures/armor')
STEPLADDER = Item('Боевая стремянка [+3]', 'footgear', 3, require='Хафлинг', image='monster_treasures/footgear')
treasures_for_rank = [
    STAFF_NAPALM, SHIELD_UBIQUITY, MACE_SHARPNESS,
    FRIENDSHIP_POTION, SPIKY_KNEES, WISHING_RING,
    HORNY_HELMET, SHORT_WIDE_ARMOR, STEPLADDER
]

# базовые сокровища монстров
IMPRESSIVE_TITLE = Buff('Реально впечатляющий титул!\nДелает из тебя персону голубых кровей.\nПолучаешь +3 к боевой силе.', 'title', image='monster_treasures/title')
INVISIBILITY_POTION = Buff(
    'Зелье невидимости.\nПозволит автоматически убежать от монстра,\nесли провалишь смывку.', 'invisibility',
    after_use=USE_INVISIBLE, image='monster_treasures/invisibility'
)
PRETTY_BALLOONS = Boost('Клёвые шарики: +7 к дальнобойной атаке.', 7, image='monster_treasures/baloons')
MAGIC_MISSILE = Boost('Ракета магического назначения.\nУвеличивает дальнобойную атаку на 7', 7, image='monster_treasures/missile')
EL_RAD_ACID_POTION = Boost('Электро-кислотно-радиационное зелье.\nУвеличивает дальнобойную атаку на 7', 7, image='monster_treasures/electric')
# буст-заглушка для заполнения опустевшего списка сокровищ монстров (если игрок уровня 3 победил 7 монстров)
PLUG = Boost('Буст с истёкшим сроком годности.\nНичего не даёт - ты и так уже Рэмбо...', 0)
monster_treasures_base = [
    IMPRESSIVE_TITLE, INVISIBILITY_POTION, PRETTY_BALLOONS, MAGIC_MISSILE, EL_RAD_ACID_POTION
]

# сокровища монстров, специфичные для расы и класса
ELF_BOW = Item('Лучок с ленточками [+4]', 'arm', 4, require='Эльф', image='monster_treasures/bow')
DVARF_HUMMER = Item('Коленоотбойный молот [+4]', 'arm', 4, require='Дварф', image='monster_treasures/hummer')
HALFLING_SANDWICH = Item('Сэндвич «Душистая смерть» [+4]', 'arm', 4, require='Хафлинг', image='monster_treasures/sandwich')
# здесь ещё одно хотельное кольцо (определено выше)
POLLYMORPH_POTION = Buff(
    'Зелье попуморфа - превращает монстра в попугая,\nкоторый тут же улетает, оставляя свои сокровища.', 'pollymorph',
    after_use=POLLYMORPH, require='Волшебник', image='monster_treasures/pollymorph'
)
DOPPLEGANGER = Buff('Дупельгангер: увеличивает силу\nтвоих шмоток в два раза!', 'doppleganger', require='Воин', image='monster_treasures/dopple')
monster_treasures_specific = [
    ELF_BOW, DVARF_HUMMER, HALFLING_SANDWICH,
    POLLYMORPH_POTION, DOPPLEGANGER, WISHING_RING
]

# сокровища свободной комнаты
SLEEP_POTION = Boost('Спячечное зелье:\nувеличивает дальнобойную атаку на 3', 3, image='free_door/sleep')
BRAVERY_POTION = Boost('Зелье идиотской храбрости:\nувеличивает дальнобойную атаку на 3', 3, image='free_door/bravery')
COTION_PONFUSION = Boost('Пелье зутаницы:\nувеличивает дальнобойную атаку на 3', 3, image='free_door/ponfusion')
FLAMING_POTION = Boost('Зелье пламенной отравы:\nувеличивает дальнобойную атаку на 4', 4, image='free_door/flaming')
FREEZING_POTION = Boost('Зелье холодильного взрыва:\nувеличивает дальнобойную атаку на 4', 4, image='free_door/freezing')
SING_DANCE_SWORD = Item('Меч песни и пляски [+2]', 'arm', 2, image='free_door/sword')
SWISS_POLEARM = Item('Швейцарская армейская алебарда [+2]', 'arm', 2, image='free_door/swiss')
BANDANA = Item('Бандана сволочизма [+2]', 'helmet', 2, image='free_door/helmet')
FLAMING_ARMOR = Item('Пылающие латы [+2]', 'armor', 2, image='free_door/armor')
KICKING_BOOTS = Item('Башмаки могучего пенделя [+2]', 'footgear', 2, image='free_door/footgear')
free_room_treasures = [
    SLEEP_POTION, BRAVERY_POTION, COTION_PONFUSION, FLAMING_POTION, FREEZING_POTION,
    SING_DANCE_SWORD, SWISS_POLEARM, BANDANA, FLAMING_ARMOR, KICKING_BOOTS
]

# карты комнаты с проклятьями общие
LOSE_HELMET = Curse('Потеряй головняк.\nЕсли нет головняка - потеряй волосы.', 'lose', lose='helmet', image='curses/helmet')
LOSE_ARMOR = Curse('Потеряй броник.\nНет броника - нет проблем.', 'lose', lose='armor', image='curses/armor')
LOSE_FOOTGEAR = Curse('Потеряй обувку.\nЕсли её нет, то и терять нечего.', 'lose', lose='footgear', image='curses/footgear')
LOSE_MIN_ARM = Curse('Потеряй оружие в руках - скинь самое слабое.', 'lose', lose='min_arm', image='curses/min_arm')
LOSE_MAX_ARM = Curse('Невыносимо гнусное проклятье.\nПотеряй самое сильное оружие в руках.', 'lose', lose='max_arm', image='curses/max_arm')
MALING_MIRROR = Curse('Кривое зеркало.\nВ следующем бою бонус будет только у броника.', 'only_armor', image='curses/only_armor')
CHANGE_SEX = Curse('Смена пола - стань женщиной!\nИз-за смятения получаешь -5 в следующем бою.', 'woman', image='curses/woman')
CHICKEN = Curse('Курица на башке.\nПолучаешь минус один ко всем броскам кубика!', 'chicken', image='curses/chicken')
door_cards_base = [
    LOSE_HELMET, LOSE_ARMOR, LOSE_FOOTGEAR,
    LOSE_MIN_ARM, LOSE_MIN_ARM, LOSE_MAX_ARM,
    MALING_MIRROR, CHANGE_SEX, CHICKEN
]

# карты комнаты с проклятьями, специфичные для расы и класса
CHEAT = Buff('Чит. Можешь носить запрещённую шмотку.', 'cheat', after_use=TIGHTS, require='Воин', image='curses/cheat')
ILLUSION = Buff(
    ILLUSION, 'illusion',
    after_use='Ужасный, огромный, непобедимый монстр за дверью был заменён на Огорошенную траву при помощи заклинания «Иллюзия».',
    require='Волшебник', image='curses/illusion'
)
DIVINE_INTERDICTION = Buff(
    'Божественное вмешательство!\nПозволяет автоматически пройти следующий уровень.', 'god',
    after_use=GOD, require='Клирик', image='curses/god'
)
door_cards_specific = [CHEAT, ILLUSION, DIVINE_INTERDICTION]
TIGHTS = Item('Колготы великанской силы [+2]', 'legs', 2, image='curses/tights')
