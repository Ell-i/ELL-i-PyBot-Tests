"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    """Set the pin mode to output"""
    pinMode(      GPIO[port][pin], PinMode['OUTPUT']);

def read_high(port, pin):
    pinMode(      GPIO[port][pin], PinMode['OUTPUT']);
    digitalWrite( GPIO[port][pin], PinValue['HIGH']);
    pinMode(      GPIO[port][pin], PinMode['INPUT']);

    print digitalRead(GPIO[port][pin]);

    high = c_bool(0);
    high.value = digitalRead(GPIO[port][pin]);
    return high.value;

def read_low(port, pin):
    pinMode(      GPIO[port][pin], PinMode['OUTPUT']);
    digitalWrite( GPIO[port][pin], PinValue['LOW']);
    pinMode(      GPIO[port][pin], PinMode['INPUT']);

    low = c_bool(1);
    low.value = digitalRead(GPIO[port][pin]);
    return low.value;

"""
TEST CASES END
"""
