#!/usr/bin/env python3

from gpiozero import LED, Button, Motor
from time import sleep

motor = Motor(forward=4, backward=14)
led = LED(17)
button = Button(2)

while True:
    if button.is_pressed:
        led.on()
        motor.forward()
        print("Motor starting!")
    else:
        led.off()
        motor.backward()
        print("Motor stopped!")