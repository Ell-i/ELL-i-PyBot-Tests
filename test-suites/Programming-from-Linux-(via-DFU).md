This section covers how to flash the STM32F4DISCOVERY from linux (I was using Linux Mint 14, which is derived from ubuntu 12.10).

* Install dfu-utils

`sudo apt-get install dfu-util`

* Create a udev rules file. I used sudo vi /etc/udev/49-stmdiscovery.rules and put the following contents:

```
# 0483:5740 - STM32F4 Dsicovery in USB Serial Mode (CN5)
ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", ENV{ID_MM_DEVICE_IGNORE}="1"
ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", ENV{MTP_NO_PROBE}="1"
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", MODE:="0666"
KERNEL=="ttyACM*", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", MODE:="0666"
# 0483:df11 - STM32F4 Discovery in DFU mode (CN5)
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="df11", MODE:="0666"
```
Tell udev to reload its rules:

`sudo udevadm control --reload-rules`

* Plug in the discovery board. To use DFU, you need to connect CN5 (the micro-USB connector on the bottom of the board) into your PC. Unfortunately, the CN5 connector doesn't power the board, so you can either connect CN1 (mini-USB connector at the top of the board), or run a jumper wire from PA9 to 5V (PA9 connects to VBUS on CN5) in order to power the board. CN1 connects to the STM32F103 chip near the mini connector in order to support stlink. CN5 connects to the STM32F407 chip.

* Put the board in DFU mode. To do this, you need to make BOOT0 high, and BOOT1 low, and reset the board. Since the onboard bootloader supports bootloading over UARTs, CAN bus, and USB, you need to make sure that UART1 (PA9/PA10) UART3 (PB10/11 and PC10/11) and CAN (PB5/13) are quiescent while bootloading.

On the discovery board, BOOT1 is pulled low through SB19 and a 510 ohm resistor, and BOOT0 is pulled low through SB18 and another 510 ohm resistor. Since BOOT1 is already low, you just need to make BOOT0 high. Conveniently the BOOT0 signal is beside a VDD signal on the P2 header. So you can install a shorting jumper (there are a couple of spares included with the board on JP2 and JP3 on the bottomside of the board) between BOOT0 and VDD and press the reset button.

You should now be able to program the board using:

`sudo dfu-util -d 0483:df11 -c 1 -i 0 -a 0 -s 0x08000000 -D elua_lua_stm32f4discovery.bin`

For more information regarding the dfu-util arguments please refer to [dfu-util manual][1].


[1]: http://dfu-util.gnumonks.org/dfu-util.1.html