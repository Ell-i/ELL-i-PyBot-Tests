"""
TEST CASES START
"""

import digitalWrite

def write_high(pin, value):
    """Write 'HIGH' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    print digitalWrite.writeHigh(pin, value);

def check_high(pin, value):
    """Check 'HIGH' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for checking input value from pin.'

"""
**********************************************************************************************************************************
"""

def write_low(pin, value):
    """Write 'LOW' to pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for writing value to pin.'
    print digitalWrite.writeLow(pin, value);

def check_low(pin, value):
   """Check 'LOW' from pin"""
   #print 'Here it uses test library to interact with Ell-i runtime C code for checking input value from pin.'

"""
TEST CASES END
"""
