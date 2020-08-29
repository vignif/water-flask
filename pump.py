pin = 21
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
while True:
    GPIO.output(pin, True)
    time.sleep(2)
    GPIO.output(pin, False)
    time.sleep(2)
