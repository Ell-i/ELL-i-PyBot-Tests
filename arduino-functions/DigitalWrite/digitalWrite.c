#include <Python.h>

static PyObject* writeHigh(PyObject* self, PyObject* args) {
	char* pin;
	char* high;
	if (!PyArg_ParseTuple(args, "ss", &pin, &high)) {
		return NULL;
  	}

  	int pinNum = atoi(pin);
  	int highValue = atoi(high);
  	
  	/*
  	pinMode(pinNum, INPUT);
  	digitalWrite(pinNum, highValue);
  	*/

	return Py_BuildValue("ii", pinNum, highValue);
}

static PyObject* checkHigh(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkHigh, Python extensions!!");
}

static PyObject* writeLow(PyObject* self, PyObject* args) {
	char* pin;
	char* low;
	if (!PyArg_ParseTuple(args, "ss", &pin, &low)) {
		return NULL;
  	}

  	int pinNum = atoi(pin);
  	int lowValue = atoi(low);
  	
  	/*
  	pinMode(pinNum, INPUT);
  	digitalWrite(pinNum, highValue);
  	*/

	return Py_BuildValue("ii", pinNum, lowValue);
}

static PyObject* checkLow(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkLow, Python extensions!!");
}

static char digitalWrite_docs[] = "c-python extention module for Digital Write";

static PyMethodDef digitalWrite_methods[] = {
	{"writeHigh", (PyCFunction)writeHigh, METH_VARARGS, digitalWrite_docs},
	{"checkHigh", (PyCFunction)checkHigh, METH_VARARGS, digitalWrite_docs},
	{"writeLow", (PyCFunction)writeLow, METH_VARARGS, digitalWrite_docs},
	{"checkLow", (PyCFunction)checkLow, METH_VARARGS, digitalWrite_docs},
	{NULL, NULL}
};

void initdigitalWrite(void) {
	(void) Py_InitModule3("digitalWrite", digitalWrite_methods, "Digital Write Extension Module.");
}