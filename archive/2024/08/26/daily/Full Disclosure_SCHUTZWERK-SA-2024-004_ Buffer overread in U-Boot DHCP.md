---
title: SCHUTZWERK-SA-2024-004: Buffer overread in U-Boot DHCP
url: https://seclists.org/fulldisclosure/2024/Aug/38
source: Full Disclosure
date: 2024-08-26
fetch_date: 2025-10-06T18:03:45.334814
---

# SCHUTZWERK-SA-2024-004: Buffer overread in U-Boot DHCP

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

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# SCHUTZWERK-SA-2024-004: Buffer overread in U-Boot DHCP

---

*From*: David Brown via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 23 Aug 2024 13:46:12 +0200

---

```
-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512

Title
=====

SCHUTZWERK-SA-2024-004: Buffer overread in U-Boot DHCP

Status
======

PUBLISHED

Version
=======

1.0

CVE reference
=============

CVE-2024-42040

Link
====

https://www.schutzwerk.com/advisories/schutzwerk-sa-2024-004/

Text-only version:
https://www.schutzwerk.com/advisories/SCHUTZWERK-SA-2024-004.txt

Affected products/vendor
========================

Das U-Boot, https://docs.u-boot.org

Summary
=======
```

Das U-Boot (U-Boot) is a widespread open-source boot loader used in
embedded devices to perform various low-level hardware initialization
tasks and boot the device's operating system kernel. During an embedded
security assessment, we identified a buffer overread vulnerability
(CWE-126) in the DHCP implementation of U-Boot that could leak memory
onto the network. The amount of leaked data depends on the later use of
the hostname, DNS-server IP, gateway IP, or other DHCP options in
unencrypted network traffic. The vulnerability has been present since
the "Initial revision" commit (3861aa5) from 2002.

```
Risk
====
```

An attacker with access to the local network and faster response times
than the default DHCP server can trigger a memory leak by responding
with malicious DHCP offers to a vulnerable U-Boot DHCP client. In the
current implementation, only 4 Bytes of data can be leaked via gateway
or DNS server address. When net\_hostname would be used and also sent
over the network, 32 Bytes could be retrieved. When the bp\_vend field is
filled with zeroes besides the magic number, it could also lead the loop
to continue outside the packet to process data. This can cause further
data to be leaked when values like 0x1,0x3,0x6, and 0x12 are present in
that data. When further vulnerabilities can be found they might be
combined to achieve further harmful impact to the system.

```
Description
===========
```

After U-Boot sends an initial DHCP request, the vulnerable bootp\_handler
gets registered as a callback for incoming packets. The handler first
checks if the received packet is the expected reply packet. If
VENDOR\_MAGIC is in the first four bytes of bp->bp\_vend, the address of
bp->bp\_vend[4] and the total length of the packet is passed to
bootp\_process\_vendor (net/bootp.c:381) without being reduced to
len-(offsetof(struct bootp\_hdr,bp\_vend)+4). There is also a missing
check whether the first four bytes of bp->pb\_vend[] are in range of the
packet length before retrieving them to compare with htonl(VENDOR\_MAGIC).

```

```

In bootp\_process\_vendor, an incorrect end address is then calculated
based on the full packet length (net/bootp.c:312) instead of the rest of
the bp\_vend buffer size. Then, the function increases the ext pointer
until it no longer points to zero bytes within the too-long buffer range
or when one byte is 0xff. When a none-zero value is discovered the ext
pointer is passed to bootp\_process\_vendor\_field.

```

```

In bootp\_process\_vendor\_field, the de-referenced value of the passed
pointer is used to select the case for processing the field, and its
length is de-referenced from ext+1. Based on the selected case, values
are then copied to variables and buffers like net\_gateway.s\_addr or
net\_hostname from ext+2. The copied lengths are only limited by the size
of their destination. The end of the bp\_vend structure or the end of the
packet is never checked in bootp\_process\_vendor\_field.

```

```

This allows an attacker, who can respond to DHCP requests, to craft a
packet that causes the code to copy the contents of the target's RAM
directly following the received packet into parameters. These parameters
are sent via the network during later use, leaking the RAM content to
the attacker.

```
Solution/Mitigation
===================
```

