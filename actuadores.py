from machine import Pin, PWM
from config import Pin_IN1, Pin_IN2, Pin_ENA, Pin_servo

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
