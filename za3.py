class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f"The {self.color} {self.name} is moving")

    def stop(self):
        print(f"The {self.color} {self.name} stopped")

    def turn(self, direction):
        print(f"The car turned {direction}")

    def show_speed(self):
        print(f"The current speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Speed exceeded in TownCar")
        else:
            print(f"The current speed of the {self.color} TownCar {self.name} is {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Speed exceeded in WorkCar")
        else:
            print(f"The current speed of the {self.color} WorkCar {self.name} is {self.speed}")


class PoliceCar(Car):
    pass


# Пример использования классов
town_car = TownCar(70, "red", "Sedan")
work_car = WorkCar(30, "white", "Van")
police_car = PoliceCar(80, "black and white", "Interceptor", True)

town_car.show_speed()
town_car.go()
town_car.turn("left")
town_car.stop()

work_car.show_speed()
work_car.go()
work_car.turn("right")
work_car.stop()

police_car.show_speed()
police_car.go()
police_car.turn("right")
police_car.stop()