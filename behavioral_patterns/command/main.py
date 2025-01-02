from __future__ import annotations
from abc import ABC, abstractmethod


# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# Simple Command for placing the order
class PlaceOrderCommand(Command):
    def __init__(self, order: Order) -> None:
        self._order = order

    def execute(self) -> None:
        print(f"Placing order for {self._order.product_name}...")


# Complex Command for handling post-order actions
# (e.g., sending emails, updating inventory)
class PostOrderCommand(Command):
    def __init__(self, receiver: Receiver, order: Order) -> None:
        self._receiver = receiver
        self._order = order

    def execute(self) -> None:
        print("Post-order actions initiated.")
        self._receiver.send_confirmation_email(self._order.customer_email)
        self._receiver.update_inventory(self._order.product_name)


# Receiver that knows how to perform the business logic
class Receiver:
    def send_confirmation_email(self, email: str) -> None:
        print(f"Receiver: Sending confirmation email to {email}.")

    def update_inventory(self, product_name: str) -> None:
        print(f"Receiver: Updating inventory for {product_name}.")


# The Order class holds the details of the order
class Order:
    def __init__(self, product_name: str, customer_email: str) -> None:
        self.product_name = product_name
        self.customer_email = customer_email


# Invoker responsible for triggering commands
class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def process_order(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: Processing order...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


# Client code
if __name__ == "__main__":
    # The client creates an order and sets up commands
    order = Order("Laptop", "customer@example.com")
    invoker = Invoker()
    invoker.set_on_start(PlaceOrderCommand(order))
    receiver = Receiver()
    invoker.set_on_finish(PostOrderCommand(receiver, order))

    # Process the order using the invoker
    invoker.process_order()
