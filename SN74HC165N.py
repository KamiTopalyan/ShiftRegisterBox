from machine import Pin
import time

class SN74HC165N():
    def __init__(self, latch_pin, clock_pin, data_pin):
        self.PIN_LATCH = Pin(latch_pin, Pin.OUT)
        self.PIN_CLOCK = Pin(clock_pin, Pin.OUT)
        self.PIN_DATA = Pin(data_pin, Pin.IN)
        
    def __setLow__(self, Pin: Pin):
        Pin.low()
        time.sleep_us(5)
        return Pin
    
    def __setHigh__(self, Pin: Pin):
        Pin.high()
        time.sleep_us(5)
        return Pin
    def 
    
    def read_shift_registers(self, register_count) -> int:
        """Üç 74HC165 shift register'ından seri olarak veri okur."""
        self.__setLow__(self.PIN_LATCH)
        self.__setHigh__(self.PIN_LATCH)

        register_values = 0
        for _ in range(register_count * 8):  # Her shift register için 8 bit okuma
            register_values <<= 1
            if self.PIN_DATA.value():
                register_values |= 1
            self.PIN_CLOCK.high()
            self.__wait_change__()
            self.PIN_CLOCK.low()
            self.__wait_change__()
        
        return register_values
    