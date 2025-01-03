# **Visitor**

## **Propósito**

Permite agregar nuevas operaciones a una estructura de objetos sin modificar sus clases.

## **Problema**

Añadir funcionalidades a clases complejas de una jerarquía sin romper el Principio Abierto/Cerrado.

## **Solución**

Crear una clase _visitor_ separada que implemente las operaciones, delegando la ejecución a métodos específicos para cada tipo de objeto de la jerarquía.

## **Pros:**

- Cumple el Principio Abierto/Cerrado.
- Centraliza las operaciones en un único lugar.
- Facilita agregar nuevas operaciones.

## **Contras:**

- Dificulta la adición de nuevos tipos de elementos en la jerarquía.
- Aumenta el acoplamiento entre el visitor y las clases visitadas.

## **Casos de Uso Reales**

- **Compiladores:** Recorrer árboles sintácticos para analizar o generar código.
- **Herramientas de reporte:** Extraer datos de estructuras complejas como XML/JSON.
- **Sistemas gráficos:** Operaciones como renderizado o cálculo de bounding boxes.

## **Relaciones con Otros Patrones**

- **Composite:** Visitor opera frecuentemente sobre estructuras jerárquicas manejadas por Composite.
- **Iterator:** Ayuda a recorrer estructuras en las que se aplicará el Visitor.
- **Strategy:** Puede compararse con Visitor cuando se desea cambiar dinámicamente una operación.
