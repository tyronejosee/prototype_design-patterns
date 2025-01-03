# **Observer Pattern**

## **Purpose**

Allow an object (subject) to notify other objects (observers) about state changes without tightly coupling them.

## **Problem**

When an object changes its state and other objects depend on it, direct coupling can be difficult to manage.

## **Solution**

Use a subscription and notification mechanism where observers subscribe to a subject to receive updates.

## **Pros**

- Decouples the subject from the observers.
- Makes it easier to add new observers without modifying the subject.
- Ideal for systems with multiple reactions to state changes.

## **Cons**

- There could be a performance impact if there are many observers.
- The order of notifications can be difficult to control.

## **Real-World Use Cases**

- Updating user interfaces when data changes in an application.
- Event systems in games or graphical interfaces.
- Implementing notifications in mobile applications.

## **Relations with Other Patterns:**

- **Mediator:** Both decouple components, but the Mediator organizes centralized communication, while the Observer distributes updates in a decentralized way.
- **Strategy:** Both allow changing behaviors without modifying the object using them, but in the Observer, the observer objects react to changes in the subject.
