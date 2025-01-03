# **State**

## **Purpose**

Allows an object to change its behavior when its internal state changes, making it appear as though the object is changing its class.

## **Problem**

When an object has many possible states, the code can become difficult to manage, with scattered conditionals and state changes.

## **Solution**

Use the State pattern to delegate the logic related to each state to separate objects, each representing a different possible state.

## **Pros**

- Improves code readability and organization.
- Avoids excessive use of conditionals.
- Facilitates the addition of new states without modifying the main object.

## **Cons**

- Can lead to a large number of classes for each state.
- If the number of states is small, using this pattern may be unnecessary.

## **Real-World Use Cases**

- Flow control in state machines (e.g., payments, order statuses).
- Applications with different operating modes (e.g., a text editor with editing and preview modes).
- Games where characters or environments have different behaviors depending on their state.

## **Relations with Other Patterns**

- **Strategy:** Both allow an object's behavior to change based on state, but in **Strategy**, the behavior is defined outside of the object, while in **State**, the object itself changes its behavior.
- **State** and **Command** can be used together to manage behavior based on the state and the actions to be executed.
