# Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
# Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
# добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
# этих чисел к полученной ранее сумме и после этого завершить программу.


def repack(packed_str):
    new_num.clear()
    for n in packed_str.split():
        if n.isdigit():
            num_list.append(int(n))
            new_num.append(int(n))
        elif n in ['q', 'Q']:
            return 'q'
        else:
            print(f'Введены некорректные данные! "{n}" не является целым числом!')
    return


num_list = list()
new_num = list()
while repack(input('Введие данные: ')) != 'q':
    print(f'{sum(new_num)}({sum(num_list)})')
print(f'{sum(new_num)}({sum(num_list)})')