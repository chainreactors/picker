---
title: Intel Data Center Manager 4.1.1.45749 Authentication Bypass / Spoofing
url: https://cxsecurity.com/issue/WLB-2022120005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-02
fetch_date: 2025-10-04T00:15:57.467807
---

# Intel Data Center Manager 4.1.1.45749 Authentication Bypass / Spoofing

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
|  |  | |  | | --- | | **Intel Data Center Manager 4.1.1.45749 Authentication Bypass / Spoofing** **2022.12.01**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-33942](https://cxsecurity.com/cveshow/CVE-2022-33942/ "Click to see CVE-2022-33942")**  CWE: **[CWE-290](https://cxsecurity.com/cwe/CWE-290 "Click to see CWE-290")** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: Intel Data Center Manager
Vendor URL: https://www.intel.com/content/www/us/en/developer/tools/data-center-manager-console/overview.html
Type: Authentication Bypass by Spoofing [CWE-290]
Date found: 2022-06-01
Date published: 2022-11-23
CVSSv3 Score: 10.0 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H)
CVE: CVE-2022-33942
2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.
3. VERSIONS AFFECTED
====================
Intel Data Center Manager 4.1.1.45749 and below
4. INTRODUCTION
===============
Energy costs are the fastest rising expense for today’s data centers. Intel® Data
Center Manager (Intel® DCM) provides real-time power and thermal consumption data,
giving you the clarity you need to lower power usage, increase rack density, and
prolong operation during outages.
(from the vendor's homepage)
5. VULNERABILITY DETAILS
========================
The application allows configuring authentication via Active Directory groups. While
this by itself isn't an issue, it becomes one as soon as an Active Directory group
with a well-known SID (such as "S-1-5-32-544" or "S-1-5-32-546") is configured to
allow authentication to DCM. This is because Intel's DCM only relies on the group's
SID to allow authentication but doesn't verify the authenticating domain, which the
user can give during the authentication process against the DCM Console and its REST
interface.
Since the DCM will send all Kerberos and LDAP (authentication) requests against the
given domain, it is trivially easy to spoof the authentication responses by using an
arbitrary Kerberos and LDAP server and replying with the SID of one of the configured
Active Directory groups.
This allows an attacker to bypass the authentication schema by using any domain
with any user/password combination without actually being part of any Active Directory
groups.
6. PROOF OF CONCEPT
===================
See the referenced blog post for a full exploit.
7. SOLUTION
===========
Update to Intel DCM 5.0 or later
8. REPORT TIMELINE
==================
2022-06-01: Discovery of the vulnerability
2022-06-28: Sent notification to Intel via their PSIRT
2022-06-28: Vendor response: Sent to appropriate reviewers.
2022-06-29: Vendor acknowledges the vulnerability and asks for coordinated disclosure on Nov. 8, 2022
2022-06-30: Rejected the disclosure date, due to my own policy, which makes it: August 13, 2022
2022-07-08: After a vendor call, I've submitted the issue through Intel's bug bounty program
2022-xx-xx: Vendor releases version 5.0 without any notification which fixes this vulnerability
2022-11-08: Vendor (responsible CNA) assigns CVE-2022-33942
2022-11-08: Vendor publishes security advisory INTEL-SA-00713
2022-11-23: Public disclosure
9. REFERENCES
=============
https://www.rcesecurity.com/2022/11/from-zero-to-hero-part-1-bypassing-intel-dcms-authentication-by-spoofing-kerberos-and-ldap-responses-cve-2022-33942
https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00713.html
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120005)

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