#!/bin/sh

#export ELLIRUNTIME="../Runtime"

#############################################################################################
## Setting path variables by users.
#############################################################################################

#Command-line argument as <emulator> or <hardware>
PLATFORM=${1}

# Path to ELL-i Runtime
export ELLIRUNTIME=${2}

# Path to 32-bit python installation
export PATH=${3}:${PATH}


#############################################################################################



#############################################################################################
## No user serviceable parts below.
#############################################################################################

export PATH_TO_TESTS=`dirname $_`

run_test() {
	pybot  --pythonpath test-scripts/${PLATFORM} \
	--outputdir $PATH_TO_TESTS/test-results/${PLATFORM}/$1 \
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

if test -z "$4"; then
	command="help"
else
	command=$4
fi

case "$command" in
	list)
	    echo ""
		ls -1 test-cases/|grep ".rest"|awk -F '.' '{print $1}'
	    echo ""
		;;
	help)
		echo ""
		echo "Usage: ./run-tests.sh <PLATFORM> <path/to/elli-runtime> <path/to/python-and-pybot-binaries> <COMMAND> [parameter]"
		echo "       e.g. ./run-tests.sh emulator /home/asif/Ell-i-Working-Directory/Ell-i-Software-Development/Runtime/ /opt/pym32/bin/ run DigitalWrite"
		echo ""
		echo "run-tests.sh is a script to launch emulator or hardware based test cases."
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
		if test -z "$5"; then
			echo "Please provide name of the test suite to run e.g."
			echo "./run-tests.sh run <test-suite name>"
		else 
			TESTS=`ls -1 test-cases/ | grep ".rest" | awk -F '.' '{print $1}'`
			testAvailable=false
			testAvailable=`contains $5` 
			if test $testAvailable = "true"; then
				run_test $5
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
esac

#############################################################################################