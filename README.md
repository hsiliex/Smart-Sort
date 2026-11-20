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

* Estructura Modular: Organización limpia del código separada en archivos de configuración de pines (`firmware/config.py`), gestión de sensores (`firmware/sensores.py`), control de actuadores (`firmware/actuadores.py`) y lógica principal (`firmware/main.py`).
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
| LED verde / LED rojo | GPIO 22 / 23 |

El motor se alimenta con una fuente externa a través del L298N, nunca directamente desde el ESP32.

## Estructura del Repositorio

El repositorio se encuentra organizado de manera modular para diferenciar el firmware local de la interfaz gráfica de supervisión:

```
Smart-Sort/
├── firmware/                  # Código fuente en MicroPython (ESP32)
│   ├── main.py                # Lógica principal y flujo del sistema
│   ├── config.py              # Pines y ángulos del servo
│   ├── sensores.py            # Clase GestorSensores (IR, botón, TCS230)
│   └── actuadores.py          # Clases Motor, Servo y Led
│
├── interfaz/                  # Aplicación de supervisión y control 
│   ├── paleta_colores.py      # Asignación de colores de la interfaz
│   ├── navegacion.py          # Barra superior y menú lateral de navegación           
│   ├── graficas.py            # Construcción de grafica de conteo por color          
│   ├── tablas.py              # Tabla de registros frecuentes y control de filas               
│   ├── vistas.py              # Vistas secundarias (Control y Motor, Eventos y Alertas)
│   ├── main.py                # Punto de entrada, dashboard principal y estado de la app
├── .gitignore
└── README.md                  # Documentación general del proyecto

## Interfaz Gráfica (GUI)

La interfaz de usuario de **Smart-Sort** está desarrollada en **Python** utilizando el framework **Flet**, bajo una arquitectura modular que separa la lógica principal de los componentes visuales. En esta entrega, la aplicación opera con **datos simulados localmente** para validar el flujo de monitoreo y control antes de la integración física mediante MQTT.

### Vistas principales
* **Dashboard Principal:** Muestra el estado actual del sistema (*En marcha* / *Detenido*), contadores acumulados por categoría de color (Rojo, Verde, Azul y Total), un botón alternable de marcha, simulación manual de detección de objetos, una gráfica comparativa en tiempo real y una tabla con los últimos registros procesados.
* **Control y Motor:** Permite ajustar parámetros operativos simulados como la velocidad de la banda transportadora, el modo de clasificación por color y el reinicio de contadores e historial.
* **Eventos y Alertas:** Registra cronológicamente las acciones ejecutadas en el sistema, cambios de estado y advertencias operativas.

### Estructura de módulos de la interfaz
```text
├── assets/                # Recursos gráficos e ícono de la aplicación
├── paleta_colores.py      # Constantes y paleta de colores de la interfaz
├── navegacion.py          # Barra superior y menú lateral de navegación
├── graficas.py            # Construcción de gráficas de conteo por color
├── tablas.py              # Tabla de registros recientes y control de filas
├── vistas.py              # Vistas secundarias (Control y Motor, Eventos y Alertas)
└── main.py                # Punto de entrada, dashboard principal y estado de la app

## Lógica de Funcionamiento

1. El sistema inicia detenido (LED rojo encendido).
2. Al pulsar el botón, la banda arranca y se enciende el LED verde.
3. Cuando el IR detecta un objeto, la banda se detiene.
4. Se lee el color con los tres filtros del TCS230.
5. El servo se mueve a la posición del color detectado. Si no se reconoce, se enciende
