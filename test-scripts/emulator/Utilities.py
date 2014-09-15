
#The utilities module is useful for declaring datatypes, functions or classes to be
#used by the test library scripts.

from ctypes import *
import subprocess
import os

from STM_constants import *

DLLPATH = os.environ['ELLIRUNTIME']+"/tests/robot_library/emulator/ellduino/"
#############################################################################################

# Load the emulator shared library.
sot_emulator = CDLL(DLLPATH + "librobot_library.so")

pinMode       = getattr(sot_emulator, "t_pinMode")
digitalRead   = getattr(sot_emulator, "t_digitalRead")
digitalWrite  = getattr(sot_emulator, "t_digitalWrite")

#############################################################################################
