
"""
TEST CASES START
"""

from Utilities import *
from subprocess import call

#Load the emulator shared library. Call the c-functions directly from 
#the python script using ctypes modules.
emulator = CDLL(DLLPATH + "libemulator.so")

#import digitalWrite

def set_pin_mode(port, pin):
    emulator.pinMode(GPIO[port][pin], PinMode['OUTPUT']);

def write_high(port, pin):
    emulator.digitalWrite(GPIO[port][pin], PinValue['HIGH']);

def write_low(port, pin):
    emulator.digitalWrite(GPIO[port][pin], PinValue['LOW']);

"""
TEST CASES END
"""
