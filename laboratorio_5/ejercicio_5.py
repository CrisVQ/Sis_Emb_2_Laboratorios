import serial
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button_pin = 17

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

uart = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

while True:
    if GPIO.input(button_pin) == GPIO.LOW:
        uart.write(b"buzzer\n")
        time.sleep(0.2)
