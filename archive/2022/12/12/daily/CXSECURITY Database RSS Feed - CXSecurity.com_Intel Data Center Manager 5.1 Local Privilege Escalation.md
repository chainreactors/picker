---
title: Intel Data Center Manager 5.1 Local Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2022120027
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-12
fetch_date: 2025-10-04T01:14:06.521819
---

# Intel Data Center Manager 5.1 Local Privilege Escalation

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
|  |  | |  | | --- | | **Intel Data Center Manager 5.1 Local Privilege Escalation** **2022.12.11**  Credit:  **[Julien Ahrens](https://cxsecurity.com/author/Julien%2BAhrens/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2021-44228](https://cxsecurity.com/cveshow/CVE-2021-44228/ "Click to see CVE-2021-44228")**  CWE: **[CWE-648](https://cxsecurity.com/cwe/CWE-648 "Click to see CWE-648")  [CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")**  CVSS Base Score: **9.3/10**  Impact Subscore: **10/10**  Exploitability Subscore: **8.6/10**  Exploit range: **Remote**  Attack complexity: **Medium**  Authentication: **No required**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

RCE Security Advisory
https://www.rcesecurity.com
1. ADVISORY INFORMATION
=======================
Product: Intel Data Center Manager
Vendor URL: https://www.intel.com/content/www/us/en/developer/tools/data-center-manager-console/overview.html
Type: Incorrect Use of Privileged APIs [CWE-648]
Date found: 2022-07-16
Date published: 2022-12-07
CVSSv3 Score: 7.4 (CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H)
CVE: -
2. CREDITS
==========
This vulnerability was discovered and researched by Julien Ahrens from
RCE Security.
3. VERSIONS AFFECTED
====================
Intel Data Center Manager 5.1 (latest) and below
4. INTRODUCTION
===============
Energy costs are the fastest rising expense for today’s data centers. Intel® Data
Center Manager (Intel® DCM) provides real-time power and thermal consumption data,
giving you the clarity you need to lower power usage, increase rack density, and
prolong operation during outages.
(from the vendor's homepage)
5. VULNERABILITY DETAILS
========================
The latest version (5.1) and all prior versions of Intel's DCM are vulnerable to a
local privileges escalation vulnerability using the application user "dcm" used to
run the web application and the rest interface. An attacker who gained RCE using
this dcm user (i.e., through Log4j) is then able to escalate their privileges to
root by abusing a weak Sudo configuration for the "dcm" user:
dcm ALL=(ALL) NOPASSWD:/usr/local/bin/SDPTool
dcm ALL=(ALL) NOPASSWD:/usr/bin/cp
dcm ALL=(ALL) NOPASSWD:/usr/bin/chmod
The Intel Server Debug and Provisioning Tool (SDP Tool) must be installed for the
Data Center Manager to be vulnerable. Successful exploits can allow an authenticated
attacker to execute commands as root. In this way, the attacker can compromise the
victim system's entire confidentiality, integrity, and availability, thereby allowing
to persist within the attached network.
6. PROOF OF CONCEPT
===================
Just one way of exploitation is by replacing the current sudoers configuration:
1.Create a new sudoers configuration file using the compromised "dcm" user in i.e. /tmp/
2.sudo chmod 440 /tmp/sudoers
3.sudo cp sudoers /etc/sudoers
4.sudo /bin/bash
7. SOLUTION
===========
None. Intel thinks that this is not a vulnerability and therefore does also not assign
a CVE for it.
8. REPORT TIMELINE
==================
2022-07-16: Discovery of the vulnerability
2022-07-16: Reported to vendor via their bug bounty program
2022-07-18: Vendor response: Sent to "appropriate reviewers"
2022-07-26: Vendor states that the vulnerability "depends on something that does not exist (eg; RCE)."
2022-07-26: Sent a clarification that a compromise of the "dcm" account is indeed necessary, but there have been RCEs in the past (i.e. through Log4j)
2022-09-22: Vendor has troubles to reproduce the bug and asks for another PoC
2022-09-22: Sent a clarification about the PoC
2022-09-22: Vendor states that the report "does not clearly demonstrate a vulnerability in DCM" and the report will be closed.
2022-09-23: Provided the vendor with a PoC utilizing Log4shell (CVE-2021-44228) in a former version of DCM
2022-10-10: Vendor asks whether the Log4shell bug is still reproducible in the latest version of DCM
2022-10-10: Made clear that Log4shell is not the point about the report
2022-10-11: Vendor states "We do not clearly see a a vulnerability demonstrated in DCM"
2022-10-12: [Back and forth about the provided PoCs]
2022-10-12: I'm giving up.
2022-12-07: Public disclosure
9. REFERENCES
==============
https://github.com/MrTuxracer/advisories

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120027)

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