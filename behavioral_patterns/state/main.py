from __future__ import annotations
from abc import ABC, abstractmethod


class OrderContext:
    """
    The OrderContext defines the interface for the order status.
    It also maintains a reference to the current state of the order.
    """

    _state = None

    def __init__(self, state: OrderState) -> None:
        self.transition_to(state)

    def transition_to(self, state: OrderState) -> None:
        """
        The Context allows changing the State object at runtime.
        """
        print(f"Order Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def handle_approve(self) -> None:
        if self._state is not None:
            self._state.handle_approve()
        else:
            print("State is None")

    def handle_ship(self) -> None:
        if self._state is not None:
            self._state.handle_ship()
        else:
            print("State is None")

    def handle_deliver(self) -> None:
        if self._state is not None:
            self._state.handle_deliver()
        else:
            print("State is None")


class OrderState(ABC):
    """
    The base OrderState class declares methods
    that all Concrete States should implement.
    """

    @property
    def context(self) -> OrderContext:
        return self._context

    @context.setter
    def context(self, context: OrderContext) -> None:
        self._context = context

    @abstractmethod
    def handle_approve(self) -> None:
        pass

    @abstractmethod
    def handle_ship(self) -> None:
        pass

    @abstractmethod
    def handle_deliver(self) -> None:
        pass


class PendingState(OrderState):
    def handle_approve(self) -> None:
        print("PendingState: Order approved, transitioning to Processing.")
        self.context.transition_to(ProcessingState())

    def handle_ship(self) -> None:
        print("PendingState: Order cannot be shipped yet.")

    def handle_deliver(self) -> None:
        print("PendingState: Order cannot be delivered yet.")


class ProcessingState(OrderState):
    def handle_approve(self) -> None:
        print("ProcessingState: Order is already being processed.")

    def handle_ship(self) -> None:
        print("ProcessingState: Order shipped, transitioning to Shipped.")
        self.context.transition_to(ShippedState())

    def handle_deliver(self) -> None:
        print("ProcessingState: Order cannot be delivered yet.")


class ShippedState(OrderState):
    def handle_approve(self) -> None:
        print("ShippedState: Order has already been shipped.")

    def handle_ship(self) -> None:
        print("ShippedState: Order is already shipped.")

    def handle_deliver(self) -> None:
        print("ShippedState: Order delivered, transitioning to Delivered.")
        self.context.transition_to(DeliveredState())


class DeliveredState(OrderState):
    def handle_approve(self) -> None:
        print("DeliveredState: Order has been delivered, no changes possible.")

    def handle_ship(self) -> None:
        print("DeliveredState: Order cannot be shipped anymore.")

    def handle_deliver(self) -> None:
        print("DeliveredState: Order has already been delivered.")


if __name__ == "__main__":
    # Creating the Order Context with Pending State
    order = OrderContext(PendingState())

    # Approving the order, moving to Processing State
    order.handle_approve()

    # Shipping the order, moving to Shipped State
    order.handle_ship()

    # Delivering the order, moving to Delivered State
    order.handle_deliver()

    # Trying to approve an order that has already been delivered
    order.handle_approve()
