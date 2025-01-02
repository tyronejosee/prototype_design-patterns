from abc import ABC, abstractmethod
from typing import Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


# The base class that implements the chain of responsibility.
class AbstractHandler(Handler):
    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


# Stock verification handler
class StockHandler(AbstractHandler):
    def handle(self, request) -> Optional[str]:
        for item in request["items"]:
            if not item["in_stock"]:
                return f"Error: The product {item['name']} is not available in stock."
        return super().handle(request)


# Payment verification handler
class PaymentHandler(AbstractHandler):
    def handle(self, request) -> Optional[str]:
        if not request["payment_successful"]:
            return "Error: The payment was not processed correctly."
        return super().handle(request)


# Shipping handler
class ShippingHandler(AbstractHandler):
    def handle(self, request) -> Optional[str]:
        if not request["shipping_address"]:
            return "Error: No shipping address was provided."
        return super().handle(request)


# Final handler (if everything passed correctly)
class FinalHandler(AbstractHandler):
    def handle(self, request) -> Optional[str]:
        return "Order processed successfully!"


# Client function that simulates order processing
def process_order(handler: Handler, order: dict) -> None:
    result = handler.handle(order)
    print(result)


if __name__ == "__main__":
    # Creating the chain of handlers
    stock_handler = StockHandler()
    payment_handler = PaymentHandler()
    shipping_handler = ShippingHandler()
    final_handler = FinalHandler()

    stock_handler.set_next(
        payment_handler,
    ).set_next(
        shipping_handler
    ).set_next(final_handler)

    # Simulating an order with all necessary fields
    order = {
        "items": [
            {"name": "Laptop", "in_stock": True},
            {"name": "Mouse", "in_stock": True},
        ],
        "payment_successful": True,
        "shipping_address": "123 Main St, City, Country",
    }

    # Processing the order
    print("Processing the order...")
    process_order(stock_handler, order)

    # Simulating an order with an out-of-stock product
    order_invalid_stock = {
        "items": [
            {"name": "Laptop", "in_stock": True},
            {"name": "Mouse", "in_stock": False},
        ],
        "payment_successful": True,
        "shipping_address": "123 Main St, City, Country",
    }
    print("\nProcessing an order with an out-of-stock product...")
    process_order(stock_handler, order_invalid_stock)

    # Simulating an order with a failed payment
    order_invalid_payment = {
        "items": [
            {"name": "Laptop", "in_stock": True},
            {"name": "Mouse", "in_stock": True},
        ],
        "payment_successful": False,
        "shipping_address": "123 Main St, City, Country",
    }
    print("\nProcessing an order with a failed payment...")
    process_order(stock_handler, order_invalid_payment)

    # Simulating an order without a shipping address
    order_invalid_shipping = {
        "items": [
            {"name": "Laptop", "in_stock": True},
            {"name": "Mouse", "in_stock": True},
        ],
        "payment_successful": True,
        "shipping_address": None,
    }
    print("\nProcessing an order without a shipping address...")
    process_order(stock_handler, order_invalid_shipping)
