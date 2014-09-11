
"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    """Set the pin mode to output"""
    getattr(emulator, pinMode)(GPIO[port][pin], PinMode['OUTPUT']);

def read_high(port, pin):
    getattr(emulator, digitalWrite)(GPIO[port][pin], PinValue['HIGH']);
    getattr(emulator, pinMode)(GPIO[port][pin], PinMode['INPUT']);
    high = c_bool(0);
    high.value = getattr(emulator, digitalRead)(GPIO[port][pin]);    
    return high.value;

def read_low(port, pin):
    getattr(emulator, digitalWrite)(GPIO[port][pin], PinValue['LOW']);
    getattr(emulator, pinMode)(GPIO[port][pin], PinMode['INPUT']);
    low = c_bool(1);
    low.value = getattr(emulator, digitalRead)(GPIO[port][pin]);    
    return low.value; 

"""
TEST CASES END
"""
