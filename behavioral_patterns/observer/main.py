from abc import ABC, abstractmethod


class Task(ABC):
    """
    The Task class is the Subject that will notify
    observers when the state changes.
    """

    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class TaskManager(Task):
    """
    The Concrete Task stores the task's state
    and notifies observers when it changes.
    """

    _state: str = "Pending"
    _observers = []

    def attach(self, observer) -> None:
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def set_state(self, state: str) -> None:
        self._state = state
        print(f"Task: The state has changed to: {self._state}")
        self.notify()


# 3. The Observer (Notification System)
class Observer(ABC):
    """
    The Observer defines the `update` method,
    which will be called by the Subject when its state changes.
    """

    @abstractmethod
    def update(self, task: Task) -> None:
        pass


# 4. ConcreteObservers (Concrete Notification Systems)
class NotificationSystem(Observer):
    """
    A notification system that reacts when the task's state changes.
    """

    def update(self, task: Task) -> None:
        print("Notification: The task has changed state.")


class UserInterface(Observer):
    """
    A user interface that must update
    when the task's state changes.
    """

    def update(self, task: Task) -> None:
        print("UI: Updating the interface with the new task state.")


if __name__ == "__main__":
    # Create the Subject
    task = TaskManager()

    # Create the observers (Notification System and User Interface)
    notification_system = NotificationSystem()
    ui_system = UserInterface()

    # Attach observers
    task.attach(notification_system)
    task.attach(ui_system)

    # Change the subject's state
    task.set_state("Completed")

    # Detach an observer
    task.detach(ui_system)

    # Only the remaining observer will be notified
    task.set_state("Pending")
