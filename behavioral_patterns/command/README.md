# **Command**

## **Purpose**

Encapsulates a request as an object, allowing you to parameterize objects with operations, delay command execution, or record their history.

## **Problem**

When you need to execute operations at different times, reverse them, or allow different requesters (clients) to invoke commands independently of the object that performs the action (receiver).

## **Solution**

1. Create a common `Command` interface with an `execute()` method.
2. Implement concrete command classes that encapsulate requests and send them to the receiver.
3. Use an invoker to manage commands and control their execution.

## **Pros**

- **Decouples** the client from the receiver.
- Supports **undo/redo** actions.
- Allows implementing **command queues** and **macro-commands**.
- Facilitates **extensibility** by adding new commands.

## **Cons**

- Increases code **complexity** due to the creation of multiple classes.
- May lead to **overengineering** in simple cases.

## **Real-World Use Cases**

- **Text editors** with undo/redo support.
- **Job queues** in distributed systems.
- Device control in **home automation** (turning lights on/off, locking doors, etc.).
- **Menus** in graphical interfaces that perform different actions when clicked.

## **Relationships with Other Patterns**

- **Chain of Responsibility**: Can be used to delegate commands to different handlers.
- **Memento**: Can store the state before/after executing a command to support undo/redo.
- **Prototype**: Useful for cloning commands if they need to be reused.
- **Strategy**: Similar in encapsulating logic, but Command is more focused on requests and execution.
