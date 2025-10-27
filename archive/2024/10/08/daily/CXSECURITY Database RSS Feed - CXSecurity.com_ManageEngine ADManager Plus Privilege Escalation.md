---
title: ManageEngine ADManager Plus Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2024100012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-10-08
fetch_date: 2025-10-06T18:49:39.960558
---

# ManageEngine ADManager Plus Privilege Escalation

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
|  |  | |  | | --- | | **ManageEngine ADManager Plus Privilege Escalation** **2024.10.07**  Credit:  **[Metin Yunus Kandemir](https://cxsecurity.com/author/Metin%2BYunus%2BKandemir/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-24409](https://cxsecurity.com/cveshow/CVE-2024-24409/ "Click to see CVE-2024-24409")**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: ManageEngine ADManager Plus Build < 7210 Elevation of Privilege Vulnerability
# Exploit Author: Metin Yunus Kandemir
# Vendor Homepage: https://www.manageengine.com/
# Software Link: https://www.manageengine.com/products/ad-manager/
# Details: https://docs.unsafe-inline.com/0day/admanager-plus-build-less-than-7210-elevation-of-privilege-vulnerability-cve-2024-24409
# Version: ADManager Plus Build < 7210
# Tested against: Build 7203
# CVE: CVE-2024-24409
# Description
The Modify Computers is a predefined role in ADManager for managing computers. If a technician user has the Modify Computers privilege
over a computer can change the userAccountControl and msDS-AllowedToDelegateTo attributes of the computer object. In this way, the technician user can set Constrained Kerberos Delegation over any computer within the Organizational Unit that the user was delegated so that the attacker can perform DCSync after setting Constrained Kerberos Delegation over a computer for LDAP service of a Domain Controller server.
# Proof Of Concept
https://docs.unsafe-inline.com/0day/admanager-plus-build-less-than-7210-elevation-of-privilege-vulnerability-cve-2024-24409

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024100012)

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