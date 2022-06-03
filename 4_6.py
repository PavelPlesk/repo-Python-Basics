# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

from itertools import count, cycle
from time import time, sleep

for i in count(int(input('Введите начальное значение итератора целых чисел: '))):
    if i <= 10:
        print(i)
    else:
        break

_alarm = cycle(['Внимание!!!', 'Пожар!!!', 'Срочно покиньте здание!!!'])
current_time = time()
while time() < current_time + 15:
    print(next(_alarm))
    sleep(0.5)
    print(next(_alarm))
    sleep(0.5)
    print(next(_alarm))
    sleep(1)
