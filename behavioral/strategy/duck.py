from abc import ABC, abstractmethod
import behavior


class Duck(ABC):

    def __init__(self, fly_behavior: behavior.FlyBehavior, quack_behavior: behavior.QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self) -> None:
        pass

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()


class MallardDuck(Duck):

    def __init__(self):
        super().__init__(behavior.FlyWithWings(), behavior.Quack())

    def display(self):
        print("I'm a real Mallard duck.")


class RedHeadDuck(Duck):

    def __init__(self):
        super().__init__(behavior.FlyNoWay(), behavior.Quack())

    def display(self):
        print("I'm a real Red Head duck.")


class RubberDuck(Duck):

    def __init__(self):
        super().__init__(behavior.FlyNoWay(), behavior.Squeak())

    def display(self):
        print("I'm a real Rubber duck.")


class ModelDuck(Duck):

    def __init__(self):
        super().__init__(behavior.FlyNoWay(), behavior.MuteQuack())

    def display(self):
        print("I'm a model duck.")
