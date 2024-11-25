import RPi.GPIO as GPIO
import time

# Configuración de pines GPIO
led_pins = [17, 27, 22, 23]  # Pines GPIO para los 4 LEDs
button1_pin = 24  # Pin GPIO para el botón 1 (incremento)
button2_pin = 25  # Pin GPIO para el botón 2 (decremento)

# Inicialización del sistema GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pins, GPIO.OUT)
GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables
counter = 0  # Contador inicial en 0
max_value = 15  # Valor máximo (4 bits = 15 en binario)
previous_button1_state = GPIO.input(button1_pin)
previous_button2_state = GPIO.input(button2_pin)

# Función para mostrar el valor binario en los LEDs
def display_binary(value):
    if value >= 8:
        GPIO.output(led_pins[3], 1)
        value -= 8
    else:
        GPIO.output(led_pins[3], 0)

    if value >= 4:
        GPIO.output(led_pins[2], 1)
        value -= 4
    else:
        GPIO.output(led_pins[2], 0)

    if value >= 2:
        GPIO.output(led_pins[1], 1)
        value -= 2
    else:
        GPIO.output(led_pins[1], 0)

    if value >= 1:
        GPIO.output(led_pins[0], 1)
    else:
        GPIO.output(led_pins[0], 0)


try:
    while True:
        # Lectura de los estados de los botones
        button1_state = GPIO.input(button1_pin)
        button2_state = GPIO.input(button2_pin)
        
        # Incrementar contador cuando se presiona el botón 1
        if button1_state == GPIO.LOW and previous_button1_state == GPIO.HIGH:
            counter += 1
            if counter > max_value:
                counter = 0
            display_binary(counter)
            print(f"Botón 1 presionado. Contador incrementado a {counter}")
            time.sleep(0.3)  # Anti-rebote
        
        # Decrementar contador cuando se presiona el botón 2
        if button2_state == GPIO.LOW and previous_button2_state == GPIO.HIGH:
            if counter > 0:
                counter -= 1
            display_binary(counter)
            print(f"Botón 2 presionado. Contador decrementado a {counter}")
            time.sleep(0.3)  # Anti-rebote

        # Actualizar el estado anterior de los botones
        previous_button1_state = button1_state
        previous_button2_state = button2_state

except KeyboardInterrupt:
    GPIO.cleanup()
