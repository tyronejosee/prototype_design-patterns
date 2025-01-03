from __future__ import annotations
from abc import ABC, abstractmethod


class PaymentContext:
    """
    The Context defines the interface of interest to clients.
    It allows clients to choose a payment strategy at runtime.
    """

    def __init__(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> PaymentStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: PaymentStrategy) -> None:
        self._strategy = strategy

    def process_payment(self, amount: float) -> None:
        """
        The Context delegates the payment processing to the Strategy object.
        """

        print(f"Payment of {amount} using {self._strategy.__class__.__name__}")
        self._strategy.process_payment(amount)


class PaymentStrategy(ABC):
    """
    The PaymentStrategy interface declares operations common to all supported
    payment methods.
    """

    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing Credit Card payment of {amount}...")


class PayPalPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of {amount}...")


class BankTransferPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing Bank Transfer payment of {amount}...")


if __name__ == "__main__":
    # Client code: the user selects the payment method dynamically

    # Initially, the payment strategy is Credit Card
    payment_context = PaymentContext(CreditCardPayment())
    print("Client: Using Credit Card payment method.")
    payment_context.process_payment(100.0)
    print()

    # Changing strategy to PayPal
    print("Client: Switching to PayPal payment method.")
    payment_context.strategy = PayPalPayment()
    payment_context.process_payment(200.0)
    print()

    # Changing strategy to Bank Transfer
    print("Client: Switching to Bank Transfer payment method.")
    payment_context.strategy = BankTransferPayment()
    payment_context.process_payment(300.0)
