# **Decorator**

## **Purpose**

Add additional responsibilities to an object dynamically without modifying its structure.

## **Problem**

When we need to extend the functionality of objects without altering their base code or creating subclasses, and we want to do so flexibly.

## **Solution**

Use a wrapper object (decorator) to extend the functionality of the original object.

## **Pros**

- Promotes the open/closed principle.
- Enhances flexibility by dynamically adding functionality.
- Facilitates behavior composition without altering existing classes.

## **Cons**

- Can lead to a large number of small classes, increasing complexity.
- May become difficult to maintain if decorators are excessively nested.

## **Real-World Use Cases**

1. **User Interfaces**: Add behaviors like validation, security, or formatting to an input field without modifying the base object.
2. **Logging**: Add event logging functionality to functions or methods without altering their original logic.
3. **Caching**: Apply caching to a function without changing its code.

## **Relationships with Other Patterns**

- **Strategy**: Both aim to extend behavior, but while Decorator wraps objects, Strategy changes behavior by selecting a different strategy.
- **Composite**: Decorator can be used with Composite to add responsibilities to components without modifying their classes.
