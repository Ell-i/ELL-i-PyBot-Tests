#-------------------------------------------------------------------------------------------#
# The following values are taken from arduelli_gpio.h for Arduino API compatibility.        #
# Such declarations are more readable in test library scripts.                              #
#-------------------------------------------------------------------------------------------#

from ctypes import *

# XXX TODO: Autogenerate these Python definitions from C code.

zero  = c_uint(0)
one   = c_uint(1)
two   = c_uint(2)
three = c_uint(3)

PinMode = {
    'INPUT': zero.value,
    'INPUT_PULLUP': one.value,
    'INPUT_PULLDOWN': two.value,
    'OUTPUT': three.value
    }

high = c_uint(1)
low  = c_uint(0)
PinValue = {
    'HIGH': high.value,
    'LOW': low.value
    }

SPITransferMode = {
    'SPI_CONTINUE': zero.value,
    'SPI_LAST': one.value
    }

SPI_CR1_LSBFIRST = 0x0080;
SPIBitOrder = {
    'MSBFIRST': c_ushort(~SPI_CR1_LSBFIRST).value,
    'LSBFIRST': c_ushort(SPI_CR1_LSBFIRST).value
}

SPI_CR1_BR_0 = 0x0008
SPI_CR1_BR_1 = 0x0010
SPI_CR1_BR_2 = 0x0020
SPIClockDivider = {
    'SPI_CLOCK_DIV2':   c_ushort(~SPI_CR1_BR_2 | ~SPI_CR1_BR_1 | ~SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV4':   c_ushort(~SPI_CR1_BR_2 | ~SPI_CR1_BR_1 |  SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV8':   c_ushort(~SPI_CR1_BR_2 |  SPI_CR1_BR_1 | ~SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV16':  c_ushort(~SPI_CR1_BR_2 |  SPI_CR1_BR_1 |  SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV32':  c_ushort(SPI_CR1_BR_2  | ~SPI_CR1_BR_1 | ~SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV64':  c_ushort(SPI_CR1_BR_2  | ~SPI_CR1_BR_1 |  SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV128': c_ushort(SPI_CR1_BR_2  |  SPI_CR1_BR_1 | ~SPI_CR1_BR_0).value,
    'SPI_CLOCK_DIV256': c_ushort(SPI_CR1_BR_2  |  SPI_CR1_BR_1 |  SPI_CR1_BR_0).value
}

SPI_CR1_CPHA = 0x0001
SPI_CR1_CPOL = 0x0002
SPIDataMode = {
    'SPI_MODE0': c_ushort(~SPI_CR1_CPHA | ~SPI_CR1_CPOL).value,
    'SPI_MODE1': c_ushort(SPI_CR1_CPHA  | ~SPI_CR1_CPOL).value,
    'SPI_MODE2': c_ushort(~SPI_CR1_CPHA |  SPI_CR1_CPOL).value,
    'SPI_MODE3': c_ushort(SPI_CR1_CPHA  |  SPI_CR1_CPOL).value
}
#-------------------------------------------------------------------------------------------#
