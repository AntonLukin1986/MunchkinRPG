"""Общий текст для функции main."""
from termcolor import colored

PUSH_ENTER = '{} {} '.format(
    colored('Для продолжения нажми', 'blue'),
    colored('[enter]', 'blue', attrs=['bold', 'underline'])
)
ATTENTION = (
    '{attention} В ходе игры тебе нужно будет вводить различный текст.\n'
    'Кнопка {enter} служит для подтверждения ввода.\n'
    'Руководствуйся подсказками на экране!\n'
    'Для выхода из игры нажми {ctrl}+{c} или закрой основное окно.'
).format(
    attention=colored('Внимание!', 'red'),
    enter=colored('[enter]', 'blue', attrs=['bold', 'underline']),
    ctrl=colored('[Ctrl]', 'blue', attrs=['bold', 'underline']),
    c=colored('[C]', 'blue', attrs=['bold', 'underline'])
)
