# Edit line 6 to match your chosen GPIO pin

from gpiozero import Motor, DistanceSensor
from time import sleep

motor = motor(forward=4)
sensor = DistanceSensor(23,24, max_distance=1, threshold_distance=0.2)

sensor.when_in_range = motor.forward
sensor.when_out_of_range = motor.close