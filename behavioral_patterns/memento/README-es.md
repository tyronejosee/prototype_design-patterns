# **Memento**

Es un patrón de diseño que permite capturar y restaurar el estado interno de un objeto sin exponer su estructura.

## **Propósito**

Facilitar la restauración de un objeto a un estado previo sin revelar detalles internos.

## **Problema**

Necesitas guardar y restaurar el estado de un objeto, pero no quieres que los detalles internos sean accesibles o modificables.

## **Solución**

El patrón usa tres componentes: el **Originator** (que guarda el estado), el **Memento** (que almacena el estado), y el **Caretaker** (que gestiona el memento).

## **Pros**

- Permite deshacer acciones o restaurar estados anteriores.
- Encapsula los detalles internos de un objeto.
- Facilita la implementación de funcionalidades como el "deshacer" en aplicaciones.

## **Contras**

- Puede generar un consumo elevado de memoria si se guardan muchos estados.
- Complica el diseño al requerir múltiples objetos para gestionar los estados.

## **Casos de Usos Reales**

- Funcionalidades de "deshacer" en editores de texto.
- Juegos donde se pueden restaurar el estado del juego a un punto anterior.
- Aplicaciones con flujos complejos que necesitan una opción de retroceso.

## **Relaciones con otros patrones**

- **Command**: El patrón Memento puede usarse junto con Command para implementar operaciones reversibles.
- **Iterator**: Puede trabajar con el patrón Iterator para recorrer y guardar diferentes estados de una colección de objetos.
