# Robot Framework Setup
Conventions about the test suites, scripts and repository structure are discussed in the following sections.

* Environment Setup Prerequisites
* Repository Folder Structure
* Test Library Scripts and Emulator Shared Library
* Test Data Suites
* Git Cloning
* Run Tests

### Environment Setup Prerequisites

- For using latest version (2.5 or higher) of ***Robot Framework*** test automation environment along with ***Python***, installing latest version (2.5 or higher) of ***Python*** is necessary. Latest version I am using is ***Python-2.7.6***.

- ***Robot Framework*** (version 2.7 or higher) needs to be installed. Package ***docutils*** is also necessary from *python documentation utilities for python* to read test suites written in ***.rest*** format. Please check latest version of ***docutils***, I am using version 0.11 from [docutils download][2].

- ***Ell-i/Runtime*** needs to be pull/fetched from git repository and then make with GCC toolchain. The successful build will create binaries for the Runtime & emulator. The build also contains the emulator shared library **libemulator.so** which can be loaded in the test scripts for testing purposes. The Ell-i/Runtime can be pulled/fetched from [asifsardar26 Runtime][14].

For detailed instruction of ***Robot Framework*** installation for particular operating system, please refer to [Installing Robot Framework][1]. If you are already using the 32-bit Linux, the default installation for ***Python***, ***docutils*** and ***Robot Framework*** using the above link may suffice the requirements for running a 32-bit shared dynamic library for ***emulator*** written in C/C++.

For using 64-bit Linux, please read the below instructions to customize, build and install the 32-bit versions of above packages such as ***Python***, ***docutils*** and ***Robot Framework***.

To customize, build and install 32-bit packages, you may need [32-bit Linux Dependencies][12].

***32-bit Python Installation***

The source code for 32-bit ***Python*** can be found from [32-bit Python Source Code][9]. For building and installing 32-bit ***Python*** from source code, you may need some packages. These can be installed either using GUI ***Synaptic Package Manager*** or ***Command Line Interface (CLI)***. The ***CLI*** uses ***apt-get install*** under ***Linux***. The ***apt-get install*** can be used in terminal/bash login session as: ***sudo apt-get install package-name***.

```
sudo apt-get install zlib1g-dev lib32z1-dev libreadline-dev libreadline6-dev 
lib32readline-dev lib32readline6-dev libgdm-dev libsqlite3-dev libgdbm-dev 
libdbm-ocaml-dev libdb4o-cil-dev libx11-dev lib32bz2-dev libbz2-dev 
libncurses5-dev lib32ncurses5-dev tk-dev
```
After installing the above packages, go to the downloaded source code directory of ***Python*** and execute:

```
BASECFLAGS=-m32 LDFLAGS=-m32 CFLAGS=-m32 ./configure --prefix=/opt/pym32
make
sudo make install
``` 
Ignore if some modules still didn't built, refer to this [article][10].

Be carefull in make step ... complete installing necessary packages first and then again configure and make the ***Python*** from source code. You might need dev packages for these. Atlast, sudo make install.

After successful installation, you may find the path to this 32-bit ***Python*** at ***/opt/pym32/bin/python***. You may add this to the ***PATH*** environment variable, but it may not be needed at all. But, if you still want to add it, you may do.

You may add this path to the ***PATH*** environment variable persistently by adding the following line to ~/.bashrc files and save it.

```
export PATH="/opt/pym32/bin:${PATH}"
```

***Note*** that the path is added to the beginning of the ***PATH*** environment variable. This is done intentionally, so that, the bash/shell could look for ***python*** in /opt/pym32/bin/python first instead of the default 64-bit /usr/bin/python. This way, it runs your chosen 32-bit ***Python*** when you type *python*, but when some program on your system tries to run a script with /usr/bin/python it runs the standard 64-bit ***Python***.

But, adding it to the ***PATH*** environment variable is unnecessary at all! You may still use the 32-bit ***Python*** explicitly as you already know the path to it such as ***/opt/pym32/bin/python***. So, I would recommend not to mess your ***PATH***, especially trying to override the 32-bit ***Python*** over 64-bit ***Python***. Otherwise, the consequences would be disastrous! I messed up Ubuntu 12.04 LTS by removing symbolic link to default 64-bit ***Python*** and making symbolic link to 32-bit ***Python*** at ***/usr/bin/python***. The reason is that, some of your system level scripts and software packages might be dependent on default 64-bit ***Python***. In general, monkeying with ***/usr/bin*** can break your package manager's ability to manage packages. The cost was to back-up all my working directory and re-install Ubuntu and setup the whole Runtime and Ell-i-Pybot-Tests environment from scratch.

***Robot Framework and docutils***

