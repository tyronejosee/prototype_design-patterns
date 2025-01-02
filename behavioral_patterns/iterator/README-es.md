# **Iterator**

## **Propósito**

Proporciona una forma de acceder secuencialmente a los elementos de una colección sin exponer su representación interna.

## **Problema**

Cuando tienes una colección compleja (listas, árboles, gráficos) y necesitas recorrer sus elementos de manera uniforme sin revelar su estructura interna o acoplar la lógica de iteración a la colección.

## **Solución**

1. Define una interfaz para iteradores con métodos como `next()` y `has_next()`.
2. Implementa iteradores concretos para manejar las formas de recorrer la colección.
3. La colección proporciona iteradores compatibles sin exponer su estructura.

## **Pros**

- **Desacopla** la lógica de iteración de la colección.
- Permite múltiples formas de iteración (directa, inversa, aleatoria).
- Facilita **agregar nuevos algoritmos de recorrido** sin modificar la colección.
- **Simplifica** el trabajo con colecciones complejas.

## **Contras**

- Puede aumentar la **complejidad** del código si la lógica de iteración es simple.
- **Sobrecarga** cuando no se necesita un diseño extensible.

## **Casos de Uso Reales**

- **Exploradores de archivos**: Recorrer carpetas y archivos en orden jerárquico.
- **Aplicaciones de streaming**: Navegar listas de reproducción o episodios en diferentes órdenes.
- **Sistemas de juegos**: Iterar sobre nodos en gráficos o estructuras jerárquicas.
- **Bases de datos**: Recorrer registros de consultas de manera uniforme.

## **Relaciones con Otros Patrones**

- **Composite**: El iterador puede recorrer estructuras compuestas (árboles).
- **Factory Method**: Crea iteradores concretos personalizados para diferentes colecciones.
- **Memento**: Puede usar el iterador para guardar y restaurar el estado de una colección.
- **Observer**: Puede recorrer colecciones para notificar observadores.
