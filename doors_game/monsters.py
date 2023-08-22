"""Монстры."""
from doors_game.classes import Monster

# монстры 1 уровня
GOBLIN = Monster('Увечный гоблин', 1, 'Нельзя недооценивать калеку', image='monsters/1_goblin')
KOSTIN = Monster('Мистер Костин', 1.2, 'Скелет в чьём-то шкафу', image='monsters/1_kostin')
KRISOTKA = Monster('Молотая крысотка', 1.4, 'Опасная милашка', image='monsters/1_krisotka')
PLANT = Monster('Огорошенная трава', 1, 'Даже если умудришься проиграть - смывка автоматическая!', image='monsters/trava')
# монстры 2 уровня
HORSE = Monster('Конь андедный', 1.2, 'Жеребец апокалипсиса', image='monsters/2_horse')
LEPROKON = Monster('Лепрокон', 1.4, 'Сбежал из лепрозория', image='monsters/2_leprokon')
SLIZ = Monster('Сочащаяся слизь', 1.6, 'Мерзкая жижа', image='monsters/2_sliz')
# монстры 3 уровня
GARPISTKI = Monster('Гарпистки', 1.4, 'Песни на заказ', image='monsters/3_garpistki')
RIGACHU = Monster('Рыгачу', 1.6, 'Отвратительная атака', image='monsters/3_rigachu')
UTKONTIKORA = Monster('Утконтикора', 1.8, 'Родом из Австралии', image='monsters/3_utkontikora')
# монстры 4 уровня
GAZEBO = Monster('Газебо', 1.6, 'Обычная беседка...', image='monsters/4_gazebo')
LAGUSHKI = Monster('Улётные лягушки', 1.8, 'Летающие земноводные', image='monsters/4_lagushki')
PITBUL = Monster('Питбуль', 2, 'Осторожно - злая собака!', image='monsters/4_pitbul')
# монстры 5 уровня
AMAZONKA = Monster('Амазонка', 1.8, 'Подружка Конана-варвара', image='monsters/5_amazonka')
LICESOS = Monster('Лицесос', 2, 'Этот поцелуй ты не забудешь...', image='monsters/5_licesos')
MADEMONUAZELI = Monster('Мадемонуазели', 2.2, 'Светские львицы', image='monsters/5_mademonuazeli')
# монстры 6 уровня
NOS = Monster('Блуждающий нос', 2, 'С Гоголем на короткой ноге', image='monsters/6_nos')
ORKI = Monster('3872 орка', 2.2, 'Орки. 3872 шт. Ни больше, ни меньше', image='monsters/6_orki')
TROLL = Monster('Сетевой тролль', 2.4, 'Обитает на просторах Интернета', image='monsters/6_troll')
# монстры 7 уровня
BIGFUT = Monster('Бигфут', 2.2, 'Покупает обувь под заказ', image='monsters/7_bigfut')
VAMPIR = Monster('Закос под вампира', 2.4, 'Пересмотрел фильмов про Дракулу...', image='monsters/7_vampir')
YAZICHDEMON = Monster('Языческий демон', 2.6, 'Свободно владеет десятью языками', image='monsters/7_yazichdemon')
# монстры 8 уровня
BROILER = Monster('Сердитый бройлер', 2.4, 'Узнал, что не сможет летать', image='monsters/8_broiler')
GOLEM = Monster('Обдолбанный голем', 2.6, 'Смотрит мультики без телевизора', image='monsters/8_golem')
UZAS = Monster('Невыразимо жуткий неописуемый ужас', 2.8, 'Страх, как он есть', image='monsters/8_uzas')
# монстры 9 уровня
BRATIA = Monster('Бледные братья', 2.6, 'Джентельмены удачи', image='monsters/9_bratia')
GIPOGRIF = Monster('Гиппогриф', 2.8, 'Плод необычного союза', image='monsters/9_gipogrif')
TSAR = Monster('Царь Тут', 3, 'И Тут и Там', image='monsters/9_tsar')
# монстры 10 уровня
BULROG = Monster('Бульрог', 2.8, 'Из самой преисподней', image='monsters/10_bulrog')
DRAKON = Monster('Плутониевый дракон', 3, 'Бурей рожденный, с блондинкой обручённый', image='monsters/10_drakon')
KALMADZILA = Monster('Кальмадзилла', 3.2, 'Бывшая жена Паладина', image='monsters/10_kalmadzila')
# финальный босс
CTHULHU = Monster('Великий и Ужасный Ктулху', 3.5, 'Пощады не жди!', image='monsters/cthulhu')

MONSTERS = {
    1: (GOBLIN, KOSTIN, KRISOTKA),
    2: (HORSE, LEPROKON, SLIZ),
    3: (GARPISTKI, RIGACHU, UTKONTIKORA),
    4: (GAZEBO, LAGUSHKI, PITBUL),
    5: (AMAZONKA, LICESOS, MADEMONUAZELI),
    6: (NOS, ORKI, TROLL),
    7: (BIGFUT, VAMPIR, YAZICHDEMON),
    8: (BROILER, GOLEM, UZAS),
    9: (BRATIA, GIPOGRIF, TSAR),
    10: (BULROG, DRAKON, KALMADZILA)
}
