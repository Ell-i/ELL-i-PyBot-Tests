"""
TEST CASES START
"""

from Utilities import *

def input_pin_mode(port, pin):
    VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'INPUT')

def output_pin_mode(port, pin):
    VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'OUTPUT')

def input_pullup_mode(port, pin):
	VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'INPUT_PULLUP')

"""
TEST CASES END
"""
