#!/usr/bin/env python3

# Imports
import logging
import platform
import sys
import os
from gpiozero import LED, Button, Motor
from time import sleep

# Vars
motor = Motor(forward=4, backward=14)
led = LED(17)
button = Button(2)
fileLocation = 'doorknob.log'

# Logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',filename=fileLocation)

# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()

# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')

# tell the handler to use this format
console.setFormatter(formatter)

# add the handler to the root logger
logging.getLogger('').addHandler(console)

# Create Dirs and files
def create_dirs():
    if not os.path.exists('./log'):
        os.path.join(fileLocation)
        logFile = open(fileLocation,"w")
    else:
        return

def get_os():
    logging.debug("==[ OS INFO ]==")
    logging.debug("OS VERSION: " + osVersion)
    logging.debug("OS RELEASE: " + osRelease)
    logging.debug("OS VERSION: " + osVersion)
    logging.debug("OS SYSTEM: " + osSystem)
    logging.debug("==[ OS INFO ]==")

# Checks and installs dependencies
def check_dependencies():
    
    # Two arrays to compare the required dependencies to have the project to work
    installedDependencies = ['']
    requiredDependencies = ['']
    
    # Check the arrays for discrepancies
    if requiredDependencies not in installedDependencies:
        logging.error("Dependencies not installed!")
        logging.info("Installing dependencies...")
        return
    else:
        logging.info("Dependencies installed!")
        return
# Checks for the right OS platform
def os_probe():
    logging.info("Checking OS...")
    warnFlag = 0
    
    # Supported platforms to run the script
    supportedPlatforms = ['linux1','linux2','linux']
    
    # Unsupported platforms to run the script, this is not recommended to run
    unsupportedPlatforms = ['win32','win64','Windows','darwin','macOS']
    try:
        # Pull information from system
        osVersion = platform.version()
        osRelease = platform.release()
        osSystem = platform.system()
        osPlatform = platform.system()
        
        # If system is supported
        if osPlatform in supportedPlatforms:
            logging.info("Detected OS is supported!")
            get_os()
            return
        
        # If system is not supported
        elif osPlatform in unsupportedPlatforms:
            warnFlag = 1
            logging.warning("Detected OS is **NOT** SUPPORTED, I AM NOT RESPONSIBLE FOR CATESTROPHIC FAILURE")
            get_os()
            # Run through a check to see if user is okay with the script being broken
            while warnFlag == 1:
                logging.warning("ARE YOU SURE YOU WANT TO CONTINUE? [Y/n]")
                confirmWarn = str(input(""))
                
                # Run script
                if confirmWarn == 'Y' or confirmWarn == 'y':
                    logging.info("Continuing on...")
                    return
                
                # Stop script
                elif confirmWarn == 'N' or confirmWarn == 'n':
                    logging.info("Closing application...")
                    exit()
                else:
                    logging.info("")
            return
    except:
        logging.error("ERROR! CHECK STACKTRACE! LOGFILE IS LOCATED IN " + fileLocation)

# main class
def main():
    print("     _                  _                _")
    print("  __| | ___   ___  _ __| | ___ __   ___ | |__")
    print(" / _` |/ _ \\ / _ \\| '__| |/ / '_ \\ / _ \\| '_ \\")
    print("| (_| | (_) | (_) | |  |   <| | | | (_) | |_) |")
    print(" \\__,_|\\___/ \\___/|_|  |_|\\_\\_| |_|\\___/|_.__/")
    print("by doorX // version 0.1.3 alpha")
    # Setting up logs and other dependencies
    create_dirs()
    check_dependencies()
    # Check OS
    os_probe()
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