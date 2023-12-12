from machine import Pin
import time
from SN74HC165N import SN74HC165N
from Registers import Registers

# Shift Register pin tanımlamaları
PIN_LATCH = 13
PIN_CLOCK = 14
PIN_DATA = 6

register = SN74HC165N(PIN_LATCH, PIN_CLOCK, PIN_DATA)
registerGrid = Registers(1, 5, register)

while True:
    print(registerGrid)
    time.sleep(1)