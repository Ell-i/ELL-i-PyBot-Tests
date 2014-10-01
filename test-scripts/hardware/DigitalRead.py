
"""
TEST CASES START
"""

import re
from Utilities import *

CURRENTPATH = os.getcwd();

def compile_flash_code(setupFlag):
    try:
        if setupFlag == "High":
            compile_ = compile(TESTPATH, DigitalReadHigh);
        elif setupFlag == "Low":
            compile_ = compile(TESTPATH, DigitalReadLow);
        else:
            print "Wrong setup flag parameter!"

        if compile_ != True:
            raise RuntimeError, "Compiling the source code failed!"
    except RuntimeError, arg:
        print arg;
    else:
        print "Source code compiled! HEX file created!"

def read_high():
    flash_ = flash(TESTPATH, DigitalReadHigh);
    if flash_ != True:
        raise RuntimeError, "Flashing the device failed!"

    os.chdir(CURRENTPATH);

    sigrok_ = call_sigrok('1');
    if sigrok_ != True:
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

def read_low():
    flash_ = flash(TESTPATH, DigitalReadLow);
    if flash_ != True:
        raise RuntimeError, "Flashing the device failed!"

    os.chdir(CURRENTPATH);

    sigrok_ = call_sigrok('1');
    if sigrok_ != True:
        raise RuntimeError, "Call to sigrok to dump output from device failed!"

    try:
        fo = open("sigrok-output", "r");
        dataLines = fo.readlines();
        testLine = dataLines[2][2:];
        test_output = re.compile('[0-1]');
        str = re.search(test_output, testLine);
        assert (str.group() == '0'), "High at pin!"
    except IOError, arg:
        print arg;
        raise RuntimeError, "Couldn't find/read file!"
    except AssertionError, arg:
        print arg;
        raise RuntimeError, "Test case failed. The value is not low at pin!"
    except RuntimeError, arg:
        print arg;
    else:
        print "Test case passed. The value is low at pin!"

def clean_code(teardownFlag):
    if teardownFlag == "High":
        os.chdir(TESTPATH + DigitalReadHigh + "/");
    elif teardownFlag == "Low":
        os.chdir(TESTPATH + DigitalReadLow + "/");
    else:
        print "Wrong teardown flag!"

    try:
        args = shlex.split("'make clean'");
        p = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE);
        output, error = p.communicate();
        if p.returncode != 0:
            raise RuntimeError, error;
    except RuntimeError, arg:
        print arg;
        print "Make clean failed!"
    else:
        print "Make clean completed!"



"""
TEST CASES END
"""
