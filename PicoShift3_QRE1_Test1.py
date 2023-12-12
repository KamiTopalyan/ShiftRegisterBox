from machine import Pin
import time

# Shift Register pin tanımlamaları
PIN_LATCH = Pin(13, Pin.OUT)
PIN_CLOCK = Pin(14, Pin.OUT)
PIN_DATA = Pin(6, Pin.IN)

def read_shift_registers():
    """Üç 74HC165 shift register'ından seri olarak veri okur."""
    PIN_LATCH.low()
    time.sleep_us(5)
    PIN_LATCH.high()
    time.sleep_us(5)

    register_values = 0
    for _ in range(24):  # Üç shift register için 24 bit okuma
        register_values <<= 1
        if PIN_DATA.value():
            register_values |= 1
        PIN_CLOCK.high()
        time.sleep_us(5)
        PIN_CLOCK.low()
        time.sleep_us(5)
    
    return register_values

while True:
    values = read_shift_registers()
    print(values)
    if values & 0b1:  # İlk shift register'ın QRE sensörü (P0)
        print("Shift 1, QRE Aktif")
    if values & 0b100000000:  # İkinci shift register'ın QRE sensörü (P0)
        print("Shift 2, QRE Aktif")
    if values & 0b100000000000000000:  # Üçüncü shift register'ın QRE sensörü (P0)
        print("Shift 3, QRE Aktif")
    time.sleep(1)
