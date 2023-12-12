from time import sleep
import os
string = ""
colors = {
    "red": "\033[0;31m",
    "green": "\033[1;32m",
    "end": "\033[0m",
}
column_count = 5
row_count = 1
total_count = column_count * row_count
for i in range(0, total_count * 8, 8):
    string += "| {} ".format(colors["green"] + "X" + colors["end"] True else colors["red"] + "X" + colors["end"])
    if(i // 8 % column_count == column_count - 1):
        string += "|"
        
while True:
    print(string)
    sleep(1)
    os.system('cls')
    