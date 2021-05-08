"""
import RPi.GPIO as GPIO

print(GPIO.BCM)
print(GPIO.BOARD)

GPIO.setmode(BCM)
GPIO.setmode(BOARD)
mode = GPIO.getmode()

print(mode)
"""

import RPi.GPIO as GPIO

print(GPIO.getmode())
print(GPIO.BCM)
print(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()
print(mode)

GPIO.setwarnings(False)
GPIO.setup(25,GPIO.OUT)

import time
while True:
    GPIO.output(25,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(25,GPIO.LOW)
    time.sleep(0.5)