We recommend providing an adequate length to bootp\_process\_vendor to
prevent the while loop from stepping outside the packet frame and
checking in bootp\_process\_vendor\_field if the copied data is still
within the packet structure's range.

```
Disclosure timeline
===================

2024-06-21: Vulnerability discovered
```

2024-08-19: Vulnerability reported to public mailing list by request of
maintainer.

```
Contact/Credits
===============
```

The vulnerability was discovered during an assessment by Simon Diepold
of SCHUTZWERK GmbH.

```
References
==========

Disclaimer
==========

The information provided in this security advisory is provided "as is" and
```

without warranty of any kind. Details of this security advisory may be
updated

```
in order to provide as accurate information as possible. The most recent
version of this security advisory can be found at SCHUTZWERK GmbH's website
( https://www.schutzwerk.com ).

SCHUTZWERK Advisories: https://www.schutzwerk.com/blog/tags/advisories/

SCHUTZWERK Advisory Policy: https://www.schutzwerk.com/en/advisories/
-----BEGIN PGP SIGNATURE-----

iQJOBAEBCgA4FiEEgLsg7Oj/wY3LSF87GrXfkTIXLrsFAmbC+YgaHGFkdmlzb3Jp
ZXNAc2NodXR6d2Vyay5jb20ACgkQGrXfkTIXLrtSeRAAi6OrwHBpbFgKlyqROQnw
zYxmHTYBiWzBEEmI1zN+iNb5uQlnZXgBoodbEneiRmVQDSiT4zT/DWe3EGV2TlRR
56hEIGvkvleURqCjwRYeYnPF3Ef/XMTvTu/x08h8UfGr7XNwhwCpANxUTE7aI01b
jZLa4jDv8vpNd7JKNF32S2Ak6GRjfEE9aEAxUKliNXCA5SU1gYvOWQ+BJ0oth7fN
grkTKffltk8dUBFy8TsrxcAG5ye4f1Dvm51dU8JNPBLkmouOrEvX1K4UTjvAyD8e
bCn2dXs2rDLfywrTPV0k2zj3APZiwhYxNA3MaTUGscZAIUMn3WE/cUyYDpQDqOYx
wrZzz9K59m+x8F6c1lBUxlmU3t9Z15/i/tL6Kropb+HDxjWaLCZPG3dzdlR54/fn
gvzS393FNWakNNAJIqN2jvvol+zvJGn2rsSsfp5CPEdrQEHgvQa0TkBOpdtFZ/h1
muVFwj9yDup07yStTXRJHjg2WCH0LdL5x+mDfcBspjLflpVP/0Yj+MnR8e3Eb7v/
Cb12PeBHww9VObUhgbMecanSn6Epf7Nc5a5wIh5kEWKoviBYNY/0cu7GDN+70PK4
JhD86Tww5RFJJfkLcJqlCAMC4AkAc7Sq5FS7WTK5Jx3Ymh/+Lsuhx9ENq38VyVGh
tFe3V0joTUxg7Yy78PoEOrs=
=XKZo
-----END PGP SIGNATURE-----

--
SCHUTZWERK GmbH, Pfarrer-Weiß-Weg 12, 89077 Ulm, Germany
Zertifiziert / Certified ISO 27001, 9001 and TISAX

Phone +49 731 977 191 0

advisories () schutzwerk com / www.schutzwerk.com

Geschäftsführer / Managing Directors:
Jakob Pietzka, Michael Schäfer

Amtsgericht Ulm /  HRB 727391
Datenschutz / Data Protection www.schutzwerk.com/datenschutz
```

**Attachment:
[OpenPGP\_0x1AB5DF9132172EBB.asc](att-38/OpenPGP_0x1AB5DF9132172EBB_asc.bin)**
*Description:* OpenPGP public key

**Attachment:
[OpenPGP\_signature.asc](att-38/OpenPGP_signature_asc.bin)**
*Description:* OpenPGP digital signature

```
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](37)
[By Date](date.html#38)
[![Next](/images/right-icon-16x16.png)](39)

[![Previous](/images/left-icon-16x16.png)](37)
[By Thread](index.html#38)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **SCHUTZWERK-SA-2024-004: Buffer overread in U-Boot DHCP** *David Brown via Fulldisclosure (Aug 24)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap...