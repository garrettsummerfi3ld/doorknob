#!/usr/bin/env python3

# Imports
import init
import main_functions
import logging
import platform
import subprocess
import sys
import os
from time import sleep

# Vars
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

# main class
def main():
    init.setup()
    if init.initCode == 1:
        main_functions.main()

if __name__ == "__main__":
    main()