from gpiozero import CPUTemperature
import time

while (True):
    cpu = CPUTemperature()
    print(cpu.temperature)
    time.sleep(1.0)