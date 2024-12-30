# **Factory Method**

- **Purpose**: Provide an interface for creating objects without specifying the exact class of the object to be created.

- **Problem**: The need to create class instances without directly coupling to concrete classes, making the code easier to extend and more flexible.

- **Solution**: Define a method for object creation, allowing subclasses to decide which class to instantiate. This decouples object creation from its usage.

## **Pros**

- **Decoupling**: Separates object creation from its usage.
- **Flexibility**: Allows changing the type of object without modifying client code.
- **Extensibility**: Makes it easier to add new product classes without changing existing code.

## **Cons**

- **Additional Complexity**: Introduces more classes and methods, potentially making the system more complex.
- **Excessive Abstraction**: Might be unnecessary if object creation is straightforward or rarely changes.

## **Real-World Use Cases**

- **Graphical User Interfaces**: When different types of buttons, text boxes, etc., need to be created depending on the operating system or platform.
- **Database Frameworks**: When different types of database connections (e.g., MySQL, PostgreSQL) need to be created without modifying client code.

## **Relationships with Other Patterns**

- **Abstract Factory**: Factory Method is a specific case of Abstract Factory, where a single method is used to create products.
- **Builder**: Both assist in object creation, but Builder focuses on step-by-step construction, while Factory Method centers on simple creation.
- **Singleton**: Can be used together to ensure that only one instance of an object is created via the Factory Method.
