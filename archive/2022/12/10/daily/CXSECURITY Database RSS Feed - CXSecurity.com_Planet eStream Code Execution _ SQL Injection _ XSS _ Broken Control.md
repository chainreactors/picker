---
title: Planet eStream Code Execution / SQL Injection / XSS / Broken Control
url: https://cxsecurity.com/issue/WLB-2022120019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-10
fetch_date: 2025-10-04T01:05:19.576712
---

# Planet eStream Code Execution / SQL Injection / XSS / Broken Control

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
|  |  | |  | | --- | | **Planet eStream Code Execution / SQL Injection / XSS / Broken Control** **2022.12.09**  Credit:  **[Philipp Espernberger](https://cxsecurity.com/author/Philipp%2BEspernberger/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45891](https://cxsecurity.com/cveshow/CVE-2022-45891/ "Click to see CVE-2022-45891")** | **[CVE-2022-45890](https://cxsecurity.com/cveshow/CVE-2022-45890/ "Click to see CVE-2022-45890")** | **[CVE-2022-45895](https://cxsecurity.com/cveshow/CVE-2022-45895/ "Click to see CVE-2022-45895")** | **[CVE-2022-45896](https://cxsecurity.com/cveshow/CVE-2022-45896/ "Click to see CVE-2022-45896")** | **[CVE-2022-45893](https://cxsecurity.com/cveshow/CVE-2022-45893/ "Click to see CVE-2022-45893")** | **[CVE-2022-45889](https://cxsecurity.com/cveshow/CVE-2022-45889/ "Click to see CVE-2022-45889")** | **[CVE-2022-45892](https://cxsecurity.com/cveshow/CVE-2022-45892/ "Click to see CVE-2022-45892")** | **[CVE-2022-45894](https://cxsecurity.com/cveshow/CVE-2022-45894/ "Click to see CVE-2022-45894")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")  [CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

SEC Consult Vulnerability Lab Security Advisory < 20221130-0 >
=======================================================================
title: Multiple critical vulnerabilities
product: Planet Enterprises Ltd - Planet eStream
vulnerable version: <6.72.10.07
fixed version: 6.72.10.07
CVE number: CVE-2022-45896, CVE-2022-45893, CVE-2022-45891,
CVE-2022-45889, CVE-2022-45892, CVE-2022-45890,
CVE-2022-45894, CVE-2022-45895
impact: critical
homepage: https://www.planetestream.co.uk
found: 2022-09-01
by: Timon Vogel (Office Vienna)
Philipp Espernberger (Office Linz)
Hrvoje Filakovic (Office Osijek)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Planet eStream is a powerfully simple and secure video platform,
making media more accessible and engaging for students and educators
across secondary, further, and higher education"
Source: https://www.planetestream.co.uk
Business recommendation:
------------------------
The vendor provides an update for the affected version which should
be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the
Planet eStream video streaming platform conducted by security
professionals to identify and resolve potential further security issues.
Vulnerability overview/description:
-----------------------------------
1) Upload of Arbitrary Files Leading to Remote Code Execution (CVE-2022-45896)
The application allows users to upload files at multiple places. It was
identified that it is possible to upload arbitrary malicious files without any
restriction and also without prior authentication! An attacker can upload
a webshell and takeover the system.
2) Account Takeover (CVE-2022-45893)
A problem identified in the cookie and session management of the web application
allows users with low privileges to bypass the authentication and authorization
mechanisms. They can be bypassed by changing the value of the ON cookie. In this way,
users with low privileges can gain access to application features that are only accessible
to administrative and privileged users.
3) Broken Access Control (CVE-2022-45891)
Due to flaws in the authorization scheme, an authorization bypass vulnerability
allows an attacker to get access to restricted functions of the web application.
This can be leveraged to upload files to the web server without authentication
and gain access to restricted content that was uploaded by other users.
4) SQL Injection (CVE-2022-45889)
Due to insufficient input validation, the application allows the injection of
direct SQL commands. By exploiting the vulnerability, an attacker gains access
to all records stored in the database and can execute arbitrary SQL commands.
5) Multiple Stored Cross-Site Scripting (XSS) (CVE-2022-45892)
User input is not properly sanitized or encoded in various places. This leads to
several stored cross-site scripting (XSS) vulnerabilities. By exploiting this
vulnerability, an attacker can persistently embed arbitrary HTML or JavaScript
code into the affected web page. The code is executed in the context of the
victim's browser when visiting the manipulated site. Additionally, users are
potential victims of browser exploits and JavaScript trojans.
6) Reflected Cross-Site Scripting (XSS) (CVE-2022-45890)
One of the application scripts returns unfiltered or unescaped user input. This
leads to a reflected cross-site scripting (XSS) vulnerability. With reflected
cross-site scripting, an attacker can inject arbitrary HTML or JavaScript code
into the victim's web browser. Once the victim clicks a malicious link, the
attacker's code is executed in the context of the victim's web browser. The
vulnerability can be used to change the contents of the displayed site or
redirect to other malicious sites. Additionally, users are potential
victims of browser exploits and JavaScript trojans.
7) Path Traversal (CVE-2022-45894)
Attackers can gain access to files and directories outside the web root through
the use of relative file paths. In this case an authenticated
attacker with any role can inject "..\" sequences into a certain URL parameter
in order to navigate through the file system and access local files.
8) Information Disclosure (CVE-2022-45895)
Parts of the application were discovered that disclose sensitive data to
application users. While securely disclosing necessary information to authorized
users will normally not present a security threat, the identified components
disclose sensitive data that belongs to other users.
Proof of concept:
-----------------
1) Upload of Arbitrary Files Leading to Remote Code Execution (CVE-2022-45896)
Various file upload vulnerabilities were identified in the web application. The
following sections ...