from abc import ABC, abstractmethod
from enum import Enum


class Size(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage(ABC):
    def __init__(self, size: Size) -> None:
        self.description = "Unknown Beverage"
        self.__size = size

    def get_description(self) -> str:
        return f"{self.description}, size: {self.size.name}"

    @abstractmethod
    def cost(self) -> float:
        pass

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: Size):
        self.__size = size


class HouseBlend(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89 * self.size.value


class Decaf(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05 * self.size.value


class DarkRoast(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99 * self.size.value


class Espresso(Beverage):

    def __init__(self, size: Size) -> None:
        super().__init__(size)
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99 * self.size.value

