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

## Implementación en Python

### 1. `SingletonMeta` (Metaclase)

La clase `SingletonMeta` es una **metaclase**, que es una clase para clases. Define el comportamiento para crear instancias de la clase `Singleton`, asegurando que solo se cree una instancia, incluso con múltiples hilos.

- **`_instances = {}`**: Este diccionario almacena las instancias de la clase Singleton. Se usa para asegurar que solo se cree una instancia de la clase.
  
- **`_lock = Lock()`**: Este es un objeto de tipo `Lock`, utilizado para la sincronización de hilos. Cuando varios hilos intentan acceder a un recurso compartido al mismo tiempo, el lock asegura que solo un hilo pueda acceder al recurso a la vez, previniendo condiciones de carrera (race conditions).

- **`__call__(cls, *args, **kwargs)`**: Este método se llama cuando se intenta crear una nueva instancia de la clase Singleton. El método `__call__` es usado por la metaclase para controlar el proceso de instanciación. Aquí está la lógica clave:
  - **`with cls._lock:`**: La declaración `with` adquiere el lock, asegurando que solo un hilo pueda ejecutar el bloque de código a la vez.
  - **`if cls not in cls._instances:`**: Si no existe una instancia de la clase, se crea una nueva usando `super().__call__(*args, **kwargs)`. Esto llama al método `__call__` de la clase padre (es decir, el método `__call__` de la clase que se está instanciando).
  - **`cls._instances[cls] = instance`**: La instancia creada se guarda en el diccionario `_instances`, para que futuras llamadas a `Singleton` reutilicen esta misma instancia.

La combinación del `Lock` y la condición **`if cls not in cls._instances:`** asegura que **solo se cree una instancia** del Singleton, incluso si múltiples hilos intentan crear la instancia simultáneamente.

### 2. Clase `Singleton`

Esta clase usa `SingletonMeta` como su **metaclase**, lo que le otorga el comportamiento definido en `SingletonMeta` (es decir, asegurar una única instancia).

- **`value: str`**: Este es un atributo para almacenar un valor, el cual se usará para demostrar que la instancia Singleton es compartida.
  
- **`__init__(self, value: str)`**: Este constructor inicializa el atributo `value`. El valor solo puede ser establecido la primera vez que se instancia el Singleton.
  
- **`some_business_logic(self)`**: Este es un espacio reservado para cualquier lógica de negocio que la instancia del Singleton pueda necesitar ejecutar. No se utiliza en este ejemplo, pero representa la idea de que las instancias de un Singleton pueden tener lógica asociada.

### 3. Función `test_singleton`

Esta función es llamada en dos hilos diferentes para probar si el patrón Singleton funciona correctamente. Recibe un valor como argumento, crea una instancia del Singleton y luego imprime el valor.

```python
def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)
```

- La función imprime el `value` de la instancia del Singleton, lo que nos permitirá verificar si se está reutilizando la misma instancia en ambos hilos.

### 4. Código principal

El bloque principal crea y lanza dos hilos que llaman a la función `test_singleton` con valores diferentes (`"FOO"` y `"BAR"`). Si el patrón Singleton está funcionando correctamente, ambos hilos deberían imprimir el mismo valor, ya que ambos deberían estar usando la misma instancia del Singleton.

```python
if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
        "If you see different values, "
        "then 2 singletons were created (booo!!)\n\n"
        "RESULT:\n"
    )

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
```

- **Salida esperada:** Si ves el mismo valor en ambas impresiones, significa que el Singleton se reutilizó correctamente. Si ves valores diferentes, significa que se crearon dos instancias de Singleton, lo cual no debería ocurrir.
