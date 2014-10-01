#-------------------------------------------------------------------------------------------#
# The utilities module is useful for declaring datatypes, functions, classes or modules to  #
# be used by the test library scripts.                                                      #
#-------------------------------------------------------------------------------------------#

import subprocess
import os

from stm32fxxx_gpio import *
from ellduino_gpio  import *
from STM_constants  import *

# XXX TODO: Error management and exception catching for the wrong board and DLLPATH

if os.environ['VARIANT'] != "ellduino" and \
   os.environ['VARIANT'] != "stm32f4discovery" and \
   os.environ['VARIANT'] != "stm32f334nucleo":
   print "Unknown board"
else:
	# Path to shared library
	DLLPATH = os.environ['ELLIRUNTIME']   \
				+ "/tests/robot_library/" \
				+ os.environ['PLATFORM']  \
				+ "/"                     \
				+ os.environ['VARIANT']   \
				+ "/"
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Shared library function names and loading shared library into python, common to most      #
# of test cases                                                                             #
#-------------------------------------------------------------------------------------------#

# Load the emulator shared library.
sot_emulator = CDLL(DLLPATH + "librobot_library.so")

pinMode             = getattr(sot_emulator, "t_pinMode")
digitalRead         = getattr(sot_emulator, "t_digitalRead")
digitalWrite        = getattr(sot_emulator, "t_digitalWrite")
SerialBegin         = getattr(sot_emulator, "t_SerialBegin")
SerialWrite         = getattr(sot_emulator, "t_SerialWrite")
SPI_Begin           = getattr(sot_emulator, "t_SPI_begin")
SPI_End             = getattr(sot_emulator, "t_SPI_end")
SPI_setBitOrder     = getattr(sot_emulator, "t_SPI_setBitOrder")
SPI_setClockDivider = getattr(sot_emulator, "t_SPI_setClockDivider")
SPI_setDataMode     = getattr(sot_emulator, "t_SPI_setDataMode")
SPI_Transfer        = getattr(sot_emulator, "t_SPI_transfer")
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------#
# Utility functions outside library test scripts                                                                          #
#-------------------------------------------------------------------------------------------------------------------------#
STM32FXXX_GPIO_PORTA_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
STM32FXXX_GPIO_PORTB_PINS = [0, 3, 4, 5, 6, 8, 9, 10]
STM32FXXX_GPIO_PORTC_PINS = [0, 1, 7]

def Stm32fxxxValidPort(port):
	return (port == 'A' or port == 'B' or port == 'C')

def Stm32fxxxValidPin(port, pin):
	if port == 'A':
		for idx in STM32FXXX_GPIO_PORTA_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	elif port == 'B':
		for idx in STM32FXXX_GPIO_PORTB_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	elif port == 'C':
		for idx in STM32FXXX_GPIO_PORTC_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	else:
		return False;

ELLDUINO_GPIO_PORTA_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ELLDUINO_GPIO_PORTB_PINS = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ELLDUINO_GPIO_PORTC_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ELLDUINO_GPIO_PORTD_PINS = [2]
ELLDUINO_GPIO_PORTF_PINS = [6, 7]

def EllduinoValidPort(port):
	return (port == 'A' or port == 'B' or port == 'C' or port == 'D' or port == 'F')

def EllduinoValidPin(port, pin):
	if port == 'A':
		for idx in ELLDUINO_GPIO_PORTA_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	elif port == 'B':
		for idx in ELLDUINO_GPIO_PORTB_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	elif port == 'C':
		for idx in ELLDUINO_GPIO_PORTC_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	elif port == 'D':
		for idx in ELLDUINO_GPIO_PORTD_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	elif port == 'F':
		for idx in ELLDUINO_GPIO_PORTF_PINS:
			if pin == idx:
				return True
			else:
				continue
		return False
	else:
		return False

ValidPort = {
   'stm32f4discovery': lambda port: Stm32fxxxValidPort(port),
   'stm32f334nucleo':  lambda port: Stm32fxxxValidPort(port),
   'ellduino':         lambda port: EllduinoValidPort(port)
}

ValidPin = {
   'stm32f4discovery': lambda port, pin: Stm32fxxxValidPin(port, pin),
   'stm32f334nucleo':  lambda port, pin: Stm32fxxxValidPin(port, pin),
   'ellduino':         lambda port, pin: EllduinoValidPin(port, pin)
}

VariantPinMode = {
    'stm32f4discovery': lambda port, pin, mode: pinMode( STM32FXXX_GPIO[port][pin], PinMode[mode] ),
    'stm32f334nucleo':  lambda port, pin, mode: pinMode( STM32FXXX_GPIO[port][pin], PinMode[mode] ),
    'ellduino':         lambda port, pin, mode: pinMode( ELLDUINO_GPIO[port][pin], PinMode[mode] )
}

VariantDigitalRead = {
	'stm32f4discovery': lambda port, pin: digitalRead( STM32FXXX_GPIO[port][pin] ),
    'stm32f334nucleo':  lambda port, pin: digitalRead( STM32FXXX_GPIO[port][pin] ),
    'ellduino':         lambda port, pin: digitalRead( ELLDUINO_GPIO[port][pin] )
}

VariantDigitalWrite = {
	'stm32f4discovery': lambda port, pin, value: digitalWrite( STM32FXXX_GPIO[port][pin], PinValue[value] ),
    'stm32f334nucleo':  lambda port, pin, value: digitalWrite( STM32FXXX_GPIO[port][pin], PinValue[value] ),
    'ellduino':         lambda port, pin, value: digitalWrite( ELLDUINO_GPIO[port][pin], PinValue[value] )
}
#-------------------------------------------------------------------------------------------------------------------------#
