"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    """Set the pin mode to output"""
    VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'OUTPUT')

def read_high(port, pin):
    """Read high from pin"""
    VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'OUTPUT')
    VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'HIGH')
    VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'INPUT')

    high = c_bool(0);
    high.value = VariantDigitalRead[ os.environ['VARIANT'] ](port, pin)
    return high.value;

def read_low(port, pin):
    """Read low from pin"""
    VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'OUTPUT')
    VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'LOW')
    VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'INPUT')

    low = c_bool(1);
    low.value = VariantDigitalRead[ os.environ['VARIANT'] ](port, pin)
    return low.value;

"""
TEST CASES END
"""
