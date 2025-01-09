# **Composite**

## **Propósito**

Permitir tratar objetos individuales y compuestos (estructuras jerárquicas) de manera uniforme.

## **Problema**

Trabajar con estructuras jerárquicas (por ejemplo, árbol de elementos) es complejo porque el código debe diferenciar entre nodos simples y compuestos al procesar estos elementos.

## **Solución**

Definir una interfaz común para todos los objetos en la jerarquía. Los objetos compuestos delegan operaciones a sus hijos y permiten tratar objetos simples y compuestos de manera uniforme.

## **Pros**

- Facilita trabajar con estructuras jerárquicas de objetos.
- Se pueden agregar nuevos tipos de elementos sin cambiar el código existente.
- Componentes simples y compuestos reutilizan la misma lógica.

## **Contras:**

- La estructura puede ser más complicada de implementar.
- Puede ser innecesario para estructuras simples y sobrecargar el diseño.

## **Casos de Uso Reales**

1. **Sistemas de Archivos**: Archivos y carpetas tratados de manera uniforme.
2. **Menús de Aplicaciones**: Opciones de menú individuales o submenús anidados.
3. **Gráficos**: Dibujar formas simples (círculos) o compuestas (grupos de formas).
4. **Sistemas de Organización**: Organigramas con empleados y equipos.

## **Relaciones con Otros Patrones**

1. **Composite + Decorator**: Los componentes pueden ser extendidos con responsabilidades adicionales.
2. **Composite + Visitor**: Facilita agregar nuevas operaciones sobre la jerarquía sin cambiarla.
3. **Composite + Iterator**: Recorre jerarquías complejas de objetos.
4. **Composite + Chain of Responsibility**: Permite que objetos compuestos manejen o deleguen solicitudes.
