from dataclasses import dataclass
from abc import ABC, abstractmethod


class BookState(ABC):
    @abstractmethod
    def handle(self, book):
        pass


class AvailableState(BookState):
    def handle(self, book):
        print("The book is now checked out.")
        book.state = CheckedOutState()


class CheckedOutState(BookState):
    def handle(self, book):
        print("The book is now returned.")
        book.state = AvailableState()


@dataclass
class Book:
    state: BookState

    def change_state(self):
        self.state.handle(self)


if __name__ == "__main__":
    book = Book(AvailableState())
    book.change_state()  # Outputs: The book is now checked out.
    book.change_state()  # Outputs: The book is now returned.
