from enum import Enum
from pizza import Pizza, CheesePizza, ClamPizza, PepperoniPizza, VeganPizza, Size


class PizzaType(Enum):
    CHEESE = "cheese"
    PEPPERONI = "pepperoni"
    CLAM = "clam"
    VEGGIE = "veggie"


class SimplePizzaFactory:
    """A simple pizza factory."""

    @staticmethod
    def create_pizza(size: Size, pizza_type: PizzaType) -> Pizza:
        """Create a pizza of the specified type and size."""
        pizza_types = {
            PizzaType.CHEESE: CheesePizza,
            PizzaType.PEPPERONI: PepperoniPizza,
            PizzaType.CLAM: ClamPizza,
            PizzaType.VEGGIE: VeganPizza
        }
        return pizza_types[pizza_type](size)


if __name__ == "__main__":
    factory = SimplePizzaFactory()
    cheese_pizza = factory.create_pizza(Size.SMALL, PizzaType.CHEESE)
    veggie_pizza = factory.create_pizza(Size.LARGE, PizzaType.VEGGIE)
    print(cheese_pizza)
    print(veggie_pizza)
