# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [2, 4.5, 'Maria Andreeva is the best)', True, 2 + 3j, None]
for i in my_list:
    print(f'{i}: {type(i)}')