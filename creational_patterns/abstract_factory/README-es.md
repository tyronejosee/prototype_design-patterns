# **Abstract Factory Pattern**

- **Propósito**: Define una interfaz para crear familias de objetos relacionados sin especificar sus clases concretas.

- **Problema**: Cuando el sistema necesita crear diferentes tipos de objetos, pero no se quiere acoplar a clases concretas de esos objetos, especialmente cuando el conjunto de objetos varía según el contexto.

- **Solución**: Usar una **fábrica abstracta** que proporcione un conjunto de métodos para crear los objetos relacionados. Cada implementación concreta de la fábrica crea una familia de objetos específicos.

## **Pros**

- Permite intercambiar familias de productos fácilmente.
- Facilita la creación de sistemas independientes de las clases de productos.
- Aísla la lógica de creación de objetos del resto del código.

## **Contras**

- Aumenta la complejidad al añadir más clases.
- Puede ser innecesario si solo hay un tipo de producto.
- No es adecuado cuando hay una gran variedad de productos que no están relacionados entre sí.

## **Casos de Uso Reales**

- **Interfaces de usuario**: Crear diferentes interfaces (como una interfaz para Windows y otra para macOS) que tengan componentes gráficos (botones, ventanas, etc.) de diferentes estilos.
- **Juegos**: Crear diferentes mundos o niveles con enemigos, armas y objetos específicos para cada escenario.
- **Sistemas de bases de datos**: Proveer diferentes implementaciones de bases de datos con una interfaz común.

## **Relaciones con Otros Patrones**

- **Builder**: Ambos patrones se usan para crear objetos complejos, pero **Abstract Factory** se enfoca en familias de productos, mientras que **Builder** se usa para construir un solo objeto paso a paso.
- **Factory Method**: **Abstract Factory** es una extensión del **Factory Method**, donde se permiten crear varias familias de objetos, no solo un tipo.
