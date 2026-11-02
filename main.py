from sensores import GestorSensores
from actuadores import Motor, Servo, IndicadoresLed
import time


def main():
    print("Sistema Smart-Sort en espera...")

    sensor = GestorSensores()
    motor = Motor()
    servo = Servo()
    indicadores = IndicadoresLed()

    motor.detener()
    servo.posicion_rojo()
    indicadores.sistema_detenido()

    print("Presiona el botón de inicio para arrancar el sistema...")

    while not sensor.esta_presionado():
        time.sleep_ms(100)

    print("¡Botón presionado! Iniciando Smart-Sort...")
    time.sleep(1)

    motor.avanzar()
    indicadores.funcionamiento_normal()
    print("Banda transportadora en marcha. Esperando objetos...")

    try:
        while True:

            if sensor.hay_objeto():
                print("¡Objeto detectado! Deteniendo banda para lectura...")
                motor.detener()
                indicadores.sistema_detenido()
                time.sleep(0.5)
                color_detectado = sensor.leer_color()
                print(f"Color identificado: {color_detectado}")


                if color_detectado == "rojo":
                    servo.posicion_rojo()
                    time.sleep(1.5)
                elif color_detectado == "verde":
                    servo.posicion_verde()
                    time.sleep(1.5)
                elif color_detectado == "azul":
                    servo.posicion_azul()
                    time.sleep(1.5)
                else:
                    print("Color no reconocido. Siguiendo de largo...")

                motor.avanzar()
                indicadores.funcionamiento_normal()
                print("Reanudando banda...")

                time.sleep(1)  # Antirrebote

            time.sleep_ms(100)

    except KeyboardInterrupt:
        print("\nSistema detenido por el usuario.")
        motor.detener()
        indicadores.sistema_detenido()


if __name__ == "__main__":
    main()