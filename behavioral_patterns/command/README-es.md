# **Command**

## **Propósito**

Encapsula una solicitud como un objeto, permitiendo parametrizar objetos con operaciones, retrasar la ejecución de comandos, o registrar su historial.

## **Problema**

Cuando necesitas ejecutar operaciones en diferentes momentos, revertirlas o permitir que diferentes solicitantes (clientes) invoquen comandos de manera independiente del objeto que realiza la acción (receptor).

## **Solución**

1. Crear una interfaz común `Command` con un método `execute()`.
2. Implementar clases concretas de comando que encapsulen las solicitudes y las envíen al receptor.
3. Usar un invocador que maneje los comandos y controle su ejecución.

## **Pros**

- **Desacopla** el cliente del receptor.
- Soporte para **deshacer/rehacer** acciones.
- Permite implementar **colas** de comandos y **macro-comandos**.
- Facilita la **extensibilidad** al agregar nuevos comandos.

## **Contras**

- Incrementa la **complejidad** del código debido a la creación de múltiples clases.
- Puede llevar a una **sobreingeniería** en casos simples.

## **Casos de Uso Reales**

- Sistemas de **edición de texto** con soporte para deshacer/rehacer.
- **Colas de trabajos** en sistemas distribuidos.
- Control de dispositivos en **domótica** (encender/apagar luces, cerrar puertas, etc.).
- **Menús** en interfaces gráficas que realizan diferentes acciones al ser clicados.

## **Relaciones con Otros Patrones**

- **Chain of Responsibility**: Puede usarse para delegar comandos a diferentes manejadores.
- **Memento**: Puede almacenar el estado antes/después de ejecutar un comando para soportar deshacer/rehacer.
- **Prototype**: Útil para clonar comandos si necesitan ser reusados.
- **Strategy**: Similar en encapsular lógica, pero Command es más enfocado en solicitudes y ejecución.
