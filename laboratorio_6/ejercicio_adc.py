import RPi.GPIO as GPIO
import time
import serial

# Configuración de los pines del HC-SR04
TRIG = 23  # Pin GPIO para TRIG
ECHO = 24  # Pin GPIO para ECHO

# Configuración de UART
ser = serial.Serial('/dev/ttyS0', 9600)  # Cambia a tu puerto UART si es diferente

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    # Enviar pulso de disparo
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Medir el tiempo del pulso de respuesta
    while GPIO.input(ECHO) == 0:
        start_time = time.time()

    while GPIO.input(ECHO) == 1:
        end_time = time.time()

    # Calcular la distancia en cm
    duration = end_time - start_time
    distance = (duration * 34300) / 2  # Velocidad del sonido: 34300 cm/s

    return distance

try:
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.2f} cm")

        # Enviar la distancia a la Tiva por UART
        ser.write(f"{int(distance)}\n".encode())

        time.sleep(1)  # Leer la distancia cada segundo

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
    ser.close()
