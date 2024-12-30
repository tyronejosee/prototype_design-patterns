# **Builder Pattern**

- **Propósito**: Separar la construcción de un objeto complejo de su representación, permitiendo crear diferentes representaciones de un mismo tipo de objeto.

- **Problema**: La creación de objetos con múltiples parámetros opcionales o configuraciones complejas puede ser difícil de manejar en un solo constructor.

- **Solución**: Utilizar un objeto "builder" para construir el objeto paso a paso, separando la lógica de construcción de la lógica de negocio.

## **Pros**

- Facilita la creación de objetos complejos con múltiples configuraciones.
- Mejora la legibilidad y mantenibilidad del código.
- Permite la creación de distintos tipos de objetos de una misma clase base.

## **Contras**

- Puede ser excesivo para objetos simples con pocos atributos.
- Aumenta la cantidad de clases a gestionar.
- Puede resultar innecesario si no se tienen muchos parámetros opcionales.

## **Casos de Uso Reales**

- **Desarrollo de interfaces de usuario**: Construcción de ventanas o formularios con múltiples opciones de configuración.
- **Generación de documentos o informes**: Crear documentos complejos con diferentes secciones o configuraciones.

## **Relaciones con otros patrones**

- **Abstract Factory**: El Builder puede ser utilizado en combinación con Abstract Factory para crear objetos complejos de manera flexible.
- **Factory Method**: Ambos patrones facilitan la creación de objetos, pero Builder es más adecuado para objetos con muchas configuraciones.
