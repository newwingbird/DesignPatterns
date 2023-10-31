from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class State(ABC):
    @abstractmethod
    def handle(self, context):
        pass


class StateA(State):
    def handle(self, context):
        print("Handling in State A")
        context.state = StateB()


class StateB(State):
    def handle(self, context):
        print("Handling in State B")
        context.state = StateA()


@dataclass
class Context:
    state: State

    def request(self):
        self.state.handle(self)


if __name__ == "__main__":
    context = Context(StateA())
    context.request()  # Outputs: Handling in State A
    context.request()  # Outputs: Handling in State B
