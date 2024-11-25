import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

motor1_pin = 23
motor2_pin = 24

GPIO.setup(motor1_pin, GPIO.OUT)
GPIO.setup(motor2_pin, GPIO.OUT)

pwm_motor1 = GPIO.PWM(motor1_pin, 100)
pwm_motor2 = GPIO.PWM(motor2_pin, 100)

pwm_motor1.start(0)
pwm_motor2.start(0)

uart = serial.Serial("/dev/ttyACM0", baudrate=9600, timeout=1)

while True:
    if uart.in_waiting > 0:
        message = uart.readline().decode('utf-8').strip()
        if message == "motor1":
            pwm_motor1.ChangeDutyCycle(50)
        elif message == "motor2":
            pwm_motor2.ChangeDutyCycle(50)
