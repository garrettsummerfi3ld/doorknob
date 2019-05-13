#!/usr/bin/env python3

# Imports
import logging
import platform
import sys
#from gpiozero import LED, Button, Motor
from datetime import datetime
from time import sleep

# Vars
#motor = Motor(forward=4, backward=14)
#led = LED(17)
#button = Button(2)
filelocation = './log/doorknob.log'

# Create Dirs and files
def createDirs():
    if not os.path.exists('./log'):
        os.path.join(filelocation)
    else:
        return

# Logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename=filelocation)
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)
# Logging vars
mainLogger = logging.getlogger('doorknob.main')
osLogger = logging.getLogger('doorknob.os')

# Checks for the right OS Host
def osProbe():
    osLogger.info("Checking OS...")
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
        osVersion = str(platform.version())
        osRelease = str(platform.release())
        osSystem = str(platform.system())
        osPlatform = str(sys.platform())
        # If system is supported
        if osPlatform in supportedPlatforms:
            osLogger.info("Detected OS is supported!")
            osLogger.debug("==[ OS INFO ]==")
            osLogger.debug("OS VERSION: " + osVersion)
            osLogger.debug("OS RELEASE: " + osRelease)
            osLogger.debug("OS VERSION: " + osVersion)
            osLogger.debug("OS SYSTEM: " + osSystem)
            osLogger.debug("==[ OS INFO ]==")
            return
        # If system is not supported
        elif osPlatform in unsupportedPlatforms:
            warnFlag = 1
            osLogger.warning("Detected OS is **NOT** SUPPORTED, I AM NOT RESPONSIBLE FOR CATESTROPHIC FAILURE")
            osLogger.debug("==[ OS INFO ]==")
            osLogger.debug("OS VERSION: " + osVersion)
            osLogger.debug("OS RELEASE: " + osRelease)
            osLogger.debug("OS VERSION: " + osVersion)
            osLogger.debug("OS SYSTEM: " + osSystem)
            osLogger.debug("==[ OS INFO ]==")
            # Run through a check to see if user is okay with the script being broken
            while warnFlag == 1:
                osLogger.warning("ARE YOU SURE YOU WANT TO CONTINUE? [Y/n]")
                confirmWarn = str(input(""))
                # Run script
                if confirmWarn == 'Y' & confirmWarn == 'y':
                    osLogger.info("Continuing on...")
                    return
                # Stop script
                else:
                    osLogger.info("Closing application...")
                    break
            return
    except:
        osLogger.error("ERROR! CHECK STACKTRACE! LOGFILE IN")

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
            mainLogger.info("Motor starting!")
        elif testCondition == 'no':
            led.off()
            motor.off()
            mainLogger.info("Motor stopped!")
    except:
        mainLogger.error("ERROR! CHECK STACKTRACE! LOGFILE IN")
