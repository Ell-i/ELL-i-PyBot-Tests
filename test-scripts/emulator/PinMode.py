"""
TEST CASES START
"""

from Utilities import *

def input_pin_mode(port, pin):
    pinMode(GPIO[port][pin], PinMode['INPUT']);

def output_pin_mode(port, pin):
    pinMode(GPIO[port][pin], PinMode['OUTPUT']);

def input_pullup_mode(port, pin):
    pinMode(GPIO[port][pin], PinMode['INPUT_PULLUP']);

"""
TEST CASES END
"""
