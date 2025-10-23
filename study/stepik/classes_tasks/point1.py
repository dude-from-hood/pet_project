
class Point:
    list_points = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

        # вводим учет всех экземпляров класса
        self.list_points.append(self)

    # def __repr__(self):
    #     return f"({self.x}:{self.y})"

    def get_distance_to_origin(self):
        # Проверяем наличие атрибутов x и y
        if hasattr(self, 'x') and hasattr(self, 'y'):
            return (self.x ** 2 + self.y ** 2) ** 0.5

    def display(self):
        # Проверяем наличие атрибутов x и y
        if not hasattr(self, 'x') or not hasattr(self, 'y'):
            print("Координаты не заданы")
        else:
            print(f"Point({self.x}, {self.y})")

    def get_distance(self, point):
        # Проверяем, является ли point экземпляром класса Point
        if not isinstance(point, Point):
            print("Передана не точка")
            return None

        if (hasattr(self, 'x') and hasattr(self, 'y')) and (hasattr(point, 'x') and hasattr(point, 'y')):
            d = ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** (0.5)
            return d

        else:
            print("Координаты не заданы")
            return None


    def get_point_with_max_distance(self):
        """
        Найти самую удаленную точку из созданных.

        Если есть несколько точек, находящихся на одинаковом максимальном расстоянии от начала координат,
        нужно выбрать ту, которая находится выше остальных на координатной плоскости.

        Если и таких точек несколько, покажите первую.
        """

        list_dict_points = []

        for item in Point.list_points:
            list_dict_points.append(item.__dict__)

        # Сортируем точки по двум ключам:
        # 1. Расстояние до начала координат (в порядке убывания)
        # 2. Координата y (в порядке убывания)

        list_dict_points.sort(
            key=lambda p: ((p['x'] ** 2 + p['y'] ** 2) ** 0.5, p['y']),
            reverse=True
        )

        # Выводим самую удаленную точку через метод display
        max_point = Point(list_dict_points[0]['x'], list_dict_points[0]['y'])
        max_point.display()
        return max_point

if __name__ == '__main__':
    p1 = Point(4, 5)
    p2 = Point(2, 4)
    p3 = Point(5, 1)
    p2.get_point_with_max_distance()


