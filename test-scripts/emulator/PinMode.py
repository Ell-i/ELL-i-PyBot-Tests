"""
TEST CASES START
"""

from Utilities import *

def input_pin_mode(port, pin):
	"""Set the pin mode to input"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
		print arg
	else:
		VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'INPUT')
		GPIO_PUPDR(port, python_cb_func)
        GPIO_MODER(port, python_cb_func)
        print "Pin mode set to INPUT"

def output_pin_mode(port, pin):
	"""Set the pin mode to output"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
		print arg
	else:
		VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'OUTPUT')
		GPIO_PUPDR(port, python_cb_func)
        GPIO_MODER(port, python_cb_func)
        print "Pin mode set to OUTPUT"

def input_pullup_mode(port, pin):
	"""Set the pin mode to input_pullup"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
		print arg
	else:
		VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'INPUT_PULLUP')
		GPIO_PUPDR(port, python_cb_func)
        GPIO_MODER(port, python_cb_func)
        print "Pin mode set to INPUT_PULLUP"

"""
TEST CASES END
"""
