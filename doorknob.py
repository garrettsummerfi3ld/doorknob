#!/usr/bin/env python3

from gpiozero import LED, Button

led = LED(17)
button = Button(2)

while True:
    if button.is_pressed:
        led.on()
        print("LED On!")
    else:
        led.off()
        print("LED Off")