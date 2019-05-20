#!/usr/bin/env python3

# Imports
import logging
import gpiozero
import time
import flask

# Vars
motor = gpiozero.Motor(forward=20, backward=26)

# Handle HTTP requests
@route('/')
def index():
    return 'Nothing is here!'

# Reqest handling
@route('/doorclose/:req')
def close_door_req(close_rq=0):
    # If no request has been made...
    if close_rq == '0':
        logging.info("No request is made!")
        logging.debug("REQUEST CODE: " + close_rq)
        return 'No request made!'

    # If there is a request made...
    elif close_rq == '1':
        logging.info("Closing Door...")
        motor.forward()
        time.sleep(5)
        logging.info("Door closed!")
        logging.debug("REQUEST CODE: " + close_rq)
        return 'Door closed!'

    elif close_rq == '2':
        logging.info("Opening door...")
        motor.backward()
        time.sleep(5)
        logging.info("Door opened!")
        logging.debug("REQUEST CODE: " + close_rq)


def main():
    logging.info("Starting main functions...")


if __name__ == '__main__':
    main()
