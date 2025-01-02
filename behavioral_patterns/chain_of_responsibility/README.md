# **Chain of Responsibility**

**Purpose**:  
Allows a request to be passed through a chain of receiver objects, where each object has the opportunity to handle the request, without the sender knowing who will process it.

**Problem**:  
When you have multiple objects that can handle a request, but you don’t want the sender to know which specific object will handle it.

**Solution**:  
A chain of objects capable of handling requests is established. Each object in the chain decides whether to handle the request or pass it to the next one.

## **Pros**

- Decouples the sender from the logic that handles the request.
- Facilitates adding new functionality without modifying existing code.
- Simplifies request management by breaking the process into smaller handlers.

## **Cons**

- Can make the control flow harder to follow.
- If the chain is long, it may impact performance.
- Errors can be difficult to trace if not properly handled.

## **Real-World Use Cases**

- **Order processing** in e-commerce, where different steps like stock verification, payment, and shipping are handled by different objects.
- **Technical support**, where different agents handle issues based on the type of request (billing, configuration, etc.).
- **Request filtering** in security systems, where different levels of validation are performed by different modules.

## **Relationships with Other Patterns**

- **Strategy**: Both patterns delegate tasks to different objects, but **Chain of Responsibility** handles a sequential flow, while **Strategy** allows explicit selection of a strategy.
- **Command**: Although both can invoke behavior on different objects, **Command** encapsulates a request in an object, while **Chain of Responsibility** allows a series of objects to process the request.
