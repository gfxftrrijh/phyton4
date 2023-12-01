class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount / 100)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)  # переопределение метода init


class Human:
    def __init__(self, money):
        self.money = money
        self.current_house = None

    def make_deal(self, house, price):
        self.money -= price
        self.current_house = house
        print("Поздравляем, вы купили дом!")

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if final_price <= self.money:
            self.make_deal(house, final_price)
        else:
            print("У вас недостаточно денег для покупки этого дома.")


def main():
    human = Human(100000)
    small_house = SmallHouse(60000)

    while True:
        print("\nМеню:")
        print("1. Показать доступные деньги")
        print("2. Показать текущий дом")
        print("3. Купить дом")
        print("4. Выход")
        choice = input("Выберите действие (1/2/3/4): ")

        if choice == '1':
            print("У вас", human.money, "денег")
        elif choice == '2':
            if human.current_house:
                print("У вас есть дом со следующими параметрами:")
                print("Площадь:", human.current_house._area, "м2")
                print("Цена:", human.current_house._price)
            else:
                print("У вас нет текущего дома")
        elif choice == '3':
            discount = float(input("Введите размер скидки: "))
            human.buy_house(small_house, discount)
        elif choice == '4':
            print("Выход из меню")
            break
        else:
            print("Неправильный выбор. Пожалуйста, выберите 1, 2, 3 или 4")


if __name__ == "__main__":
    main()
