#!/opt/pym32/bin/python

import os
from subprocess import call


TESTNAME='DigitalRead'
TESTPATH=os.environ['HOME']+'/Ell-i-Working-Directory/Ell-i-Software-Testing/ELL-i-PyBot-Tests/test-scripts/'

print TESTPATH

call(
	'pybot'+
	' --variable TESTPATH:'+TESTPATH+ 
	' --outputdir ../test-results/'+TESTNAME+
	' ../test-suites/ELL-i-PyBot-Tests.wiki/'+TESTNAME+'.rest',
	shell=True
	)
