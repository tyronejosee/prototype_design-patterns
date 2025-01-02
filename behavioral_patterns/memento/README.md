# **Memento**

It is a design pattern that allows capturing and restoring the internal state of an object without exposing its structure.

## **Purpose**

Facilitate the restoration of an object to a previous state without revealing internal details.

## **Problem**

You need to save and restore the state of an object, but you don’t want the internal details to be accessible or modifiable.

## **Solution**

The pattern uses three components: the **Originator** (which saves the state), the **Memento** (which stores the state), and the **Caretaker** (which manages the memento).

## **Pros**

- Allows undoing actions or restoring previous states.
- Encapsulates the internal details of an object.
- Facilitates the implementation of features like "undo" in applications.

## **Cons**

- Can lead to high memory consumption if many states are saved.
- Complicates the design by requiring multiple objects to manage the states.

## **Real-World Use Cases**

- "Undo" functionalities in text editors.
- Games where the game state can be restored to a previous point.
- Applications with complex workflows that need a backtracking option.

## **Relations with Other Patterns**

- **Command**: The Memento pattern can be used alongside Command to implement reversible operations.
- **Iterator**: It can work with the Iterator pattern to traverse and save different states of a collection of objects.
