class Car():
    def __init__(self, name, color, is_police=False):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, new_speed=90):
        self.speed = new_speed
        return print(f"{self.color} {self.name} движется со скоростью {self.speed} км/ч.")

    def stop(self):
        self.speed = 0
        return print(f"{self.color} {self.name} остановился.")

    def turn(self, direction):
        return print(f"{self.color} {self.name} повернул {direction}.")

    def show_speed(self):
        return print(f"{self.speed} км/ч.")


class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            return print(f"{self.speed} км/ч.")
        else:
            return print(f"{self.speed} км / ч. Превышение разрешенной скорости!")


class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    def show_speed(self):
        if self.speed <= 40:
            return print(f"{self.speed} км/ч.")
        else:
            return print(f"{self.speed} км / ч. Превышение разрешенной скорости!")


class PoliceCar(Car):
    pass


auto_1 = Car("Мерседес", "Красный")
auto_1.go(120)
auto_1.show_speed()
auto_1.turn("налево")
auto_1.show_speed()
auto_1.stop()
auto_1.show_speed()

auto_2 = TownCar("Фольксваген", "Серый")
auto_2.go(30)
auto_2.show_speed()
auto_2.go(120)
auto_2.show_speed()
auto_2.stop()
auto_2.show_speed()

auto_3 = SportCar("Феррари", "Желтый")
auto_3.go(30)
auto_3.show_speed()
auto_3.go(120)
auto_3.show_speed()
auto_3.stop()
auto_3.show_speed()

auto_4 = PoliceCar("полицейский автомобиль", "Синий")
auto_4.go(30)
auto_4.show_speed()
auto_4.go(120)
auto_4.show_speed()
auto_4.stop()
auto_4.show_speed()

auto_5 = WorkCar("ГАЗ", "Синий")
auto_5.go(30)
auto_5.show_speed()
auto_5.go(120)
auto_5.show_speed()
auto_5.stop()
auto_5.show_speed()
