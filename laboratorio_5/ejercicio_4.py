import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

motor1_pin = 23
GPIO.setup(motor1_pin, GPIO.OUT)

pwm_motor1 = GPIO.PWM(motor1_pin, 100)
pwm_motor1.start(50)

try:
    while True:
        duty_cycle = input("Ingresa tu duty")
        pwm_motor1.ChangeDutyCycle(float(duty_cycle))
except KeyboardInterrupt:
    pwm_motor1.stop()
    GPIO.cleanup()
