#!/bin/sh

#export ELLIRUNTIME="../Runtime"

#############################################################################################
## Setting path variables by users.
#############################################################################################
# Path to ELL-i Runtime
export ELLIRUNTIME=${3}
#"/home/asif/Ell-i-Working-Directory/Ell-i-Software-Development/Runtime"

# Path to 32-bit python installation
#export PATH="/opt/pym32/bin:${PATH}"
export PATH=${4}:${PATH}

#############################################################################################



#############################################################################################
## No user serviceable parts below.
#############################################################################################
export PATH_TO_TESTS=`dirname $_`
export PYTHONPATH=$PATH_TO_TESTS/test-scripts:$PYTHONPATH

run_test() {
	pybot  --outputdir $PATH_TO_TESTS/test-results/$1 $PATH_TO_TESTS/test-cases/$1.rest
}

contains() {
	local flag=false
	TESTS=`ls -1 test-cases/ | grep ".rest" | awk -F '.' '{print $1}'`
	for test in $TESTS; do
		if [ "$1" = "$test" ]; then
			flag=true
		fi
	done
	echo "$flag"
}

if test -z "$1"; then
	command="help"
else
	command=$1
fi

case "$command" in
	list)
	    echo ""
		ls -1 test-cases/|grep ".rest"|awk -F '.' '{print $1}'
	    echo ""
		;;
	help)
		echo ""
		echo "Usage: ./run-tests.sh command [parameter]"
		echo "       ./run-tests.sh testname"
		echo ""
		echo "run-tests.sh is a script to launch emulator based test cases."
		echo ""
		echo "Commands: "
		echo "          list                  List the available test cases"
		echo "          run <test-suite name> Run the particular test case"
		echo "          run-all               Run all the test cases"
		echo "          help                  This help document"
		echo ""
		;;
	run-all)
		echo ""
		TESTS=`ls -1 test-cases/|grep ".rest"|awk -F '.' '{print $1}'`
		for TEST in $TESTS; do
	    	run_test $TEST
		done
		echo ""
		;;
	run)
		echo ""
		if test -z "$2"; then
			echo "Please provide name of the test suite to run e.g."
			echo "./run-tests.sh run <test-suite name>"
		else 
			TESTS=`ls -1 test-cases/ | grep ".rest" | awk -F '.' '{print $1}'`
			testAvailable=false
			testAvailable=`contains $2` 
			if test $testAvailable = "true"; then
				run_test $2
			elif test $testAvailable = "false"; then
				echo "Test name is wrong. Available tests are:"
				echo ""
				ls -1 test-cases/|grep ".rest"|awk -F '.' '{print $1}'
	    	else
	    		echo "Shell script unknown error"
	    	fi
		fi		
		echo ""
		;;
	*)
		echo ""
		echo "Wrong command. Please use the following commands;"
		echo "Commands: "
		echo "          list                  List the available test cases"
		echo "          run <test-suite name> Run the particular test case"
		echo "          run-all               Run all the test cases"
		echo "          help                  This help document"
		echo ""
		;;
    #run_test $1
	#;;
esac
#############################################################################################