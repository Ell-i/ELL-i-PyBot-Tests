#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from Utilities import *

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

#import digitalWrite

def set_pin_mode(port, pin):
    """Set the pin mode to output"""
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['OUTPUT']);

def write_high(port, pin):
    """Write 'HIGH' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['HIGH']);

def write_low(port, pin):
    """Write 'LOW' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['LOW']);

"""
TEST CASES END
"""
