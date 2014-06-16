#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from ctypes import *
from Utilities import PinMode

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

def set_pin_mode(pin):
    """Set the pin mode to input"""
    pinNum = c_uint(pin);
    emulator.pinMode(pinNum.value, PinMode['INPUT']);


def read_high(pin):
    """Read 'HIGH' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    pinNum = c_uint(pin);
    high = c_int(1);
    high.value = emulator.digitalRead(pinNum.value);
    return high.value;


def read_low(pin):
    """Read 'LOW' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    pinNum = c_uint(pin);
    low = c_int(0);
    low.value = emulator.digitalRead(pinNum.value);
    return low.value; 

"""
TEST CASES END
"""
