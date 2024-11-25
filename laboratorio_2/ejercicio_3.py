import random
import time
import RPi.GPIO as GPIO
import Adafruit_DHT

# Configuración de pines
HEATER_PIN = 17
FAN_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(HEATER_PIN, GPIO.OUT)
GPIO.setup(FAN_PIN, GPIO.OUT)

# Función para leer la temperatura
def read_temperature():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    return temperature if temperature is not None else random.randint(5, 30)

# Función para controlar los dispositivos
def control_temperature(temp):
    if temp < 12:
        GPIO.output(HEATER_PIN, GPIO.HIGH)
        GPIO.output(FAN_PIN, GPIO.LOW)
    elif temp > 20:
        GPIO.output(HEATER_PIN, GPIO.LOW)
        GPIO.output(FAN_PIN, GPIO.HIGH)
    else:
        GPIO.output(HEATER_PIN, GPIO.LOW)
        GPIO.output(FAN_PIN, GPIO.LOW)

# Bucle principal
try:
    while True:
        temp = read_temperature()
        print("Temperatura actual: ", temp)
        control_temperature(temp)
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
