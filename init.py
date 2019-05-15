#!/usr/bin/env python3
#!/usr/bin/env python3

# Imports
import logging
import platform
import subprocess
import sys
import os
from time import sleep

# Vars
fileLocation = 'doorknob.log'
version = str(subprocess.check_output(['git', 'rev-parse', 'HEAD']), 'utf-8')

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

# Checks and installs dependencies
def check_dependencies():
    logging.info("Checking installed dependencies...")
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
    
    try:
        # Supported platforms to run the script
        supportedPlatforms = ['linux1','linux2','linux']
        
        # Unsupported platforms to run the script, this is not recommended to run
        unsupportedPlatforms = ['win32','win64','Windows','darwin','macOS']
        
        # Pull information from system
        logging.debug("Pulling system information...")
        osVersion = platform.version()
        osRelease = platform.release()
        osSystem = platform.system()
        osPlatform = platform.system()
        
        logging.debug("==[ OS INFO ]==")
        logging.debug("OS VERSION: " + osVersion)
        logging.debug("OS RELEASE: " + osRelease)
        logging.debug("OS VERSION: " + osVersion)
        logging.debug("OS SYSTEM: " + osSystem)
        logging.debug("==[ OS INFO ]==")

        # If system is supported
        if osPlatform in supportedPlatforms:
            logging.info("Detected OS is supported!")
            return
        
        # If system is not supported
        elif osPlatform in unsupportedPlatforms:
            warnFlag = 1
            logging.warning("Detected OS is **NOT** SUPPORTED, I AM NOT RESPONSIBLE FOR CATESTROPHIC FAILURE")
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
def init():
    init_complete = 0
    logging.info("Initializing...")
    logging.info("     _                  _                _")
    logging.info("  __| | ___   ___  _ __| | ___ __   ___ | |__")
    logging.info(" / _` |/ _ \\ / _ \\| '__| |/ / '_ \\ / _ \\| '_ \\")
    logging.info("| (_| | (_) | (_) | |  |   <| | | | (_) | |_) |")
    logging.info(" \\__,_|\\___/ \\___/|_|  |_|\\_\\_| |_|\\___/|_.__/")
    logging.info("by doorX // version " + version)
    # Check OS
    os_probe()
    # Setting up logs and other dependencies
    check_dependencies()
    init_complete = 1
    return init_complete

if __name__ == '__main__':
    init()