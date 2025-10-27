---
title: Quorum onQ OS 6.0.0.5.2064 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025020002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-02-02
fetch_date: 2025-10-06T20:32:33.935972
---

# Quorum onQ OS 6.0.0.5.2064 Cross Site Scripting

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
|  |  | |  | | --- | | **Quorum onQ OS 6.0.0.5.2064 Cross Site Scripting** **2025.02.01**  Credit:  **[\_striv3r\_](https://cxsecurity.com/author/_striv3r_/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

[+] Credits: Shahnawaz Shaikh, Security Researcher at Cybergate Defense LLC
[+] twitter.com/\_striv3r\_
[Vendor]
https://quorum.com/about/
[Product]
Quorum onQ OS - 6.0.0.5.2064
Vulnerability Type]
Reflected Cross Site Scripting (XSS)
[Affected Component]
Login page get parameter 'msg' is vulnerable to Reflected Cross site
scripting
[CVE Reference]
CVE-2024-44449
[Security Issue]
Cross Site Scripting vulnerability in Quorum onQ OS v.6.0.0.5.2064 allows a
remote attacker to obtain sensitive information via the msg parameter in
the Login page.
[Attack Vectors]
After obtaining the API key, an attacker can use tools such as curl,
Postman, or custom scripts to craft unauthorized requests to the target API.
[Network Access]
Remote
[Severity]
Medium
[Disclosure Timeline]
Vendor Notification: July 20, 2024
Vendor released fixed: September 13, 2024

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025020002)

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