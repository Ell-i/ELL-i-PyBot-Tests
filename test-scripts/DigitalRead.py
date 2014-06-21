#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from Utilities import *

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

def set_pin_mode(port, pin):
    """Set the pin mode to output"""
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['OUTPUT']);

def read_high(port, pin):
    """Read 'HIGH' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""    
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['HIGH']);
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['INPUT']);
    high = c_int(0);
    high.value = emulator.digitalRead(GPIO[port]['PIN'+str(pin)]);    
    return high.value;

def read_low(port, pin):
    """Read 'LOW' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['LOW']);
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['INPUT']);
    low = c_int(1);
    low.value = emulator.digitalRead(GPIO[port]['PIN'+str(pin)]);    
    return low.value; 

"""
TEST CASES END
"""
