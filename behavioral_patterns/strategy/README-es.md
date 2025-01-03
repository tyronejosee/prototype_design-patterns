# **Strategy**

## **Propósito**

Permite cambiar el comportamiento de un objeto en tiempo de ejecución mediante la selección de una estrategia (algoritmo) diferente.

## **Problema**

Cuando un objeto tiene varios comportamientos posibles, el código puede volverse complejo debido a la necesidad de condicionales para decidir qué comportamiento ejecutar.

## **Solución**

Se define una interfaz común para las diferentes estrategias y se permite cambiar la estrategia utilizada sin modificar el objeto que la utiliza.

## **Pros**

- Mejora la flexibilidad y extensibilidad del código.
- Facilita la adición de nuevas estrategias sin modificar el código existente.
- Reduce la complejidad al eliminar condicionales.

## **Contras**

- Puede generar una gran cantidad de clases para cada estrategia.
- Si el número de estrategias es pequeño, este patrón podría ser innecesario.

## **Casos de Usos Reales**

- Algoritmos de ordenación, donde se puede elegir entre diferentes estrategias.
- Comportamientos de pago en una tienda online (diferentes métodos de pago).
- Diferentes tipos de compresión de archivos.

## **Relaciones con Otros Patrones**

- **State:** Ambos patrones permiten cambiar el comportamiento de un objeto, pero en **State**, el objeto cambia su comportamiento según su estado, mientras que en **Strategy**, el comportamiento es seleccionado explícitamente.
- **Strategy** y **Command** pueden usarse juntos para cambiar la forma de ejecutar acciones, seleccionando el comportamiento adecuado para una acción.
