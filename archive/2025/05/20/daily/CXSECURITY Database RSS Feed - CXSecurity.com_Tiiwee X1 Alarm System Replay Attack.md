---
title: Tiiwee X1 Alarm System Replay Attack
url: https://cxsecurity.com/issue/WLB-2025050039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-20
fetch_date: 2025-10-06T22:23:23.053275
---

# Tiiwee X1 Alarm System Replay Attack

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Tiiwee X1 Alarm System Replay Attack** **2025.05.19**  Credit:  **[Sebastian](https://cxsecurity.com/author/Sebastian/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-294](https://cxsecurity.com/cwe/CWE-294 "Click to see CWE-294")** | |

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA512
Advisory ID: SYSS-2025-006
Product: Tiiwee X1 Alarm System
Manufacturer: Tiiwee B.V.
Affected Version(s): TWX1HAKV2
Tested Version(s): TWX1HAKV2
Vulnerability Type: Authentication Bypass by Capture-replay
(CWE-294)
Risk Level: CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N
Solution Status: Open
Manufacturer Notification: 2025-01-27
Public Disclosure: 2025-05-12
CVE Reference: CVE-2025-30072
Author of Advisory: Sebastian Auwärter, SySS GmbH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Overview:
Tiiwee X1 Alarm System is an alarm system which contains a base station
and
various components like motion detectors, door sensors and remotes. The
components communicate via 433 MHz radio signals.
The manufacturer describes the product as follows (see [2]):
"The Tiiwee Alarm Kit is a versatile alarm system that detects if
people or
animals are entering your home or shop."
Due to missing security features like key rolling or encryption in the
433 MHz
radio communication, the alarm system is vulnerable to replay attacks.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Vulnerability Details:
The radio signal of the alarm system remote can be captured and
replayed using
appropriate antennae and, for example, software-defined radio software.
Once
any signal from the software is captured, it can be either directly
replayed
(in case the "disarm" signal is captured) or recalculated and sent (in
case
only the "arm" signal is captured).
According to the Flipper Zero (see [3]) used, the protocol is
"Princeton",
which contains an ID that is being evaluated for arming and disarming
the
alarm system. For calculating the ID of the signal for disarming if
only the
signal for arming has been captured, subtract two from the ID.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Proof of Concept (PoC):
Using a Flipper Zero hardware, go to Sub-GHz. Read and capture the
signals for
disarming the alarm system by pressing the disarm button on a remote.
Arm the
alarm system again by pressing the arm button on the remote. Now, the
alarm
system can be disarmed again by selecting and sending the captured
signal using
the Flipper Zero.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Solution:
Do not use this device if capture replay attacks are a valid attack
vector for
your assets.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Disclosure Timeline:
2025-01-22: Vulnerability discovered
2025-01-27: Vulnerability reported to manufacturer
2025-05-12: Public disclosure of vulnerability
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
References:
[1] Amazon link for the Tiiwee X1 Alarm System
https://www.amazon.de/dp/B08B8T95NH
[2] Product manual for the Tiiwee X1 Alarm System
https://cdn.shopify.com/s/files/1/1880/6197/files/Manual\_Tiiwee\_X1\_ALL\_LANGUAGES\_WEB.pdf?406
[3] Flipper Zero homepage
https://flipperzero.one/
[4] SySS Security Advisory SYSS-2025-006
https://www.syss.de/fileadmin/dokumente/Publikationen/Advisories/SYSS-2025-006.txt
[5] SySS Responsible Disclosure Policy
https://www.syss.de/en/responsible-disclosure-policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Credits:
This security vulnerability was found by Sebastian Auwärter of SySS
GmbH.
E-Mail: sebastian.auwaerter@syss.de
LinkedIn: https://de.linkedin.com/in/sebastian-auw%C3%A4rter-156035305
Public Key: https://www.syss.de/kontakt/pgp-keys
Key Fingerprint: F98C 3E12 6713 19D9 9E2F BE3E E9A3 0D48 E2F0 A8B6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Disclaimer:
The information provided in this security advisory is provided "as is"
and without warranty of any kind. Details of this security advisory may
be updated in order to provide as accurate information as possible. The
latest version of this security advisory is available on the SySS
website.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~
Copyright:
Creative Commons - Attribution (by) - Version 4.0
URL: https://creativecommons.org/licenses/by/4.0/deed.en
-----BEGIN PGP SIGNATURE-----
iQIzBAEBCgAdFiEE+Yw+EmcTGdmeL74+6aMNSOLwqLYFAmgi8DwACgkQ6aMNSOLw
qLaYFA/9FPRpn9F+eNEyQe205Kvu0Fwyq9eLOiDHkFDhnx3AFwg/AnrLqFoxjuRA
r2G5RGc6CluvRTaR5y40F6wCb4QhGr51UhhClRcfQJ7wt0yOAGwiAEMgHHDjDcc/
Tm2O/zHPheS+MGHA/S7jUU2nCac/0/T1IJr5KaWJ7jOsR+2v8fLXk3fG5wX3sSNe
b4bPkSR6Sjtx7nEdTnEsSbU2bT5h/0PEQdtBEv6vOGNpDmAWCyNgAnnuhCuH8jy0
6/19vQeb5Wu+dA+x3z/n4jrHTW8U5WkemCWDZoCtCQ+XDL0fSsipsQJ+Au/Bv2rT
yB+/8nakbvcxb6kPwkqOJ4cUMUIeHO6xUcM15I3pivvdmFQIR8uwzQOLSYji0tQG
6bA3HZ8gFBsIfDkwdevaXWiq+dlbVJKUEO8bnb0tIDeSw/KoAmWTV7Hcmu8Fai4g
fpYfi0G6BcQL5SrXww6Ouhv9N3SmeR6Dn+HYNOGC4vfmyMlkpmjMmaHNGLHacqhy
J6+FNQKgfhE027mQnJaMP8SQoK8bpeNyEmUEdAIZa/YHJywcCAQ5g8SqYwwnewm2
LAUnT++BHRYB4jPplvkfCVP1dGGCSuVxErDV6xruK9WZjyDcz4rImhd38Tf2JiOA
AXbhtaffbSGKwGTEj7GnXhfgxNipFq570fWnAx+bkbEmWRLdJAo=
=ANhN
-----END PGP SIGNATURE-----

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050039)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top