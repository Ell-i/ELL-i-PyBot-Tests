
"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    pinMode(GPIO[port][pin], PinMode['OUTPUT']);

def write_high(port, pin):
    digitalWrite(GPIO[port][pin], PinValue['HIGH']);

def write_low(port, pin):
    digitalWrite(GPIO[port][pin], PinValue['LOW']);

"""
TEST CASES END
"""