"""
Make the led change colors
"""

import RPi.GPIO as GPIO

from time import sleep

#       R   B   G
pins = [17, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

while True:
    # Red
    GPIO.output(pins[0], GPIO.LOW)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.HIGH)
    spleep(1)
    # Blue
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.LOW)
    GPIO.output(pins[2], GPIO.HIGH)
    spleep(1)
    # Green
    GPIO.output(pins[0], GPIO.HIGH)
    GPIO.output(pins[1], GPIO.HIGH)
    GPIO.output(pins[2], GPIO.LOW)
    spleep(1)
