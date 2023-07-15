"""Текст для функции play_intro. Введение."""
from termcolor import colored

from texts import colored_text as clr

INTRO_1 = '''Приветствую тебя, искатель приключений! Приготовься познакомиться с удивительной страной {}.
Шаг за шагом тебе предстоит открыть для себя её бескрайние просторы и восхитительные пейзажи, таинственные
закоулки и скрытые от любопытных глаз потусторонние измерения. Так же ты обязательно познакомишься с
необычными обитателями, населяющими эту чудесную страну, которые точно не оставят тебя равнодушным.
Тебе предстоит раскрыть множество тайн и загадок, а может быть, кто знает, совершить не один героический подвиг!
И для всего этого тебе даже не понадобятся ни виза, ни заграничный паспорт! В наше-то время...'''.format(clr.COUNTRY)

INTRO_2 = '''Запасись чаёчком с печеньками и дай волю своему воображению, ведь впереди тебя ждёт уникальная ролевая игра
с небывалым открытым миром и невероятно богатой игровой механикой. А гибкость и вариабельность игрового процесса
просто поражает воображение. Только не забывай поглядывать на часы. Потому что этот фэнтезийный мир обязательно увлечёт
тебя с головой. Удачи в твоих приключениях! И помни: {}, что бы это ни значило...'''.format(colored('vivus ercapus', 'yellow', attrs=['bold']))