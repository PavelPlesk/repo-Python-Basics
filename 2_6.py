# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
# название, цена, количество, единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.

n = 1
catalog = list()

# Создадим небольшой исходный каталог:
catalog.append((n, {'Название': 'Компьютер', 'Цена': 2700, 'Количество': 4, 'Единицы': 'шт.'}))
n += 1
catalog.append((n, {'Название': 'Холодильник', 'Цена': 2000, 'Количество': 7, 'Единицы': 'шт.'}))
n += 1
catalog.append((n, {'Название': 'Удлинитель', 'Цена': 500, 'Количество': 25, 'Единицы': 'м'}))
n += 1

# analitics = dict(Название=set(), Цена=set(), Количество=set(), Единицы=set())

# Далее можно добавить элементы по запросу:
while True:
    if input('Хотите создать новый товар? ') in ['Да', 'да', 'Д', 'д']:
        new_item = {'Название': input('Введите название товара: '),
                    'Цена': input('Введите цену товара: '),
                    'Количество': input('Введите количество товара: '),
                    'Единицы': input('Укажите единицы измерения товара: ')}
        # Также для новых элементов можно задать дополнительные характеристики
        if input('Хотите добавить характеристики? ') in ['Да', 'да', 'Д', 'д']:
            charact = input('Введите название характеристики: ')
            new_item[charact] = input('Введите значение:')
        catalog.append((n, new_item))
        n += 1
    else:
        break

# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например, название. Тогда значение — список
# значений-характеристик, например, список названий товаров.

analitics = dict()
for i in catalog:
    for k in i[1]:
        analitics.setdefault(k, set())

for i in catalog:
    for k in analitics:
        analitics[k].add(i[1].get(k))
        analitics[k].discard(None)

for i, k in analitics.items():
    print(i, k)
