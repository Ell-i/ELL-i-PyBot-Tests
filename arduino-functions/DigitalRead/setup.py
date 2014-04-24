from distutils.core import setup, Extension
setup(name='digitalRead', version='1.0',  \
      ext_modules=[Extension('digitalRead', ['digitalRead.c'])])