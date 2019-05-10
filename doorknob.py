#!/usr/bin/env python3

# Imports
import logging
from gpiozero import LED, Button, Motor
from datetime import datetime
from time import sleep

# Logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/temp/doorknob.log',
                    filemode='a')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

mainLogger = logging.getlogger('doorknob.main')

# Vars
motor = Motor(forward=4, backward=14)
led = LED(17)
button = Button(2)

# main class
def main():
    try:
        testCondition = input("input a condition: ")

        if testCondition == yes:
            led.on()
            motor.forward()
            mainLogger.info("Motor starting!")
        if testCondition == no:
            led.off()
            motor.off()
            mainLogger.info("Motor stopped!")
    except:
        mainLogger.error("ERROR! CHECK STACKTRACE!")
