from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters
import time


class Originator(ABC):
    """
    The Originator class contains the state that needs to be saved.
    """

    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def save(self) -> Memento:
        """
        Saves the current state in a memento.
        """
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Restores the state from a memento.
        """
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")

    @abstractmethod
    def do_something(self) -> None:
        """
        A method that can change the state of the Originator.
        """
        pass


class Memento(ABC):
    """
    Memento interface. Does not expose the real state, only the metadata.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    """
    Concrete Memento that stores the real state.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        Returns the state of the Originator.
        """
        return self._state

    def get_name(self) -> str:
        """
        Display name of the memento.
        """
        return f"{self._date} / ({self._state}...)"

    def get_date(self) -> str:
        return self._date


class TextEditor(Originator):
    """
    Text editor that contains the document content.
    """

    def __init__(self, content: str) -> None:
        super().__init__(content)

    def edit(self, new_content: str) -> None:
        """
        The editor changes the text content.
        """
        print(f"Editor: Changing text content to: {new_content}")
        self._state = new_content

    def do_something(self) -> None:
        """
        Simulated operation method,
        which does not change the state in this case,
        but could be any other method that affects the content.
        """
        print("Editor: Performing an important operation.")
        self._state = self._generate_random_string(30)
        print(f"Editor: My new state is: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))


class Caretaker:
    """
    The caretaker holds the text editor's mementos.
    """

    def __init__(self, editor: TextEditor) -> None:
        self._mementos = []
        self._editor = editor

    def backup(self) -> None:
        print("\nCaretaker: Saving the editor's state...")
        self._mementos.append(self._editor.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring to state: {memento.get_name()}")
        try:
            self._editor.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Edit history:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    editor = TextEditor("Initial document text.")
    caretaker = Caretaker(editor)

    caretaker.backup()  # Save the first state
    time.sleep(1)
    editor.edit("Edited text 1.")

    caretaker.backup()  # Save the second state
    time.sleep(1)
    editor.edit("Edited text 2.")

    caretaker.backup()  # Save the third state
    time.sleep(1)
    editor.edit("Edited text 3.")

    print()
    caretaker.show_history()  # Show edit history

    print("\nClient: Now, let's undo the last change.\n")
    caretaker.undo()  # Undo to previous state

    print("\nClient: Once more!\n")
    caretaker.undo()  # Undo to previous state
