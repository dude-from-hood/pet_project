

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_exists(self):
        """
        Треугольник существует, если каждая сторона треугольника меньше суммы двух других сторон.
        """
        if (
            self.a < self.b + self.c) and (
            self.b < self.a + self.c) and (
            self.c < self.a + self.b
        ):
            return True

        return False

    def is_equilateral(self):
        """
        Треугольник называется равносторонним, если у него все стороны равны
        """
        if not self.is_exists():
            return False

        return True if self.a == self.b == self.c else False

    def is_isosceles(self):
        """
        Треугольник называется равнобедренным, если у него две стороны равны
        """
        if not self.is_exists():
            return False

        if (
            self.a == self.b) or (
            self.b == self.c) or (
            self.c == self.a
        ):
            return True

        return False


if __name__ == '__main__':
    triangle = Triangle(5, 16, 5)
    print(f"Is Triangle exist: {triangle.is_exists()}")
    print(f"Is Equilateral: {triangle.is_equilateral()}")
    print(f"Is Isosceles: {triangle.is_isosceles()}")

