---
title: Panel Amadey.d.c MVID-2024-0680 Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024050031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-12
fetch_date: 2025-10-06T17:14:40.759562
---

# Panel Amadey.d.c MVID-2024-0680 Cross Site Scripting

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
|  |  | |  | | --- | | **Panel Amadey.d.c MVID-2024-0680 Cross Site Scripting** **2024.05.11**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source: https://malvuln.com/advisory/50467c891bf7de34d2d65fa93ab8b558.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Panel Amadey.d.c
Vulnerability: Cross Site Scripting (XSS)
Family: Amadey
Type: Web Panel
MD5: 50467c891bf7de34d2d65fa93ab8b558 (Login.php)
SHA256: 65623eead2bcba66817861246e842386d712c38c5c5558e50eb49cffa2a1035d
Vuln ID: MVID-2024-0680
Disclosure: 05/09/2024
Description: The Amadey C2 web panel is written in PHP for remote administration capability. The Login.php webpage accepts HTTP GET "l" and "p" parameters which are passed to the backend server side code: $\_GET["l"] name=\"login\", $\_GET["p"] , name=\"password\". However, there is no secure coding practice of filtering input or sanitization of output. Panel users who visit a third-party attacker website or click an infected link, can trigger arbitrary client side JS code execution in the security context of the current user. This can result in data theft or GEO location disclosure of the user accessing the Amadey web interface.
The submit button contains the text "Unlock".
Entering incorrect password results in URI of "?wrong=1" and displays "Wrong login or password", after a few seconds delay redirects back to Login.php.
http://127.0.0.1/Panel.Amadey.d.c/Login.php?wrong=1
Wrong login or password
The web panel HTML source code for the URL "Login.php?wrong=1" contains the letters "CC" plus the Domain/IP within brackets[x.x.x.x] within the HTML title tag.
%3Ctitle%3E CC [127.0.0.1] %3C/title%3E
Tested successfully in Firefox.
Exploit/PoC:
Vulnerable parameters: "l" and "p"
http://x.x.x.x/Panel.Amadey.d.c/Login.php?l=%22/%3E%3Cscript%3Ealert(document.cookie)%3C/script%3E
http://x.x.x.x/Panel.Amadey.d.c/Login.php?p=%22/%3E%3Cscript%3Ealert(666)%3C/script%3E
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050031)

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