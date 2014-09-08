
"""
TEST CASES START
"""

from Utilities import *

#Load the emulator shared library. Call the c-functions directly from 
#the python script using ctypes modules.
emulator = CDLL(DLLPATH + "libemulator.so")

#Make the test cases fail, if not implemented yet -> read RF guide 

def set_pin_mode(pin):
    """Set the pin mode to output"""

def write_high(pin, high):
    """Write 'HIGH' to pin"""
    print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'

def note_time():
    """Note time till 10 seconds"""
    print 'Here it uses test library to interact with Ell-i runtime C code to note time till 10 seconds.'

def write_low(pin, low):
    """Write 'LOW' to pin"""
    print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'

"""
TEST CASES END
"""
