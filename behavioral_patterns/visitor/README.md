# **Visitor**

## **Purpose**

Allows adding new operations to an object structure without modifying its classes.

## **Problem**

Adding functionality to complex classes in a hierarchy without breaking the Open/Closed Principle.

## **Solution**

Create a separate _visitor_ class that implements the operations, delegating execution to specific methods for each type of object in the hierarchy.

## **Pros:**

- Complies with the Open/Closed Principle.
- Centralizes operations in one place.
- Makes it easier to add new operations.

## **Cons:**

- Makes it harder to add new types of elements in the hierarchy.
- Increases coupling between the visitor and the visited classes.

## **Real Use Cases**

- **Compilers:** Traversing syntax trees to analyze or generate code.
- **Reporting tools:** Extracting data from complex structures like XML/JSON.
- **Graphics systems:** Operations such as rendering or bounding box calculation.

## **Relationships with Other Patterns**

- **Composite:** Visitor often operates on hierarchical structures managed by Composite.
- **Iterator:** Helps to traverse structures where the Visitor will be applied.
- **Strategy:** Can be compared to Visitor when a dynamic change in operations is needed.
