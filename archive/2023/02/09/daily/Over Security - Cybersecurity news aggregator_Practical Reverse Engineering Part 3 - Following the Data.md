---
title: Practical Reverse Engineering Part 3 - Following the Data
url: https://jcjc-dev.com/2016/05/23/reversing-huawei-3-sniffing/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:09:15.850843
---

# Practical Reverse Engineering Part 3 - Following the Data

# [Hack The World](https://jcjc-dev.com)

Projects and learnt lessons on Systems Security, Embedded Development, IoT and anything worth writing about

[Archive](/archive/)
[Consulting](/consulting/)
[Juan Carlos Jimenez](https://uk.linkedin.com/in/juan-carlos-jim%C3%A9nez-bba49033/en)
[Twitter](https://twitter.com/Palantir555)
[GitHub](https://github.com/Palantir555)
e-mail

# Practical Reverse Engineering Part 3 - Following the Data

23 May 2016

* [Part 1](https://jcjc-dev.com/2016/04/08/reversing-huawei-router-1-find-uart/):
  Hunting for Debug Ports
* [Part 2](https://jcjc-dev.com/2016/04/29/reversing-huawei-router-2-scouting-firmware/):
  Scouting the Firmware
* **Part 3**: Following the Data
* [Part 4](https://jcjc-dev.com/2016/06/08/reversing-huawei-4-dumping-flash/):
  Dumping the Flash
* [Part 5](https://jcjc-dev.com/2016/12/14/reversing-huawei-5-reversing-firmware/):
  Digging Through the Firmware

The best thing about hardware hacking is having full access to very bare metal,
and all the electrical signals that make the system work. With ingenuity and
access to the right equipment we should be able to obtain any data we want. From
simply sniffing traffic with a cheap logic analyser to using thousands of
dollars worth of equipment to obtain private keys by measuring the power
consumed by the device with enough precision (power analysis side channel
attack); if the physics make sense, it’s likely to work given the right
circumstances.

In this post I’d like to discuss traffic sniffing and how we can use it to gather
intel.

Traffic sniffing at a practical level is used all the time for all sorts of
purposes, from regular debugging during the delopment process to reversing the
interface of gaming controllers, etc. It’s definitely worth a post of its own,
even though this device can be reversed without it.

*Please check out the
[legal disclaimer](https://gist.github.com/Palantir555/de23c2ceb5355efe6ec105a8d2d73486)
in case I come across anything sensitive.*

*Full disclosure: I’m in contact with Huawei’s security team. I tried to contact
TalkTalk, but their security staff is nowhere to be seen.*

## Data Flows In the PCB

Data is useless within its static memory cells, it needs to be read, written
and passed around in order to be useful. A quick look at the board is enough to
deduce where the data is flowing through, based on IC placement and PCB traces:

![PCB With Data Flows and Some IC Names](https://jcjc-dev.com/assets/practical-reversing/JRgtMEM.jpg)

We’re not looking for hardware backdoors or anything buried too deep, so we’re
only gonna look into the SPI data flowing between the Ralink and its external
Flash.

Pretty much every IC in the market has a datasheet documenting all its technical
characteristics, from pinouts to power usage and communication protocols. There
are tons of public datasheets on google, so find the ones relevant to the traffic
you want to sniff:

* [Ralink RT3352F product brief](https://wikidevi.com/files/Ralink/RT3352%20product%20brief.pdf):
  Not a datasheet, but it’s got some useful data
* [Spansion FL064PIF](https://www.dropbox.com/s/55c3hj349k8b8hj/Flash_S25FL064P.pdf?dl=0):
  64-Mbit SPI Flash Memory

Now we’ve got pinouts, electrical characteristics, protocol details… Let’s
take a first look and extract the most relevant pieces of data.

## Understanding the Flash IC

We know which data flow we’re interested: The SPI traffic between the Ralink IC
and Flash. Let’s get started; the first thing we need is to figure out how to
connect the logic analyser. In this case we’ve got the datasheet for the Flash
IC, so there’s no need to reverse engineer any pinouts:

![Flash Pic Annotated Pinout](https://jcjc-dev.com/assets/practical-reversing/54ih2LZ.jpg)

Standard SPI communication uses 4 pins:

1. MISO (Master In Slave Out): **Data** line `Ralink<-Flash`
2. MOSI (Master Out Slave In): **Data** line `Ralink->Flash`
3. SCK (**Clock** Signal): Coordinates when to read the data lines
4. CS# (**Chip Select**): Enables the Flash IC when set to `0` so multiple of them
   can share MISO/MOSI/SCK lines.

We know the pinout, so let’s just connect a logic analyser to those 4 pins and
capture some random transmission:

![Connected Logic Analyser](https://jcjc-dev.com/assets/practical-reversing/TjSkKyN.jpg)

In order to set up our logic analyser we need to find out some SPI configuation
options, specifically:

* Transmission endianness [Standard: **MSB First**]
* Number of bits per transfer [Standard: **8**]. *Will be obvious in the capture*
* CPOL: Default state of the clock line while inactive [0 or 1]. *Will be obvious
  in the capture*
* CPHA: Clock edge that triggers the data read in the data lines [0=leading,
  1=trailing]. *We’ll have to deduce this*

The datasheet explains that the flash IC understands only 2 combinations of
CPOL and CPHA: (CPOL=0, CPHA=0) or (CPOL=1, CPHA=1)

![Datasheet SPI Settings](https://jcjc-dev.com/assets/practical-reversing/Jut5DCs.png)

Let’s take a first look at some sniffed data:

![Logic Screencap With CPOL/CPHA Annotated](https://jcjc-dev.com/assets/practical-reversing/vaPgOc4.png)

In order to understand exactly what’s happenning you’ll need the FL064PIF’s
instruction set, available in its datasheet:

![FL064PIF Instruction Set](https://jcjc-dev.com/assets/practical-reversing/EwOqG0x.jpg)

Now we can finally analyse the captured data:

![Logic Sample SPI Packet](https://jcjc-dev.com/assets/practical-reversing/IT1yDVu.png)

In the datasheet we can see that the FL064PIF has high-performance features for
read and write operations: Dual and Quad options that multiplex the data over
more lines to increase the transmission speed. From taking a few samples, it
doesn’t seem like the router uses these features much -if at all-, but it’s
important to keep the possibility in mind in case we see something odd in a
capture.

Transmission modes that require additional pins can be a problem if your logic
analyser is not powerful enough.

## The Importance of Your Sampling Rate [Theory]

A logic analyser is a conceptually simple device: It reads signal lines as
digital inputs every `x` microseconds for `y` seconds, and when it’s done it
sends the data to your computer to be analysed.

For the protocol analyser to generate accurate data it’s vital that we record
digital inputs faster than the device writes them. Otherwise the data will be
mangled by missing bits or deformed waveforms.

Unfortunately, your logic analyser’s maximum sampling rate depends on how
powerful/expensive it is and how many lines you need to sniff at a time.
High-speed interfaces with multiple data lines can be a problem if you don’t have
access to expensive equipment.

I recorded this data from the Ralink-Flash SPI bus using a low-end Saleae
analyser at its maximum sampling rate for this number of lines,
`24 MS/s`:

![Picture of Deformed Clock Signal](https://jcjc-dev.com/assets/practical-reversing/9wFGIj3.png)

As you can see, even though the clock signal has the 8 low to high transitions
required for each byte, the waveform is deformed.

Since the clock signal is used to coordinate when to read the data lines, this
kind of waveform deformation may cause data corruption even if we don’t drop any
bits (depending partly on the design of your logic analyser). There’s always
some wiggle room for read inaccuracies, and we don’t need 100% correct data at
this point, but it’s important to keep all error vectors in mind.

Let’s sniff the same bus using a higher performance logic analyser at
`100 MS/s`:

![High Sampling Rate SPI Sample Reading](https://jcjc-dev.com/assets/practical-reversing/vVgxUa4.png)

As you can see, this clock signal is perfectly regular when our Sampling Rate is
high enough.

If you see anything dodgy in your traffic capture, consider how much data you’re
willing to lose and whether you’re being limited by your equipment. If that’s
the case, either skip this Reversing vector or consider investing in a better
logic ...