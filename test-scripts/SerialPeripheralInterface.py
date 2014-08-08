
"""
TEST CASES START
"""

from Utilities import *

#Load the emulator shared library. Call the c-functions directly from 
#the python script using ctypes modules.
emulator = CDLL(DLLPATH + "libemulator.so")

#-------------------------------------------------------------------------------------------------------#
#Utility functions outside library test functions
#-------------------------------------------------------------------------------------------------------#

setBitOrder = {
	0: lambda slaveSelectPin: emulator.spiSetBitOrder(c_ubyte(slaveSelectPin).value, SPIBitOrder['MSBFIRST']), 
	1: lambda slaveSelectPin: emulator.spiSetBitOrder(c_ubyte(slaveSelectPin).value, SPIBitOrder['LSBFIRST'])
};

setClockDivider = {
	2:   lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV2']),
	4:   lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV4']),
	8:   lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV8']),
	16:  lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV16']),
	32:  lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV32']),
	64:  lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV64']),
	128: lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV128']),
	256: lambda slaveSelectPin: emulator.spiSetClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV256'])
};

setDataMode = {
	0: lambda slaveSelectPin: emulator.spiSetDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE0']),
	1: lambda slaveSelectPin: emulator.spiSetDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE1']),
	2: lambda slaveSelectPin: emulator.spiSetDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE2']),
	3: lambda slaveSelectPin: emulator.spiSetDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE3'])
};
#-------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------#
#Test Library Functions
#-------------------------------------------------------------------------------------------------------#
def begin_spi(slaveSelectPin):
	"""Begin the SPI port"""
	emulator.spiBegin(c_ubyte(slaveSelectPin).value);

def end_spi(slaveSelectPin):
	"""End the SPI port"""
	emulator.spiEnd(c_ubyte(slaveSelectPin).value);

def bit_order(slaveSelectPin, bitOrder):
	"""Sets the bit order to LSB or MSB"""
	setBitOrder[bitOrder](slaveSelectPin);

def clock_divider(slaveSelectPin, clockDiv):
	"""Sets the clock divider to 2, 4, 8, 16, 32, 64 or 128"""
	setClockDivider[clockDiv](slaveSelectPin);

def data_mode(slaveSelectPin, dataMode):
	""""Sets the data mode to 0, 1, 2 or 3"""
	setDataMode[dataMode](slaveSelectPin);

def transfer_value(slaveSelectPin, value):
	"""Transfer the value from SPI port using the MOSI pin"""
	emulator.spiTransfer(c_ubyte(slaveSelectPin).value, value);
#-------------------------------------------------------------------------------------------------------#

"""
TEST CASES END
"""
