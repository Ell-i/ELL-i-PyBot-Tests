#!/bin/sh

#------------------------------------------------------------------------------------------------------------#
# Setting path variables by users.
#------------------------------------------------------------------------------------------------------------#
#Command-line argument as <emulator> or <hardware>
export PLATFORM=${1}

#Command-line argument as <variant>
export VARIANT=${2}

# Path to ELL-i Runtime
export ELLIRUNTIME=${3}

#------------------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------------------#
# No user serviceable parts below.
#------------------------------------------------------------------------------------------------------------#
export PATH_TO_TESTS=`dirname $_`

#:${ELLIRUNTIME}/tests/robot_library/${PLATFORM}/${VARIANT}/pythonCallback.so
run_test() {
	pybot  --pythonpath test-scripts/${PLATFORM}:${ELLIRUNTIME}/stm32/tests/robot_library/${PLATFORM}/${VARIANT} \
	--outputdir $PATH_TO_TESTS/test-results/${PLATFORM}/${VARIANT}/$1 \
	$PATH_TO_TESTS/test-cases/${PLATFORM}/$1.rest
}

contains() {
	local flag=false
	TESTS=`ls -1 test-cases/${PLATFORM}/ | grep ".rest" | awk -F '.' '{print $1}'`
	for test in $TESTS; do
		if [ "$1" = "$test" ]; then
			flag=true
		fi
	done
	echo "$flag"
}

if test -z "${4}"; then
	command="help"
else
	command=${4}
fi

case "$command" in
	list)
	    echo ""
		ls -1 test-cases/${PLATFORM}/ | grep ".rest"|awk -F '.' '{print $1}'
	    echo ""
		;;
	help)
		echo ""
		echo "Usage: ./run-tests.sh <PLATFORM> <VARIANT> <path/to/elli-runtime>"\
		     "<COMMAND> [parameter]"
		echo "e.g. ./run-tests.sh emulator ellduino"\
			 "/home/asif/Ell-i-Working-Directory/Ell-i-Software-Development/Runtime/"\
			 "run DigitalWrite"
		echo ""
		echo "run-tests.sh is a script to launch emulator or hardware based test cases."
		echo ""
		echo "Commands: "
		echo "          <COMMAND>  [parameter]        Description"
		echo "          list                          List the available test cases"
		echo "          run        [test-suite name]  Run the particular test case"
		echo "          run-all                       Run all the test cases"
		echo "          help                          This help document"
		echo ""
		;;
	run-all)
		echo ""
		TESTS=`ls -1 test-cases/${PLATFORM}/ | grep ".rest"|awk -F '.' '{print $1}'`
		for TEST in $TESTS; do
	    	run_test $TEST
		done
		echo ""
		;;
	run)
		echo ""
		if test -z "${5}"; then
			echo "Please provide name of the test suite to run e.g."
			echo "./run-tests.sh run <test-suite name>"
		else
			TESTS=`ls -1 test-cases/${PLATFORM}/ | grep ".rest" | awk -F '.' '{print $1}'`
			testAvailable=false
			testAvailable=`contains ${5}`
			if test $testAvailable = "true"; then
				run_test ${5}
			elif test $testAvailable = "false"; then
				echo "Test name is wrong. Available tests are:"
				echo ""
				ls -1 test-cases/${PLATFORM}/ | grep ".rest"|awk -F '.' '{print $1}'
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
		echo "          <COMMAND>  [parameter]        Description"
		echo "          list                          List the available test cases"
		echo "          run        [test-suite name]  Run the particular test case"
		echo "          run-all                       Run all the test cases"
		echo "          help                          This help document"
		echo ""
		;;
esac
#------------------------------------------------------------------------------------------------------------#
