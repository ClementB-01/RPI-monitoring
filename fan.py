import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.out)

while True:
    var = input()
    if (var == 'y'):
        GPIO.output(12, GPIO.HIGH)
        print("Ventilateur allumé")
    if (var == "stop"):
        GPIO.cleanup()
        break;
    else:
        GPIO.output(12, GPIO.LOW)