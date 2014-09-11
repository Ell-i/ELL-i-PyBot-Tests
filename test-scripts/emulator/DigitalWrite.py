
"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    getattr(emulator, pinMode)(GPIO[port][pin], PinMode['OUTPUT']);

def write_high(port, pin):
    getattr(emulator, digitalWrite)(GPIO[port][pin], PinValue['HIGH']);

def write_low(port, pin):
    getattr(emulator, digitalWrite)(GPIO[port][pin], PinValue['LOW']);

"""
TEST CASES END
"""
