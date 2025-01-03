# **Template Method**

## **Purpose**

Defines the structure of an algorithm in a method, leaving some steps for subclasses to implement. It allows subclasses to redefine certain steps without changing the overall structure.

## **Problem**

When there are similar algorithms with common steps, but some details need to be implemented differently in each subclass.

## **Solution**

A method is created in the base class that defines the algorithm, calling methods that can be overridden by subclasses to implement the specific details.

## **Pros**

- Promotes code reuse.
- Maintains consistency in the structure of the algorithms.
- Allows subclasses to customize steps without changing the overall flow.

## **Cons**

- Can lead to a rigid design if subclasses need to change the base algorithm too much.
- Difficult to maintain if the base algorithm changes frequently.

## **Real-World Use Cases**

- Online payment processes with common steps (validation, payment, confirmation), where some steps vary depending on the payment method.
- File or data processing with a common flow of operations, but with specific details depending on the file type or format.
- Test automation with common steps, but with differences in configuration or execution of the tests.

## **Relationships with Other Patterns**

- **Strategy:** Both allow modifying behaviors, but in **Template Method**, the flow is predetermined, and only variations in specific steps are allowed, while in **Strategy**, the entire behavior is interchangeable.
- **Factory Method:** Both can be used to create products (objects), but **Factory Method** focuses on creating objects, while **Template Method** defines an algorithm with steps to be implemented.
