#!/usr/bin/python

from subprocess import call

TESTNAME='PinMode'

call(
	'pybot'+
	' --outputdir ../test-results/'+TESTNAME+ 
	' ../test-suites/ELL-i-PyBot-Tests.wiki/'+TESTNAME+'.rest',
	shell=True
	)