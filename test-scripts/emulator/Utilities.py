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
GPIO_MODER          = getattr(sot_emulator, "t_GPIO_MODER")
GPIO_PUPDR          = getattr(sot_emulator, "t_GPIO_PUPDR")
GPIO_ODR            = getattr(sot_emulator, "t_GPIO_ODR")
GPIO_IDR            = getattr(sot_emulator, "t_GPIO_IDR")
if os.environ['VARIANT'] == "stm32f4discovery" or os.environ['VARIANT'] == "stm32f334nucleo":
	GPIO_BSRRL          = getattr(sot_emulator, "t_GPIO_BSRRL")
	GPIO_AFR            = getattr(sot_emulator, "t_GPIO_AFR")
	GPIO_BSRRH          = getattr(sot_emulator, "t_GPIO_BSRRH")
elif os.environ['VARIANT'] == "ellduino":
	GPIO_BSRR           = getattr(sot_emulator, "t_GPIO_BSRR")
	GPIO_AFR            = getattr(sot_emulator, "t_GPIO_AFR")
	GPIO_BRR            = getattr(sot_emulator, "t_GPIO_BRR")
else:
	print "Unknown MCU die.  Please define."
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Python callback functions. Binding through ctypes wrapper                                 #
#-------------------------------------------------------------------------------------------#

#Write wrapper functions to bind c callbacks from gpio registers
CB_FUNC_TYPE = CFUNCTYPE(None, c_char_p, c_char_p, c_uint)

#Python callback function to be called from gpio class member functions
def GPIO_REGISTER_VALUES_CALLBACK(periph, name, value):
	print '{0}:{1}:Value={2}'.format(periph, name, hex(value))

python_cb_func = CB_FUNC_TYPE(GPIO_REGISTER_VALUES_CALLBACK)
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------#
# Utility functions outside library test scripts                                                                          #
#-------------------------------------------------------------------------------------------------------------------------#
#
#GPIO functions
#
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

#
#GPIO port and pins for stm32f4discovery and stm32f334nucleo
#
STM32FXXX_GPIO_PORTA_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
STM32FXXX_GPIO_PORTB_PINS = [0, 3, 4, 5, 6, 8, 9, 10]
STM32FXXX_GPIO_PORTC_PINS = [0, 1, 7]
STM32FXXX_GPIO_PORTS      = ['A', 'B', 'C']
Stm32fxxxValidPin = {
	'A': lambda pin: ( pin in STM32FXXX_GPIO_PORTA_PINS ),
	'B': lambda pin: ( pin in STM32FXXX_GPIO_PORTB_PINS ),
	'C': lambda pin: ( pin in STM32FXXX_GPIO_PORTC_PINS )
}

#
#GPIO port and pins for ellduino
#
ELLDUINO_GPIO_PORTA_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ELLDUINO_GPIO_PORTB_PINS = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ELLDUINO_GPIO_PORTC_PINS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ELLDUINO_GPIO_PORTD_PINS = [2]
ELLDUINO_GPIO_PORTF_PINS = [6, 7]
ELLDUINO_GPIO_PORTS      = ['A', 'B', 'C', 'D', 'F']
EllduinoValidPin = {
	'A': lambda pin: ( pin in ELLDUINO_GPIO_PORTA_PINS ),
	'B': lambda pin: ( pin in ELLDUINO_GPIO_PORTB_PINS ),
	'C': lambda pin: ( pin in ELLDUINO_GPIO_PORTC_PINS ),
	'D': lambda pin: ( pin in ELLDUINO_GPIO_PORTD_PINS ),
	'F': lambda pin: ( pin in ELLDUINO_GPIO_PORTF_PINS )
}

#
#Function to check port validity for variant boards
#
ValidPort = {
   'stm32f4discovery': lambda port: ( port in STM32FXXX_GPIO_PORTS ),
   'stm32f334nucleo':  lambda port: ( port in STM32FXXX_GPIO_PORTS ),
   'ellduino':         lambda port: ( port in ELLDUINO_GPIO_PORTS )
}

#
#Function to check pin validity for variant boards
#
ValidPin = {
   'stm32f4discovery': lambda port, pin: Stm32fxxxValidPin[port](pin),
   'stm32f334nucleo':  lambda port, pin: Stm32fxxxValidPin[port](pin),
   'ellduino':         lambda port, pin: EllduinoValidPin[port](pin)
}

#
#USARTs for variant boards
#
Stm32f4discovery_USART = [1, 2]
Stm32f334nucleo_USART  = [1, 2, 3]
Ellduino_USART         = [2, 1]

#
#Function to check usart validity for variant boards
#
ValidUSART = {
	'stm32f4discovery': lambda usart: ( usart in Stm32f4discovery_USART ),
	'stm32f334nucleo':  lambda usart: ( usart in Stm32f334nucleo_USART ),
	'ellduino':         lambda usart: ( usart in Ellduino_USART )
}
#-------------------------------------------------------------------------------------------------------------------------#
