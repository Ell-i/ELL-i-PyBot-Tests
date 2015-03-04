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
				+ "/stm32/tests/robot_library/" \
				+ os.environ['PLATFORM']  \
				+ "/"                     \
				+ os.environ['VARIANT']   \
				+ "/"
#DLLPATH = "/home/asif/Ell-i-Working-Directory/Ell-i-Software-Development/Runtime/stm32/tests/robot_library/emulator/ellduino/"
#DLLPATH = "/home/asif/Ell-i-Working-Directory/Ell-i-Software-Development/Runtime/stm32/tests/robot_library/emulator/stm32f4discovery/"
#DLLPATH = "/home/asif/Ell-i-Working-Directory/Ell-i-Software-Development/Runtime/stm32/tests/robot_library/emulator/stm32f334nucleo/"
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Shared library function names and loading shared library into python, common to most      #
# of test cases                                                                             #
#-------------------------------------------------------------------------------------------#

# Load the emulator shared library.
sot_emulator = CDLL(DLLPATH + "librobot_library.so")

# Arduino Digital API References
pinMode             = getattr(sot_emulator, "t_pinMode")
digitalRead         = getattr(sot_emulator, "t_digitalRead")
digitalWrite        = getattr(sot_emulator, "t_digitalWrite")

# Arduino Serial API References
SerialBegin         = getattr(sot_emulator, "t_SerialBegin")
SerialWrite         = getattr(sot_emulator, "t_SerialWrite")

# Arduino Serial Peripheral Interface (SPI) library API References
SPI_Begin           = getattr(sot_emulator, "t_SPI_begin")
SPI_End             = getattr(sot_emulator, "t_SPI_end")
SPI_setBitOrder     = getattr(sot_emulator, "t_SPI_setBitOrder")
SPI_setClockDivider = getattr(sot_emulator, "t_SPI_setClockDivider")
SPI_setDataMode     = getattr(sot_emulator, "t_SPI_setDataMode")
SPI_Transfer        = getattr(sot_emulator, "t_SPI_transfer")

#  General Purpose Input Output (GPIO) callback function references for VARIANT boards
GPIO_MODER          = getattr(sot_emulator, "t_GPIO_MODER")
GPIO_PUPDR          = getattr(sot_emulator, "t_GPIO_PUPDR")
GPIO_ODR            = getattr(sot_emulator, "t_GPIO_ODR")
GPIO_IDR            = getattr(sot_emulator, "t_GPIO_IDR")
if os.environ['VARIANT'] == "stm32f4discovery" or os.environ['VARIANT'] == "stm32f334nucleo":
	GPIO_BSRRL      = getattr(sot_emulator, "t_GPIO_BSRRL")
	GPIO_AFR        = getattr(sot_emulator, "t_GPIO_AFR")
	GPIO_BSRRH      = getattr(sot_emulator, "t_GPIO_BSRRH")
elif os.environ['VARIANT'] == "ellduino":
	GPIO_BSRR       = getattr(sot_emulator, "t_GPIO_BSRR")
	GPIO_AFR        = getattr(sot_emulator, "t_GPIO_AFR")
	GPIO_BRR        = getattr(sot_emulator, "t_GPIO_BRR")
else:
	print "Unknown MCU die.  Please define."

# Universal Synchronous Asynchronous Reciever Transmitter (USART) callback function references
# for VARIANT boards
if os.environ['VARIANT'] == "stm32f4discovery":
	USART_SR        = getattr(sot_emulator, "t_USART_SR")
	USART_DR        = getattr(sot_emulator, "t_USART_DR")
	USART_BRR       = getattr(sot_emulator, "t_USART_BRR")
	USART_CR1       = getattr(sot_emulator, "t_USART_CR1")
	USART_CR2       = getattr(sot_emulator, "t_USART_CR2")
	USART_CR3       = getattr(sot_emulator, "t_USART_CR3")
	USART_GTPR      = getattr(sot_emulator, "t_USART_GTPR")
