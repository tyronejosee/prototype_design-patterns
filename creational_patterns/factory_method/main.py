from abc import ABC, abstractmethod


class Notification(ABC):
    """
    The Notification interface declares the operations that all concrete
    notifications must implement.
    """

    @abstractmethod
    def send(self, message: str) -> str:
        pass


class NotificationCreator(ABC):
    """
    The Creator declares the factory method that must return an object
    of the Notification type.
    """

    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def notify(self, message: str) -> str:
        """
        Core business logic that uses the notification object.
        """
        notification = self.create_notification()
        return notification.send(message)


class EmailNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending Email: {message}"


class SMSNotification(Notification):
    def send(self, message: str) -> str:
        return f"Sending SMS: {message}"


def client_code(
    notification_creator: NotificationCreator,
    message: str,
) -> None:
    print(f"Notification System: {notification_creator.notify(message)}")


if __name__ == "__main__":
    print("App: Launched with EmailNotificationCreator.")
    client_code(EmailNotificationCreator(), "Your order has been shipped!")
    print("\n")

    print("App: Launched with SMSNotificationCreator.")
    client_code(SMSNotificationCreator(), "Your OTP code is 123456.")
