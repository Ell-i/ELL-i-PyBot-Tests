"""
TEST CASES START
"""

import pinMode

def input_pin_mode(pin, mode):
    """Logs setting of input pin mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for setting input pin mode for the corresponding pin.'
    print pinMode.inputPinMode(pin, mode);

def check_input_mode(pin, mode):
    """Logs checking of input pin mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for checking input pin mode for the corresponding pin.'

"""
**********************************************************************************************************************************
"""

def output_pin_mode(pin, mode):
    """Logs setting of output pin mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for setting output pin mode for the corresponding pin.'
    print pinMode.outputPinMode(pin, mode);
    
def check_output_mode(pin, mode):
    """Logs checking of output pin mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for checking output pin mode for the corresponding pin.'

"""
**********************************************************************************************************************************
"""

def input_pullup_mode(pin, mode):
    """Logs setting of input pin pullup mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for setting input pin pullup mode for the corresponding pin.'
    print pinMode.inputPullupMode(pin, mode);

def check_pullup_mode(pin, mode):
    """Logs checking of input pin pullup mode"""
    #print 'Here it uses test library to interact with Ell-i runtime C code for checking input pin pullup mode for the corresponding pin.'

"""
TEST CASES END
"""
