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

## Implementation in Python

### 1. `SingletonMeta` (Metaclass)

The `SingletonMeta` class is a **metaclass**, which is a class for classes. It defines the behavior for creating instances of the `Singleton` class, ensuring that only one instance is created, even with multiple threads.

- **`_instances = {}`**: This dictionary stores the instances of the Singleton class. It is used to ensure that only one instance of the class is created.
  
- **`_lock = Lock()`**: This is a `Lock` object used for thread synchronization. When multiple threads attempt to access a shared resource at the same time, the lock ensures that only one thread can access the resource at a time, preventing race conditions.

- **`__call__(cls, *args, **kwargs)`**: This method is called when trying to create a new instance of the Singleton class. The `__call__` method is used by the metaclass to control the instantiation process. Here's the key logic:
  - **`with cls._lock:`**: The `with` statement acquires the lock, ensuring that only one thread can execute the code block at a time.
  - **`if cls not in cls._instances:`**: If an instance of the class does not exist, a new one is created using `super().__call__(*args, **kwargs)`. This calls the `__call__` method of the parent class (i.e., the method `__call__` of the class being instantiated).
  - **`cls._instances[cls] = instance`**: The created instance is saved in the `_instances` dictionary so that future calls to `Singleton` reuse this same instance.

The combination of the `Lock` and the condition **`if cls not in cls._instances:`** ensures that **only one instance** of the Singleton is created, even if multiple threads attempt to create the instance simultaneously.

### 2. `Singleton` Class

This class uses `SingletonMeta` as its **metaclass**, which gives it the behavior defined in `SingletonMeta` (i.e., ensuring a single instance).

- **`value: str`**: This is an attribute used to store a value, which will be used to demonstrate that the Singleton instance is shared.
  
- **`__init__(self, value: str)`**: This constructor initializes the `value` attribute. The value can only be set the first time the Singleton is instantiated.
  
- **`some_business_logic(self)`**: This is a placeholder for any business logic that the Singleton instance may need to execute. It is not used in this example but represents the idea that Singleton instances can have associated logic.

### 3. `test_singleton` Function

This function is called on two different threads to test whether the Singleton pattern is working correctly. It receives a value as an argument, creates a Singleton instance, and then prints the value.

```python
def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)
```

- The function prints the `value` of the Singleton instance, allowing us to check if the same instance is being reused across both threads.

### 4. Main Code

The main block creates and starts two threads that call the `test_singleton` function with different values (`"FOO"` and `"BAR"`). If the Singleton pattern is working correctly, both threads should print the same value, as they should be using the same Singleton instance.

```python
if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
        "If you see different values, "
        "then 2 singletons were created (booo!!)\n\n"
        "RESULT:\n"
    )

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
```

- **Expected output:** If you see the same value in both prints, it means that the Singleton was reused correctly. If you see different values, it means that two Singleton instances were created, which should not happen.
