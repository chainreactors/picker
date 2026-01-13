---
title: CarRentalMS 2.0 Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2026010007
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-12
fetch_date: 2026-01-13T03:26:06.340415
---

# CarRentalMS 2.0 Cross Site Request Forgery

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
|  |  | |  | | --- | | **CarRentalMS 2.0 Cross Site Request Forgery** **2026.01.12**  Credit:  **[Parthiv](https://cxsecurity.com/author/Parthiv/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Description
A Cross-Site Request Forgery (CSRF) vulnerability exists in the administrator profile update functionality of \*\*CarRentalMS v2.0\*\*. The affected endpoint does not implement anti-CSRF protections, allowing an attacker to perform unauthorized profile modifications on behalf of an authenticated administrator via crafted HTML content.
This issue has been assigned \*\*CVE-2025-66683\*\*.
## Affected Product
- Project: CarRentalMS
- Version: 2.0
- Vendor: Mart Mbithi
## Affected Component
- Endpoint: `/CarRentalMS/ui/backoffice\_settings`
- Functionality: Admin profile update
## Vulnerability Type
- Cross-Site Request Forgery (CSRF)
- CWE-352
## Attack Vector
Remote. An attacker can lure an authenticated administrator into visiting a malicious webpage (e.g., via a malicious advertisement or compromised website), which silently submits a forged POST request to the vulnerable endpoint.
## Impact
Successful exploitation allows unauthorized modification of administrator profile details, including email address changes. This can result in:
- Full account takeover
- Privilege escalation
- Persistence establishment
- Potential data exfiltration
## Conditions for Exploitation
- Administrator is authenticated
- No anti-CSRF tokens are implemented
- No SameSite cookie protections are enforced
- User interaction with attacker-controlled HTML content
## Proof of Concept
A working proof of concept demonstrates exploitation by auto-submitting a crafted HTML form while an administrator session is active, resulting in profile data being modified without user consent.
(PoC details provided to maintainers; not fully reproduced here.)
## Mitigation Recommendations
- Implement anti-CSRF tokens (e.g., synchronizer token pattern)
- Enforce `SameSite` cookie attributes
- Validate request origin and referer headers
- Apply additional server-side authorization checks for state-changing requests
## References
- [https://cwe.mitre.org/data/definitions/352.html](https://cwe.mitre.org/data/definitions/352.html)
- [https://owasp.org/www-community/attacks/csrf](https://owasp.org/www-community/attacks/csrf)
- [https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site\_Request\_Forgery\_Prevention\_Cheat\_Sheet.html)
- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)
## Discoverer
Parthiv Kumar Nikku ([parthivkumarnikku@gmail.com](mailto:parthivkumarnikku@gmail.com))

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010007)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top