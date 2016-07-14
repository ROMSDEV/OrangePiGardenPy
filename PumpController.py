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

gpio.setcfg(port.PG9, gpio.OUTPUT)
gpio.setcfg(port.PA11, gpio.INPUT)

sensor = port.PA11
led = port.PG9  

if gpio.input(sensor) == 1:
    gpio.output(led, 1)
    logging.info("Watering now : %s" % time.ctime())
    time.sleep(5)
    gpio.output(led, 0)
else:
    gpio.output(led, 0)

while gpio.input(sensor) == 0:
    logging.info('lol just waiting : %s' % time.ctime())
    time.sleep(60)
