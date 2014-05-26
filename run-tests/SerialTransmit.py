#!/usr/bin/python

import os
from subprocess import call


TESTNAME='SerialTransmit'
TESTPATH=os.environ['HOME']+'/Ell-i/Ell-i-Pybot/ELL-i-PyBot-Tests/test-scripts/'

print TESTPATH

call(
	'pybot'+
	' --variable TESTPATH:'+TESTPATH+ 
	' --outputdir ../test-results/'+TESTNAME+ 
	' ../test-suites/ELL-i-PyBot-Tests.wiki/'+TESTNAME+'.rest',
	shell=True
	)