---
title: SpagoBI 3.5.1 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2025010031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-29
fetch_date: 2025-10-06T20:04:54.157890
---

# SpagoBI 3.5.1 Cross Site Scripting

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
|  |  | |  | | --- | | **SpagoBI 3.5.1 Cross Site Scripting** **2025.01.28**  Credit:  **[MarioTesoro](https://cxsecurity.com/author/MarioTesoro/1/)**  Risk: **Low**  Local: ****Yes****  Remote: ****Yes****  CVE: **[CVE-2024-54795](https://cxsecurity.com/cveshow/CVE-2024-54795/ "Click to see CVE-2024-54795")**  CWE: **N/A** | |

# CVE-2024-54795
\*\*Severity :\*\* \*\*Medium\*\* (\*\*5.4\*\*)
\*\*CVSS score :\*\* `CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:L/I:L/A:N`
## Summary :
Engineering Ingegneria Informatica \*\*SpagoBI\*\* version \*\*3.5.1\*\* is affected by multiple \*\*stored XSS\*\* inside of the worksheet designer page.
## Poc
### Steps to Reproduce :
1. While editing a document inserting custom text or while seving inserting filename and info insert the following payload:
```
"><img src="#" onerror=alert(1)>
```
2. Visit the home/worksheet designer page and the pages of the file saved. The html will be reflected and the alert prompted.
## Affected Version Details :
- <= 3.5.1
## Impact :
If the attacker is logged into the app with sufficient permissions to access the worksheet designer page, can store a JS script that can steal user cookies, perform horizontal/vertical privilege escalation, or perform malicious actions such as downloading a malicious file.
## Mitigation :
- Update to the latest version.
## References :
- https://nvd.nist.gov/vuln/detail/CVE-2024-54795

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010031)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

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