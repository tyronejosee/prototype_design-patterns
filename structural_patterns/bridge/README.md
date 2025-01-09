# **Bridge**

## **Purpose**

Separate an abstraction from its implementation so that both can evolve independently.

## **Problem**

A change in the implementation directly affects the abstraction and vice versa, resulting in a rigid system that is difficult to scale.

## **Solution**

Split the abstraction and implementation into separate hierarchies and connect them using composition.

## **Pros**

- Decouples abstraction from implementation.
- Enhances scalability: you can change the abstraction or implementation independently.
- Encourages adherence to the dependency inversion principle.

## **Cons**

- Increases design complexity.
- May be unnecessary if the system does not require multiple implementations.

## **Real-World Use Cases**

1. **Graphical Interfaces**: Abstraction of a component (button, window) with specific implementations for different operating systems (Windows, macOS, Linux).
2. **Databases**: Abstraction of SQL queries with implementations for different engines (PostgreSQL, MySQL, SQLite).
3. **Rendering**: Abstraction of geometric shapes (circle, square) with implementations for 2D or 3D rendering.

## **Relationships with Other Patterns**

- **Adapter**: Adapter converts incompatible interfaces; Bridge separates abstraction and implementation from the start.
- **Strategy**: Both delegate behavior, but Strategy does so to dynamically change algorithms, while Bridge decouples related hierarchies.
- **Composite**: Composite organizes objects into hierarchical structures, while Bridge separates related hierarchies.
