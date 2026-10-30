from machine import Pin
import time
from config import Pin_IR, Pin_S0, Pin_S1, Pin_S2, Pin_S3, Pin_OUT

class GestorSensores:
    def __init__(self):
        self.sensor_ir = Pin(Pin_IR, Pin.IN)