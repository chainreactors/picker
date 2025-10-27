---
title: Kiuwan Local Analyzer / SAST / SaaS XML Injection / XSS / IDOR
url: https://cxsecurity.com/issue/WLB-2024060029
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-06-11
fetch_date: 2025-10-06T16:54:18.507102
---

# Kiuwan Local Analyzer / SAST / SaaS XML Injection / XSS / IDOR

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
|  |  | |  | | --- | | **Kiuwan Local Analyzer / SAST / SaaS XML Injection / XSS / IDOR** **2024.06.10**  Credit:  **[C. Schwarz](https://cxsecurity.com/author/C.%2BSchwarz/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2023-49112](https://cxsecurity.com/cveshow/CVE-2023-49112/ "Click to see CVE-2023-49112")** | **[CVE-2023-49113](https://cxsecurity.com/cveshow/CVE-2023-49113/ "Click to see CVE-2023-49113")** | **[CVE-2023-49110](https://cxsecurity.com/cveshow/CVE-2023-49110/ "Click to see CVE-2023-49110")** | **[CVE-2023-49111](https://cxsecurity.com/cveshow/CVE-2023-49111/ "Click to see CVE-2023-49111")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

SEC Consult Vulnerability Lab Security Advisory < 20240606-0 >
=======================================================================
title: Multiple critical vulnerabilities
product: Kiuwan SAST on-premise (KOP) & cloud/SaaS
Kiuwan Local Analyzer (KLA)
vulnerable version: Kiuwan SAST <2.8.2402.3
Kiuwan Local Analyzer <master.1808.p685.q13371
Kiuwan SaaS before 2024-02-05
fixed version: Kiuwan SAST 2.8.2402.3
Kiuwan Local Analyzer master.1808.p685.q13371
Kiuwan SaaS after 2024-02-05
CVE number: CVE-2023-49110, CVE-2023-49111, CVE-2023-49112
CVE-2023-49113
impact: critical
homepage: https://www.kiuwan.com
found: 2022-10-28
by: C. Schwarz (Office Bochum)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Thorough code inspection is essential for designing secure software products.
While your development team may not have time to comb through every line of code,
Kiuwan does. For 20 years, it has been the choice of developers to scan code
automatically and remediate defects according to security standards like OWASP,
CWE, SANS, and CERT.
Static application security testing (SAST) scans for security flaws in the source
code without running the program. It is a white-box testing method that is the
counterpart to dynamic application software testing (DAST), which tests web applications
for run-time vulnerabilities. [...]
Our code vulnerability scanning tools create an all-encompassing process that
begins in the early stages of development and continues into production. Kiuwan’s
static application security testing software fits perfectly into any DevOps environment.
It uses a distributed engine and fast analysis to silently add security without
causing a bottleneck in your workflows. [...]"
Source: https://www.kiuwan.com/code-security-sast/
Business recommendation:
------------------------
The vendor provides a patched version for Kiuwan On-Premise (master.1808.p685.q13371)
which should be installed immediately.
Although initially communicated otherwise during responsible disclosure in 2022-2023
(see timeline below), the vendor confirmed in 2024 that the SaaS/cloud version is affected
and will also be patched. The patch date was 2024-02-05, version 2.8.2402.3.
An in-depth security analysis performed by security professionals is highly advised,
to identify and resolve potential further critical security issues and to verify whether
the developed patches really mitigate the identified critical security issues.
SEC Consult also submitted further security issues to Kiuwan, such as Docker-related
configuration issues which were also fixed during our responsible disclosure.
Vulnerability overview/description:
-----------------------------------
1) XML External Entity Injection (CVE-2023-49110)
When the Kiuwan Local Analyzer uploads the scan results to the web app (either
on-premises or cloud/SaaS solution), the transmitted data consists of a ZIP
archive containing several files, some of them in the XML file format.
During Kiuwan's server-side processing of these XML files, it resolves external
XML entities, resulting in a XML external entity injection attack.
An attacker with privileges to scan source code within the "Code Security"
module is able to extract any files of the operating system with the rights
of the application server user and is potentially able to gain sensitive files,
such as configuration and passwords. Furthermore, this vulnerability also
allows an attacker to initiate connections to internal systems, e.g. for
port scans or accessing other internal functions / applications such as the
Wildfly admin console of Kiuwan.
2) Services running as root
The Kiuwan web app process is configured to run with root privileges. In case
an attacker can compromise the application (such as documented in 1), this
provides them with unrestricted access to the system.
3) Reflected Cross-Site-Scripting (CVE-2023-49111)
For Kiuwan installations with SSO (single sign-on) enabled, an unauthenticated
reflected cross-site scripting attack can be performed on the login page. This
is possible due to some request parameter values being directly included in a
JavaScript block in the response. This is especially critical in business
environments using AD SSO authentication, e.g. via ADFS, where attackers
could potentially steal AD passwords.
4) Insecure Direct Object Reference (CVE-2023-49112)
Kiuwan provides an API endpoint to get information about any application,
providing only its name. This endpoint lacks proper access control mechanisms,
allowing other authenticated users to read information about applications, even
though they have not been granted the necessary rights to do so.
5) Sensitive Data Stored Insecurely (CVE-2023-49113)
The Kiuwan Local Analyzer (KLA) Java application contains several hard-coded secrets in
plain text format. In some cases, this can potentially compromise the confidentiality
of the scan results.
Proof of concept:
-----------------
1) XML External Entity Injection (CVE-2023-49110)
The scan results of the Kiuwan Local Analyzer (KLA) are transmitted to the Kiuwan
server (KOP on-premise or SaaS) using several XML files packed in a ZIP archive. Even
though the initial upload only contains encrypted .bxml...