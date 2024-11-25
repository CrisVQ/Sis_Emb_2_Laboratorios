import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
led1_pin = 17  # Pin GPIO para el LED 1
led2_pin = 27  # Pin GPIO para el LED 2
button_pin = 22  # Pin GPIO para el botón

# Inicialización del sistema GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1_pin, GPIO.OUT)
GPIO.setup(led2_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables
state = 1  # Estado inicial
previous_button_state = GPIO.input(button_pin)

def blink_alternating():
    GPIO.output(led1_pin, GPIO.HIGH)
    GPIO.output(led2_pin, GPIO.LOW)
    time.sleep(1)
    GPIO.output(led1_pin, GPIO.LOW)
    GPIO.output(led2_pin, GPIO.HIGH)
    time.sleep(1)

def blink_simultaneously():
    GPIO.output(led1_pin, GPIO.HIGH)
    GPIO.output(led2_pin, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(led1_pin, GPIO.LOW)
    GPIO.output(led2_pin, GPIO.LOW)
    time.sleep(2)

def turn_off_leds():
    GPIO.output(led1_pin, GPIO.LOW)
    GPIO.output(led2_pin, GPIO.LOW)

try:
    while True:
        button_state = GPIO.input(button_pin)
        
        # Cambiar estado cuando se presiona el botón
        if button_state == GPIO.LOW and previous_button_state == GPIO.HIGH:
            state += 1
            if state > 3:
                state = 1
            time.sleep(0.3)  # Anti-rebote
        
        previous_button_state = button_state

        # Ejecutar acción basada en el estado
        if state == 1:
            blink_alternating()
        elif state == 2:
            blink_simultaneously()
        elif state == 3:
            turn_off_leds()

except KeyboardInterrupt:
    GPIO.cleanup()