import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


class Component:
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    """
    Concrete Components provide default implementations of the operations.
    There might be several variations of these classes.
    """

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.
        """
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class LoggingDecorator(Decorator):
    """
    Logging Decorator adds logging functionality to any Component it wraps.
    """

    def operation(self) -> str:
        result = self.component.operation()
        logging.info(f"Operation result: {result}")
        return result


class ConcreteDecoratorA(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    print(f"RESULT: {component.operation()}", end="")


if __name__ == "__main__":
    # Componente simple
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # Componente con decoradores de logging
    logged_component = LoggingDecorator(simple)
    print("Client: Now I've got a decorated component with logging:")
    client_code(logged_component)
    print("\n")

    # Componente con decoradores adicionales
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    logged_decorator = LoggingDecorator(decorator2)
    print(
        "Client: Now I've got a decorated component with "
        "logging and additional decorators:"
    )
    client_code(logged_decorator)
