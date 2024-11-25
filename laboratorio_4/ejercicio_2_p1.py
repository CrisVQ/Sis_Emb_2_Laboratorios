import RPi.GPIO as GPIO
import time

# Definición de pines
buzzer_pin = 18  # Pin conectado al buzzer
button_start_pin = 17  # Pin del primer botón (activar buzzer)
button_stop_pin = 27   # Pin del segundo botón (desactivar buzzer)

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)  # Usar numeración BCM
GPIO.setup(buzzer_pin, GPIO.OUT)  # Pin del buzzer como salida
GPIO.setup(button_start_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Primer botón como entrada con resistencia pull-down
GPIO.setup(button_stop_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   # Segundo botón como entrada con resistencia pull-down

buzzer_on = False  # Estado del buzzer

# Bucle principal
while True:
    # Comprobar si el primer botón (start) es presionado
    if GPIO.input(button_start_pin) == GPIO.HIGH:
        buzzer_on = True  # Activar buzzer

    # Comprobar si el segundo botón (stop) es presionado
    if GPIO.input(button_stop_pin) == GPIO.HIGH:
        buzzer_on = False  # Apagar buzzer

    # Controlar el estado del buzzer
    if buzzer_on:
        GPIO.output(buzzer_pin, GPIO.HIGH)  # Encender buzzer
    else:
        GPIO.output(buzzer_pin, GPIO.LOW)  # Apagar buzzer

    # Pequeña pausa para evitar el rebote del botón
    time.sleep(0.1)

# No se alcanzará la limpieza sin excepciones
GPIO.cleanup()
