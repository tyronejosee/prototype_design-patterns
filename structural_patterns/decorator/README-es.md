# **Decorator**

## **Propósito**

Añadir responsabilidades adicionales a un objeto de manera dinámica sin modificar su estructura.

## **Problema**

Cuando necesitamos extender las funcionalidades de objetos sin alterar su código base ni crear subclases, y hacerlo de manera flexible.

## **Solución**

Se utiliza un objeto envolvente (decorador) que extiende la funcionalidad del objeto original.

## **Pros**

- Promueve el principio de abierto/cerrado.
- Mejora la flexibilidad al agregar funcionalidades de forma dinámica.
- Facilita la composición de comportamientos sin alterar clases existentes.

## **Contras**

- Puede generar una gran cantidad de clases pequeñas, lo que aumenta la complejidad.
- Puede ser difícil de mantener si los decoradores son demasiado anidados.

## **Casos de Uso Reales**

1. **Interfaces de usuario:** Agregar comportamientos como validación, seguridad o formateo a un campo de entrada sin modificar el objeto base.
2. **Logging:** Añadir funcionalidades de registro de eventos a funciones o métodos sin alterar su lógica original.
3. **Caché:** Aplicar almacenamiento en caché a una función sin cambiar su código.

## **Relaciones con otros patrones**

- **Strategy:** Ambos buscan extender el comportamiento, pero mientras que el Decorator envuelve objetos, el Strategy cambia el comportamiento al seleccionar una estrategia diferente.
- **Composite:** El Decorator puede usarse con Composite para añadir responsabilidades a los componentes sin modificar sus clases.
