#!/usr/bin/python

from os import path
from distutils.core import setup, Extension

runtime='/home/asif/Ell-i/Ell-i-March-2014/Runtime/stm32'

arduelli=path.join(runtime,'cores/arduelli')
system_inc=path.join(runtime, 'system/stm32/inc')
cmsis=path.join(runtime, 'system/stm32/CMSIS/Include')
variant=path.join(runtime, 'variants/ellduino')

include_direcs = [arduelli, system_inc, cmsis, variant]

setup(name='digitalRead', version='1.0', ext_modules=[Extension('digitalRead', ['Digital-I-O/digitalRead.c'], include_dirs=include_direcs)])
setup(name='digitalWrite', version='1.0', ext_modules=[Extension('digitalWrite', ['Digital-I-O/digitalWrite.c'], include_dirs=include_direcs)])
setup(name='pinMode', version='1.0', ext_modules=[Extension('pinMode', ['Digital-I-O/pinMode.c'], include_dirs=include_direcs)])

