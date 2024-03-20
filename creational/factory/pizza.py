from abc import ABC
from enum import Enum


class Size(Enum):
    """Represents pizza sizes."""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Pizza(ABC):
    """Represents a pizza."""

    def __init__(self, size, description: str):
        self.__size = size
        self.__description = description

    @property
    def size(self):
        """Return the size of the pizza."""
        return self.__size

    @property
    def description(self):
        """Return the description of the pizza."""
        return self.__description

    def __str__(self):
        return self.__description


class CheesePizza(Pizza):
    """Cheese pizza."""
    def __init__(self, size):
        super().__init__(size, "Cheese Pizza")


class PepperoniPizza(Pizza):
    """Pepperoni pizza."""
    def __init__(self, size):
        super().__init__(size, "Pepperroni Pizza")


class ClamPizza(Pizza):
    """Clam pizza."""
    def __init__(self, size):
        super().__init__(size, "Clam Pizza")


class VeganPizza(Pizza):
    """Vegan pizza."""
    def __init__(self, size):
        super().__init__(size, "Vegan Pizza")
