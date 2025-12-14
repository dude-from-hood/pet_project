class Circle:
    def __init__(self, radius):
        if not Circle.is_positive(radius):
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        # Преобразуем диаметр в радиус и создаем новый экземпляр
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def is_positive(num):
        return num > 0

    @staticmethod
    def area(radius):
        return 3.14 * (radius**2)


# Создание круга через радиус (обычный способ)
circle1 = Circle(5)        # радиус = 5
print(circle1.radius)
# Создание круга через диаметр (альтернативный способ)
circle2 = Circle.from_diameter(10)  # диаметр = 10, радиус = 5
print(circle2.radius)