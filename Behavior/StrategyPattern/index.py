from abc import ABC, abstractmethod
from dataclasses import dataclass


class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b


class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b


@dataclass
class Context:
    strategy: Strategy

    def execute_strategy(self, a, b):
        return self.strategy.execute(a, b)


if __name__ == "__main__":
    add_strategy = AddStrategy()
    subtract_strategy = SubtractStrategy()

    context = Context(add_strategy)
    print(context.execute_strategy(5, 3))  # Outputs: 8

    context.strategy = subtract_strategy
    print(context.execute_strategy(5, 3))  # Outputs: 2
