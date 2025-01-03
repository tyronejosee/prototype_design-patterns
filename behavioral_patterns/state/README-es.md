# **State**

## **Propósito**

Permite que un objeto cambie su comportamiento cuando su estado interno cambia, haciendo que parezca que el objeto cambia de clase.

## **Problema**

Cuando un objeto tiene muchos estados posibles, el código puede volverse difícil de manejar, con condicionales y cambios de estado dispersos.

## **Solución**

Usar el patrón State para delegar la lógica relacionada con cada estado a objetos separados, que representan los distintos estados posibles.

## **Pros**

- Mejora la legibilidad y organización del código.
- Evita el uso excesivo de condicionales.
- Facilita la adición de nuevos estados sin modificar el objeto principal.

## **Contras**

- Puede generar una gran cantidad de clases para cada estado.
- Si el número de estados es pequeño, usar este patrón puede ser innecesario.

## **Casos de Usos Reales**

- Control de flujo en máquinas de estados (ej. pagos, estados de un pedido).
- Aplicaciones que tienen diferentes modos de funcionamiento (ej. un editor de texto con modos de edición y vista previa).
- Juegos donde los personajes o el entorno tienen diferentes comportamientos según el estado.

## **Relaciones con Otros Patrones**

- **Strategy:** Ambos permiten cambiar el comportamiento de un objeto según el estado, pero en **Strategy** el comportamiento se define fuera del objeto, mientras que en **State** es el propio objeto el que cambia su comportamiento.
- **State** y **Command** pueden ser utilizados juntos para manejar el comportamiento en función del estado y las acciones que deben ejecutarse.
