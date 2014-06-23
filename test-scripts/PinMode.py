#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from Utilities import *

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

def input_pin_mode(port, pin):
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['INPUT']);

def output_pin_mode(port, pin):
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['OUTPUT']);
    
def input_pullup_mode(port, pin):
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['INPUT_PULLUP']);

"""
TEST CASES END
"""
