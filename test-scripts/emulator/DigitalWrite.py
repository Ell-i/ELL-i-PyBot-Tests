"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'OUTPUT')

def write_high(port, pin):
	VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'HIGH')

def write_low(port, pin):
	VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'LOW')

"""
TEST CASES END
"""
