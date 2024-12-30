# **Prototype**

- **Propósito**: Permitir la creación de nuevos objetos clonando una instancia existente (prototipo) en lugar de crear objetos desde cero.

- **Problema**: La creación de objetos complejos puede ser costosa o complicada, especialmente cuando se necesitan muchas instancias similares.

- **Solución**: Utilizar un prototipo (objeto base) que puede ser copiado o modificado según sea necesario, evitando la creación repetitiva.

## **Pros**

- Mejora el rendimiento al evitar la creación de nuevos objetos desde cero.
- Facilita la creación de objetos con configuraciones similares.
- Útil en escenarios donde se necesitan objetos configurados de manera similar pero con ligeras variaciones.

## **Contras**

- Puede ser difícil de implementar si los objetos son complejos o si tienen muchas dependencias internas.
- A veces, el clonaje no es posible si los objetos contienen referencias a recursos que no pueden copiarse (por ejemplo, conexiones de base de datos).

## **Casos de Uso Reales**

- **Software de diseño gráfico**: Clonar objetos como formas y estilos (p. ej., Adobe Illustrator).
- **Juegos**: Crear personajes o enemigos con características similares pero con ligeras variaciones.

## **Relaciones con otros patrones**

- **Factory Method**: Ambos crean objetos, pero el Prototype clona una instancia existente en lugar de crear una nueva desde cero.
- **Abstract Factory**: El Prototype puede ser usado en combinación con Abstract Factory para crear familias de objetos con clonación.
