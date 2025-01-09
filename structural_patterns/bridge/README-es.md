# **Bridge**

## **Propósito**

Separar una abstracción de su implementación para que ambas puedan evolucionar de manera independiente.

## **Problema**

Un cambio en la implementación afecta directamente la abstracción y viceversa, lo que resulta en un sistema rígido y difícil de escalar.

## **Solución**

Dividir la abstracción y la implementación en jerarquías separadas y conectar ambas mediante una composición.

## **Pros**

- Desacopla la abstracción de la implementación.
- Facilita la escalabilidad: puedes cambiar la abstracción o la implementación de manera independiente.
- Fomenta el cumplimiento del principio de inversión de dependencia.

## **Contras**

- Incrementa la complejidad del diseño.
- Puede ser innecesario si el sistema no requiere múltiples implementaciones.

## **Casos de Uso Reales**

1. **Interfaces gráficas**: Abstracción de un componente (botón, ventana) con implementaciones específicas para distintos sistemas operativos (Windows, macOS, Linux).
2. **Bases de datos**: Abstracción de consultas SQL con implementaciones para distintos motores (PostgreSQL, MySQL, SQLite).
3. **Renderización**: Abstracción de formas geométricas (círculo, cuadrado) con implementaciones para renderizado 2D o 3D.

## **Relaciones con Otros Patrones**

- **Adapter**: Adapter convierte interfaces incompatibles; Bridge separa abstracción e implementación desde el inicio.
- **Strategy**: Ambos delegan comportamiento, pero Strategy lo hace para cambiar algoritmos dinámicamente, mientras que Bridge lo hace para desacoplar jerarquías.
- **Composite**: Composite organiza objetos en estructuras jerárquicas, mientras Bridge separa jerarquías relacionadas.
