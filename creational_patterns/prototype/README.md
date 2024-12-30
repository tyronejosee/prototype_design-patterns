# **Prototype**

- **Purpose**: Allows the creation of new objects by cloning an existing instance (prototype) instead of creating objects from scratch.

- **Problem**: Creating complex objects can be costly or complicated, especially when many similar instances are needed.

- **Solution**: Use a prototype (base object) that can be copied or modified as needed, avoiding repetitive creation.

## **Pros**

- Improves performance by avoiding the creation of new objects from scratch.
- Facilitates the creation of objects with similar configurations.
- Useful in scenarios where objects need to be configured similarly but with slight variations.

## **Cons**

- Can be difficult to implement if objects are complex or have many internal dependencies.
- Cloning may not be possible if objects contain references to resources that cannot be copied (e.g., database connections).

## **Real-World Use Cases**

- **Graphic design software**: Cloning objects such as shapes and styles (e.g., Adobe Illustrator).
- **Games**: Creating characters or enemies with similar traits but slight variations.

## **Relationships with Other Patterns**

- **Factory Method**: Both create objects, but the Prototype clones an existing instance instead of creating a new one from scratch.
- **Abstract Factory**: The Prototype can be used in combination with Abstract Factory to create families of objects with cloning.
