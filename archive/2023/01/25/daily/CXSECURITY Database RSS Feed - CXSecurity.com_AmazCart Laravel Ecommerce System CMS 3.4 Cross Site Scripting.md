---
title: AmazCart Laravel Ecommerce System CMS 3.4 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023010045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-25
fetch_date: 2025-10-04T04:42:52.589135
---

# AmazCart Laravel Ecommerce System CMS 3.4 Cross Site Scripting

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
|  |  | |  | | --- | | **AmazCart Laravel Ecommerce System CMS 3.4 Cross Site Scripting** **2023.01.24**  Credit:  **[Sajibe Kanti](https://cxsecurity.com/author/Sajibe%2BKanti/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: AmazCart - Laravel Ecommerce System CMS 3.4 - 'Search' Cross-Site-Scripting — Reflected (AJAX)
# Date: 17/01/2023
# Exploit Author: Sajibe Kanti
# CVE ID:
# Vendor Name: CodeThemes
# Vendor Homepage: https://spondonit.com/
# Software Link: https://codecanyon.net/item/amazcart-laravel-ecommerce-system-cms/34962179
# Version: 3.4
# Tested on: Live Demo
# Demo Link : https://amazy.rishfa.com/
# Description #
AmazCart - Laravel Ecommerce System CMS 3.4 is vulnerable to Reflected
cross-site scripting because of insufficient user-supplied data
sanitization. Anyone can submit a Reflected XSS payload without login in
when searching for a new product on the search bar. This makes the
application reflect our payload in the frontend search ber, and it is fired
everything the search history is viewed.
# Proof of Concept (PoC) : Exploit #
1) Goto: https://amazy.rishfa.com/
2) Enter the following payload in 'Search Iteam box' : "><script>alert(1)</script>
3) Now You Get a Popout as Alert 1
4) Reflected XSS payload is fired
# Image PoC : Reference Image #
1) Payload Fired: https://prnt.sc/QQaiZB3tFMVB

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010045)

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