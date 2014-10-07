"""
TEST CASES START
"""

from Utilities import *

def set_pin_mode(port, pin):
    """Set the pin mode to output"""
    try:
        PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
        if PinPortVal == False:
            raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
    except RuntimeError, arg:
        print arg
    else:
        VariantPinMode[ os.environ['VARIANT'] ](port, pin, 'OUTPUT')
        GPIO_PUPDR(port, python_cb_func)
        GPIO_MODER(port, python_cb_func)
        print "Pin mode set to OUTPUT"

def read_high(port, pin):
    """Read high from pin"""
    try:
        PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
        if PinPortVal == False:
            raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
    except RuntimeError, arg:
        print arg;
        return False
    else:
        VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'OUTPUT')
        VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'HIGH')
        GPIO_BSRR(port, python_cb_func)
        GPIO_BRR(port, python_cb_func)
        GPIO_IDR(port, python_cb_func)
        VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'INPUT')

        high = c_bool(0)
        high.value = VariantDigitalRead[ os.environ['VARIANT'] ](port, pin)

    if high.value > 0:
        print "Pin value read is high"
        return True
    else:
        return False

def read_low(port, pin):
    """Read low from pin"""
    try:
        PinPortVal = ValidPort[ os.environ['VARIANT'] ](port) and ValidPin[ os.environ['VARIANT'] ](port, pin)
        if PinPortVal == False:
            raise RuntimeError, "Wrong pin and/or port. Please check the port and pin value!"
    except RuntimeError, arg:
        print arg;
        return False
    else:
        VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'OUTPUT')
        VariantDigitalWrite[ os.environ['VARIANT'] ](port, pin, 'LOW')
        GPIO_BSRR(port, python_cb_func)
        GPIO_BRR(port, python_cb_func)
        GPIO_IDR(port, python_cb_func)
        VariantPinMode[      os.environ['VARIANT'] ](port, pin, 'INPUT')
        low = c_bool(1);
        low.value = VariantDigitalRead[ os.environ['VARIANT'] ](port, pin)

    if high.value > 0:
        print "Pin value read is high"
        return True
    else:
        return False

"""
TEST CASES END
"""
