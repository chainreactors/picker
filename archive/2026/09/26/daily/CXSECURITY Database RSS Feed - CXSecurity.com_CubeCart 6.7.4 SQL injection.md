---
title: CubeCart 6.7.4 SQL injection
url: https://cxsecurity.com/issue/WLB-2026090011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-26
fetch_date: 2026-09-27T07:24:25.943113
---

# CubeCart 6.7.4 SQL injection

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
|  |  | |  | | --- | | **CubeCart 6.7.4 SQL injection** **2026.09.26**  Credit:  **[Mikail Kocadağ](https://cxsecurity.com/author/Mikail%2BKocada%C4%9F/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-54647](https://cxsecurity.com/cveshow/CVE-2026-54647/ "Click to see CVE-2026-54647")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")** | |

# Exploit Title: CubeCart 6.7.4 - SQL injection
# Date: 2026-06-08
# Exploit Author: Mikail Kocadağ
# Vendor Homepage: https://www.cubecart.com/
# Software Link: https://github.com/cubecart/v6
# Vulnerable Version: 6.7.4
# Fixed Version: 6.7.5
# CVE: CVE-2026-54647
# Advisory / References:
https://github.com/cubecart/v6/security/advisories/GHSA-hvmw-v8gc-4c29
--------------------------------------------------------------------------------
VULNERABILITY SUMMARY
--------------------------------------------------------------------------------
An authenticated administrative SQL injection vulnerability exists in
CubeCart v6.7.4
due to unsafe concatenation of user-supplied input in raw database queries
without validation.
The vulnerability is located in `admin/sources/settings.index.inc.php` at
line 184.
The `download\_expire` parameter received via POST is directly concatenated
into an
`UPDATE` SQL statement executed via `query()` or `misc()`.
The global input sanitizer (`Sanitize::\_safety()`) relies entirely on
`htmlspecialchars()`,
which does not filter or encode commas (`,`). An attacker can leverage
comma injection
to break out of the intended syntax and manipulate the `SET` clauses or
append malicious clauses.
--------------------------------------------------------------------------------
IMPACT
--------------------------------------------------------------------------------
An authenticated attacker with access to settings can manipulate arbitrary
columns
within the settings tables or potentially perform lateral movement within
the database.
--------------------------------------------------------------------------------
PROOF OF CONCEPT (PoC)
--------------------------------------------------------------------------------
1. Authenticated as an administrator, navigate to Settings.
2. Intercept the save request and inject a payload containing a comma into
the `download\_expire` field:
1, expire=0 WHERE 1=1-- -
3. Submit the request and verify that the raw SQL syntax is successfully
altered.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026090011)

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