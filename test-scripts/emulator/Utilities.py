#-------------------------------------------------------------------------------------------#
# The utilities module is useful for declaring datatypes, functions, classes or modules to  #
# be used by the test library scripts.                                                      #
#-------------------------------------------------------------------------------------------#

import subprocess
import os

from stm32f4discovery_gpio import *
from stm32f334nucleo_gpio  import *
from ellduino_gpio         import *
from STM_constants         import *

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
# Utility functions outside library test functions
#-------------------------------------------------------------------------------------------------------------------------#

VariantPinMode = {
    'stm32f4discovery': lambda port, pin, mode: pinMode( STM32F4DISCOVERY_GPIO[port][pin], PinMode[mode] ),
    'stm32f334nucleo':  lambda port, pin, mode: pinMode( STM32F334NUCLEO_GPIO[port][pin], PinMode[mode] ),
    'ellduino':         lambda port, pin, mode: pinMode( ELLDUINO_GPIO[port][pin], PinMode[mode] )
}

VariantDigitalRead = {
	'stm32f4discovery': lambda port, pin: digitalRead( STM32F4DISCOVERY_GPIO[port][pin] ),
    'stm32f334nucleo':  lambda port, pin: digitalRead( STM32F334NUCLEO_GPIO[port][pin] ),
    'ellduino':         lambda port, pin: digitalRead( ELLDUINO_GPIO[port][pin] )
}

VariantDigitalWrite = {
	'stm32f4discovery': lambda port, pin, value: digitalWrite( STM32F4DISCOVERY_GPIO[port][pin], PinValue[value] ),
    'stm32f334nucleo':  lambda port, pin, value: digitalWrite( STM32F334NUCLEO_GPIO[port][pin], PinValue[value] ),
    'ellduino':         lambda port, pin, value: digitalWrite( ELLDUINO_GPIO[port][pin], PinValue[value] )
}
#-------------------------------------------------------------------------------------------------------------------------#