The source code for ***Robot Framework*** can be found from [Robot Framework Source Code][11] and the source code for ***docutils*** from [Docutils Source Code][2]. The ***Robot Framework*** and ***docutils*** from source code can be installed using the 32-bit ***Python*** as follows:

```
cd /absolute/path/to/robotframework/
sudo /opt/pym32/bin/python setup.py install

cd /absolute/path/to/docutils
sudo /opt/pym32/bin/python setup.py install
```
Using the 32-bit ***Python*** for installing the above packages, the binaries will be installed to the ***/opt/pym32/bin***. So, when you use the ***/opt/pym32/bin/python*** in ***Robot Framework*** test library scripts and running ***Pybot*** test scripts, you wouldn't have problems loading the 32-bit shared dynamic ***Emulator*** library from ***Python*** *ctypes* module.

### Repository Folder Structure
The git repository for tests itself contains the following folders:

* /run-tests
* /test-scripts
* /test-suites

Where the /test-suites folder contains sub-folder for its own repository such as:

* /ELL-i-PyBot-Tests.wiki

**Note**
For using ***.rest*** file format, please install ***docutils*** package in your Linux Environment as mentioned earlier.

### Test Library Scripts and Emulator Shared Library
Please save a copy of **libemulator.so** to the root directory of robot framework folder structure. The test scripts for the test suites are written using python programming language ***.py*** extension. For using the 32-bit ***Python*** for the tests library to load 32-bit ***Emulator*** shared dynamic library using ***Python*** *ctypes* module and also to run the test suites from tests scripts using the ***Pybot***, please add the path to 32-bit ***Python*** in the beginning of the these scripts as:

```
#!/opt/pym32/bin/python
```

### Test Data Suites
Each file in the wiki Pages (except for ***Home*** and ***Read Me*** pages) corresponds to the test suites for **Arduino** reference libraries and **Ell-i Runtime**, each containing several test cases. The test data follows one of the ***Robot Framework*** test data syntax, such as re-structured text format ***.rest*** extension for creating ***Setting***, ***Variable***, ***Test Case*** and ***Keyword*** tables.

### Git Cloning
For more information on git please refer to [Git Tutorial][13]. This section describes cloning the above repository structure into your local machine:

The whole of ELL-i-PyBot-Tests as of now needs be git cloned to a certain folder structure:

```
cd ~
mkdir Ell-i
cd Ell-i
git clone git@github.com:Ell-i/ELL-i-PyBot-Tests.git
cd ELL-i-PyBot-Tests
mkdir test-suites
cd test-suites
git clone git@github.com:Ell-i/ELL-i-PyBot-Tests.wiki.git
```
Note the ***.wiki.*** part in clone URL for wiki pages. Also, the folders, such as ***/test-suites/*** which contains the wiki repository (requires its own commit, pull and push), ***test-results*** which is made locally after running the test suites and ***/arduino-functions/build/*** which contains ***.o*** & ***.so*** files are added to the ***.gitignore*** file, so that they are not committed to the repository and stay local to your machine.

```
# ELL-i Robot Framework
test-suites/
test-results/
```
### Run Tests
The test data in test suites containing different cases and the test library scripts written for them in python have been targeted for its usage in ***Robot Framework Automation Testing***. For running the test cases on ***Robot Framework***, you should have it installed and configured on your local machine. For more information about ***Robot Framework*** please visit [Robot Framework][4].

If you have ***Robot Framework*** installed on your machine, you should change directory to ***/absolute path to/ELL-i-PyBot-Tests/run-tests/*** and running test cases is as simple as running python scripts in Linux Command Line Interface e.g. Terminal/bash login session:

```
./Test_Name (e.g. ./TimeMillis)
```
***Note:*** 
Please add the ***../Runtime/stm32/build*** path to the ***dllPath*** variable in the ***Utilities.py*** present in the test-scripts folder. Also, add the path to test-scripts folder to the ***PYTHONPATH*** variable in ***~/.bashrc*** file.

```
export PYTHONPATH=/path/to/test-scripts/
```
For each test suite, executing a test suite as described above makes a separate folder with the name of test suite in local folder ***/test-results/*** which contains the test result files e.g. log.html, output.xml, report.html.

[1]: https://code.google.com/p/robotframework/wiki/Installation#Preconditions
[2]: https://pypi.python.org/pypi/docutils
[3]: https://help.github.com/articles/generating-ssh-keys
[4]: http://www.robotframework.org/
[9]: https://www.python.org/download/
[10]: http://blog.devork.be/2009/02/compiling-32-bit-python-on-amd64.html
[11]: https://pypi.python.org/pypi/robotframework
[12]: https://github.com/Ell-i/Wiki/wiki/32-bit-dependencies-in-64-bit-Linux-environment
[13]: https://github.com/Ell-i/Wiki/wiki/Git-Tutorial
[14]: https://github.com/asifsardar26/Runtime/tree/feature-runtime-temp