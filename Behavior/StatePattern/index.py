class State:
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


class Context:
    def __init__(self, state: State):
        self.state = state

    def request(self):
        self.state.handle(self)


context = Context(StateA())
context.request()  # Outputs: Handling in State A
context.request()  # Outputs: Handling in State B
