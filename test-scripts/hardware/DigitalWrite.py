
"""
TEST CASES START
"""

import re
from Utilities import *
import subprocess
import shlex
from subprocess import call
from subprocess import check_call
from subprocess import check_output

#Load the emulator shared library. Call the c-functions directly from 
#the python script using ctypes modules.
#emulator = CDLL(DLLPATH + "libemulator.so")

#import digitalWrite

def set_pin_mode(port, pin):
    print "emulator.pinMode(GPIO[port][pin], PinMode['OUTPUT'])"

def write_high(port, pin):
    CURRENTPATH = os.getcwd();
    os.chdir(TESTPATH + DigitalWrite + "/");
    
    compile = _compile();
    if compile != True:
        raise RuntimeError, "Compiling the source code failed!"
    
    flash = _flash();
    if flash != True:
        raise RuntimeError, "Flashing the device failed!"
    
    os.chdir(CURRENTPATH);
    
    sigrok = _call_sigrok();
    if sigrok != True:
        raise RuntimeError, "Call to sigrok to dump output from device failed!"        
    
    try:
        fo = open("sigrok-output", "r");
        dataLines = fo.readlines();
        testLine = dataLines[2][2:];
        test_output = re.compile('[0-1]');
        str = re.search(test_output, testLine);
        assert (str.group() == '1'), "Low at pin!"
    except IOError, arg:
        print arg;
        raise RuntimeError, "Couldn't find/read file!"
    except AssertionError, arg:
        print arg;
        raise RuntimeError, "Test case failed. The value is not high at pin!"
    except RuntimeError, arg:
        print arg;
    else:
        print "Test case passed. The value is high at pin!"

def write_low(port, pin):
    print "emulator.digitalWrite(GPIO[port][pin], PinValue['LOW'])"

"""
TEST CASES END
"""
##########################################################################################################



##########################################################################################################
#                             Helper Methods Below                                                       #
##########################################################################################################
def _compile():
    args = shlex.split("make -s PLATFORM=hardware");    
    try:
        p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        arg = p.communicate();
        if p.returncode != 0:
            raise RuntimeError, arg;
    except OSError, log:
        print log;
        return False;
    except subprocess.CalledProcessError, arg:
        print arg;
        return false;
    except RuntimeError, arg:
        print arg;
        return False;
    else:
        print "Source code compiled! HEX file created!"
        return True;
    
def _flash():
    args = shlex.split("'/usr/bin/python ./../../../../Tools/stm32flasher/stm32flash.py \
            -w ./hardware/ellduino/test_digitalWrite.hex \
            -A 0x00000000 \
            /dev/ttyUSB0'");
    try:
        p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        arg = p.communicate();
        if p.returncode != 0:
            raise RuntimeError, arg;
    except OSError, log:
        print log;
        return False;
    except subprocess.CalledProcessError, arg:
        print arg;
        return false;
    except RuntimeError, arg:
        print arg;
        return False;
    else:
        print "Flashing hex file to device complete!"
        return True;
    
def _call_sigrok():
    args = shlex.split("sigrok-cli --driver fx2lafw \
        --samples 1 \
        --channels 0 \
        --output-format bits \
        --output-file sigrok-output");

    try:
        p = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        arg = p.communicate();
        if p.returncode != 0:
            raise RuntimeError, arg;
    except OSError, log:
        print log;
        return False;
    except subprocess.CalledProcessError, arg:
        print arg;
        return false;
    except RuntimeError, arg:
        print arg;
        return False;
    else:
        print "Call to sigrok to dump output from device complete!"
        return True;
##########################################################################################################