elif os.environ['VARIANT'] == "ellduino" or os.environ['VARIANT'] == "stm32f334nucleo":
	USART_BRR       = getattr(sot_emulator, "t_USART_BRR")
	USART_CR1       = getattr(sot_emulator, "t_USART_CR1")
	USART_CR2       = getattr(sot_emulator, "t_USART_CR2")
	USART_CR3       = getattr(sot_emulator, "t_USART_CR3")
	USART_GTPR      = getattr(sot_emulator, "t_USART_GTPR")
	USART_RTOR      = getattr(sot_emulator, "t_USART_RTOR")
	USART_RQR       = getattr(sot_emulator, "t_USART_RQR")
	USART_ISR       = getattr(sot_emulator, "t_USART_ISR")
	USART_ICR       = getattr(sot_emulator, "t_USART_ICR")
	USART_RDR       = getattr(sot_emulator, "t_USART_RDR")
	USART_TDR       = getattr(sot_emulator, "t_USART_TDR")
else:
	print "Unknown MCU die.  Please define."

# System Control Block (SCB) callback function references for VARIANT boards
if os.environ['VARIANT'] == "stm32f4discovery" or os.environ['VARIANT'] == "stm32f334nucleo":
	SCB_CPUID       = getattr(sot_emulator, "t_SCB_CPUID")
	SCB_ICSR        = getattr(sot_emulator, "t_SCB_ICSR")
	SCB_VTOR        = getattr(sot_emulator, "t_SCB_VTOR")

# Power Control (PWR) callback function references for VARIANT boards
if os.environ['VARIANT'] == "stm32f4discovery":
	PWR_CR			= getattr(sot_emulator, "t_PWR_CR")

# FLASH callback function references for VARIANT boards
FLASH_ACR			= getattr(sot_emulator, "t_FLASH_ACR")
FLASH_OPTKEYR		= getattr(sot_emulator, "t_FLASH_KEYR")
FLASH_OPTKEYR		= getattr(sot_emulator, "t_FLASH_OPTKEYR")
FLASH_SR			= getattr(sot_emulator, "t_FLASH_SR")
FLASH_CR			= getattr(sot_emulator, "t_FLASH_CR")

# Reset Clock Control (RCC) callback function references for VARIANT boards
if os.environ['VARIANT'] == "stm32f4discovery":
	RCC_CR          = getattr(sot_emulator, "t_RCC_CR")
RCC_CFGR            = getattr(sot_emulator, "t_RCC_CFGR")
RCC_CIR             = getattr(sot_emulator, "t_RCC_CIR")
RCC_APB1RSTR        = getattr(sot_emulator, "t_RCC_APB1RSTR")
if os.environ['VARIANT'] == "stm32f4discovery":
	RCC_AHB1ENR     = getattr(sot_emulator, "t_RCC_AHB1ENR")
elif os.environ['VARIANT'] == "ellduino" or os.environ['VARIANT'] == "stm32f334nucleo":
	RCC_AHBENR      = getattr(sot_emulator, "t_RCC_AHBENR")
else:
	print "Unknown MCU die.  Please define."
RCC_APB2ENR         = getattr(sot_emulator, "t_RCC_APB2ENR")
RCC_APB1ENR         = getattr(sot_emulator, "t_RCC_APB1ENR")
RCC_APB2RSTR        = getattr(sot_emulator, "t_RCC_APB2RSTR")
RCC_BDCR            = getattr(sot_emulator, "t_RCC_BDCR")
RCC_CSR             = getattr(sot_emulator, "t_RCC_CSR")
RCC_AHBRSTR         = getattr(sot_emulator, "t_RCC_AHBRSTR")
RCC_CFGR2           = getattr(sot_emulator, "t_RCC_CFGR2")
RCC_CFGR3           = getattr(sot_emulator, "t_RCC_CFGR3")
RCC_CR2             = getattr(sot_emulator, "t_RCC_CR2")

