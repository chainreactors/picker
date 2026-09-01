---
title: USBvalve v1.0.1
url: https://kitploit.com/en/posts/github-cecio-usbvalve-v101
source: Kitploit
date: 2026-08-31
fetch_date: 2026-09-01T06:59:40.552723
---

# USBvalve v1.0.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/48341/6f346953cc46e6356d367f06f5eda51ecd3f8d9aea1d6ab6c30cfefb46584864.png)

New releaseAug 31, 2026

# USBvalve v1.0.1

Expose USB activity on the fly

Share

# ![logo, landscape, dark text, transparent background](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/USBvalve_logo_scaled.png)

> [!NOTE]
> **USBvalve Version 1.0.0**
>
> A complete rewrite of the application has been done:
>
> * moved away from Arduino IDE environment, now the code is written for the [Pi Pico SDK](https://github.com/raspberrypi/pico-sdk)
> * dependencies on external libraries have been reduced a lot
> * USB host support for Low Speed devices is now more robust (ATTiny85, EvilCrow, etc)
> * hardware and functionalities are almost unchanged, see the [notes](https://github.com/cecio/USBvalve#notes-about-bootsel-and-version--100) below for details

### *Expose USB activity on the fly*

![The two models](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/versions.png)
![The Watch](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/USBvalve_PIWATCH.png)
![1.2](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/version1_2.png)

I'm sure that, like me, you were asked to put your USB drive in an *unknown* device...and then the doubt:

what happened to my poor dongle, behind the scene? Stealing my files? Encrypting them? Or *just* installing a malware? With **USBvalve** you can spot this out in seconds: built on super cheap off-the-shelf hardware you can quickly test any USB file system activity and understand what is going on before it's too late!

With **USBvalve** you can have an immediate feedback about what happen to the drive; the screen will show you if the *fake* filesystem built on the device is accessed, read or written:

![Selftest](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/selftest.png)
![Readme](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/readme.png)

and from version `0.8.0` you can also use it as USB Host to detect *BADUSB* devices:

![HID](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/hid.png)

This is an example of the *BADUSB* debugger available on serial port:

[![](https://asciinema.org/a/NWfC9Mvzzpj3eZfsC7s5Dz1sJ.svg)](https://asciinema.org/a/NWfC9Mvzzpj3eZfsC7s5Dz1sJ)

If you prefer videos, you can also have a look to my [Insomni'hack Presentation](https://www.youtube.com/watch?v=jy1filtQY4w)

## USBvalve Watch

Starting from version `0.15.0` a new *Pi Pico Watch* version is supported. To compile the new version you have to uncomment the `#define PIWATCH` line at the beginning of the code. The hardware is a RP2040-based 1.28-inch TFT display and watch board. You can find some more info [here](https://www.raspberrypi.com/news/how-to-build-your-own-raspberry-pi-watch/).
This is also fully compatible with the [Waveshare RP2040-LCD-1.28](https://www.waveshare.com/wiki/RP2040-LCD-1.28).

## Repository Structure

`docs`: documentation about the project, with a presentation where you can have a look to all the features

`firmware`: pre-built firmwares for the Raspberry Pi Pico. You can just use these and flash them on the board. We have several different versions, for 32 or 64 lines OLEDs, for Pico 1 or Pico2, Pi Pico Watch, etc

`PCB`: Gerber file if you want to print the custom PCB . It's not mandatory, you can use your own or build it on a breadboard

`src` and `data`: sources, if you want to modify and build the firmware yourself

`utils`: some utilities you may use to build a custom FS

`pictures`: images and resources used in this doc

`STL`: STL files for enclosure. In `1.1` and `1.2` folders there are full enclosures (thanks to [WhistleMaster](https://github.com/WhistleMaster)). In folders `1.2_64` and `1.2_64_simple` there are enclosures for the 128x64 screen (thanks to [rtmq0227](https://github.com/rtmq0227)). If you want something lighter to protect the LCD you can go with `USBvalve_sliding_cover.stl`.

## Build USBvalve

### Part list

If you want to build your own, you need:

* A Raspberry Pi Pico 1 or 2 (or another RP2040 based board)
* an I2C OLED screen 128x64 or 128x32 (**SSD1306**)
* (optional) a **USBvalve** PCB or a breadboard
* (optional) a 3D printed spacer to isolate the screen from the board ([https://www.thingiverse.com/thing:4748043](https://www.thingiverse.com/thing%3A4748043)), but you can use a piece of electrical tape instead

### Notes about BOOTSEL and version >= 1.0.0

In the `0.x.x` versions, BOOTSEL was used to reset the device or print the number of HID events (press > 2s).
The polling of BOOTSEL was creating some issues to the *BADUSB* detection so this was removed from version `1.0.0` and replaced with the following two options:

* solder a button between `GP0` and `GND` (pads 1 and 3, see pic below to see an example) to have the same functions
* use the commands `r` (reset) and `h` (HID events) from the serial monitor

![](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/reset_button.jpg)

In `PCB` you'll find also a version `1.3` of the board, with some holes on pads 1 and 3 to facilitate the mount of the button. But as you can see, you can also use your old version.

If you are not using the *BADUSB* functions or if you prefer to have less coverage on detection but keep BOOTSEL usage, I'm also providing a firmware created with *bootsel* enabled (see folder and releases).

### Building instructions

> Thanks to [Tz1rf](https://github.com/Tz1rf) we also have two great videos: one explaining the [building](https://youtu.be/7ymk8hD7-Hc) process step-by-step, and another showing how to [upload firmware](https://youtu.be/Tp8xvrlqxUY) and use the tool.

Almost all the job is done directly on the board by the software, so you just need to arrange the connection with the OLED for output.

Starting from version 0.8.0 of the firmware, **USBvalve** can detect HID devices (used to detect *BADUSB*). This require an additional USB port behaving as Host. If you are not interested in this, you can use the old instructions [in docs folder](https://github.com/cecio/USBvalve/blob/main/docs/BUILDING-1.1.md) and use PCB version `1.1`. Otherwise go ahead with PCB version `1.2` (we have version for USB-A or USB-B, see folder).

#### With USBvalve PCB

![](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/USB_valve_1-2_front.png)
![](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/USB_valve_1-2_back.png)

* solder a USB female port in `USBH` area. This is for version `A`, but there is a version for USB `Micro-B` as well if you prefer
* place the Raspberry Pi Pico on the silk screen on the front
* you don't need to solder all the PINs. Just the following:
  + D4 and D5 (left side)
  + D14 and D15 (left side)
  + GND (right side, third pin from the top)
  + GND (right side, third pin from the bottom)
  + 3v3\_OUT (right side)
  + VBUS (right side)
  + the 3 DEBUG pin on the bottom: SWCLK, GND and SWDIO
* place the 3D printer spacer or a piece of tape on the parts of the OLED that my touch the Raspberry
* solder the OLED (with a header) on the 4 PIN space

Some of the OLEDs have the GND and VCC PINs swapped, so I built the PCB to be compatible with both versions:

For example if your OLED has GND on PIN1 and VCC on PIN2 like this:

![](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/usb_valve_oled.png)

You have to place a blob of solder on these two pads on the back of the PCB:

![](https://raw.githubusercontent.com/cecio/USBvalve/main/pictures/usb_valve_pads.png)

Otherwise you should the opposi...