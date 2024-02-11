from pizza import Pizza, CheesePizza, ClamPizza, PepperoniPizza, VeganPizza, Size


class SimplePizzaFactory:

    @staticmethod
    def create_pizza(size: Size, pizza_type: str) -> Pizza:
        """Create a pizza of the specified type and size."""
        pizza_types = {
            "cheese": CheesePizza,
            "pepperoni": PepperoniPizza,
            "clam": ClamPizza,
            "veggie": VeganPizza
        }
        return pizza_types[pizza_type](size)


if __name__ == "__main__":
    factory = SimplePizzaFactory()
    cheese_pizza = factory.create_pizza(Size.SMALL, "cheese")
    veggie_pizza = factory.create_pizza(Size.LARGE, "veggie")
    print(cheese_pizza)
    print(veggie_pizza)
