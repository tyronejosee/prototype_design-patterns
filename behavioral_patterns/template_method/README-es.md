# **Template Method**

## **Propósito**

Definir la estructura de un algoritmo en un método, dejando algunos pasos para que las subclases los implementen. Permite que las subclases redefinan ciertos pasos sin cambiar la estructura general.

## **Problema**

Cuando se tienen algoritmos similares con pasos comunes, pero algunos detalles deben ser implementados de forma diferente en cada subclase.

## **Solución**

Se crea un método en la clase base que define el algoritmo, llamando a métodos que pueden ser sobrescritos por las subclases para implementar los detalles específicos.

## **Pros**

- Promueve la reutilización de código.
- Mantiene la consistencia en la estructura de los algoritmos.
- Permite que las subclases personalicen los pasos sin cambiar el flujo general.

## **Contras**

- Puede llevar a un diseño rígido si las subclases necesitan cambiar demasiado el algoritmo base.
- Difícil de mantener si el algoritmo base cambia con frecuencia.

## **Casos de Uso Reales**

- Procesos de pago en línea con pasos comunes (validación, pago, confirmación), donde algunos pasos varían según el método de pago.
- Procesamiento de archivos o datos con un flujo común de operaciones, pero con detalles específicos según el tipo de archivo o formato.
- Automatización de pruebas con pasos comunes, pero con diferencias en la configuración o ejecución de las pruebas.

## **Relaciones con Otros Patrones**

- **Strategy:** Ambos permiten modificar comportamientos, pero en **Template Method**, el flujo está predeterminado y solo se permiten variaciones en pasos específicos, mientras que en **Strategy**, el comportamiento completo es intercambiable.
- **Factory Method:** Ambos pueden usarse para crear productos (objetos), pero **Factory Method** se centra en la creación de objetos, mientras que **Template Method** define un algoritmo con pasos a implementar.
