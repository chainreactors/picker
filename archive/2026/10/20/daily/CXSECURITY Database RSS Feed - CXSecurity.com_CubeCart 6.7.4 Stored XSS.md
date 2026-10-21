---
title: CubeCart 6.7.4 Stored XSS
url: https://cxsecurity.com/issue/WLB-2026100001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-10-20
fetch_date: 2026-10-21T06:46:59.641295
---

# CubeCart 6.7.4 Stored XSS

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
|  |  | |  | | --- | | **CubeCart 6.7.4 Stored XSS** **2026.10.20**  Credit:  **[Mikail Kocadağ](https://cxsecurity.com/author/Mikail%2BKocada%C4%9F/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-54645](https://cxsecurity.com/cveshow/CVE-2026-54645/ "Click to see CVE-2026-54645")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: CubeCart 6.7.4 - Stored Cross-Site Scripting
# Date: 2026-06-08
# Exploit Author: Mikail Kocadağ (MKLKCDG)
# Vendor Homepage: https://www.cubecart.com/
# Software Link: https://github.com/cubecart/v6
# Vulnerable Version: 6.7.4
# Fixed Version: 6.7.5
# CVE: CVE-2026-54645
# Advisory / References:
https://github.com/cubecart/v6/security/advisories/GHSA-43f6-gfcf-wj9c
--------------------------------------------------------------------------------
VULNERABILITY SUMMARY
--------------------------------------------------------------------------------
A Stored Cross-Site Scripting (XSS) vulnerability exists in the product
management panel of CubeCart 6.7.4, where product descriptions bypass
global input
filters and sanitization controls.
In `admin/sources/products.index.inc.php` (lines 55-59), the application
explicitly
bypasses the global sanitizer mechanism by retrieving content directly from
`$GLOBALS['RAW']['POST']`. The only defense applied is a basic regex filter
against
`<script>` tags, which fails to block alternative XSS vectors like event
handlers
or SVG elements.
--------------------------------------------------------------------------------
IMPACT
--------------------------------------------------------------------------------
An attacker with product editing permissions can inject persistent
malicious JavaScript.
When clients or other administrators view the affected product page on
either the
public storefront or the administration panel, the payload executes within
their
active session.
--------------------------------------------------------------------------------
PROOF OF CONCEPT (PoC)
--------------------------------------------------------------------------------
1. Log into the administration panel and navigate to Product Management.
2. Edit or create a product, and inject a payload using an HTML event
handler into the product description:
<img src=x onerror=alert(document.domain)>
3. Save the product.
4. Visit the product page on the public storefront or view it within the
admin panel to trigger execution.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026100001)

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