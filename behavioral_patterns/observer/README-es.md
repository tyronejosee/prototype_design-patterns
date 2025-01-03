# **Observer Pattern**

## **Propósito**

Permitir que un objeto (subject) notifique a otros objetos (observers) sobre cambios de estado sin acoplarlos directamente.

## **Problema**

Cuando un objeto cambia su estado y otros objetos dependen de él, el acoplamiento directo puede ser difícil de manejar.

## **Solución**

Usar un mecanismo de suscripción y notificación en el que los observadores se suscriben a un sujeto para recibir actualizaciones.

## **Pros**

- Desacopla el sujeto de los observadores.
- Facilita la adición de nuevos observadores sin modificar el sujeto.
- Ideal para sistemas con múltiples reacciones a cambios de estado.

## **Contras**

- Puede haber un impacto en el rendimiento si hay muchos observadores.
- El orden de las notificaciones puede ser difícil de controlar.

## **Casos de Usos Reales**

- Actualización de interfaces de usuario cuando cambian los datos en una aplicación.
- Sistemas de eventos en juegos o interfaces gráficas.
- Implementación de notificaciones en aplicaciones móviles.

## **Relaciones con Otros Patrones:**

- **Mediator:** Ambos desacoplan componentes, pero el Mediator organiza la comunicación centralizada, mientras que el Observer distribuye las actualizaciones de manera descentralizada.
- **Strategy:** Ambos permiten cambiar comportamientos sin modificar el objeto que los usa, pero en el Observer, los objetos observadores reaccionan a cambios del sujeto.
