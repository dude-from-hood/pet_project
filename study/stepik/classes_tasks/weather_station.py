class WeatherStation:
    __shared_attr = {
        "temperature": 0,
        "humidity": 0,
        "pressure": 0
    }

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr  # Подменяем в инициализации __dict__
                                           # ссылкой на созданный моно-словарь
    def update_data(self, temperature, humidity, pressure):
        """изменяет состояние сразу трех показаний."""
        self.__dict__['temperature'] = temperature
        self.__dict__['humidity'] = humidity
        self.__dict__['pressure'] = pressure

    def get_current_data(self):
        return tuple(self.__dict__.values())


w = WeatherStation()
w.update_data(1,2,3)
print(w.get_current_data())