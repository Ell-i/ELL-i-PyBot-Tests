#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from ctypes import *
from Utilities import PinMode

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

#import digitalWrite

def set_pin_mode(pin):
    """Set the pin mode to output"""
    pinNum = c_uint(pin);
    emulator.pinMode(pinNum.value, PinMode['OUTPUT']);

def write_high(pin, value):
    """Write 'HIGH' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    pinNum = c_uint(pin);    
    val = c_uint(value);
    emulator.digitalWrite(pinNum.value, val.value);

def write_low(pin, value):
    """Write 'LOW' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    pinNum = c_uint(pin);    
    val = c_uint(value);    
    emulator.digitalWrite(pinNum.value, val.value);

"""
TEST CASES END
"""
