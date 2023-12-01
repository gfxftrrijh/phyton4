
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def check_triangle_existence(self):
        if self.side1 + self.side2 > self.side3 and self.side2 + self.side3 > self.side1 and self.side1 + self.side3 > self.side2:
            return True
        else:
            return False

    def find_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    def find_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

# Пример использования класса
triangle1 = Triangle(3, 4, 5)
print(triangle1.check_triangle_existence())  # True
print(triangle1.find_area())  # 6.0
print(triangle1.find_perimeter())  # 12