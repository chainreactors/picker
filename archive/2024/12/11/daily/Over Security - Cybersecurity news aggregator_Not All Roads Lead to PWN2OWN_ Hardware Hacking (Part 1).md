---
title: Not All Roads Lead to PWN2OWN: Hardware Hacking (Part 1)
url: https://www.hacktivesecurity.com/index.php/2024/12/10/not-all-roads-lead-to-pwn2own-hardware-hacking-part-1/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-11
fetch_date: 2025-10-06T19:49:33.503553
---

# Not All Roads Lead to PWN2OWN: Hardware Hacking (Part 1)

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Exploitation](https://www.hacktivesecurity.com/blog/category/expl/)
* Not All Roads Lead to PWN2OWN: Hardware Hacking (Part 1)

[Exploitation](https://www.hacktivesecurity.com/blog/category/expl/) [Internet of Things](https://www.hacktivesecurity.com/blog/category/iot/) [Reverse Engineering](https://www.hacktivesecurity.com/blog/category/reverse-engineering/)

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/12/Screenshot-from-2024-12-10-17-52-02.png)

\_ [December 10, 2024](https://www.hacktivesecurity.com/blog/2024/12/10/not-all-roads-lead-to-pwn2own-hardware-hacking-part-1/)\_ [Alessandro Groppo](https://www.hacktivesecurity.com/blog/author/kiks/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2024/12/10/not-all-roads-lead-to-pwn2own-hardware-hacking-part-1/#respond)

### Not All Roads Lead to PWN2OWN: Hardware Hacking (Part 1)

## Introduction

Not all stories end with the expected and hoped-for results, and this story is one of them. We’re releasing a three-part series detailing our unsuccessful [Pwn2Own](https://en.wikipedia.org/wiki/Pwn2Own) 2024 attempt targeting two IP cameras. The contest forces you into a completely different mindset compared to standard security assessment activities. Here, you have only one objective: compromise the target with an unauthenticated RCE exploit. This creates the purest hacking vibes that with a mix of passion and challenge flows directly into pure excitement.

That excitement, however, led to one of the key causes of our failure: a temporary “burnout.” For several reasons, we lost too much time (~75%) and effort stuck in the initial phase of obtaining the first interactive shell on just one device (we had purchased two devices). This left us with insufficient time to focus on the core phase: finding vulnerabilities, despite the unstable shell we had via a customized firmware.

However, this two-week journey (not much time for this kind of activity) proved incredibly valuable, providing numerous lessons we’ve since shared internally to maximize the positive impact. Along the way, we delved into hardware hacking, reverse engineering, firmware and kernel module patching, fuzzing and crash triaging (**yes, we have discovered some non-exploitable bugs**). If you’re intrigued by these hacky things, hope you will find this hardware hacking article interesting and, stay tuned for the upcoming parts too!

Most of our initial effort focused on the Lorex 2K IP camera. We highly encourage you to also explore the published work of other teams that successfully participated in the Pwn2Own contest: [Pwn2Own IoT 2024 – Lorex 2K Indoor Wi-Fi Security Camera](https://www.rapid7.com/globalassets/_pdfs/research/pwn2own-iot-2024-lorex-2k-indoor-wi-fi-security-camera-research.pdf) and [Exploiting the Lorex 2K Indoor Wi-Fi at Pwn2Own Ireland](https://blog.infosectcbr.com.au/2024/12/exploiting-lorex-2k-indoor-wifi-at.html).

## **Hardware Teardown: Laying the Foundation**

Every good reversing process begins with understanding the target. Disassembling the Lorex 2K IP Camera was the first step in uncovering its attack surface. Carefully dismantling the camera’s enclosure (pro tip: a precision screwdriver toolset is your best friend) by disconnecting the unnecessary/unwanted accessories (IR, LED, Microphone, ..), provided access to key components and revealed crucial interfaces.

A **System-on-Chip (SoC), Micro-SD Card slot, Wi-Fi SoC and two Unknown Entry Points:** from the label we got a Sigmastar SSC337D as the device’s processing core managing all device operations and Realtek RTL8188E as the WiFi chipset. Some unknown entries test points on the PCB suggested accessible UART, SPI, and Ethernet pinouts – prime candidates for hardware exploitation.

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/12/image-12-1024x1024.png)

**SPI Flash:** Winbond W25Q64JV, a 64Mb memory chip storing the firmware.

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/12/image-13-1024x1024.png)

## Step 1: UART Discovery

![](https://www.hacktivesecurity.com/wp-content/uploads/2024/12/image-14.png)

The **Universal Asynchronous Receiver-Transmitter (UART)** is a simple two-wire protocol for exchanging serial data. Asynchronous means no shared clock, so for UART to work, the same bit or baud rate must be configured on both sides of the connection. This interface is often a go-to entry point for hardware hackers. The first...