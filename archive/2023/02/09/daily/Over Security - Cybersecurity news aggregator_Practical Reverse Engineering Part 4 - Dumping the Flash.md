---
title: Practical Reverse Engineering Part 4 - Dumping the Flash
url: https://jcjc-dev.com/2016/06/08/reversing-huawei-4-dumping-flash/
source: Over Security - Cybersecurity news aggregator
date: 2023-02-09
fetch_date: 2025-10-04T06:09:15.314009
---

# Practical Reverse Engineering Part 4 - Dumping the Flash

# [Hack The World](https://jcjc-dev.com)

Projects and learnt lessons on Systems Security, Embedded Development, IoT and anything worth writing about

[Archive](/archive/)
[Consulting](/consulting/)
[Juan Carlos Jimenez](https://uk.linkedin.com/in/juan-carlos-jim%C3%A9nez-bba49033/en)
[Twitter](https://twitter.com/Palantir555)
[GitHub](https://github.com/Palantir555)
e-mail

# Practical Reverse Engineering Part 4 - Dumping the Flash

08 Jun 2016

* [Part 1](https://jcjc-dev.com/2016/04/08/reversing-huawei-router-1-find-uart/):
  Hunting for Debug Ports
* [Part 2](https://jcjc-dev.com/2016/04/29/reversing-huawei-router-2-scouting-firmware/):
  Scouting the Firmware
* [Part 3](https://jcjc-dev.com/2016/05/23/reversing-huawei-3-sniffing/):
  Following the Data
* **Part 4**: Dumping the Flash
* [Part 5](https://jcjc-dev.com/2016/12/14/reversing-huawei-5-reversing-firmware/):
  Digging Through the Firmware

In Parts 1 to 3 we’ve been gathering data within its context. We could sniff
the specific pieces of data we were interested in, or observe the resources
used by each process. On the other hand, they had some serious limitations;
we didn’t have access to ALL the data, and we had to deal with very minimal
tools… And what if we had not been able to find a serial port on the PCB?
What if we had but it didn’t use default credentials?

In this post we’re gonna get the data straight from the source, sacrificing
context in favour of absolute access. We’re gonna dump the data from the Flash
IC and decompress it so it’s usable. This method doesn’t require expensive
equipment and is independent of everything we’ve done until now. An external
Flash IC with a public datasheet is a reverser’s great ally.

## Dumping the Memory Contents

As discussed in Part 3, we’ve got access to the datasheet for the Flash IC, so
there’s no need to reverse its pinout:

![Flash Pic Annotated Pinout](https://jcjc-dev.com/assets/practical-reversing/54ih2LZ.jpg)

We also have its instruction set, so we can communicate with the IC using almost
any device capable of ‘speaking’ SPI.

We also know that powering up the router will cause the Ralink to start
communicating with the Flash IC, which would interfere with our own attempts to
read the data. We need to stop the communication between the Ralink and the
Flash IC, but the best way to do that depends on the design of the circuit we’re
working with.

#### Do We Need to Desolder The Flash IC? [Theory]

The perfect way to avoid interference would be to simply desolder the Flash IC
so it’s completely isolated from the rest of the circuit. It gives us absolute
control and removes all possible sources of interference. Unfortunately, it also
requires additional equipment, experience and time, so let’s see if we can avoid
it.

The second option would be to find a way of keeping the Ralink inactive while
everything else around it stays in standby. Microcontrollers often have a `Reset`
pin that will force them to shut down when pulled to `0`; they’re commonly used
to force IC reboots without interrupting power to the board. In this case we
don’t have access to the Ralink’s full datasheet (it’s probably distributed only
to customers and under NDA); the IC’s form factor and the complexity of the
circuit around it make for a very hard pinout to reverse, so let’s keep
thinking…

What about powering one IC up but not the other? We can try applying voltage
directly to the power pins of the Flash IC instead of powering up the whole
circuit. Injecting power into the PCB in a way it wasn’t designed for could
blow something up; we could reverse engineer the power circuit, but that’s
tedious work. This router is cheap and widely available, so I took the ‘fuck it’
approach. The voltage required, according to the
[datasheet](https://www.dropbox.com/s/55c3hj349k8b8hj/Flash_S25FL064P.pdf?dl=0),
is 3V; I’m just gonna apply power directly to the Flash IC and see what happens.
It may power up the Ralink too, but it’s worth a try.

![Flash Powered UART Connected](https://jcjc-dev.com/assets/practical-reversing/JBTsUfo.png)

We start supplying power while observing the board and waiting for data from
the Ralink’s UART port. We can see some LEDs light up at the back of the PCB,
but there’s no data coming out of the UART port; the Ralink must not be running.
Even though the Ralink is off, its connection to the Flash IC may still interfere
with our traffic because of multiple design factors in both power circuit and the
silicon. It’s important to keep that possibility in mind in case we see anything
dodgy later on; if that was to happen we’d have to desolder the Flash IC (or just
its data pins) to physically disconnect it from everything else.

The LEDs and other static components can’t communicate with the Flash IC, so they
won’t be an issue as long as we can supply enough current for all of them.
I’m just gonna use a bench power supply, with plenty of current available for
everything. If you don’t have one you can try using the *Master*’s power lines,
or some USB power adapter if you need some more current. They’ll probably do
just fine.

Time to connect our SPI *Master*.

### Connecting to the Flash IC

Now that we’ve confirmed there’s no need to desolder the Ralink we can connect
any device that *speaks* SPI and start reading memory contents block by block.
Any microcontroller will do, but a purpose-specific SPI-USB bridge will often
be much faster. In this case I’m gonna be using a board based on the `FT232H`,
which supports SPI among some other low level protocols.

We’ve got the pinout for both the Flash and my
[USB-SPI bridge](http://www.xipiter.com/uploads/2/4/4/8/24485815/shikra_documentation.pdf),
so let’s get everything connected.

![Shikra and Power Connected to Flash](https://jcjc-dev.com/assets/practical-reversing/SyUFtey.jpg)

Now that the hardware is ready it’s time to start pumping data out.

### Dumping the Data

We need some software in our computer that can understand the USB-SPI bridge’s
traffic and replicate the memory contents as a binary file. Writing our own
wouldn’t be difficult, but there are programs out there that already support
lots of common Masters and Flash ICs. Let’s try the widely known and open source
[flashrom](https://www.flashrom.org/Flashrom).

`flashrom` is old and buggy, but it already supports both the `FT232H` as
Master and the `FL064PIF` as Slave. It gave me lots of trouble in both OSX and
an Ubuntu VM, but ended up working just fine on a Raspberry Pi (Raspbian):

![flashrom stdout](https://jcjc-dev.com/assets/practical-reversing/VzvjX31.png)

**Success!** We’ve got our memory dump, so we can ditch the hardware and start
preparing the data for analysis.

## Splitting the Binary

The `file` command has been able to identify some data about the binary, but
that’s just because it starts with a header in a supported format. In a
0-knowledge scenario we’d use [binwalk](https://github.com/devttys0/binwalk)
to take a first look at the binary file and find the data we’d like to extract.

*Binwalk is a very useful tool for binary analysis created by the
awesome hackers at [/dev/ttyS0](http://www.devttys0.com/); you’ll certainly get
to know them if you’re into hardware hacking.*

![binwalk spidump.bin](https://jcjc-dev.com/assets/practical-reversing/vdmjcDt.png)

In this case we’re not in a 0-knowledge scenario; we’ve been gathering data since
day 1, and we obtained a complete memory map of the Flash IC in Part 2. The
addresses mentioned in the debug message are confirmed by binwalk, and it makes
for much cleaner splitting of the binary, so let’s use it:

![Flash Memory Map From Part 2](https://jcjc-dev.com/assets/practical-reversing/CX9raje.png)

With the binary and the relevant addresses, it’s time to split the binary into
its 4 basic segments. `dd` takes its parameters in terms of block size (`bs`,
bytes), offset (`skip`, blocks) and size (`count`, blocks); all of them in
decimal. We can use a calculator or let the shell do the...