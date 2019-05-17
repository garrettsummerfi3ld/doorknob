#!/usr/bin/env python3

# Imports
import gpiozero
import time
import bottle

# Handle HTTP rewuests
@route('/')
def index():
    return 'Nothing is here!'

@route('/doorclose/:req')
def close_door_req(close_rq = 0):
    if close_rq == '0':
        logging.info("No request is made!")
        logging.debug("REQUEST CODE: " + close_rq)
        return 'No request made!'

    elif close_rq == '1':
        logging.info("Closing Door...")
        # GPIO COMMANDS TO CONTROL DOOR
        # NOT IMPLEMENTED FOR LACK OF TESTING
        logging.info("Door closed!")
        logging.debug("REQUEST CODE: " + close_rq)
        return 'Door closed!'

def main():
    logging.info("Starting main functions...")


if __name__ == '__main__':
    main()