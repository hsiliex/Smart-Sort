from machine import Pin, PWM
from config import Pin_IN1, Pin_IN2, Pin_ENA, Pin_servo, led_rojo, led_verde

class IndicadoresLed():
    def __init__ (self):
        self.led_verde = Pin(led_verde, Pin.OUT)
        self.led_rojo = Pin(led_rojo, Pin.OUT)

    def funcionamiento_normal(self):
        self.led_verde.value(1)
        self.led_rojo.value(0)

    def sistema_detenido(self):
        self.led_rojo.value(1)
        self.led_verde.value(0)

class Motor:
    def __init__(self):
        self.in1 = Pin(Pin_IN1, Pin.OUT)
        self.in2 = Pin(Pin_IN2, Pin.OUT)
        self.ena = PWM (Pin(Pin_ENA), freq=1000)

    def detener (self):
        self.in1.value(0)
        self.in2.value(0)
        self.ena.duty_u16(0)
    def avanzar(self):
            self.in1.value(1)
            self.in2.value(0)
            self.ena.duty_u16(40000)

    def retroceder(self):
         self.in1.value(0)
         self.in2.value(1)
         self.ena.duty_u16(40000)

class Servo:
    def __init__ (self):
        self.servo = PWM(Pin (Pin_servo), freq = 50)

    def mover(self, posicion):
        self.servo.duty_u16(posicion)


        # los valores son para probar no son reales
    def posicion_rojo(self):
        self.mover(3000)

    def posicion_verde(self):
        self.mover(5000)

    def posicion_azul(self):
        self.mover(7000)
