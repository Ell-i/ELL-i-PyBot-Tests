#!/opt/pym32/bin/python

#The utilities module is useful for declaring datatypes, functions or classes to be
#used by the test library scripts.

from ctypes import *

#The following values for pin mode are taken from arduelli_gpio.h for Arduino API
#compatibility. Such declarations are more readable in test library scripts.

zero  = c_uint(0);
one   = c_uint(1);
two   = c_uint(2);
three = c_uint(3);

PinMode = {'INPUT': zero, 'INPUT_PULLUP': one, 'INPUT_PULLDOWN': two, 'OUTPUT': three}