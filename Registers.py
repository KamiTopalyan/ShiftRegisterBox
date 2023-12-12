from SN74HC165N import SN74HC165N
class Registers:
    def __init__(self, row: int, col: int, register: SN74HC165N) -> None:
        self.row_count = row
        self.column_count = col
        self.total_count = row * col
        self.register: SN74HC165N  = register
    
    def read_shift_registers(self) -> int:
        """Üç 74HC165 shift register'ından seri olarak veri okur."""
        self.register.doLowHigh(self.register.PIN_LATCH)

        register_values = 0
        for _ in range(self.total_count * 8):  # Her shift register için 8 bit okuma
            register_values <<= 1
            if self.register.PIN_DATA.value():
                register_values |= 1
        self.register.doLowHigh(self.register.PIN_CLOCK)
        
        return register_values
    def coloredText(self, number: int, string: str) -> str:
        COLOR_SEQS = {0:"\033[0;33m", 1:"\033[0;35m", 2:"\033[1;37m", 3:"\033[0;34m"}
        END_COLOR = "\033[0m"
        return COLOR_SEQS[number % len(COLOR_SEQS)] + string + END_COLOR
        
    def __str__(self) -> str:
        string = "".join([f"| {i} " for i in range(1,self.column_count+1)]) + "|\n"
        values = self.read_shift_registers()
        colors = {
            "red": "\033[0;31m",
            "green": "\033[1;32m",
        }
        for i in range(0, self.total_count * 8, 8):
            condition = values & (1 << i)
            string += "| {} ".format(colors["green"] + "X" + colors["end"] if condition else colors["red"] + "X" + colors["end"])
            if(i // 8 % self.column_count == self.column_count - 1):
                string += "|\n"
        return string