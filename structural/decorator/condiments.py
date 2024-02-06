from beverage import Beverage


class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(size=beverage.size)
        self.beverage = beverage

    def cost(self) -> float:
        return self.beverage.cost()


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", with Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20 * self.beverage.size.value


class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", with Milk"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10 * self.beverage.size.value


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", with Soy"

    def cost(self) -> float:
        return self.beverage.cost() + 0.15 * self.beverage.size.value


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        super().__init__(beverage)

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10 * self.beverage.size.value

