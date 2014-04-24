from distutils.core import setup, Extension
setup(name='digitalRead', version='1.0', ext_modules=[Extension('digitalRead', ['DigitalRead/digitalRead.c'])])
setup(name='digitalWrite', version='1.0', ext_modules=[Extension('digitalWrite', ['DigitalWrite/digitalWrite.c'])])