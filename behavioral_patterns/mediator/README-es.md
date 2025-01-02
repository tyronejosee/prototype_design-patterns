# **Mediator Pattern**

## **Propósito**

Centraliza la comunicación entre objetos para reducir dependencias directas entre ellos. Facilita la interacción y mantenimiento de objetos en un sistema.

## **Problema**

Cuando muchos objetos necesitan comunicarse entre sí, las relaciones pueden volverse complejas, lo que dificulta el mantenimiento y escalabilidad del sistema.

## **Solución**

El patrón Mediator introduce un objeto intermedio (mediador) que gestiona las interacciones entre los objetos. Los objetos no se comunican directamente, sino a través del mediador.

## **Pros**

- Desacopla los objetos, mejorando la flexibilidad y escalabilidad.
- Facilita el mantenimiento al reducir la complejidad en las relaciones directas.
- Centraliza la lógica de comunicación.

## **Contras**

- El mediador puede volverse un punto de congestión si maneja demasiadas interacciones.
- Añade una capa adicional que puede aumentar la complejidad en sistemas pequeños.

## **Casos de Uso Reales**

- **Chatrooms:** Un mediador gestiona la comunicación entre diferentes usuarios sin que los usuarios se comuniquen directamente.
- **Sistemas de control de tráfico aéreo:** Un mediador coordina la comunicación entre distintos aviones y controladores.
- **Aplicaciones de UI complejas:** Donde varios componentes deben interactuar, pero no deben depender directamente entre sí.

## **Relaciones con otros patrones**

- **Observer:** Mediator y Observer pueden trabajar juntos, con el Mediator gestionando eventos y el Observer notificado de los cambios.
- **Command:** Mediator puede invocar comandos que encapsulan solicitudes, centralizando la lógica de ejecución.
