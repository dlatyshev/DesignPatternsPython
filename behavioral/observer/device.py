from observer import StatisticsDisplay, CurrentConditionDisplay
from subject import WeatherData


def main():
    weather_data = WeatherData()
    statistics_display = StatisticsDisplay(weather_data)
    current_condition_display = CurrentConditionDisplay(weather_data)
    weather_data.set_measurements(10, 20, 30)
    weather_data.set_measurements(20, 30, 40)
    weather_data.set_measurements(30, 40, 50)


if __name__ == "__main__":
    main()
