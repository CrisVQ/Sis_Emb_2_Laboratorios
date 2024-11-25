import RPi.GPIO as GPIO
import time

# Configuración de pines
LED_PINS = [17, 27, 22, 5]  # Pinas de los 4 LEDs
BUTTON1_PIN = 6  # Primer botón
BUTTON2_PIN = 13  # Segundo botón

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables de estado
led_index = 0
led_time = 1

# Bucle principal
try:
    while True:
        if GPIO.input(BUTTON1_PIN) == GPIO.LOW:  # Si se presiona el primer botón
            led_index = (led_index + 1) % 4  # Cambia el LED
            led_time = 1  # Resetea el tiempo a 1 segundo
            time.sleep(0.2)  # Pequeño retardo para evitar múltiples registros
        
        if GPIO.input(BUTTON2_PIN) == GPIO.LOW:  # Si se presiona el segundo botón
            led_time += 1  # Aumenta el tiempo
            time.sleep(0.2)  # Pequeño retardo para evitar múltiples registros
        
        # Apagar todos los LEDs
        for i in range(4):
            GPIO.output(LED_PINS[i], GPIO.LOW)
        
        # Encender el LED seleccionado
        GPIO.output(LED_PINS[led_index], GPIO.HIGH)
        time.sleep(led_time)  # Mantiene el LED encendido durante el tiempo seleccionado
        GPIO.output(LED_PINS[led_index], GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()
