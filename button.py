import RPi.GPIO as GPIO
from time import sleep

servoPin = 17
buttonPin = 27
prevState = 1
currentState = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin, GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
servo = GPIO.PWM(servoPin, 50)
servo.start(0)

def lock():
        print("Servo Lock")
        servo.ChangeDutyCycle(round(2+(30/18), 1))
        sleep(1.0)
#        servo.ChangeDutyCycle(2+(110/18))
 #       sleep(0.5)

def unlock():
        print("Servo Unlock")
        servo.ChangeDutyCycle(round(2+(130/18), 1))
        sleep(1.0)
  #      servo.ChangeDutyCycle(2+(160/18))
   #     sleep(0.5)

def cleanUp():
    servo.stop()
    GPIO.cleanup()

def main():
    s= False

    try:
        while True:
            currentState = GPIO.input(buttonPin)

            if currentState != prevState:
                if currentState == 0:
                    s = not s
                    if s:
                        lock()
                        print("lock")
                    else:
                        unlock()
                        print("unlock")

                prevState = currentState

    except KeyboardInterrupt:
        cleanUp()
        print("clean")

