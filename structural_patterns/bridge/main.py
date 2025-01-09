from __future__ import annotations
from abc import ABC, abstractmethod


# Abstraction
class PaymentProcessor:
    """
    Defines the interface for clients (platform users).
    """

    def __init__(self, implementation: PaymentGateway) -> None:
        self.implementation = implementation

    def process_payment(self, amount: float) -> str:
        return (
            f"PaymentProcessor: Processing payment of {amount} USD:\n"
            f"{self.implementation.execute_payment(amount)}"
        )


# Extended Abstraction
class PremiumPaymentProcessor(PaymentProcessor):
    """
    Extends functionality for premium users.
    """

    def process_payment(self, amount: float) -> str:
        return (
            f"PremiumPaymentProcessor: Processing premium payment of {amount} USD:\n"
            f"{self.implementation.execute_payment(amount)}"
        )


# Implementation
class PaymentGateway(ABC):
    """
    Defines the interface for different payment gateways.
    """

    @abstractmethod
    def execute_payment(self, amount: float) -> str:
        pass


# Concrete Implementations
class CreditCardPayment(PaymentGateway):
    def execute_payment(self, amount: float) -> str:
        return f"CreditCardPayment: Payment of {amount} USD processed with credit card."


class PayPalPayment(PaymentGateway):
    def execute_payment(self, amount: float) -> str:
        return f"PayPalPayment: Payment of {amount} USD processed with PayPal."


# Client Code
def client_code(payment_processor: PaymentProcessor, amount: float) -> None:
    print(payment_processor.process_payment(amount), end="")


if __name__ == "__main__":
    # Credit card payment for a basic user
    gateway = CreditCardPayment()
    processor = PaymentProcessor(gateway)
    client_code(processor, 100.0)

    print("\n")

    # PayPal payment for a premium user
    gateway = PayPalPayment()
    processor = PremiumPaymentProcessor(gateway)
    client_code(processor, 250.0)
