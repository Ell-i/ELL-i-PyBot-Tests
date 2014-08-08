# STM32F4DISCOVERY eLua Setup
The following sections describe the elua build environment setup on Linux (Ubuntu 14.04 LTS) for stm32f4discovery board.

### eLua Build setup in Linux

You need a few packages installed to build eLua:

* **Toolchain**

Please refer to [Runtime Setup and Toolchain][1]. For more general information about eLua toolchains, please refer to [eLua Toolchain Instructions][2]. If you already have environment for Runtime and ARM toolchain binaries in the path, you may skip to following package installations.

* **lua**

Lua should be installed in your environment.

`sudo apt-get install lua5.1`

* **luarocks**

A simple package manager for Lua.

`sudo apt-get install luarocks`

* **luafilesystem, lpack, md5**

Lua modules needed by the elua builder.

```
sudo luarocks install luafilesystem
sudo luarocks install lpack
sudo luarocks install md5
```

* **nasm**

If you’re building for the i386 platform, you’ll also need *nasm*.

`sudo apt-get install nasm`

* **GCC**

If you want to use the ROMFS precompile feature (see [here][8] for details) you need to build an image of the eLua cross compiler, and you need an i386 toolchain for this. It should be already installed, but if you want to be on the safe side do this:

`sudo apt-get install build-essential`

After installing these packages, please refer to [eLua Git Repository][3] for cloning the latest eLua version to build elau binary from source code. For more general information about other MCU boards and already built binaries, please refer to [eLua Download][4]

You may clone elua using [git][5]:

`git clone git@github.com:elua/elua.git`

then build the cross compiler [luac][9]

`lua cross-lua.lua`

To use ROMFS, all you have to do is copy the files you need on your eLua image to the romfs/ directory. The build system will automatically take care of including the files in romfs/ in your eLua image. So all that’s left to do is build eLua after configuration.

### Configuring eLua Firmware Image File

The elua provides a configurator to configure elua image by specifying the various modules and components that will be part of the eLua firmware image, as well as their specific parameters. The configurator works by reading a Lua based board configuration file and generating the corresponding C header file. For more information, please refer to [eLua Configuration][6]. 

The source code from [eLua][3] already contains the configurator file ***stm32f4discovery.lua*** in /boards/known for stm32f4discovery. It contains a number of sections:

**cpu:** The CPU of the board

**components:** The components and their configuration

**config:** Other configuration items

**modules:** List of Lua modules that will be part of the build

We need to change the ***rpc*** section in components from uart=0 to "cdc" in file stm32f4discovery.lua e.g. rpc = { uart = "cdc", speed = 115200 }. The serial connection from desktop to stm32f4discovey board's UART is connected through a micro-usb cable. For knowledge about ***cdc***, please refer to [Communication Device Class][7]. We will be needing the *remote procedure call* for client/server communication between host (Linux) and MCU (stm32f4discovery).

### Building eLua Firmware Image File

Invoke the build system *build_elua.lua* with the [right arguments][10]. For stm32f4discovery, the build system can be invoked for ***standard*** boot as:

`lua build_elua.lua board=stm32f4discovery romfs=compile prog`

and for ***rpc*** boot as:

`lua build_elua.lua board=stm32f4discovery romfs=compile boot=luarpc prog`

The build can be cleaned as above command with -c option at the end of command line e.g.:

`lua build_elua.lua board=stm32f4discovery romfs=compile boot=luarpc prog -c`

You will see stm32f4discovery .bin & .elf files in the directory. Your elua firmware is ready for device upload.

With ***rpc*** boot, we can make use of [luaRPC module][17] for testing the device from Linux. The luaRPC interpreter can be build from the elua base directory using command as:

`lua rpc-lua.lua`

You should get a file called luarpc in the same directory which, when started, should give you a normal Lua interpreter with a built-in rpc module.

### Device Firmware Upload

The firmware can be uploaded to the device and programming over USB OTG DFU is possible using [dfu-util][11]. Using other tools is also possible e.g. [Debugging/Programming using UART][16]. Holding BOOT0 high and BOOT1=PB2 low during reset, and keeping the USART and CAN lines quiescent, should bring up a DFU bootloader on the USB micro-AB port of stm32f4discovery board. For using dfu-util, pleases refer to [Programming via DFU][12]. 

Remove the BOOT0 jumper and press reset. For more information regarding serial connection between Linux and MCU board, please refer to [eLua over Serial Connection][13] and [Setting Minicom on Linux][14]. You should now be able to fire up a terminal emulator, [eLua Shell][15] (i.e. minicom) on /dev/ttyACM0.

`sudo minicom -D STM32F4DISCOVERY`

Running your scripts compiled in romfs/ folder in the firmware image is as simple as:

`lua /rom/<your script file>.lc`






[1]:  https://github.com/Ell-i/Runtime/wiki/Compiling-and-development-environment-setup
[2]:  http://www.eluaproject.net/doc/master/en_toolchains.html
[3]:  https://github.com/elua/elua
[4]:  http://www.eluaproject.net/get-started/downloads
[5]:  https://github.com/Ell-i/Wiki/wiki/Git-Tutorial
[6]:  http://www.eluaproject.net/doc/master/en_configurator.html#manualedit
[7]:  https://github.com/Ell-i/ELL-i-PyBot-Tests/wiki/Communication-Device-Class
[8]:  http://www.eluaproject.net/doc/master/en_arch_romfs.html
[9]:  http://www.eluaproject.net/doc/master/en_using.html#cross
[10]: http://www.eluaproject.net/doc/master/en_building.html
[11]: http://dfu-util.gnumonks.org/
[12]: https://github.com/Ell-i/ELL-i-PyBot-Tests/wiki/Programming-from-Linux-(via-DFU)
[13]: http://www.eluaproject.net/doc/master/en_using.html#uart
[14]: https://github.com/Ell-i/ELL-i-PyBot-Tests/wiki/Minicom-Linux
[15]: http://www.eluaproject.net/doc/master/en_using.html#shell
[16]: http://wiki.eluaproject.net/STM32F4DISCOVERY
[17]: http://www.eluaproject.net/doc/master/en_using.html#rpc