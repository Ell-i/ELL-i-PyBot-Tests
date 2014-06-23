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
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['HIGH']);
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['INPUT']);
    high = c_bool(0);
    high.value = emulator.digitalRead(GPIO[port]['PIN'+str(pin)]);    
    return high.value;

def read_low(port, pin):
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['LOW']);
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['INPUT']);
    low = c_bool(1);
    low.value = emulator.digitalRead(GPIO[port]['PIN'+str(pin)]);    
    return low.value; 

"""
TEST CASES END
"""
