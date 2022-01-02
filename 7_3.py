# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать
# класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки
# (целое число). В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно.
class Cell:
    def __init__(self, cells):
        self.cells = cells

    # Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
    # исходных двух клеток.
    def __add__(self, other):
        return Cell(self.cells + other.cells)

    # Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
    # двух клеток больше нуля, иначе выводить соответствующее сообщение.
    def __sub__(self, other):
        return Cell(self.cells - other.cells) if self.cells > other.cells else "Операция вычитания невозможна!"

    # Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
    # количества ячеек этих двух клеток.
    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    # Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
    # количества ячеек этих двух клеток.
    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def __str__(self):
        return str(self.cells)

    # В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    # Данный метод позволяет организовать ячейки по рядам.
    # Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно
    # переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются
    # все оставшиеся.
    # Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
    # вернет строку: *****\n*****\n**.
    # Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
    # строку: *****\n*****\n*****.
    def make_order(self, str_len):
        return "".join(["*" if _ % str_len else "*\n" for _ in range(1, self.cells + 1)])


cell_1 = Cell(3)
cell_2 = Cell(4)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(Cell(12).make_order(5))
