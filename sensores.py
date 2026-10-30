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