# **Iterator**

## **Purpose**

Provides a way to sequentially access elements of a collection without exposing its internal representation.

## **Problem**

When you have a complex collection (lists, trees, graphs) and need to traverse its elements uniformly without revealing its internal structure or coupling the iteration logic to the collection.

## **Solution**

1. Define an interface for iterators with methods like `next()` and `has_next()`.
2. Implement concrete iterators to handle different ways of traversing the collection.
3. The collection provides compatible iterators without exposing its structure.

## **Pros**

- **Decouples** iteration logic from the collection.
- Allows multiple ways of iteration (forward, reverse, random).
- Facilitates **adding new traversal algorithms** without modifying the collection.
- **Simplifies** working with complex collections.

## **Cons**

- May increase **complexity** of the code if the iteration logic is simple.
- **Overhead** when an extensible design is not required.

## **Real Use Cases**

- **File explorers**: Traverse folders and files in a hierarchical order.
- **Streaming applications**: Navigate playlists or episodes in different orders.
- **Game systems**: Iterate over nodes in graphs or hierarchical structures.
- **Databases**: Traverse query results uniformly.

## **Relationships with Other Patterns**

- **Composite**: The iterator can traverse composite structures (trees).
- **Factory Method**: Creates custom concrete iterators for different collections.
- **Memento**: The iterator can be used to save and restore the state of a collection.
- **Observer**: Can traverse collections to notify observers.
