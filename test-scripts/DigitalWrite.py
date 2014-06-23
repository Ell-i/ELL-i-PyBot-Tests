#!/opt/pym32/bin/python

"""
TEST CASES START
"""

from Utilities import *

#Load the emulator shared library. Call the c-functions directly from the python script using ctypes modules.
emulator = CDLL("../libemulator.so")

#import digitalWrite

def set_pin_mode(port, pin):
    emulator.pinMode(GPIO[port]['PIN'+str(pin)], PinMode['OUTPUT']);

def write_high(port, pin):
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['HIGH']);

def write_low(port, pin):
    emulator.digitalWrite(GPIO[port]['PIN'+str(pin)], PinValue['LOW']);

"""
TEST CASES END
"""
