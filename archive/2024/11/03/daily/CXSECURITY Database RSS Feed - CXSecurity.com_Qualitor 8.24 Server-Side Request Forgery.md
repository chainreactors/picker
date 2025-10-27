---
title: Qualitor 8.24 Server-Side Request Forgery
url: https://cxsecurity.com/issue/WLB-2024110005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-03
fetch_date: 2025-10-06T19:13:46.754075
---

# Qualitor 8.24 Server-Side Request Forgery

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
|  |  | |  | | --- | | **Qualitor 8.24 Server-Side Request Forgery** **2024.11.02**  Credit:  **[OpenXP Research Team](https://cxsecurity.com/author/OpenXP%2BResearch%2BTeam/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-48360](https://cxsecurity.com/cveshow/CVE-2024-48360/ "Click to see CVE-2024-48360")**  CWE: **N/A** | |

# CVE-2024-48360 | Qualitor <= v8.24 Unauthenticated SSRF
## Description
Qualitor is a platform for business process management, and this system is present in various companies in Brazil that can be identified simply by using Google dorking.
Our team identified a vulnerability in the application susceptible to SSRF, which allows enumerate internal systems/ports.
## Proof of Concept (POC)
Qualitor v8.24 was discovered to contain a Server-Side Request Forgery (SSRF) via the component /request/viewValidacao.php.
To exploit, just send a request to host.com/html/ad/adformmobile/request/viewValidacao.php?url=ATTACKER\_WEBHOOK, you will receive the request from vulnerable server.
![image](https://github.com/user-attachments/assets/c7f3dd6f-759d-430c-a135-fdc01e802619)
### Researches
https://www.linkedin.com/in/xvinicius/
- OpenXP Research Team

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110005)

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