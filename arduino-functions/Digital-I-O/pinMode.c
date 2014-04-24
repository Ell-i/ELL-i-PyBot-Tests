#include <Python.h>

static PyObject* inputPinMode(PyObject* self, PyObject* args) {
	char* pin;
	char* mode;
	if (!PyArg_ParseTuple(args, "ss", &pin, &mode)) {
		return NULL;
	}

	int pinNumber = atoi(pin);
	int pinMode = atoi(mode);

	return Py_BuildValue("ii", pinNumber, pinMode);
}

static PyObject* checkInputMode(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkInputMode, Python extensions!!");
}

static PyObject* outputPinMode(PyObject* self, PyObject* args) {
	char* pin;
	char* mode;
	if (!PyArg_ParseTuple(args, "ss", &pin, &mode)) {
		return NULL;
	}

	int pinNumber = atoi(pin);
	int pinMode = atoi(mode);

	return Py_BuildValue("ii", pinNumber, pinMode);
}

static PyObject* checkOutputMode(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkOutputMode, Python extensions!!");
}

static PyObject* inputPullupMode(PyObject* self, PyObject* args) {
	char* pin;
	char* mode;
	if (!PyArg_ParseTuple(args, "ss", &pin, &mode)) {
		return NULL;
	}

	int pinNumber = atoi(pin);
	int pinMode = atoi(mode);

	return Py_BuildValue("ii", pinNumber, pinMode);
}

static PyObject* checkPullupMode(PyObject* self, PyObject* args) {
	return Py_BuildValue("s", "checkPullupMode, Python extensions!!");
}

static char pinMode_docs[] = "c-python extension module for pin mode";

static PyMethodDef pinMode_Methods[] = {
	{"inputPinMode", (PyCFunction)inputPinMode, METH_VARARGS, pinMode_docs},
	{"checkInputMode", (PyCFunction)checkInputMode, METH_VARARGS, pinMode_docs},
	{"outputPinMode", (PyCFunction)outputPinMode, METH_VARARGS, pinMode_docs},
	{"checkOutputMode", (PyCFunction)checkOutputMode, METH_VARARGS, pinMode_docs},
	{"inputPullupMode", (PyCFunction)inputPullupMode, METH_VARARGS, pinMode_docs},
	{"checkPullupMode", (PyCFunction)checkPullupMode, METH_VARARGS, pinMode_docs},
	{NULL, NULL}
};

void initpinMode(void) {
	(void) Py_InitModule3("pinMode", pinMode_Methods, "Pin Mode Extension Module.");
}