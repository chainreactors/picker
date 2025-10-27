---
title: Hands-On IoT Hacking Rapid7 at DEF CON 30 IoT Village, Part 1
url: https://www.rapid7.com/blog/post/2022/10/18/hands-on-iot-hacking-rapid7-at-def-con-30-iot-village-part-1/
source: Instapaper: Unread
date: 2022-10-20
fetch_date: 2025-10-03T20:25:49.610136
---

# Hands-On IoT Hacking Rapid7 at DEF CON 30 IoT Village, Part 1

[![Rapid7](/_next/static/media/rapid7-logo.cd245920.svg)](/)

* Platform
* Services
* Resources
* Partners
* Company

##

[Request Demo](/request-demo/)

[Back to Blog](/blog/)

Detection and Response

# Hands-On IoT Hacking: Rapid7 at DEF CON 30 IoT Village, Part 1

[![Deral Heiland](https://www.rapid7.com/cdn/assets/blt9f9db121928e3816/6840441898bc4eb9f1818b21/Deral-Heiland.jpg)

Deral Heiland](/blog/author/deral-heiland/)

Oct 18, 2022|Last updated on Oct 18, 2022|xx min read

![Hands-On IoT Hacking: Rapid7 at DEF CON 30 IoT Village, Part 1](https://www.rapid7.com/cdn/assets/blt522b1baa8610fecc/683ddca43e68ee6ddc889824/GettyImages-1370233320.jpg)

Rapid7 was back this year at [DEF CON 30](/blog/post/2022/08/15/video-an-inside-look-at-black-hat-2022-from-the-rapid7-team/) participating at the [IoT Village](https://iotvillage.org/) with another hands-on hardware hacking exercise, with the goal of teaching attendees' various concepts and methods for IoT hacking. Over the years, these exercises have covered several different embedded device topics, including how to use a Logic Analyzer, extracting firmware, and gaining root access to an embedded IoT device.

Like last year, we had many IoT Village attendees request a copy of our exercise manual, so again I decided to create an in-depth write-up about the exercise we ran, with some expanded context to answer several questions and expand on the discussion we had with attendees at this year's DEF CON IoT Village.

This year's exercise focused on the following key areas:

* Interaction with eMMC in circuit
* Using Linux dd command to make binary copy of flash memory
* Use unsquashfs and mksquashfs commands to unpack and repack read only squash file systems
* Alter startup files within the embedded Linux operating system to execute code during device startup
* Leverage dropbear to enable SSH access

## Summary of exercise

The goal of this year's hands-on hardware hacking exercise was to gain root access to a Arris SB6190 Cable modem without needing to install any external code. To do this, the user interacted with the device via a PHISON PS8211-0 embedded multimedia controller (eMMC) to mount up and gain access to the NAND flash memory storage. With NAND flash memory access, the user was able to identify the partitions of interest and extract those partitions using the Linux dd command.

Next, the user extracted the filesystem from the partition binary files and was then able to modify key elements to enable SSH access over the ethernet connection. After the modification where completed the filesystems were repacked and written back to the modem device. Finally, the attendee was able to power up the device and login over ethernet using SSH with root access and default device password.

![image.png](https://www.rapid7.com/cdn/assets/blted9aa63b82f67f9b/683ddbe85619a17a02c6e94a/image.png)

## **eMMC access to flash memory**

In this first section of the exercise, we focused on understanding the process of gaining access to the NAND flash memory by interacting with a PHISON PS8211-0 embedded multimedia controller (eMMC).

## **Wiring up eMMC and SD card breakout board**

To interact with typical eMMC devices, we typically need the following connections.

* CMD Command
* DAT Data
* CLK Clock
* VCC Voltage 3.3v
* VCCq Controller Voltage 1.8v – 3.3v
* GND Ground

As shown in the above bullets, there are typically two different voltages required to interact with eMMC chips. However, in this case, we determined that the PHISON PS8211-0 eMMC chip did not have a different controller voltage for VCCq, meaning that the voltage used was only 3.3v for this example.

When connecting to and interacting with an eMMC device, we usually can utilize the internal power supply of the device. This often works well when different VCC and VCCq voltages are required, but in those cases, we also have to hold the microcontroller unit (MCU) at reset state to prevent the processor from causing interruption when trying to read memory. In this example, we found that the PHISON eMMC chip and NAND memory could be powered by supplying the voltage externally via the SD Card reader.

When using an SD Card reader to supply voltage, we must avoid hooking up the device's normal source of power also. Hooking both sources – normal and SD Card – into the devices will lead to permanent damage to the device.

When it comes to soldering the needed wiring for this exercise, we realized allowing attendees to do the soldering connection would be much more complex than we could support. So, all the wiring was presoldered before the IoT Village event using 30-gauge color-coded wirewrap wire. This wiring was then attached to a [SD Card breakout board](https://shop.exploitee.rs/) as shown below in Figure 1:

* White = Data
* Blue = Clock
* Yellow = Command
* Red = Voltage (VCC)
* Black = Ground

![image-1.png](https://www.rapid7.com/cdn/assets/blt5e388a0e24c70b6f/683ddc0eda5c3083bfa8334b/image-1.png)
![image-2.png](https://www.rapid7.com/cdn/assets/blt6f135044c3ef0021/683ddc32590d7f3bfcde1a0f/image-2.png)

Also, as you can see in the above images, the wires do not run parallel against each other, but have a reasonable gap between them and pass over each other perpendicularly when they cross over. This is because we found during testing that if we ran wires directly next to each other, it caused the partitions to fail to mount properly, most likely because noise was induced into the lines from the other lines affecting the signal.

**Note:** *If you are looking to do your own wiring, the 30-gauge wirewrap wire I used is a* [*Polyvinylidene fluoride*](https://en.wikipedia.org/wiki/Polyvinylidene_fluoride) *coated insulation wire under the brand name of Kynar. The benefit of using Kynar wirewrap is that this insulation does not melt or shrink as easily from heat from the solder iron. When heated by a solder iron, standard plastic-coated insulation will shrink back, exposing uninsulated wire. This can lead to wires shorting out on the circuit board.*

## Connect SD card reader

With the modem wired up to SD Card breakout as shown above we can mount NAND flash memory by connecting a SD Card reader. Note, not all SD Card readers will work, I used a simple trial and error method with several SD Card readers I had in my possession until I found that an inexpensive DYNEX brand reader worked. It should be attached as shown below in Figure 2:

![image-3.png](https://www.rapid7.com/cdn/assets/bltb80d01fec48f6708/683ddc58590d7fa2aede1a1f/image-3.png)

Once plugged in, the various partitions on the Cable modem NAND Flash memory should start loading. In this case a total of seven partitions mounted up. This can take a few minutes to complete. If your system opened each one of the volumes as it mounted, I typically shut them down to avoid all the confusion on your system desktop. To see the layout of the various partitions on the NAND Flash and gather information as needed for reading and writing to the correct partitions. We used the Linux application Disks. Once Disks is opened you can click on the 118 MB Drive in the left column, and it will show all of the partitions and should look something like Figure 3 below:

![image-4.png](https://www.rapid7.com/cdn/assets/blt1f9dbcc2827cae19/683ddc7d543b8d4a28bf105a/image-4.png)

In our second installment of this 4-part blog series, we'll discuss the step of extracting partition data. Check back with us next week!

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F10%2F18%2Fhands-on-iot-hacking-rapid7-at-def-con-30-iot-village-part-1&title=Hands-On%20IoT%20Hacking%3A%20Rapid7%20at%20DEF%20CON%2030%20IoT%20Village%2C%20Part%201)[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F10%2F18%2Fhands-on-iot-hacking-rapid7-at-def-con-30-iot-village-part-1)[![X](/x-logo.s...