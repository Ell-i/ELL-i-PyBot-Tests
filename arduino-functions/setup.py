from distutils.core import setup, Extension
setup(name='digitalRead', version='1.0', ext_modules=[Extension('digitalRead', ['Digital-I-O/digitalRead.c'])])
setup(name='digitalWrite', version='1.0', ext_modules=[Extension('digitalWrite', ['Digital-I-O/digitalWrite.c'])])
setup(name='pinMode', version='1.0', ext_modules=[Extension('pinMode', ['Digital-I-O/pinMode.c'])])
