"""
TEST CASES START
"""

import digitalRead

#print digitalRead.readHigh()

def read_high(pin):
    """Read 'HIGH' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    return digitalRead.readHigh(pin)

def check_high(pin, high):
    """Check 'HIGH' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for checking input value from pin.'

"""
**********************************************************************************************************************************
"""

def read_low(pin):
    """Read 'LOW' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for reading input value from pin.'
    #"""Also returns value for pin"""
    return digitalRead.readLow(pin)

def check_low(pin, low):
    """Check 'LOW' from pin"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for checking input value from pin.'

"""
TEST CASES END
"""
