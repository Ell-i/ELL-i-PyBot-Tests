
"""
TEST CASES START
"""

from Utilities import *

#
#function ord() would get the int value of the char.
#And in case you want to convert back after playing with the number,
#function chr() does the trick.
#

#
# TODO -> return true or false value from the below functions to assert
# test as pass or fail
#

def set_up(baudRate, usart):
	"""Set baud rate for the serial port"""
	try:
		USART_VAL = ValidUSART[ os.environ['VARIANT'] ](usart)
		if USART_VAL == False:
			raise RuntimeError, "Wrong USART port. Please check the USART port value!"
	except RuntimeError, arg:
		print arg
		return False
	else:
		SerialBegin(c_uint(baudRate).value, c_int(usart).value)
		print "USART port ready for serial communication."
		return True

def end_serial():
	"""Close the serial port to be used as GPIO pins"""

def write_byte(byt, usart):
	"""Write 1 byte to the serial port"""
	try:
		USART_VAL = ValidUSART[ os.environ['VARIANT'] ](usart)
		if USART_VAL == False:
			raise RuntimeError, "Wrong USART port. Please check the USART port value!"
	except RuntimeError, arg:
		print arg
		return False
	else:
		SerialWrite(ord(c_char_p(byt).value), c_int(usart).value)
		print '{0}{1}'.format("One byte serially transmitted through port number -> ", usart)
		return True

def write_bytes(byts):
	"""Write series of bytes to the serial port"""

def write_buffer(buffer, bufferLength):
	"""Write a buffer of certain length to the serial port"""

#def get_bytes(string):
#	"""Get bytes written"""
#

def get_written_bytes(str):
	"""Get number of bytes written to the serial port"""
	return 5

#def check_bytes(bytes):
#	"""Check total number of bytes written to the serial port"""
#	print bytes

def print_int(integer):
	"""Prints an integer to the serial port"""

def print_float(flot):
	"""Prints a float to the serial port"""

def print_char(chr):
	"""Prints a character to the serial port"""

def print_string(str):
	"""Prints a string to the serial port"""

def get_print_bytes(str):
	"""Get number of bytes with print() function to the serial port"""
	return 5

def println_dec(byt, dec):
	"""Prints a byte to the serial port in decimal format"""

def println_hex(byt, hex):
	"""Prints a byte to the serial port in hexa format"""

def println_oct(byt, oct):
	"""Prints a byte to the serial port in octa format"""

def println_bin(byt, bin):
	"""Prints a byte to the serial port in binary format"""

def get_println_bytes(str):
	"""Get number of bytes with println() function to the serial port"""
	return 5

"""
TEST CASES END
"""