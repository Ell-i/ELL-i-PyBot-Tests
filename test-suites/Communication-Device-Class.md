### CDC: Communication Device Class

The Communication Device Class (CDC) supports a wide range of devices that can perform telecommunications and networking functions. Examples for communications equipment are:

1. Telecommunications devices, such as analog phones and modems, ISDN terminal adapters, digital phones, as well as COM-port devices
2. Networking devices, such as ADSL and cable modems, as well as Ethernet adapters and hubs

Detailed description about CDC is provided by USB Implementers Forum (USB-IF).

### CDC Class Features and Limitations

A communications device has three basic tasks:

1. Device management (controlling an configuring a specific device and notifying the USB Host of certain events)
2. Call management (establishing and terminating telephone calls or other connections)
3. Data transmission (sending and receiving application data)

The CDC implementation in the USB Component has the following features and limitations:

1. Emulation of a virtual COM-port using the ACM (Abstract Control Model) subclass of CDC.
2. One interrupt IN endpoint for notifications to the USB Host
3. One bulk IN and one bulk OUT endpoint for data transfer
4. The USB Component supports the CDC Class for USB Device applications only.
5. Control Transfers

The CDC Subclass for PSTN devices document describes the nine available request types for the Abstract Control Model. Other requests, specific to the CDC class are not supported for a CDC ACM USB Device and will generate a Stall condition.

### Descriptor Requirements

The following descriptors are required in an USB CDC (ACM) Device:

1. Standard device descriptor
2. Standard configuration descriptor
3. Standard interface descriptor for the CDC Class communication interface
4. Standard endpoint descriptor for Interrupt IN endpoint
5. Standard interface descriptor for the CDC Class data interface
6. Standard endpoint descriptors for Bulk IN and Bulk OUT endpoints