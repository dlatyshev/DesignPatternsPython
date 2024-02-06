from beverage import *
from condiments import *


def main() -> None:
    my_coffee = HouseBlend(Size.VENTI)
    my_coffee = Mocha(my_coffee)
    my_coffee = Soy(my_coffee)
    my_coffee = Whip(my_coffee)

    print(my_coffee.get_description() + ". Cost: $" + str(my_coffee.cost()))


if __name__ == "__main__":
    main()