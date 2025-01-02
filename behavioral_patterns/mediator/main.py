from __future__ import annotations
from abc import ABC
from typing import List


class Mediator(ABC):
    """
    Mediator interface that declares methods
    for sending and receiving messages.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ChatMediator(Mediator):
    """
    Concrete Mediator that acts as a chat server,
    managing messages between users.
    """

    def __init__(self) -> None:
        self._users: List[User] = []

    def add_user(self, user: User) -> None:
        self._users.append(user)
        user.mediator = self

    def notify(self, sender: object, event: str) -> None:
        for user in self._users:
            # Avoid sending the message back to the sender.
            if user != sender:
                user.receive(event)


class BaseComponent:
    """
    Base class that allows storing a mediator instance within components.
    """

    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class User(BaseComponent):
    """
    Represents a user in the chat system.
    """

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def send(self, message: str) -> None:
        print(f"{self.name} sends: {message}")
        self.mediator.notify(self, f"{self.name}: {message}")

    def receive(self, message: str) -> None:
        print(f"{self.name} receives: {message}")


if __name__ == "__main__":
    # Client Code
    mediator = ChatMediator()

    user1 = User("Tyrone")
    user2 = User("Héctor")
    user3 = User("Alejandra")

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)

    print("Chat started:\n")
    user1.send("Hello everyone!")
    print("\n")
    user2.send("Hi Alejandra!")
    print("\n")
    user3.send("Hi to both of you!")
