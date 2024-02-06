from typing import Protocol


class Observer(Protocol):
    def update(self, temp: float, humidity: float, pressure: float):
        pass


class DisplayElement(Protocol):
    def display(self):
        pass


class CurrentConditionDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")


class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.measurements = []
        self.temperature = None
        self.humidity = None

    def update(self, temp, humidity, pressure):
        self.temperature = temp
        self.humidity = humidity
        self.measurements.append((self.temperature, self.humidity))
        self.display()

    def display(self):
        print(f"Average temperature: {sum(measurement[0] for measurement in self.measurements) / len(self.measurements)}F degrees")
        print(f"Average humidity: {sum(measurement[1] for measurement in self.measurements) / len(self.measurements)}% humidity")
