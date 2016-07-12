#!/usr/bin/env python
import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port



pump = port.PA12

gpio.init()
gpio.setcfg(pump, gpio.OUTPUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        gpio.output(led, 1)
        sleep(0.1)
        gpio.output(led, 0)
        sleep(0.1)

        gpio.output(led, 1)
        sleep(0.1)
        gpio.output(led, 0)
        sleep(0.1)

        sleep(0.6)
except KeyboardInterrupt:
    print ("Goodbye.")
