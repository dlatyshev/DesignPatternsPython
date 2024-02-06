from typing import Protocol


class Subject(Protocol):

    def register_observer(self, observer) -> None:
        pass

    def remove_observer(self, observer) -> None:
        pass

    def notify_observers(self) -> None:
        pass


class WeatherData(Subject):

    def __init__(self):
        self.__observers = []
        self.__temperature = 0
        self.__humidity = 0
        self.__pressure = 0

    def set_measurements(self, temperature, humidity, pressure):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.notify_observers()

    def get_temperature(self):
        return self.__temperature

    def get_humidity(self):
        return self.__humidity

    def get_pressure(self):
        return self.__pressure

    def register_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temperature, self.__humidity, self.__pressure)

