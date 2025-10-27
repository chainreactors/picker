---
title: A journey into IoT – Unknown Chinese alarm – Part 4 – Internal communications
url: https://security.humanativaspa.it/a-journey-into-iot-unknown-chinese-alarm-part-4-internal-communications/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-22
fetch_date: 2025-10-04T02:16:17.907712
---

# A journey into IoT – Unknown Chinese alarm – Part 4 – Internal communications

[![logo](https://hnsecurity.it/wp-content/uploads/2025/09/HN_Security_v2.svg)](https://hnsecurity.it/)

* [Home](https://hnsecurity.it)
* [Company](https://hnsecurity.it/company/)
* [Services](https://hnsecurity.it/services/)
  + [Red Teaming](https://hnsecurity.it/services/red-teaming/)
  + [DORA TLPT](https://hnsecurity.it/services/threat-led-penetration-test-dora/)
  + [AI Red Teaming](https://hnsecurity.it/services/ai-red-teaming/)
  + [Network Assessment](https://hnsecurity.it/services/network-assessment/)
  + [Web Assessment](https://hnsecurity.it/services/web-application-assessment/)
  + [Mobile Assessment](https://hnsecurity.it/services/mobile-application-assessment/)
  + [Mainframe Assessment](https://hnsecurity.it/services/mainframe-assessment/)
  + [Cloud Assessment](https://hnsecurity.it/services/cloud-assessment/)
  + [OT Assessment](https://hnsecurity.it/services/ot-assessment/)
  + [IoT Assessment](https://hnsecurity.it/services/iot-assessment/)
  + [Hardware Assessment](https://hnsecurity.it/services/hardware-assessment/)
  + [Security by Design](https://hnsecurity.it/services/security-by-design/)
* [Blog](https://hnsecurity.it/blog/)
* [Careers](https://hnsecurity.it/careers/)
* [Contacts](https://hnsecurity.it/contacts/)
* [![Italian](https://hnsecurity.it/wp-content/plugins/sitepress-multilingual-cms/res/flags/it.svg)](https://hnsecurity.it/it/blog/a-journey-into-iot-unknown-chinese-alarm-part-4-internal-communications/ "Switch to ")

Get in touch

info@hnsecurity.it

![](https://hnsecurity.it/wp-content/uploads/2025/09/IOT-uai-836x836.jpg)

# A journey into IoT – Unknown Chinese alarm – Part 4 – Internal communications

December 21, 2022|[![Federico Dotta](https://hnsecurity.it/wp-content/uploads/2025/09/Dotta-sm-150x150.jpg)](https://hnsecurity.it/blog/author/federico-dotta/)By [Federico Dotta](https://hnsecurity.it/blog/author/federico-dotta/)

[Articles](https://hnsecurity.it/blog/category/articles/ "View all posts in Articles")

*Disclaimer: as many other security researchers approaching IoT, I have a background in computer science and I started to work on these subjects with little knowledge about electronics and often with a [“YOLO” approach](https://en.wikipedia.org/wiki/YOLO_%28aphorism%29) (blame it on an old colleague of mine 🙂). So, it is definitely possible that many of the things you will read here can be inaccurate or can be done in a much better way, especially with more knowledge in the field. Sorry about that. I take advantage of this disclaimer to add a thing: pay particular attention when you put your hands on electronics, especially when you deal with cheap Chinese devices powered by 220V! Some capacitors can cause serious damages even if the device is not plugged into the electric socket!*

Today we will have a look at the ports we discovered in the [first article](https://hnsecurity.it/blog/a-journey-into-iot-unknown-chinese-alarm-part-1-discover-components-and-ports/) of this [blog series](https://hnsecurity.it/tag/iot/) in our initial analysis with the device powered off. The ports we discovered were the following:

![](https://hnsecurity.it/wp-content/uploads/2022/02/situazione2-1.png)

We already analyzed the SWD port in the [second article of the series](https://hnsecurity.it/blog/a-journey-into-iot-unknown-chinese-alarm-part-2-firmware-dump-and-analysis/), using that port to dump the firmware. Now we will look at the **two potential UART ports** and to the **unknown port named “RF”** on the board.

For this analysis we will use a **logic analyzer**, a hardware device able to read, show and often interpret digital signals. One of the best choices for this type of instrument is the [**Saleae Logic Analyzer**,](https://www.saleae.com/) that comes with an awesome software able to decode multiple protocols on its own. Depending on the model, the original Saleae Logic Analyzer costs from 400€ to 1200€.

Let’s start to analyze the UART communication port between our main ARM microcontroller and the Tuya WB3S wireless module. The easiest way to sniff communications is to connect the Saleae to the pins of the Tuya module, which are quite large on the board and very easy to reach. The documentation of the module gives us the location of the UART pins:

![](https://hnsecurity.it/wp-content/uploads/2022/02/datasheet2_edit-1.png)

The datasheet shows two serial ports (TXD1-RXD1 and TXD2-RXD2), but according to the documentation the second one should not be available to Tuya customers (but obviously **we will verify that**).

### UART Port 1 – Tuya module and ARM microcontroller

Let’s start with the fist serial port (TXD1-RXD1). During our [initial analysis](https://hnsecurity.it/blog/a-journey-into-iot-unknown-chinese-alarm-part-1-discover-components-and-ports/), we hypothesized that this would be some kind of communication port between the main ARM micro-controller and the WiFi Tuya chip.

To sniff communications we need to connect the logic analyzer to the pins of the serial UART port. A quick solution that does not require soldering is to use specific **probes**. At the office we have a great kit of hands-free probes by [SensePeek](https://sensepeek.com/), but when working on this project I was at home and I had only a basic Chinese BDM frame:

![](https://hnsecurity.it/wp-content/uploads/2022/03/PXL_20220224_182105479_edit-scaled-2.jpg)

Once connected, we can run the Saleae software and power on our device. As we can see at the beginning of the track (when the device powers on) both pins pass from “Low” (~0V) to “High” (~3.3V) and then we can see some sort of potential communications (the vertical lines):

![](https://hnsecurity.it/wp-content/uploads/2022/03/saleae1-1.png)

If we zoom into the sections in which we saw the vertical lines, we can clearly see that probably some data is transmitted on those pins:

![](https://hnsecurity.it/wp-content/uploads/2022/03/saleae2-1.png)

We know from the [Tuya documentation](https://developer.tuya.com/en/docs/iot/wb3s-module-datasheet?id=K9dx20n6hz5n4) that this port should be an UART port. The Saleae software already implements some modules name “Analyzers” able to decode many different protocols, including this one (named “Async Serial”). We can go to the “Analyzers” section (at the right) and add a new analyzer of type “Async Serial” on each of our two channels (that I renamed RXD1 and TXD1 for convenience). To be correctly interpreted, the UART protocol requires some **parameters**, among which the **baud rate**, the number of **data bits and stop bits** and the presence of a **parity** **bit.** Old versions of the Saleae software implemented auto-detection of the **baud rate** while newer ones don’t have this feature anymore. Anyhow, there are simple ways to manually estimate this value or we can use a dedicated Saleae plugin for the job, as [described in the Saleae Support website](https://support.saleae.com/protocol-analyzers/analyzer-user-guides/using-async-serial). For data, stop and parity bit we can follow a trial-and-error approach, but usually these protocols use only a couple of different configurations.

Our “Async serial” parameters are the following:

![](https://hnsecurity.it/wp-content/uploads/2022/03/saleae3-1.png)

We can add this analyzer to both our channels and have a look at the decoded data (with a right click on the data we can select different data visualizations: **binary, decimal, hexadecimal or ascii**):

![](https://hnsecurity.it/wp-content/uploads/2022/03/saleae4-1.png)

UART ports work this way: the TX pin of one party is connected to the RX of the other and vice-versa. Each pin is used by a party to transmit and by the other to receive. The names I used in the screenshots are related to the Tuya side and consequently:

* In TXD1 there are communications **from** the Tuya WiFi module **to** the ARM micro-controller
* in RXD1 there are communications **from** the ARM micro-controller **to** the Tuya WiFi module

So, after the boot, the...