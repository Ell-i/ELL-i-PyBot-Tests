//#include any header files required for serial port ...
#include <Python.h>

static PyObject* beginSerial(PyObject* self, PyObject* args) {
	long baudRate;

	if (!PyArg_ParseTuple(args, "l", &baudRate)) {
		return NULL;
  	}

  	//Call the serial.begin() function with the baudRate as a parameter

}

static PyObject* endSerial(PyObject* self) {	
	//Call the serial.end() function
}

static PyObject* writeByte(PyObject* self, PyObject* args) {
	char byt;
	if (!PyArg_ParseTuple(args, "c", &byt)) {
		return NULL;
  	}

  	//Call the serial.write() function with 1 byte as parameter

}

static PyObject* writeBytes(PyObject* self, PyObject* args) {
	char* byts;
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Call the serial.write() function with string of several bytes as parameter

}

static PyObject* writeBuffer(PyObject* self, PyObject* args) {
	/// refer to the python C API for -> working with sequences ... 
}

static PyObject* getWrittenBytes(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printInt(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printFloat(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printChar(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}	
}

static PyObject* printString(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* getPrintBytes(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printlnDec(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printlnHex(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printlnOct(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* printlnBin(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static PyObject* getPrintlnBytes(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}
}

static char serialCommunication_docs[] = "c-python extention module for serial communication";

static PyMethodDef serialCommunication_methods[] = {
	{"beginSerial", (PyCFunction) beginSerial, METH_VARARGS, serialCommunication_docs},
	{"endSerial",   (PyCFunction) endSerial,   METH_NOARGS,  serialCommunication_docs},	
	
	{"writeByte",       (PyCFunction) writeByte,       METH_VARARGS, serialCommunication_docs},
	{"writeBytes",      (PyCFunction) writeBytes,      METH_VARARGS, serialCommunication_docs},
	{"writeBuffer",     (PyCFunction) writeBuffer,     METH_VARARGS, serialCommunication_docs},
	{"getWrittenBytes", (PyCFunction) getWrittenBytes, METH_VARARGS, serialCommunication_docs},

	{"printInt",      (PyCFunction) printInt,      METH_VARARGS, serialCommunication_docs},
	{"printFloat",    (PyCFunction) printFloat,    METH_VARARGS, serialCommunication_docs},
	{"printChar",     (PyCFunction) printChar,     METH_VARARGS, serialCommunication_docs},
	{"printString",   (PyCFunction) printString,   METH_VARARGS, serialCommunication_docs},
	{"getPrintBytes", (PyCFunction) getPrintBytes, METH_VARARGS, serialCommunication_docs},

	{"printlnDec",      (PyCFunction) printlnDec,      METH_VARARGS, serialCommunication_docs},
	{"printlnHex",      (PyCFunction) printlnHex,      METH_VARARGS, serialCommunication_docs},
	{"printlnOct",      (PyCFunction) printlnOct,      METH_VARARGS, serialCommunication_docs},
	{"printlnBin",      (PyCFunction) printlnBin,      METH_VARARGS, serialCommunication_docs},
	{"getPrintlnBytes", (PyCFunction) getPrintlnBytes, METH_VARARGS, serialCommunication_docs},

	{NULL, NULL}
};

void initSerial(void) {
	(void) Py_InitModule3("Serial", serialCommunication_methods, "Serial Communication Extension Module.");
}

