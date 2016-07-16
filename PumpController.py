#!/usr/bin/env python
import os
import sys
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
import logging
import datetime
import time

#script must be run as root
if not os.getegid() == 0:
    sys.exit('Script must be run as root')

check_wait == 7200 #checks for arduino signal every 2 hours
pump_on == 4 #turns on the pump for this long (seconds)

#creates a log file
logging.basicConfig(filename='watering.log',level=logging.DEBUG)

#starts gpio
gpio.init()

logging.info('starting scipt')
time.sleep(10)
logging.info('started script')

#sets up gpio
gpio.setcfg(port.PG6, gpio.OUTPUT)#this pin asks for signal from arduino
gpio.setcfg(port.PG9, gpio.OUTPUT)#this pin starts the pump
gpio.setcfg(port.PG8, gpio.INPUT)#this pin reads the signal from arduino

#if nothing is connected input is 0
gpio.pullup(port.PG8, 0)
gpio.pullup(port.PG8, gpio.PULLDOWN)

while True:
    gpio.output(port.PG6, 1) #asks arduino for the signal
    time.sleep(5) #gives some time for the arduino to respond
    logging.info("Checking for signal : %s" % time.ctime())
    if gpio.input(port.PG8) == 1:
        gpio.output(port.PG9, 1)
        logging.info("Turned the Pump on : %s" % time.ctime())
        time.sleep(int(pump_on))
        logging.info("Turned the Pump off : %s" % time.ctime())
        gpio.output(port.PG9, 0)
        time.sleep(int(check_wait))
    else:
        gpio.output(port.PG9, 0)
        logging.info('waiting for arduino signal: %s' % time.ctime())
        time.sleep(int(check_wait))
