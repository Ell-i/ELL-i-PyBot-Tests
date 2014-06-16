#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from ctypes import *
from Utilities import PinMode

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

def input_pin_mode(pin):
    """Logs setting of input pin mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for setting input pin mode for the corresponding pin.'
    #print pinMode.inputPinMode(pin, mode);
    pinNum = c_uint(pin);
    emulator.pinMode(pinNum.value, PinMode['INPUT']);

def output_pin_mode(pin):
    """Logs setting of output pin mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for setting output pin mode for the corresponding pin.'
    #print pinMode.outputPinMode(pin, mode);
    pinNum = c_uint(pin);
    emulator.pinMode(pinNum.value, PinMode['OUTPUT']);
    
def input_pullup_mode(pin):
    """Logs setting of input pin pullup mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for setting input pin pullup mode for the corresponding pin.'
    #print pinMode.inputPullupMode(pin, mode);
    pinNum = c_uint(pin);
    emulator.pinMode(pinNum.value, PinMode['INPUT_PULLDOWN']);

"""
TEST CASES END
"""
