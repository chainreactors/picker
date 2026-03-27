---
title: esiclivre 0.2.2 SQL Injection
url: https://cxsecurity.com/issue/WLB-2026030034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-26
fetch_date: 2026-03-27T04:26:43.615850
---

# esiclivre 0.2.2 SQL Injection

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
|  |  | |  | | --- | | **esiclivre 0.2.2 SQL Injection** **2026.03.26**  Credit:  **[Bryan](https://cxsecurity.com/author/Bryan/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# CVE-2026-30655 — SQL Injection in esiclivre (password reset)
## Summary
A SQL injection vulnerability exists in the password reset endpoint of esiclivre. An unauthenticated attacker can inject SQL via the `cpfcnpj` POST parameter, potentially resulting in unauthorized access to sensitive information.
## Affected Project
- Repository: https://github.com/esiclivre/esiclivre
- Affected versions: v0.2.2 and earlier
- Affected commit: up to and including 0a72b4c9ab89244ec3bd3d7fa0b765850cc9afd7
## Technical Details
- Endpoint: `POST /reset/index.php`
- Parameter: `cpfcnpj`
- Root cause: user input is concatenated into a SQL query in `Solicitante::resetaSenha()` without parameterization.
## Impact
- Potential unauthorized access to sensitive database information (information disclosure).
## Mitigation / Fix
No upstream fix is available at the time of publication.
Recommended remediation:
- Use parameterized queries (prepared statements) for database access.
- Validate and sanitize user input.
- Consider temporarily restricting access to the password reset endpoint until patched.
## Timeline
- 2025-04-12: Reported to vendor/maintainers
- 2026-02-09: CVE request submitted
- 2026-03-23: CVE-2026-30655 assigned
## Credits
Discovered by Bryan Romero (https://github.com/brynax).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030034)

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