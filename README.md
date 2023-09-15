# Munchkin RPG
### Текстовая ролевая игра по мотивам настолки "Манчкин"

Чтобы поиграть на Windows - *скачать Munchkin RPG.exe и запустить*

Конвертация в исполняемый Windows файл:
1. Установить *pyinstaller*
```
pip install pyinstaller
```
2. Клонировать проект
```
git clone https://github.com/AntonLukin1986/MunchkinRPG.git
```
3. Создать и активировать виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
4. Установить зависимости
```
pip install -r requirements.txt
```
5. Перейти на уровень выше корневой папки игры
```
cd ..
```
6. Выполнить команду
```
pyinstaller --onefile --add-data="munchkin_rpg/images;./images/" --add-data="munchkin_rpg/mp3;./mp3/" --collect-all=pyfiglet --name="Munchkin RPG" --icon="munchkin_rpg/icon.ico" munchkin_rpg/main.py
```
7. Файл с игрой **Munchkin RPG.exe** появится в папке **dist**
