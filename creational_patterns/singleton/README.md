# **Singleton**

## **Purpose**

- Ensures that a class has **only one instance** throughout the entire program and provides a **global access point** to that instance.

## **Problem it solves**

- Guarantees that a class has only one instance, which is useful for managing shared resources like databases or files.
- Prevents the creation of additional instances of a class, providing **global access** to the same instance.

## **Solution**

- **Privatize the constructor** of the class to prevent other objects from creating new instances.
- Create a **static method** to control the creation of the instance, ensuring that the same instance is always returned.

## **Analogy**

- A **government** is an example, as there is only one government for a country, and its access is global.

## **Applicability**

- Used when **only one instance** of a class is required, such as a **shared database**.
- Allows for **stricter control of global variables**, but guarantees that only one instance of the class exists.

## **Pros**

- Guarantees that a class has only one instance.
- Provides a global access point.
- The instance is **initialized only when needed**.

## **Cons**

- **Violates the Single Responsibility Principle** (solves two problems at once).
- Can mask **poor design** if used incorrectly.
- **Makes unit testing harder**, especially in multi-threaded environments.

## **Relationships with other patterns**

- **Facade** can turn into a Singleton.
- **Flyweight** can share instances, but a Singleton only has **one instance**.
- **Abstract Factory, Builder, Prototype** can be implemented as Singletons.
