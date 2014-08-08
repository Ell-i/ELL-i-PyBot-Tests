#!/bin/sh

## Path to ELL-i Runtime
export ELLIRUNTIME="../Runtime"



##############################################################################
## No user serviceable parts below.
##############################################################################

export PATH_TO_TESTS=`dirname $_`
export PYTHONPATH=$PATH_TO_TESTS/test-scripts:$PYTHONPATH

run_test() {
    pybot  --outputdir $PATH_TO_TESTS/test-results/$1 $PATH_TO_TESTS/testcases/$1.rest
}

if test -z "$1"; then
    command="help"
else
    command=$1
fi

case "$command" in
  list)
        ls -1 testcases/|grep ".rest"|awk -F '.' '{print $1}'
        ;;
  help)
        echo "Usage: ./run-tests.sh command [parameter]"
        echo "       ./run-tests.sh testname"
	echo ""
	echo "run-tests.sh is a script to launch emulator based test cases."
	echo ""
	echo "Commands: "
	echo "          list           List the available test cases"
	echo "          run <testcase> Run the particular test case"
	echo "          run-all        Run all the test cases"
	echo "          help           This help document"
        ;;
  run-all)
	TESTS=`ls -1 testcases/|grep ".rest"|awk -F '.' '{print $1}'`
	for TEST in $TESTS; do
	    run_test $TEST
	done
	;;
  run)
	run_test $2
	;;
  *)
	run_test $1
	;;
esac
