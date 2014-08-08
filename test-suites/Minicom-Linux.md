**Setting minicom over Linux for the micro-usb port of stm32f4discovery board**.

* Download minicom

`sudo apt-get install minicom`

* Open up a terminal window. Type "sudo minicom -s" (minicom -s is for setting up minicom). The sudo here is important - since we need administrative rights to set the default settings for the minicom.

* Now connect your serial (or usb --> serial) connection

* Open a new terminal window

  Type "dmesg | grep tty" (this command lists the devices). Check for a ttyACM0 listing. In Linux, serial  ports are named tty, and ttyACM0 for serial devices connected via micro-USB.

* Now go back to the terminal where minicom is already open.
* Select "serial port setup"

  Change option A (device) to "/dev/ttyACM0" (case sensitive!)
  
  115200 baud (38400 for STR7)

  8N1 (8 data bits, no parity, one stop bit).

  flow control: none, unless your eLua image is configured to use hardware flow control

* Go back to main menu and select "save as STM32F4DISCOVERY"
* Select "exit" - and minicom should now launch and you should see output from your device



