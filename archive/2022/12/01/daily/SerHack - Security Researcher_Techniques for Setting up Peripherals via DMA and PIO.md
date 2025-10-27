---
title: Techniques for Setting up Peripherals via DMA and PIO
url: https://serhack.me/articles/techniques-setting-up-pheripherals-dma-pio/
source: SerHack - Security Researcher
date: 2022-12-01
fetch_date: 2025-10-04T00:14:46.734407
---

# Techniques for Setting up Peripherals via DMA and PIO

[![SerHack logo](https://serhack.me/images/serhack-120.png)

SerHack Security Research](https://serhack.me/)

[ ]

[About](https://serhack.me/about/ "About")
[Blog](https://serhack.me/blog/ "Blog")
[Books](https://serhack.me/books/ "Books")
[EN](https://serhack.me/articles/techniques-setting-up-pheripherals-dma-pio/ "en version")
[IT](https://serhack.me/it/articles/tecniche-impostare-periferiche-direct-memory-access/ "it version")

# Techniques for Setting up Peripherals via PIO and DMA

Published at November 30, 2022 – 14 min read – 2867 words

![Techniques for Setting up Peripherals via DMA and PIO](https://serhack.me/images/articles/reolink-firmware/reolink_6_800px.jpg)

In [Part 5](https://serhack.me/articles/operating-system-reolink-rlc-810-a/) of our series, we focused our efforts on understanding how the firmware was structured. In doing so, we analyzed the folder with the system executables and delved into the various configuration files.

Before tackling the analysis of a device driver, we need to focus on some hardware aspects that will come in handy for this article. These aspects include the management of peripherals and input/output devices.

## The Registers Associated with the Peripherals

Mouse, keyboard, webcam, and optical sensors all have something in common: they are all peripherals ― hardware devices that extend the functionality of a computer and interface with the real world. There are input peripherals (e.g., mouse, keyboard, sensors in general), output peripherals (e.g., keyboard), but also input/output peripherals (e.g., the network card).

Peripherals have always been difficult to manage because of the countless different configurations between manufacturers. *How can we get the operating system and peripheral to talk to each other?* Each peripheral has associated registers and a hardware controller that allow low-level commands to be issued to the peripheral. A hardware controller is an electronic interface that allows a device to be commanded (e.g., move a frame, configure the device’s mode), while a register is a very expensive, but also very fast and volatile memory that allows virtually instantaneous exchange of information.

Each device/peripheral consists of at least three registers:

* a register for **data** (*data register*) containing some information that the operating system needs to know (e.g., mouse position, keyboard character typed);
* a register for the **status** of the peripheral device (*status register*) that makes note as to whether it has been recently used, whether some sudden error has happened, etc.; and
* a register for the **control** (*control register*) that allows commands to be given to the device.

By accessing data from these registers, any device can be configured, installed, and controlled. The main problem is the variety of hardware configurations on the market.

Take, for example, the abstract concept of a mouse. How many mouse manufacturers exist in the world? Certainly there are enough of them that it is not possible to constitute a communication standard. It is unthinkable to encode, within code, an algorithm that can interface with all devices in the world. To get around the problem, manufacturers therefore enclose with the physical product a program, called a *device driver*, that allows those who install the peripheral to be able to use it.

The device driver presents a high-level interface for the operating system and application services that want to use, configure, and set up a peripheral. From a technical point of view, the device driver is nothing more than a program mapped to a specific memory location. Whenever the operating system receives a request to use such a peripheral, the system will call the handler (i.e., device driver), which will provide the requested service.

![Overview of iteration between device drivers and operating system.](https://serhack.me/images/articles/reolink-firmware/device_drivers_800px.jpg)

Overview of iteration between device drivers and operating system.

Since the device driver is proprietary and given that it is a “bottleneck” for controlling the hardware, we are very interested in understanding how a device works and what settings it can provide. It is indeed possible to hide features by setting stringent limits via the device driver ― not surprisingly, most problems with peripherals occur because of a problem with the device driver and not the device itself. However, the manufacturer does not always attach the device driver. It is also possible to write it from scratch, following documentation from the manufacturer.

To share data from a peripheral and transmit it to the mainframe, there are two main techniques:

* **Programmed Input Output (PIO)** ― a technique originated in the early days of computing that continues to be used for embedded devices. Its main purpose is to transfer data between the memory and the peripheral, using the central processing unit (CPU). Interferes with normal execution flow.
* **Direct Memory Access (DMA)** ― optimization of the Programmed Input Output technique. Provides for a new device that interfaces directly with memory and peripherals, but does not involve CPU contribution.

In the following paragraphs, we will explore the difference between the two techniques by introducing a communication protocol that is used within the Reolink RLC-810A camera.

For the board used by the Reolink RLC-810A, Novatek included both the ability to connect peripherals in PIO (used mainly for the optical sensor) and DMA for the board’s internal RAM (used, for example, by other devices such as UART, USB).

### Programmed Input Output

The Programmed Input Output technique is a method of data transmission between a peripheral device and the CPU. Each data transfer is initiated by an instruction in the program involving the CPU. The processor executes a program that gives it direct control of the I/O operation, including detecting the status of the device, sending a read/write command, and transferring data.

The operation of the Programmed Input Output can be summarized as follows:

1. The CPU is executing a program and encounters an instruction related to an I/O operation.
2. The CPU executes the instruction, querying the peripheral device.
3. The peripheral device performs the requested action according to the instruction given by the CPU and sets the appropriate bits in the status register.
4. The processor periodically checks the status of the I/O module until it detects that the operation has not been completed.

As one can easily guess, Step 4 uses the CPU for the longest period of time ― cyclically checking the status of the operation is an unnecessary waste of time. This is the main disadvantage of the Programmed Input Output technique. The CPU must stop the execution flow in order to periodically check the status of the peripheral, which impacts system performance.

The second disadvantage of PIO lies in the size of the data that can be sent to the CPU. Since the registers are fixed and small in size, the CPU must spend several clock cycles in an effort to transfer large masses of data. PIO speeds range from a few kBytes per second up to 55 MB per second, which is more than enough for some embedded purposes.

On the other hand, not implementing a DMA allows for simpler electronic logic. This strongly impacts development costs, making large-scale savings possible. The simplicity of PIO is strongly chosen by embedded device manufacturers because peripheral devices do not need to transfer large amounts of data at high speed. For the connection between the OMNIVISION optical sensor and the board, Novatek decided not to implement DMA, instead taking advantage of one of the two CPU cores that is fully dedicated to image encoding.

### Direct Memory Access

When you have multiple hardware devices (e.g., network card, keyboard, mouse) transferring data abruptly, such as in a general-purpose system, the use of the PIO could w...