#!/opt/pym32/bin/python

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
def msbFirst(slaveSelectPin):
	emulator.setBitOrder(c_ubyte(slaveSelectPin).value, SPIBitOrder['MSBFIRST']);
def lsbFirst(slaveSelectPin):
	emulator.setBitOrder(c_ubyte(slaveSelectPin).value, SPIBitOrder['LSBFIRST']);
setBitOrder = {
	0: msbFirst, 
	1: lsbFirst
};

def spiClockDiv2(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV2']);
def spiClockDiv4(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV4']);
def spiClockDiv8(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV8']);
def spiClockDiv16(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV16']);
def spiClockDiv32(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV32']);
def spiClockDiv64(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV64']);
def spiClockDiv128(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV128']);
def spiClockDiv256(slaveSelectPin):
	emulator.setClockDivider(c_ubyte(slaveSelectPin).value, SPIClockDivider['SPI_CLOCK_DIV256']);
setClockDivider = {
	2: spiClockDiv2, 
	4: spiClockDiv4, 
	8: spiClockDiv8, 
	16: spiClockDiv16, 
	32: spiClockDiv32, 
	64: spiClockDiv64, 
	128: spiClockDiv128, 
	256: spiClockDiv256
};

def spiMode0(slaveSelectPin):
	emulator.setDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE0']);
def spiMode1(slaveSelectPin):
	emulator.setDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE1']);
def spiMode2(slaveSelectPin):
	emulator.setDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE2']);
def spiMode3(slaveSelectPin):
	emulator.setDataMode(c_ubyte(slaveSelectPin).value, SPIDataMode['SPI_MODE3']);
setDataMode = {
	0: spiMode0,
	1: spiMode1,
	2: spiMode2,
	3: spiMode3
};
#-------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------#
#Test Library Functions
#-------------------------------------------------------------------------------------------------------#
def begin_spi(slaveSelectPin):
	"""Begin the SPI port"""
	emulator.begin(c_ubyte(slaveSelectPin).value);

def end_spi(slaveSelectPin):
	"""End the SPI port"""
	emulator.end(c_ubyte(slaveSelectPin).value);

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
	emulator.transfer(c_ubyte(slaveSelectPin).value, value);
#-------------------------------------------------------------------------------------------------------#

"""
TEST CASES END
"""