from machine import Pin
import time
from config import Pin_IR, Pin_S0, Pin_S1, Pin_S2, Pin_S3, Pin_OUT

class GestorSensores:
    def __init__(self):
        # Sensor IR
        self.sensor_ir = Pin(Pin_IR, Pin.IN)

        # Sensor de color
        self.sensor_s0 = Pin(Pin_S0, Pin.IN)
        self.sensor_s1 = Pin(Pin_S1, Pin.OUT)
        self.sensor_s2 = Pin(Pin_S2, Pin.OUT)
        self.sensor_s3 = Pin(Pin_S3, Pin.OUT)
        self.sensor_out = Pin(Pin_OUT, Pin.IN)

        self.sensor_s0.value(0)
        self.sensor_s1.value (1)

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
    def _medir_frecuencia(self):
        contador=0
        tiempo_inicio = time.ticks_ms()
        ultimo_estado = self.sensor_out.value()

        while time.ticks_diff(time.ticks_ms(), tiempo_inicio)<50:
            estado_actual = self.sensor_out.value ()
            if estado_actual != ultimo_estado and estado_actual == 1:
                contador += 1
            ultimo_estado = estado_actual
        return contador

    def leer_color (self):
        v = self.leer_color_tcs230()
        r,g,b= v["R"], v["G"], v["B"]
        m = max (r, g, b)
        if m < 5:
            return "no_reconocido"
        if r == m and r > g * 1.2 and r > b *1.2:
            return "rojo"
        if g == m and g > r *1.2 and g > b *1.2:
            return "verde"
        if b == m and b > r * 1.2 and b>g * 1.2:
            return "azul"
        return "no_reconocido"


