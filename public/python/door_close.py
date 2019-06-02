# Edit line 6 to match your chosen GPIO pin

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
sleep(5)
GPIO.cleanup()