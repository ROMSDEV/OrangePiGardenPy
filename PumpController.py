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
import time

logging.basicConfig(filename='watering.log',level=logging.DEBUG)


gpio.init()

logging.info('starting scipt')
time.sleep(10)
logging.info('started script')
gpio.setcfg(port.PG9, gpio.OUTPUT)
gpio.setcfg(port.PG8, gpio.INPUT)

gpio.pullup(port.PG8, 0)
gpio.pullup(port.PG8, gpio.PULLDOWN)

while True:
    if gpio.input(port.PG8) == 1:
        gpio.output(port.PG9, 1)
        logging.info("Watering now : %s" % time.ctime())
        time.sleep(10)
        gpio.output(port.PG9, 0)
    else:
        gpio.output(port.PG9, 0)
        logging.info('waiting')
        time.sleep(3600)

