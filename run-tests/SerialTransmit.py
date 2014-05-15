#!/usr/bin/python

import os
from subprocess import call


TESTNAME='Serial'
TESTPATH=os.environ['HOME']+'/Ell-i/Ell-i-Pybot/ELL-i-PyBot-Tests/test-scripts/'

print TESTPATH

call(
	'pybot'+
	' --variable TESTPATH:'+TESTPATH+ 
	' --log ../test-results/'+TESTNAME+'/log.html'+ 
	' --report ../test-results/'+TESTNAME+'/report.html'+ 
	' --output ../test-results/'+TESTNAME+'/output.xml'+ 
	' ../test-suites/ELL-i-PyBot-Tests.wiki/'+TESTNAME+'.rest',
	shell=True
	)