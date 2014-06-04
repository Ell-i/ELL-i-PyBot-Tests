"""
TEST CASES START
"""

from ctypes import *

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

#import digitalWrite

def set_pin_mode(pin):
    """Set the pin mode to output"""
    emulator.pinMode(pin, 3);

def write_high(pin, value):
    """Write 'HIGH' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    emulator.digitalWrite(pin, value);

def write_low(pin, value):
    """Write 'LOW' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    emulator.digitalWrite(pin, value);

"""
TEST CASES END
"""
