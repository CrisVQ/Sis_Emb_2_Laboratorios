import RPi.GPIO as GPIO  # Importamos la librería para controlar los pines GPIO
import time  # Importamos la librería para usar retrasos de tiempo

# Configuración básica de los pines
GPIO.setmode(GPIO.BCM)  # Usamos la numeración BCM de los pines
GPIO.setwarnings(False)  # Desactivamos las advertencias

# Definimos el pin del botón y el buzzer
boton_pin = 17  # El botón está conectado al pin GPIO 17
buzzer_pin = 27  # El buzzer está conectado al pin GPIO 27

# Configuramos los pines como entrada (botón) y salida (buzzer)
GPIO.setup(boton_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Botón como entrada con resistencia pull-up
GPIO.setup(buzzer_pin, GPIO.OUT)  # Buzzer como salida

# Variable para almacenar el estado anterior del botón
estado_anterior = GPIO.input(boton_pin)

# Bucle principal del programa
try:
    while True:
        estado_actual = GPIO.input(boton_pin)  # Leemos el estado actual del botón
        
        if estado_actual == GPIO.LOW and estado_anterior == GPIO.HIGH:  # Botón presionado
            print("Botón presionado")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Encendemos el buzzer
        
        elif estado_actual == GPIO.HIGH and estado_anterior == GPIO.LOW:  # Botón liberado
            print("Botón liberado")
            GPIO.output(buzzer_pin, GPIO.LOW)  # Apagamos el buzzer

        estado_anterior = estado_actual  # Actualizamos el estado anterior
        time.sleep(0.1)  # Esperamos un poco para no saturar el procesador

# Cuando detienes el programa (Ctrl+C), limpiamos la configuración de los pines GPIO
except KeyboardInterrupt:
    GPIO.cleanup()
