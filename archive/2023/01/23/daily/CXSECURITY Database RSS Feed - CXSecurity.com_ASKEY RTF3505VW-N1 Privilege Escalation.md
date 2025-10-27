---
title: ASKEY RTF3505VW-N1 Privilege Escalation
url: https://cxsecurity.com/issue/WLB-2023010035
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-23
fetch_date: 2025-10-04T04:35:26.041446
---

# ASKEY RTF3505VW-N1 Privilege Escalation

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
|  |  | |  | | --- | | **ASKEY RTF3505VW-N1 Privilege Escalation** **2023.01.22**  Credit:  **[LNS](https://cxsecurity.com/author/LNS/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **[CWE-264](https://cxsecurity.com/cwe/CWE-264 "Click to see CWE-264")** | |

# Exploit Title: ASKEY RTF3505VW-N1 - Privilege escalation
# Date: 07-12-2022
# Exploit Author: Leonardo Nicolas Servalli
# Vendor Homepage: www.askey.com
# Platform: ASKEY router devices RTF3505VW-N1
# Tested on: Firmware BR\_SV\_g000\_R3505VMN1001\_s32\_7
# Vulnerability analysis: https://github.com/leoservalli/Privilege-escalation-ASKEY/blob/main/README.md
#Description:
#----------
# ASKEY RTF3505VW-N1 devices are provided with access through ssh into a restricted default shell (credentials are on the back of the router and in some cases these routers use default credentials).
# The command “tcpdump” is present in the restricted shell and do not handle correctly the -z flag, so it can be used to escalate privileges through the creation of a local file in the /tmp directory of the router, and injecting packets through port 80 (used for the router's Web GUI) with the string ";/bin/bash" in order to be executed by "-z sh". By using “;/bin/bash” as injected string we can spawn a busybox/ash console.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010035)

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