---
title: LISTSERV 17 Reflected Cross Site Scripting (XSS)
url: https://cxsecurity.com/issue/WLB-2023040001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-03
fetch_date: 2025-10-04T11:29:18.121061
---

# LISTSERV 17 Reflected Cross Site Scripting (XSS)

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
|  |  | |  | | --- | | **LISTSERV 17 Reflected Cross Site Scripting (XSS)** **2023.04.02**  Credit:  **[Shaunt Der-Grigorian](https://cxsecurity.com/author/Shaunt%2BDer-Grigorian/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-39195](https://cxsecurity.com/cveshow/CVE-2022-39195/ "Click to see CVE-2022-39195")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  **[**Dork:** inurl:/scripts/wa.exe](https://cxsecurity.com/dorks/)** | |

# Exploit Title: LISTSERV 17 - Reflected Cross Site Scripting (XSS)
# Google Dork: inurl:/scripts/wa.exe
# Date: 12/01/2022
# Exploit Author: Shaunt Der-Grigorian
# Vendor Homepage: https://www.lsoft.com/
# Software Link: https://www.lsoft.com/download/listserv.asp
# Version: 17
# Tested on: Windows Server 2019
# CVE : CVE-2022-39195
A reflected cross-site scripting (XSS) vulnerability in the LISTSERV 17 web interface allows remote attackers to inject arbitrary JavaScript or HTML via the "c" parameter.
To reproduce, please visit
http://localhost/scripts/wa.exe?TICKET=test&c=%3Cscript%3Ealert(1)%3C/script%3E
(or whichever URL you can use for testing instead of localhost).
The "c" parameter will reflect any value given onto the page.
# Solution
This vulnerability can be mitigated by going under "Server Administration" to "Web Templates" and editing the BODY-LCMD-MESSAGE web template. Change &+CMD; to &+HTMLENCODE(&+CMD;); .

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040001)

[Tweet](https://twitter.com/share)

Vote for this issue:
 3
 -1

75%

25%

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