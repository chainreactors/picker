---
title: Intel Data Center Manager 4.1 SQL Injection
url: https://cxsecurity.com/issue/WLB-2022120022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-10
fetch_date: 2025-10-04T01:05:16.326771
---

# Intel Data Center Manager 4.1 SQL Injection

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
|  |  | |  | | --- | | **Intel Data Center Manager 4.1 SQL Injection** **2022.12.09**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-21225](https://cxsecurity.com/cveshow/CVE-2022-21225/ "Click to see CVE-2022-21225")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: Intel Data Center Manager
Vendor URL: https://www.intel.com/content/www/us/en/developer/tools/data-center-manager-console/overview.html
Type: SQL Injection [CWE-89]
Date found: 2022-01-21
Date published: 2022-12-01
CVSSv3 Score: 9.9 (CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H)
CVE: CVE-2022-21225
2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.
3. VERSIONS AFFECTED
====================
Intel Data Center Manager 4.1 and below
4. INTRODUCTION
===============
Energy costs are the fastest rising expense for today’s data centers. Intel® Data
Center Manager (Intel® DCM) provides real-time power and thermal consumption data,
giving you the clarity you need to lower power usage, increase rack density, and
prolong operation during outages.
(from the vendor's homepage)
5. VULNERABILITY DETAILS
========================
Intel DCM's endpoint at "/DcmConsole/DataAccessServlet?action=getRoomRackData" is
vulnerable to an authenticated, blind SQL Injection when user-supplied input to
the HTTP POST parameter "dataName" is processed by the web application.
Since the application does not properly validate and sanitize this parameter, an
attacker can inject arbitrary SQL commands against the PostgreSQL backend
database server of the web application.
Successful exploits can allow an authenticated attacker (the lowest possible
authorization level "Guest" is sufficient) to read and modify database contents
and execute any system commands on the underlying operating system. This way,
the attacker can compromise the system's entire confidentiality, integrity, and
availability.
6. PROOF OF CONCEPT
===================
POST /DcmConsole/DataAccessServlet?action=getRoomRackData HTTP/1.1
Host: [ip-address]
Cookie: JSESSIONID=[session-id]
Content-Length: 153
Accept: application/json, text/plain, \*/\*
Content-Type: text/plain
User-Agent: Mozilla/5.0
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Connection: close
{"antiCSRFId":"[your-anti-csrf-id]","requestObj":{"snapshotId":1,"roomId":1,"dataName":"test');SELECT PG\_SLEEP(5)--"}}
(see the referenced blog post for more details)
7. SOLUTION
===========
Update at least to version 5.0.0.46307.
8. REPORT TIMELINE
==================
2022-01-21: Discovery of the vulnerability
2022-01-21: Reported to vendor via their bug bounty program
2022-01-21: Vendor response: Sent to "appropriate reviewers"
2022-02-08: Vendor acknowledges the vulnerability with a severity of "medium" without sharing their CVSS calculation
2022-02-15: Endless back-and-forth discussions about the rating. Vendor proposes a rating of 6.8
2022-02-16: I don't accept the rating because the vendor downplayed it
2022-02-25: After discussions, vendor rates issue as CVSS 9.0 (CVSS:3.1/AV:A/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H)
2022-02-25: Apparently AV:A is still wrong, but I don't have more energy to fight them. However this advisory contains the proper CVSS rating.
2022-xx-xx: Vendor releases version 5.0.0.46307 which includes the fix
2022-08-09: Vendor releases advisory INTEL-SA-00662
2022-12-01: Public disclosure
9. REFERENCES
==============
https://www.rcesecurity.com/2022/12/from-zero-to-hero-part-2-intel-dcm-sql-injection-to-rce-cve-2022-21225/
https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00662.html
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120022)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top