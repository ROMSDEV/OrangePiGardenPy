#!/usr/bin/env python
import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
import logging
import datetime

logging.basicConfig(filename='watering.log',level=logging.DEBUG)


gpio.init()

gpio.setcfg(port.PG9, gpio.OUTPUT)
gpio.setcfg(port.PE11, gpio.INPUT) 


gpio.pullup(port.PE11, 0) #Clear pullups
gpio.pullup(port.PE11, gpio.PULLDOWN) #Enable pull-down
gpio.pullup(port.PE11, gpio.PULLUP) #Enable pull-up

if gpio.input(port.PE11) == 1:
gpio.output(port.PG9, gpio.HIGH)
logging.info("Watering now : %s" % time.ctime())
else:
gpio.output(port.PG9, gpio.LOW)

while gpio.input(port.PE11) == 0:
    logging.info("lol just waiting : %s" % time.ctime())
    
