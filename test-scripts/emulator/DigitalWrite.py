"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
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

def write_high(port, pin):
	"""Write high to pin"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
 		print arg;
		return False
	else:
		VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'HIGH')
		GPIO_BSRR(port, python_cb_func)
		GPIO_BRR(port, python_cb_func)
		GPIO_ODR(port, python_cb_func)
		GPIO_IDR(port, python_cb_func)
		print "Pin value write is high"

def write_low(port, pin):
	"""Write low to pin"""
	try:
		PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
		if PinPortVal == False:
			raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
	except RuntimeError, arg:
		print arg;
		return False
	else:
		VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'LOW')
		GPIO_BSRR(port, python_cb_func)
		GPIO_BRR(port, python_cb_func)
		GPIO_ODR(port, python_cb_func)
		GPIO_IDR(port, python_cb_func)
        print "Pin value write is low"

"""
TEST CASES END
"""
