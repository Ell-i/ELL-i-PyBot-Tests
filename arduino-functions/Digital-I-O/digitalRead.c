#include "wiring_digital.h"
#include <Python.h>

static PyObject* readHigh(PyObject* self, PyObject* args) {
	char* pin;
	if (!PyArg_ParseTuple(args, "s", &pin)) {
		return NULL;
  	}

  	int pinNum = atoi(pin);
  	//char high[10];
  	//sprintf(high, "%d", 1);
  	
  	
  	pinMode(pinNum, 3);
  	digitalWrite(pinNum, 1);
  	int high = digitalRead(pinNum);
  	

	return Py_BuildValue("s", high);
}

static PyObject* checkHigh(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkHigh, Python extensions!!");
}

static PyObject* readLow(PyObject* self, PyObject* args) {
	char* pin;
	if (!PyArg_ParseTuple(args, "s", &pin)) {
		return NULL;
  	}

  	int pinNum = atoi(pin);
  	char low[10];
  	sprintf(low, "%d", 0);

	return Py_BuildValue("s", low);
}

static PyObject* checkLow(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkLow, Python extensions!!");
}

static char digitalRead_docs[] = "c-python extention module for Digital Read";

static PyMethodDef digitalRead_methods[] = {
	{"readHigh", (PyCFunction)readHigh, METH_VARARGS, digitalRead_docs},
	{"checkHigh", (PyCFunction)checkHigh, METH_VARARGS, digitalRead_docs},
	{"readLow", (PyCFunction)readLow, METH_VARARGS, digitalRead_docs},
	{"checkLow", (PyCFunction)checkLow, METH_VARARGS, digitalRead_docs},
	{NULL, NULL}
};

void initdigitalRead(void) {
	(void) Py_InitModule3("digitalRead", digitalRead_methods, "Digital Read Extension Module.");
}