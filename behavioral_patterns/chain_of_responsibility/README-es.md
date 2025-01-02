# **Chain of Responsibility**

**Propósito**:
Permite pasar una solicitud a través de una cadena de objetos receptores, donde cada objeto tiene la oportunidad de manejar la solicitud, sin que el emisor sepa quién la procesará.

**Problema**:
Cuando tienes múltiples objetos que pueden manejar una solicitud, pero no quieres que el emisor sepa qué objeto específico la manejará.

**Solución**:
Se establece una cadena de objetos que tienen la capacidad de manejar solicitudes. Cada objeto en la cadena decide si maneja la solicitud o la pasa al siguiente en la cadena.

## **Pros**

- Desacopla el emisor de la lógica que maneja la solicitud.
- Facilita la adición de nuevas funcionalidades sin modificar el código existente.
- Simplifica la gestión de solicitudes al dividir el proceso en pequeños manejadores.

## **Contras**

- Puede hacer que el flujo de control sea más difícil de seguir.
- Si la cadena es larga, puede haber un impacto en el rendimiento.
- Los errores pueden ser difíciles de rastrear si no se gestionan adecuadamente.

## **Casos de uso reales**

- **Procesamiento de pedidos** en e-commerce, donde diferentes pasos como verificación de stock, pago, y envío son manejados por distintos objetos.
- **Soporte técnico** donde diferentes agentes manejan problemas según el tipo de solicitud (facturación, configuración, etc.).
- **Filtrado de solicitudes** en sistemas de seguridad, donde distintos niveles de validación son realizados por diferentes módulos.

## **Relaciones con otros patrones**

- **Strategy**: Ambos patrones delegan tareas a objetos distintos, pero **Chain of Responsibility** maneja un flujo secuencial, mientras que **Strategy** permite una selección explícita de una estrategia.
- **Command**: Aunque ambos pueden invocar un comportamiento en diferentes objetos, **Command** encapsula una solicitud en un objeto, mientras que **Chain of Responsibility** permite una serie de objetos que pueden procesar la solicitud.
