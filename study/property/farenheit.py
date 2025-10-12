if __name__ == '__main__':
    class Celsius:

        def __init__(self, temperature=None): #устанавливает значение _temperature (protected) поле
            self._temperature = temperature

        @property
        def temperature(self): #это геттер
            return self._temperature

        @temperature.setter
        def temperature(self, value): #имя в сеттере такое же, как в геттере
            if value < -273.15:
                raise ValueError("error")
            else:
                self._temperature = value

        def to_fahrenheit(self):
            return (self._temperature * 9/5) + 32


cel = Celsius(90)
print(cel.temperature)
cel.temperature = 190
print(cel.temperature)
print(cel.to_fahrenheit())