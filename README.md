# Smart-Sort

Sistema automatizado de clasificación y monitoreo de objetos mediante ESP32 y MicroPython.

**Universidad Tecnológica de Pereira** · Ingeniería Electrónica · Programación II
**Integrantes:** Sofía Tatiana Rubio Cuéllar, Ana Sofía Escobar Ibarra
**Docente:** Juan Pablo Tabares Cardona

## Descripción del Proyecto

Smart-Sort es una miniestación automatizada diseñada como prototipo académico para la asignatura de Programación II. El sistema se encarga de desplazar objetos a través de una banda transportadora, detectar su presencia mediante un sensor infrarrojo, identificar su color (rojo, verde o azul) utilizando un sensor TCS230 y direccionarlos al compartimiento correspondiente.

Este repositorio corresponde al **Parcial 2**: firmware local en MicroPython sobre ESP32. La interfaz gráfica en Python y la comunicación MQTT se desarrollarán en etapas posteriores.

**Entorno de desarrollo:** PyCharm con el plugin MicroPython, sobre una ESP32 física.

> **Nota:** la propuesta inicial contemplaba el sensor TCS34725. Durante el desarrollo se cambió al TCS230, que entrega el color como una frecuencia en lugar de usar I2C.

## Componentes Utilizados

* Microcontrolador ESP32: Núcleo de procesamiento y control general del sistema.
* Sensor de Color TCS230: Módulo encargado de medir las frecuencias de luz reflejada para determinar el color del objeto.
* Sensor Infrarrojo (IR): Detector de presencia ubicado en la zona de clasificación.
* Motor DC y Driver L298N: Sistema de tracción y control de velocidad para la banda transportadora.
* Servomotor: Mecanismo posicionador para dirigir los objetos clasificados a sus respectivos compartimientos.
* LEDs verde y rojo: Indican funcionamiento, parada o alerta.
* Pulsador: Inicia y detiene el sistema de forma local.

## Funcionalidades Implementadas (Firmware Local)

* Estructura Modular: Organización limpia del código separada en archivos de configuración de pines (`config.py`), gestión de sensores (`sensores.py`), control de actuadores (`actuadores.py`) y lógica principal (`main.py`).
* Control de Banda: Encendido, regulación de velocidad mediante PWM y parada segura del motor DC a través del driver L298N.
* Adquisición de Datos: Lectura digital de presencia por infrarrojo y medición de frecuencias RGB con el sensor TCS230.
* Clasificación Local: Algoritmo secuencial para identificar categorías de color y actualizar contadores en tiempo real.
* Inicio y parada local: El pulsador alterna entre sistema en marcha y detenido.
* Control del servo por ángulos: Una posición por color y una posición de reposo.
* Indicadores y alertas: LED verde en funcionamiento; LED rojo en parada o color no reconocido.

## Conexiones (pines)

| Elemento | Pin ESP32 |
|---|---|
| Pulsador | GPIO 15 |
| Sensor IR | GPIO 4 |
| TCS230 S0 / S1 | GPIO 16 / 17 |
| TCS230 S2 / S3 | GPIO 5 / 18 |
| TCS230 OUT | GPIO 19 |
| L298N IN1 / IN2 / ENA | GPIO 25 / 26 / 14 |
| Servo | GPIO 13 |
| LED verde / LED rojo | GPIO 21 / 22 |

El motor se alimenta con una fuente externa a través del L298N, nunca directamente desde el ESP32.

## Estructura del Repositorio

```
smart-sort/
├── main.py         # Lógica principal y flujo del sistema
├── config.py       # Pines y ángulos del servo
├── sensores.py     # Clase GestorSensores (IR, botón, TCS230)
├── actuadores.py   # Clases Motor, Servo y Led
├── imagenes/       # Fotos del montaje y capturas de consola
├── .gitignore
└── README.md
```

## Lógica de Funcionamiento

1. El sistema inicia detenido (LED rojo encendido).
2. Al pulsar el botón, la banda arranca y se enciende el LED verde.
3. Cuando el IR detecta un objeto, la banda se detiene.
4. Se lee el color con los tres filtros del TCS230.
5. El servo se mueve a la posición del color detectado. Si no se reconoce, se enciende
