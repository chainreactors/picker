---
title: ProLink PRS1841 Backdoor Account
url: https://cxsecurity.com/issue/WLB-2022120051
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-01
fetch_date: 2025-10-04T02:49:34.377698
---

# ProLink PRS1841 Backdoor Account

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
|  |  | |  | | --- | | **ProLink PRS1841 Backdoor Account** **2022.12.31**  Credit:  **[Lawrence Amer](https://cxsecurity.com/author/Lawrence%2BAmer/1/)**  Risk: **High**  Local: **No**  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

# Exploit Title: Router backdoor - ProLink PRS1841 PLDT Home fiber
# Exploit Author: Lawrence Amer @zux0x3a
# Vendor Homepage: https://prolink2u.com/product/prs1841/
# Firmware : PRS1841 U V2
# reference: https://0xsp.com/security%20research%20%20development%20srd/backdoor-discovered-in-pldt-home-fiber-routers/
Description
========================
A silent privileged backdoor account discovered on the Prolink PRS1841
routers; allows attackers to gain command execution privileges to the
router OS.
The vulnerable account issued by the vendor was identified as "adsl" and
"realtek" as the default password; attackers could use this account to
access the router remotely/internally using either Telnet or FTP
protocol.
PoC
=============================
adsl:$1$$m9g7v7tSyWPyjvelclu6D1:0:0::/tmp:/bin/cli

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120051)

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