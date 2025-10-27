---
title: Gitea 1.22.0 Stored XSS
url: https://cxsecurity.com/issue/WLB-2025040011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-04-07
fetch_date: 2025-10-06T22:03:35.564841
---

# Gitea 1.22.0 Stored XSS

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
|  |  | |  | | --- | | **Gitea 1.22.0 Stored XSS** **2025.04.06**  Credit:  **[Catalin Iovita](https://cxsecurity.com/author/Catalin%2BIovita/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-6886](https://cxsecurity.com/cveshow/CVE-2024-6886/ "Click to see CVE-2024-6886")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: Stored XSS in Gitea
# Date: 27/08/2024
# Exploit Authors: Catalin Iovita & Alexandru Postolache
# Vendor Homepage: (https://github.com/go-gitea/gitea)
# Version: 1.22.0
# Tested on: Linux 5.15.0-107, Go 1.23.0
# CVE: CVE-2024-6886
## Vulnerability Description
Gitea 1.22.0 is vulnerable to a Stored Cross-Site Scripting (XSS) vulnerability. This vulnerability allows an attacker to inject malicious scripts that get stored on the server and executed in the context of another user's session.
## Steps to Reproduce
1. Log in to the application.
2. Create a new repository or modify an existing repository by clicking the Settings button from the `$username/$repo\_name/settings` endpoint.
3. In the Description field, input the following payload:
<a href=javascript:alert()>XSS test</a>
4. Save the changes.
5. Upon clicking the repository description, the payload was successfully injected in the Description field. By clicking on the message, an alert box will appear, indicating the execution of the injected script.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025040011)

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