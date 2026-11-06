from machine import Pin
import time
from config import Pin_IR, Pin_S0, Pin_S1, Pin_S2, Pin_S3, Pin_OUT, Pin_boton

class GestorSensores:
    def __init__(self):
        self.boton_inicio = Pin(Pin_boton, Pin.IN, Pin.PULL_UP)
        # Sensor IR
        self.sensor_ir = Pin(Pin_IR, Pin.IN)

        # Sensor de color
        self.sensor_s0 = Pin(Pin_S0, Pin.OUT)
        self.sensor_s1 = Pin(Pin_S1, Pin.OUT)
        self.sensor_s2 = Pin(Pin_S2, Pin.OUT)
        self.sensor_s3 = Pin(Pin_S3, Pin.OUT)
        self.sensor_out = Pin(Pin_OUT, Pin.IN)

        self.sensor_s0.value(1)
        self.sensor_s1.value(0)

    def esta_presionado(self):
        return self.boton_inicio.value() == 0

    def hay_objeto(self):
        return self.sensor_ir.value() == 0

    def leer_color_tcs230(self):
        self.sensor_s2.value(0)
        self.sensor_s3.value(0)
        time.sleep_ms(20)
        rojo = self._medir_frecuencia()

        self.sensor_s2.value(1)
        self.sensor_s3.value(1)
        time.sleep_ms(20)
        verde = self._medir_frecuencia()

        self.sensor_s2.value(0)
        self.sensor_s3.value(1)
        time.sleep_ms(20)
        azul = self._medir_frecuencia()

        return {"R": rojo, "G": verde, "B": azul}

    def _contar_pulso(self, pin):
        self.contador += 1

    def _medir_frecuencia(self):
        self.contador = 0

        self.sensor_out.irq( trigger=Pin.IRQ_RISING, handler=self._contar_pulso)

        time.sleep_ms(200)

        self.sensor_out.irq(handler=None)

        return self.contador

    def leer_color(self):
        v = self.leer_color_tcs230()

        r = v["R"]
        g = v["G"]
        b = v["B"]

        # Identificar rojo
        if r > g * 1.2 and r > b * 1.2:
            return "rojo"

        # Identificar azul
        if b > g * 1.3 and b > r * 1.3:
            return "azul"

        # Identificar verde
        if g > r * 1.2 and b <= g * 1.15:
            return "verde"

        return "no_reconocido"



