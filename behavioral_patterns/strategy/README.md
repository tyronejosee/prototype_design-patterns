# **Strategy**

## **Purpose**

Allows changing the behavior of an object at runtime by selecting a different strategy (algorithm).

## **Problem**

When an object has multiple possible behaviors, the code can become complex due to the need for conditionals to decide which behavior to execute.

## **Solution**

A common interface is defined for the different strategies, and the strategy used can be changed without modifying the object that uses it.

## **Pros**

- Improves flexibility and extensibility of the code.
- Facilitates adding new strategies without modifying the existing code.
- Reduces complexity by eliminating conditionals.

## **Cons**

- Can generate a large number of classes for each strategy.
- If the number of strategies is small, this pattern may be unnecessary.

## **Real-World Use Cases**

- Sorting algorithms, where different strategies can be chosen.
- Payment behaviors in an online store (different payment methods).
- Different types of file compression.

## **Relationships with Other Patterns**

- **State:** Both patterns allow changing an object's behavior, but in **State**, the object changes its behavior based on its state, while in **Strategy**, the behavior is explicitly selected.
- **Strategy** and **Command** can be used together to change the way actions are executed, selecting the appropriate behavior for an action.
