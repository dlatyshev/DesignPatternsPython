from behavioral.strategy import behavior
from duck import MallardDuck, RubberDuck, ModelDuck


def main():
    mallard = MallardDuck()
    mallard.perform_fly()
    mallard.perform_quack()
    mallard.display()

    rubber = RubberDuck()
    rubber.perform_fly()
    rubber.perform_quack()
    rubber.display()

    model = ModelDuck()
    model.perform_fly()
    model.perform_quack()
    model.display()
    model.fly_behavior = behavior.FlyRocketPowered()
    model.perform_fly()


if __name__ == "__main__":
    main()
