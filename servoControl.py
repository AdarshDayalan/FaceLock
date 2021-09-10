import RPi.GPIO as GPIO
import time

servoPin = 17
GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 50)
servo.start(0)

def lock():
        servo.ChangeDutyCycle(2+(90/18))
        time.sleep(0.5)

def unlock():
        servo.ChangeDutyCycle(2+(180/18))
        time.sleep(0.5)

def cleanUp():
    servo.stop()
    GPIO.cleanup()

lock()