# Timers (TIM<num>) callback function references for VARIANT boards
TIM_CR1             = getattr(sot_emulator, "t_TIM_CR1")
TIM_CR2             = getattr(sot_emulator, "t_TIM_CR2")
TIM_SMCR            = getattr(sot_emulator, "t_TIM_SMCR")
TIM_DIER            = getattr(sot_emulator, "t_TIM_DIER")
TIM_CCMR1           = getattr(sot_emulator, "t_TIM_CCMR1")
TIM_CCMR2           = getattr(sot_emulator, "t_TIM_CCMR2")
TIM_CCER            = getattr(sot_emulator, "t_TIM_CCER")
TIM_BDTR            = getattr(sot_emulator, "t_TIM_BDTR")
TIM_PSC             = getattr(sot_emulator, "t_TIM_PSC")
TIM_ARR             = getattr(sot_emulator, "t_TIM_ARR")
TIM_CCR1            = getattr(sot_emulator, "t_TIM_CCR1")
TIM_CCR2            = getattr(sot_emulator, "t_TIM_CCR2")
TIM_CCR3            = getattr(sot_emulator, "t_TIM_CCR3")
TIM_CCR4            = getattr(sot_emulator, "t_TIM_CCR4")
#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# Python callback functions. Binding through ctypes wrapper                                 #
#-------------------------------------------------------------------------------------------#

#Write wrapper functions to bind c callbacks from different registers in VARIANT boards
CB_FUNC_TYPE = CFUNCTYPE(None, c_char_p, c_char_p, c_uint, c_uint, c_char_p)

#Python callback function to be called from different registers in VARIANT boards
def REGISTER_VALUES_CALLBACK(periph, name, value, result, opStr):
	print '{0}:{1}:Value={2} -> {4}{3}'.format(periph, name, hex(value), hex(result), opStr)

# Python callback function reference
python_cb_func = CB_FUNC_TYPE(REGISTER_VALUES_CALLBACK)

#-------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------------------------#
# Utility functions outside library test scripts                                                                          #
#-------------------------------------------------------------------------------------------------------------------------#
#
# General Purpose Input Output (GPIO) functions
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
# General Purpose Input Output (GPIO) port and pins for stm32f4discovery and stm32f334nucleo
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
# General Purpose Input Output (GPIO) port and pins for ellduino
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
# Function to check General Purpose Input Output (GPIO) port validity for variant boards
#
ValidPort = {
   'stm32f4discovery': lambda port: ( port in STM32FXXX_GPIO_PORTS ),
   'stm32f334nucleo':  lambda port: ( port in STM32FXXX_GPIO_PORTS ),
   'ellduino':         lambda port: ( port in ELLDUINO_GPIO_PORTS )
}

#
# Function to check General Purpose Input Output (GPIO) pin validity for variant boards
#
ValidPin = {
   'stm32f4discovery': lambda port, pin: Stm32fxxxValidPin[port](pin),
   'stm32f334nucleo':  lambda port, pin: Stm32fxxxValidPin[port](pin),
   'ellduino':         lambda port, pin: EllduinoValidPin[port](pin)
}

#
# Universal Synchronous Asynchronous Reciever Transmitter (USART) for variant boards
#
Stm32f4discovery_USART = [1, 2]
Stm32f334nucleo_USART  = [1, 2, 3]
Ellduino_USART         = [2, 1]

#
# Function to check Universal Synchronous Asynchronous Reciever Transmitter (USART) validity
# for variant boards
#
ValidUSART = {
	'stm32f4discovery': lambda usart: ( usart in Stm32f4discovery_USART ),
	'stm32f334nucleo':  lambda usart: ( usart in Stm32f334nucleo_USART ),
	'ellduino':         lambda usart: ( usart in Ellduino_USART )
}
#-------------------------------------------------------------------------------------------------------------------------#
