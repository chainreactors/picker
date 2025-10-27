---
title: Fuzzing µC/OS protocol stacks, Part 3: TCP/IP server fuzzing, implementing a TAP driver
url: https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-3/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-29
fetch_date: 2025-10-06T18:07:26.379367
---

# Fuzzing µC/OS protocol stacks, Part 3: TCP/IP server fuzzing, implementing a TAP driver

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2024/08/VulnDeepDive--1--3.png)

# Fuzzing µC/OS protocol stacks, Part 3: TCP/IP server fuzzing, implementing a TAP driver

By
[Kelly Patterson](https://blog.talosintelligence.com/author/kelly/)

Wednesday, August 28, 2024 12:00

[Vulnerability Deep Dive](/category/vulnerability-deep-dive/)

This is the final post in the three-part series that details techniques I used to fuzz two µC/OS protocol stacks: µC/TCP-IP and µC/HTTP-server.

[The first post](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-1/) highlighted code modifications necessary for developing a fuzzing harness tailored for the µC/HTTP-server. [The second](https://blog.talosintelligence.com/fuzzing-ucos-protocol-stacks-part-2/) discussed a technique for delivering multiple requests per fuzz test case. Finally, I’ll detail the code modifications required for fuzzing the µC/TCP-IP stack. Please refer to the first post in the series for a description of Real-Time Operating Systems (RTOS) and the motivations for this research project.

My goals in fuzzing µC/TCP-IP are the same as for µC/HTTP-server:

* Use a modern fuzzing framework (I chose AFL++).
* Modify the networking code to accept input from a file.
* Handle multiple requests per test case.

Self-imposed constraints:

* A software-only solution.
* Run natively on Linux.

I wanted to find a straightforward way to fuzz this code without relying on emulation or dedicated hardware.

# Linux port

To utilize the AFL++ fuzzing framework, this code must run on Linux rather than µC/OS. This is a similar challenge I faced in [Part 1](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-1/). This time, however, I opted to use the POSIX KAL implementation that µC/OS provided rather than develop my own. This architecture diagram shows the layout of the various software components of µC/OS. The blue highlight represents the components I will be modifying to port the application to Linux. The orange highlight represents the code that’s the fuzzer’s target.

![](https://blog.talosintelligence.com/content/images/2024/08/FuzzingProtocolStacks-Architecture1.jpg)

With my µC/HTTP-server fuzzing harness, I decided against using the provided POSIX KAL implementation. The µC/HTTP-server code I was targeting did not use many of the OS components, so it was simple to implement my own minimalist KAL interface. In contrast, the µC/TCP-IP implementation uses a separate task for receiving data and uses semaphores and message queues requiring a more complete KAL implementation.

Using the code provided by µC/OS felt like taking a shortcut. It was painless and worked right out of the box with only minor modifications. That’s not something that I can say for working with the networking side of things, which required a lot of development.

# Network port

## TAP device

My primary goal for the fuzzer is to enable it to accept network data from a file. To start, I adopted the strategy I used for my µC/HTTP-server, which involves ensuring my program functions with actual network data. Doing this initially allows for more straightforward debugging and testing of my code, as I can use standard Linux utilities to send real network traffic to my program.

It was a bit more complicated to get data from the network to be processed by µC/TCP-IP than it was for µC/HTTP-server. This is because TCP/IP is a lower-level protocol than HTTP. HTTP is an application layer protocol while TCP/IP is a transport layer protocol. Typically, user mode applications interact with the network at the application layer via POSIX sockets or a NetSock for µC/OS.

In Linux, when using sockets, the kernel manages the TCP/IP processing and only delivers application layer data to the user mode application. However, my challenge was that my user mode µC/TCP-IP application is intended to handle the TCP/IP protocol itself. To bypass the kernel’s TCP/IP stack, I utilized a TAP device — a purely software-based kernel virtual network device.

Although this module is called µC/TCP-IP, it actually covers multiple layers of the OSI model. The layers circled in orange indicate layers of the OSI model for which the µC/TCP-IP module will process:

![](https://blog.talosintelligence.com/content/images/2024/08/FuzzingProtocolStacks-OSI_highlight.jpg)

The µC/TCP-IP code is expecting to receive an Ethernet frame, and it includes handlers for ARP, IP, TCP and UDP. Because µC/TCP-IP is expecting to receive Ethernet frames, a TAP device should be used because it transfers Ethernet frames unlike a TUN device which transfers IP packets.

A TAP device is meant to be used by user space programs that attach to it. When the operating system sends packets to a TAP device, they are delivered to the attached user space program. Conversely, packets sent by the user-space program to the TAP device are injected into the kernel network stack as if they originated from an external source.

To use a TAP device, I wrote my own Ethernet device driver using the API provided by µC/TCP-IP. I needed to create and configure my TAP device with the driver and implement functions to transmit and receive data. Again, µC/OS was great to work with for this because their API was well-defined and documented. Additionally, there are dozens of device drivers in the µC/TCP-IP repository for various ethernet hardware. Having all this example code and documentation was immensely helpful. In implementing this, I used the open-source [tapip utility](https://github.com/chobits/tapip) as a guide for creating and configuring a TAP device within my µC/TCP-IP Ethernet driver.

The most confusing part of this was visualizing the network topology involving the TAP device. I created and assigned the TAP device an IP address of 10.10.10.1 and the Linux kernel assigned it a MAC address of 46...