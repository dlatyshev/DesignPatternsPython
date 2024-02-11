from abc import ABC
from enum import Enum


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Pizza(ABC):

    def __init__(self, size, description: str):
        self.__size = size
        self.__description = description

    @property
    def size(self):
        return self.__size

    @property
    def description(self):
        return self.__description

    def __str__(self):
        return self.__description


class CheesePizza(Pizza):

    def __init__(self, size):
        super().__init__(size, "Cheese Pizza")


class PepperoniPizza(Pizza):

    def __init__(self, size):
        super().__init__(size, "Pepperroni Pizza")


class ClamPizza(Pizza):

    def __init__(self, size):
        super().__init__(size, "Clam Pizza")


class VeganPizza(Pizza):

    def __init__(self, size):
        super().__init__(size, "Vegan Pizza")
