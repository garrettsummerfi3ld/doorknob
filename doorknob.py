#!/usr/bin/env python3

# Imports
import logging
import platform
import sys
import os
#from gpiozero import LED, Button, Motor
from datetime import datetime
from time import sleep

# Vars
#motor = Motor(forward=4, backward=14)
#led = LED(17)
#button = Button(2)
fileLocation = 'doorknob.log'
# Create Dirs and files
def createDirs():
    if not os.path.exists('./log'):
        os.path.join(fileLocation)
        logFile = open(fileLocation,"w")
    else:
        return

# Logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename=fileLocation)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Checks for the right OS Host
def osProbe():
    logging.info("Checking OS...")
    warnFlag = 0
    # Supported platforms to run the script
    supportedPlatforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'linux' : 'Linux'
    }
    # Unsupported platforms to run the script, this is not recommended to run
    unsupportedPlatforms = {
        'win32' : 'Windows',
        'win64' : 'Windows',
        'darwin' : 'macOS'
    }
    try:
        # Pull information from system
        osVersion = platform.version()
        osRelease = platform.release()
        osSystem = platform.system()
        osPlatform = platform.system()
        # If system is supported
        if osPlatform in supportedPlatforms:
            logging.info("Detected OS is supported!")
            logging.debug("==[ OS INFO ]==")
            logging.debug("OS VERSION: " + osVersion)
            logging.debug("OS RELEASE: " + osRelease)
            logging.debug("OS VERSION: " + osVersion)
            logging.debug("OS SYSTEM: " + osSystem)
            logging.debug("==[ OS INFO ]==")
            return
        # If system is not supported
        elif osPlatform in unsupportedPlatforms:
            warnFlag = 1
            logging.warning("Detected OS is **NOT** SUPPORTED, I AM NOT RESPONSIBLE FOR CATESTROPHIC FAILURE")
            logging.debug("==[ OS INFO ]==")
            logging.debug("OS VERSION: " + osVersion)
            logging.debug("OS RELEASE: " + osRelease)
            logging.debug("OS VERSION: " + osVersion)
            logging.debug("OS SYSTEM: " + osSystem)
            logging.debug("==[ OS INFO ]==")
            # Run through a check to see if user is okay with the script being broken
            while warnFlag == 1:
                logging.warning("ARE YOU SURE YOU WANT TO CONTINUE? [Y/n]")
                confirmWarn = str(input(""))
                # Run script
                if confirmWarn == 'Y' & confirmWarn == 'y':
                    logging.info("Continuing on...")
                    return
                # Stop script
                else:
                    logging.info("Closing application...")
                    break
            return
    except:
        logging.error("ERROR! CHECK STACKTRACE! LOGFILE IN")

# main class
def main():
    # Setting up logs and other dependencies
    createDirs()
    # Check OS
    osProbe()
    try:
        testCondition = str(input("input a condition: "))
        if testCondition == 'yes':
            led.on()
            motor.forward()
            logging.info("Motor starting!")
        elif testCondition == 'no':
            led.off()
            motor.off()
            logging.info("Motor stopped!")
    except:
        logging.error("ERROR! CHECK STACKTRACE! LOGFILE IN")

if __name__ == "__main__":
    main()