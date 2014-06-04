#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from ctypes import *

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

#import digitalRead

#print digitalRead.readHigh()

def set_pin_mode(pin):
    """Set the pin mode to input"""
    emulator.pinMode(pin, 0);


def read_high(pin):
    """Read 'HIGH' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    #return digitalRead.readHigh(pin)
    high = c_bool();
    high = emulator.digitalRead(pin);
    return high;


def read_low(pin):
    """Read 'LOW' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    #return digitalRead.readLow(pin)
    low = c_bool();
    low = emulator.digitalRead(pin);
    return low; 

"""
TEST CASES END
"""
