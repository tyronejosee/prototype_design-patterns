# **Factory Method**

- **Propósito**: Proporcionar una interfaz para crear objetos sin especificar la clase exacta del objeto que se va a crear.

- **Problema**: Necesidad de crear instancias de clases sin acoplarse directamente a las clases concretas, lo que facilita la extensión del código y mejora la flexibilidad.

- **Solución**: Definir un método para crear objetos, dejando que las subclases decidan qué clase instanciar. Esto desacopla la creación del objeto de su uso.

## **Pros**

- **Desacoplamiento**: Separa la creación de objetos de su uso.
- **Flexibilidad**: Permite cambiar el tipo de objeto sin modificar el código cliente.
- **Extensibilidad**: Facilita la adición de nuevas clases de productos sin modificar el código existente.

## **Contras**

- **Complejidad adicional**: Introduce más clases y métodos, lo que puede hacer el sistema más complejo.
- **Exceso de abstracción**: Puede ser innecesario si la creación de objetos es sencilla o no cambia.

## **Casos de Uso Reales**

- **Interfaces gráficas**: Cuando se necesita crear diferentes tipos de botones, cuadros de texto, etc., dependiendo del sistema operativo o de la plataforma.
- **Frameworks de bases de datos**: Cuando se necesita crear diferentes tipos de conexiones a bases de datos (MySQL, PostgreSQL) sin modificar el código del cliente.

## **Relaciones con otros patrones**

- **Abstract Factory**: Factory Method es un caso específico de Abstract Factory, donde se utiliza un solo método para la creación de productos.
- **Builder**: Ambos ayudan a la creación de objetos, pero Builder se enfoca en la construcción paso a paso, mientras que Factory Method se centra en la creación simple.
- **Singleton**: Puede usarse en conjunto si se necesita garantizar que solo se cree una instancia del objeto a través del Factory Method.
