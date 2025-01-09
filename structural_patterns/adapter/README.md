# **Adapter**

## **Purpose**

Allows classes with incompatible interfaces to work together by converting one class's interface to another expected by the client.

## **Problem**

A client needs to use a class with a different or incompatible interface.

## **Solution**

Create an adapter object that acts as a bridge, translating calls from the interface expected by the client to the interface of the adapted class.

## **Pros**

- Facilitates the reuse of existing classes with incompatible interfaces.
- Increases flexibility by decoupling the client from the concrete implementation.

## **Cons**

- Increases code complexity.
- Can lead to a design that is excessively dependent on adapters.

## **Real Use Cases**

1. **Legacy system integration**: Using old APIs with new clients.
2. **Frameworks**: Using external libraries with different internal structures.
3. **Hardware and software**: Translating protocols between devices or operating systems.
4. **Cloud services**: Converting interfaces between different services.

## **Relationships with Other Patterns**

- **Bridge**: Both decouple interfaces, but Bridge separates abstractions from implementations, while Adapter only translates interfaces.
- **Decorator**: Both can alter behaviors, but the purpose of Adapter is compatibility, not functionality extension.
- **Facade**: Simplifies interfaces but does not adapt them.
