---
title: The Foreigner – A (not so) quick and dirty drop box for Red Teamers
url: https://labs.yarix.com/2022/12/the-foreigner-a-not-so-quick-and-dirty-drop-box-for-red-teamers/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-30
fetch_date: 2025-10-04T02:45:45.082364
---

# The Foreigner – A (not so) quick and dirty drop box for Red Teamers

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# The Foreigner – A (not so) quick and dirty drop box for Red Teamers

* [Home](https://labs.yarix.com "Go to Home Page")
* The Foreigner – A (not so) quick and dirty drop box for Red Teamers

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2022/12/artblog-1140x445.jpg)

29Dec29/12/2022

## The Foreigner – A (not so) quick and dirty drop box for Red Teamers

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2022-12-29T17:18:11+01:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   17 minutes

Some time ago, the Yarix Red Team was engaged on a red team assessment that included an onsite activity to test the physical security posture of the Customer. Although we would have used social engineering tactics to physically enter the Customer property, this would have given us a too short amount of time to stay connected to its internal network for a deep analysis of it. We therefore decided to build a small, remotely controlled drop box that would be hidden in the Customer’s premises and connected directly to its internal network, hoping that it would not be detected. However, we only had a couple of weeks before onsite activity began, so we had to build and test the drop box as quickly as possible while using as many components as we already had on hand. In this article, we will describe the components we used, the scripts and configurations we made, the challenges we faced and how we solved them.

## The ~~big~~ small picture

As many of you may know, a drop box is a piece of equipment with different purposes which is intended to be left unattended on a targeted place. Will it be a customer office or data center, a public location or where else, if detected it can be lost or destroyed, so it must be cheap enough to justify its loss. In addition, it must also be small enough so that it can be hidden or made to go as unnoticed as possible. Nowadays, there are many possibilities to build such a device, since many different single-board computers exist and they are quite common due to their low cost.

However, because of the pandemic caused by the Covid-19 virus first and the current geopolitical environment later, we are in the midst of a microchip shortage that has led to the rising cost of these kind of computers. For example the Raspberry Pi Foundation, known for their cheap but powerful single-board computers, [had to increase their prices](https://www.raspberrypi.com/news/supply-chain-shortages-and-our-first-ever-price-increase/) for the first time ever. This made difficult to buy a new board which had an affordable price and that was available for delivery in a couple of days. Luckily, as said, they are common and we already had a Raspberry Pi 3 available in our lab. Thanks to its versatility, by simply swapping the micro SD from a previous project with a 32GB one, also already available to us, we were ready to start the installation of the operating system. Of course, if in the future we need to use the Raspberry Pi with the old project, we just need to swap back the micro SDs and we will be ready to go, obviously if it will not be somewhere in the field!

Before we start fiddling with the project, we had one more key point to unmark. The purpose of this drop box is to give us a direct but remote access to the Customer internal network and to achieve it we must be able to reach the device in some way. Many of the articles that can be found on the Internet explaining how to create a drop box, rely on leveraging the client’s network to connect to a remote control server. This is certainly the easiest scenario to implement since all that is needed is to setup DHCP on the drop box’s ethernet interface and obtain an IP address on the target network, but this does not mean that the connection to the Internet is a given. In fact, restrictions on browsing may be in place that can range from limiting available ports (e.g., ports 80 and 443 can be open to outgoing connections but not port 22), to the complete block of all egress ports and the use of a proxy server. Finally, of course, a DHCP server could not be available in the network, resulting in a failure from the very beginning.

For these reasons, we decided to add a module that could provide Internet access to the Raspberry Pi via the cellular network, thus making it autonomous. A few options are available, and the most noteworthy ones are cellular USB dongles and Hardware Attached on Top (HAT). While the former are typically less expensive and easier to use, their USB dongle form factor add chunkiness to the drop box, making it harder to hide. Moreover, those dongles may be bound to a specific cellular carrier. Raspberry Pi HATs, on the other hand, ship more features and allow for greater expandability, despite being more difficult to set up, especially at the beginning. Furthermore, although higher than a USB dongle, their price is still affordable.

## Components list

Below is the complete list of the components we used in this project (mostly hardware) and a brief description of them.

* **Raspberry Pi 3 Model B rev 1.2:**The backbone of all the project, this single-board credit card sized computer can run an ARM version of Linux that has almost all the functions that you will find on a regular computer distro; moreover, its built-in ethernet interface is perfect to quickly connect it to the target network.
* **Sandisk Ultra Micro SDHC Class 10 32 GB:** A spare micro SD memory card that we had in our lab; its 32GB capacity is more than enough to hold the operating system and any additional packages we might need.
* **5V USB power supply:** While testing the drop box, we initially used a generic purpose 5V 4A power supply but then, as we will explain later in this article, we switched to a 5.2V power supply to achieve more stability.
* **Power bank:** a generic 16750mAh (5V, 2.4A) power bank that we used on the field to power the drop box.
* **Waveshare SIM7600E-H 4G HAT:** The broadband cellular network HAT module we chose, it supports all cellular network standards up to 4G; it also has a lot of features, many of which are out of scope for this article, but that can be used for future additions (e.g., the GPS module or the breakout pins to connect an Arduino)
* **SIM cards:** The HAT supports many 3G and 4G bands and isn’t bound to a specific cellular carrier, so it is possible to use different SIM cards; in this case we used two SIMs from two distinct Italian operators.
* **Amazon EC2 Linux instance:** A simple Linux instance that we used as the control server the drop box connects to; as we will see, it did not need many configurations to be ready.

## Raspberry Pi

The first step we needed to do was to choose the operating system to be installed on the Raspberry Pi (RPi). Of course it would be Linux based and, while Raspbian (one of the most used RPi Linux distribution based on Debian) could be a good choice, we chose the ARM version of Kali Linux, since it represents the de facto choice for penetration testing and red teaming. In fact, in case we needed any tool during the activity, it would already be present by default or would be easily obtainable and/or installable. The ARM image for the Raspberry Pi is available on the [Kali Linux download page](https://www.kali.org/get-kali/#kali-arm) and, based on the advices found on their [user instructions page](https://www.kali.org/docs/arm/raspberry-pi-3/), we chose the 32-bit version over the 64-bit one because the for...