# **Singleton**

## **Propósito**

- Asegura que una clase tenga **una sola instancia** a lo largo de todo el programa y proporciona un **punto de acceso global** a esa instancia.

## **Problema que resuelve**

- Garantiza que una clase tenga solo una instancia, útil para gestionar recursos compartidos como bases de datos o archivos.
- Evita que se creen instancias adicionales de una clase, proporcionando un **acceso global** a la misma.

## **Solución**

- **Privar el constructor** de la clase para evitar que otros objetos creen nuevas instancias.
- Crear un **método estático** que controle la creación de la instancia, garantizando que siempre se devuelva la misma instancia.

## **Analogía**

- Un **gobierno** es un ejemplo, ya que hay un único gobierno para un país y su acceso es global.

## **Aplicabilidad**

- Se usa cuando solo **se debe tener una instancia** de una clase, como una **base de datos compartida**.
- Permite un **control más estricto de variables globales**, pero garantiza que solo haya una instancia de la clase.

## **Pros**

- Garantiza que una clase tenga solo una instancia.
- Proporciona un punto de acceso global.
- La instancia se **inicializa solo cuando es necesaria**.

## **Contras**

- **Vulnera el Principio de Responsabilidad Única** (resuelve dos problemas a la vez).
- Puede enmascarar **un mal diseño** si se usa incorrectamente.
- **Dificulta las pruebas unitarias**, especialmente en entornos de múltiples hilos.

## **Relaciones con otros patrones**

- **Fachada** puede transformarse en un Singleton.
- **Flyweight** puede compartir instancias, pero un Singleton solo tiene **una instancia**.
- **Abstract Factory, Builder, Prototype** pueden implementarse como Singletons.
