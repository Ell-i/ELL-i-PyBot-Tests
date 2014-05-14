"""
TEST CASES START
"""

#Import a serial c-python library here to call the serial functions ...


def begin_serial(baudRate):
	"""Set baud rate for the serial port"""

def end_serial():
	"""Close the serial port to be used as GPIO pins"""

def write_byte(byt):
	"""Write 1 byte to the serial port"""

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