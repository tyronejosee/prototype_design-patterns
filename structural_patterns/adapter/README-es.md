# **Adapter**

## **Propósito**

Permite que clases con interfaces incompatibles trabajen juntas al convertir la interfaz de una clase a otra esperada por el cliente.

## **Problema**

Un cliente necesita usar una clase con una interfaz diferente o incompatible.

## **Solución**

Crear un objeto adaptador que actúe como un puente, traduciendo las llamadas de la interfaz esperada por el cliente a la interfaz de la clase adaptada.

## **Pros**

- Facilita la reutilización de clases existentes con interfaces incompatibles.
- Aumenta la flexibilidad al desacoplar el cliente de la implementación concreta.

## **Contras**

- Incrementa la complejidad del código.
- Puede generar un diseño excesivamente dependiente de adaptadores.

## **Casos de Uso Reales**

1. **Integración de sistemas legados**: Usar APIs antiguas con nuevos clientes.
2. **Frameworks**: Usar bibliotecas externas con estructuras internas diferentes.
3. **Hardware y software**: Traducir protocolos entre dispositivos o sistemas operativos.
4. **Servicios en la nube**: Convertir interfaces de diferentes servicios.

## **Relaciones con Otros Patrones**

- **Bridge**: Ambos desacoplan interfaces, pero Bridge separa abstracciones de implementaciones, mientras Adapter solo traduce interfaces.
- **Decorator**: Ambos pueden alterar comportamientos, pero el propósito de Adapter es compatibilidad, no extensión de funcionalidad.
- **Facade**: Simplifica interfaces, pero no las adapta.
