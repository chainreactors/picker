---
title: SEC Consult SA-20221130-0 :: Multiple critical vulnerabilities in Planet Enterprises Ltd - Planet eStream
url: https://seclists.org/fulldisclosure/2022/Dec/5
source: Full Disclosure
date: 2022-12-10
fetch_date: 2025-10-04T01:09:05.175956
---

# SEC Consult SA-20221130-0 :: Multiple critical vulnerabilities in Planet Enterprises Ltd - Planet eStream

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

[![Previous](/images/left-icon-16x16.png)](4)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](4)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20221130-0 :: Multiple critical vulnerabilities in Planet Enterprises Ltd - Planet eStream

---

*From*: "SEC Consult Vulnerability Lab, Research via Fulldisclosure" <fulldisclosure () seclists org>
*Date*: Wed, 30 Nov 2022 12:01:18 +0000

---

```
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
following sections describe the vulnerabilities in detail.

The file upload is restricted to certain file types in some cases. This
restriction is only enforced in the frontend and can be bypassed by
intercepting the request and modifying it. There is no further validation of
uploaded files in the backend. Therefore, it is sufficient to change the
filename ending in the intercepted request.

a) File Upload with Path Traversal

An authenticated attacker with the permission to attach documents to already
existing content (e.g. videos) can upload any file. In some cases, the role
Member is sufficient. Under "Categories -> choose a video -> related Media" a new
malicious file can be uploaded.

The following POST request is sent to the server when a normal PNG file is uploaded:
===============================================================================
POST /Upload2.ashx?f=seclogo.png&c=0&l=53134&t=1662103112126&p=\Temp&ut=0&tc=0&bs=53134&ct=1662103112126 HTTP/2
Host: $host
Cookie: [...]

‰PNG
[...]
===============================================================================

Based on the previous POST request to upload files, the request can be
manipulated to upload any content to any directory by using path traversal
techniques. The following code shows the modified request. The content is
changed from a PNG image to an ASP web shell. The filename ending is changed to
asp and the path is inserted into the p parameter, which is vulnerable to path
traversal.
===============================================================================
POST /Upload2.ashx?f=webshell.asp&c=0&l=1024&t=1661943922096&p=..\$path\&ut=0&tc=0&bs=1024&ct=1661943922097 HTTP/2
Host: $host
Cookie: [...]

$ASPWEBSHELL
========================================================================...