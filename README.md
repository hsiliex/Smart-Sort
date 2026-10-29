# Smart-Sort

Sistema automatizado de clasificación y monitoreo de objetos mediante ESP32 y MicroPython.

## Descripción del Proyecto
**Smart-Sort** es una miniestación automatizada diseñada como prototipo académico para la asignatura de Programación II[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span). El sistema se encarga de desplazar objetos a través de una banda transportadora, detectar su presencia mediante un sensor infrarrojo, identificar su color (rojo, verde o azul) utilizando un sensor TCS230 y direccionarlos al compartimiento correspondiente[span_3](start_span)[span_3](end_span)[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).

## Componentes Utilizados
* **Microcontrolador ESP32:** Núcleo de procesamiento y control general del sistema.
* **Sensor de Color TCS230:** Módulo encargado de medir las frecuencias de luz reflejada para determinar el color del objeto.
* **Sensor Infrarrojo (IR):** Detector de presencia ubicado en la zona de clasificación.
* **Motor DC y Driver L298N:** Sistema de tracción y control de velocidad para la banda transportadora.
* **Servomotor:** Mecanismo posicionador para dirigir los objetos clasificados a sus respectivos compartimientos.

## Funcionalidades Implementadas (Firmware Local)
* **Estructura Modular:** Organización limpia del código separada en archivos de configuración de pines (`config.py`), gestión de sensores (`sensores.py`), control de actuadores (`actuadores.py`) y lógica principal (`main.py`).
* **Control de Banda:** Encendido, regulación de velocidad mediante PWM y parada segura del motor DC a través del driver L298N.
* **Adquisición de Datos:** Lectura digital de presencia por infrarrojo y medición de frecuencias RGB con el sensor TCS230.
* **Clasificación Local:** Algoritmo secuencial para identificar categorías de color y actualizar contadores en tiempo real.