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

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.write() function with 1 byte as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* writeBytes(PyObject* self, PyObject* args) {
	char* byts;
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

 	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.write() function with string of several bytes as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* writeBuffer(PyObject* self, PyObject* args) {
	/// refer to the python C API for -> working with sequences ... 

	//Always call if (Serial.if(Serial)) to check if port is open for communication
	//Call the serial.write() function with buffer of several bytes and its length as parameter
	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* getWrittenBytes(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.write() function with string of several bytes as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printInt(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.print() function with integer as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printFloat(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.print() function with float as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printChar(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.print() function with character as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printString(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.print() function with string as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* getPrintBytes(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.print() function with string as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printlnDec(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.println() function with character and DEC format as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printlnHex(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
 	}

 	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.println() function with character and HEX format as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printlnOct(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.println() function with character and OCT format as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* printlnBin(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.println() function with character and BIN format as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static PyObject* getPrintlnBytes(PyObject* self, PyObject* args) {
	if (!PyArg_ParseTuple(args, "s", &byts)) {
		return NULL;
  	}

  	//Always call if (Serial.if(Serial)) to check if port is open for communication
  	//Call the serial.println() function with string as parameter
  	//Also, call serial.flush() to wait for transmitting the data

}

static char serialTransmitCommunication_docs[] = "c-python extention module for serial communication";

static PyMethodDef serialTransmitCommunication_methods[] = {
	{"beginSerial", (PyCFunction) beginSerial, METH_VARARGS, serialTransmitCommunication_docs},
	{"endSerial",   (PyCFunction) endSerial,   METH_NOARGS,  serialTransmitCommunication_docs},	
	
	{"writeByte",       (PyCFunction) writeByte,       METH_VARARGS, serialTransmitCommunication_docs},
	{"writeBytes",      (PyCFunction) writeBytes,      METH_VARARGS, serialTransmitCommunication_docs},
	{"writeBuffer",     (PyCFunction) writeBuffer,     METH_VARARGS, serialTransmitCommunication_docs},
	{"getWrittenBytes", (PyCFunction) getWrittenBytes, METH_VARARGS, serialTransmitCommunication_docs},

	{"printInt",      (PyCFunction) printInt,      METH_VARARGS, serialTransmitCommunication_docs},
	{"printFloat",    (PyCFunction) printFloat,    METH_VARARGS, serialTransmitCommunication_docs},
	{"printChar",     (PyCFunction) printChar,     METH_VARARGS, serialTransmitCommunication_docs},
	{"printString",   (PyCFunction) printString,   METH_VARARGS, serialTransmitCommunication_docs},
	{"getPrintBytes", (PyCFunction) getPrintBytes, METH_VARARGS, serialTransmitCommunication_docs},

	{"printlnDec",      (PyCFunction) printlnDec,      METH_VARARGS, serialTransmitCommunication_docs},
	{"printlnHex",      (PyCFunction) printlnHex,      METH_VARARGS, serialTransmitCommunication_docs},
	{"printlnOct",      (PyCFunction) printlnOct,      METH_VARARGS, serialTransmitCommunication_docs},
	{"printlnBin",      (PyCFunction) printlnBin,      METH_VARARGS, serialTransmitCommunication_docs},
	{"getPrintlnBytes", (PyCFunction) getPrintlnBytes, METH_VARARGS, serialTransmitCommunication_docs},

	{NULL, NULL}
};

void initSerial(void) {
	(void) Py_InitModule3("serialTransmit", serialTransmitCommunication_methods, "Serial Communication Extension Module.");
}

