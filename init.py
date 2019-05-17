#!/usr/bin/env python3

# Imports
import logging
import platform
import subprocess
import sys
import os
from time import sleep

# Vars
version = str(subprocess.check_output(['git', 'rev-parse', 'HEAD']), 'utf-8')
fileLocation = 'doorknob.log'
initCode = 0
totalDependencies = ['bottle', 'gpiozero']

# Check for dependencies


def check_dependencies():
    logging.info("Checking for dependencies...")
    # install pip
    logging.info("Installing pip...")
    # Linux path
    if os_probe.osPlatform == os_probe.supportedPlatforms:
        logging.info("Installing pip from repo...")
        subprocess.run(["sudo", "apt", "install", "python3-pip"])
    # Windows path
    elif os_probe.osPlatform == os_probe.unsupportedPlatforms:
        logging.error("You are running a platform that does not natively support downloads from the command line! Please download pip here: https://bootstrap.pypa.io/get-pip.py")
        exit(1)
    # install dependencies
    for x in totalDependencies:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', totalDependencies[x]])

# Checks for the right OS platform


def os_probe():
    logging.info("Checking OS...")
    warnFlag = 0
    # Supported platforms to run the script
    supportedPlatforms = ['linux1', 'linux2', 'linux']

    # Unsupported platforms to run the script, this is not recommended to run
    unsupportedPlatforms = ['win32', 'win64', 'Windows', 'darwin', 'macOS']

    # Pull information from system
    logging.debug("Pulling system information...")
    osVersion = platform.version()
    osRelease = platform.release()
    osSystem = platform.system()
    osPlatform = platform.system()

    logging.debug("========== [ OS INFO ] ==========")
    logging.debug("OS VERSION: " + osVersion)
    logging.debug("OS RELEASE: " + osRelease)
    logging.debug("OS VERSION: " + osVersion)
    logging.debug("OS SYSTEM: " + osSystem)
    logging.debug("========== [ OS INFO ] ==========")
    # If system is supported
    if osPlatform in supportedPlatforms:
        logging.info("Detected OS is supported!")
        return

    # If system is not supported
    elif osPlatform in unsupportedPlatforms:
        warnFlag = 1
        # Run through a check to see if user is okay with the script being broken
        while warnFlag == 1:
            logging.warning(
                "Detected OS is **NOT** SUPPORTED, THE SCRIPT MAY NOT WORK")
            logging.warning("ARE YOU SURE YOU WANT TO CONTINUE? [Y/n]")
            confirmWarn = str(input(""))

            # Run script
            if confirmWarn == 'Y' or confirmWarn == 'y':
                logging.info(confirmWarn)
                logging.info("Continuing on...")
                return

            # Stop script
            elif confirmWarn == 'N' or confirmWarn == 'n':
                logging.info(confirmWarn)
                logging.info("Closing application...")
                quit(0)
            else:
                logging.error("INPUT NOT RECOGNIZED!")
        return

# Main class


def setup():
    logging.info("Initializing...")
    logging.info("     _                  _                _")
    logging.info("  __| | ___   ___  _ __| | ___ __   ___ | |__")
    logging.info(" / _` |/ _ \\ / _ \\| '__| |/ / '_ \\ / _ \\| '_ \\")
    logging.info("| (_| | (_) | (_) | |  |   <| | | | (_) | |_) |")
    logging.info(" \\__,_|\\___/ \\___/|_|  |_|\\_\\_| |_|\\___/|_.__/")
    logging.info("by doorX // version " + version)
    # Check OS
    os_probe()
    check_dependencies()

    initCode = 1
    return initCode


if __name__ == '__main__':
    setup()
