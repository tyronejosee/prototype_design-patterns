from abc import ABC, abstractmethod


# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Window(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_window(self) -> Window:
        pass


# Concrete Factories
class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_window(self) -> Window:
        return WindowsWindow()


class MacFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_window(self) -> Window:
        return MacWindow()


# Concrete Products
class WindowsButton(Button):
    def render(self) -> str:
        return "Rendering a Windows-style Button."


class MacButton(Button):
    def render(self) -> str:
        return "Rendering a Mac-style Button."


class WindowsWindow(Window):
    def render(self) -> str:
        return "Rendering a Windows-style Window."


class MacWindow(Window):
    def render(self) -> str:
        return "Rendering a Mac-style Window."


# Client Code
def client_code(factory: UIFactory):
    button = factory.create_button()
    window = factory.create_window()
    print(button.render())
    print(window.render())


if __name__ == "__main__":
    print("Client: Using Windows UI Factory:")
    client_code(WindowsFactory())

    print("\nClient: Using Mac UI Factory:")
    client_code(MacFactory())
