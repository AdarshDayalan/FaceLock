import RPi.GPIO as gpio
from time import sleep

SleepTime=1
pin = 4
gpio.setwarnings(True)

def main():
    
    gpio.setmode(gpio.BCM)
    gpio.setup(4,gpio.OUT)
    
    print("Garage Door Activated.")

    try:

      gpio.output(4,gpio.HIGH)

      sleep(sleepTime)

      gpio.output(4,gpio.LOW)

    except:
       print("Other error or exception occurred!")


    finally:

       print("\n Finished\n")

#       gpio.cleanup()


main()
